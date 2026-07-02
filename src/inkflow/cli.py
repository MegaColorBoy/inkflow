from __future__ import annotations

from datetime import date

import typer

from inkflow.assets import ThemeNotFoundError, sync_assets
from inkflow.builder import OUTPUT_DIR, build_section, build_all_sections, generate_json_export
from inkflow.categories import generate_categories
from inkflow.config import load_config
from inkflow.content import load_posts, CONTENT_DIR
from inkflow.context import SiteContext
from inkflow.feed import generate_rss_feed
from inkflow.server import serve
from inkflow.templates import create_jinja_env
from inkflow.types import MenuItem
from inkflow.utils import create_directory, generate_slug, generate_file_path, format_date

app = typer.Typer(
    add_completion=False,
    help="Inkflow static site generator.",
    no_args_is_help=False,
)

_DEFAULT_META_TEMPLATE = """\
---
title: {title}
date: {date}
slug: {slug}
category: {category}
summary:
status: inactive
---

"""

def __init_context(config_path: str = "site.toml") -> SiteContext:
    """Load site configuration, create jinja env and return SiteContext."""
    try:
        config = load_config(config_path)
    except FileNotFoundError as exc:
        typer.echo(f"Error: config file not found: {exc}", err=True)
        raise typer.Exit(1) from exc
    except (KeyError, TypeError, ValueError) as exc:
        typer.echo(f"Error: parsing config: {exc}", err=True)
        raise typer.Exit(1) from exc

    # Create jinja environment
    try:
        env = create_jinja_env(config.site)
    except FileNotFoundError as exc:
        typer.echo(f"Error: template directory not found: {exc}", err=True)
        raise typer.Exit(1) from exc

    return SiteContext(config=config, env=env)

def __init_full_context(config_path: str = "site.toml") -> SiteContext:
    """Fully initialize context with menu, posts and categories."""
    ctx = __init_context(config_path)
    ctx.menu = _generate_menu(ctx)
    ctx.all_posts = load_posts(ctx.config)
    generate_categories(ctx)
    return ctx

def _generate_menu(ctx: SiteContext) -> list[MenuItem]:
    """Generate menu items from the sections marked as display_in_menu"""
    return [MenuItem(link=s.url, title=s.title) for s in ctx.config.sections if s.display_in_menu]

@app.command()
def build(mode: str = "") -> None:
    """Build entire site or specific sections of the blog."""
    ctx = __init_full_context()

    # Default message
    message = "The posts for all sections are generated successfully."

    # If mode is specified, prompt the user with options.
    if len(mode) == 0:
        sections = "\n".join([f"{idx + 1}. {item.title}" for idx, item in enumerate(ctx.config.sections)])
        typer.echo(f"Which section do you want to render? Hit '0' for all sections. \n{sections}")

        try:
            option = int(typer.prompt(typer.style("Enter an appropriate option", fg="green")))
        except ValueError as exc:
            typer.echo(f"Error: please enter a valid number.", err=True)
            raise typer.Exit(1) from exc

        if option < 0 or option > len(ctx.config.sections):
            typer.echo(
                f"Error: option must be between 0 and {len(ctx.config.sections)}",
                err=True
            )
            raise typer.Exit(1)

        # Render the specific section
        if option != 0:
            section = ctx.config.sections[option - 1]
            message = f"The articles for {section.title} has been generated."
            build_section(ctx, section)
        else:
            build_all_sections(ctx)
    elif mode == "all":
        build_all_sections(ctx)
    else:
        typer.echo(f"Error: invalid build mode: {mode}. Use 'all' or omit for interactive mode.", err=True)
        raise typer.Exit(1)

    typer.echo(message)

@app.command()
def create() -> None:
    """Create a new blog post"""
    ctx = __init_context()

    title = typer.prompt("What's the title of the post?")
    section = typer.prompt("Which section does it belong to?")
    category = typer.prompt("Which category does it belong to?")

    directory = f"{CONTENT_DIR}/{section.lower()}/"
    create_directory(directory)

    today = date.today()
    slug = generate_slug(title)

    post_file_path = generate_file_path(today, directory, slug)
    post_date = format_date(today, "%B {S}, %Y")

    template = ctx.config.site.meta_template.strip()
    if not template:
        typer.echo("Warning: meta_template is not configured in site.toml, using default.", err=True)
        template = _DEFAULT_META_TEMPLATE.strip()

    meta = template.format(title=title, slug=slug, date=post_date, category=category)

    with open(post_file_path, "w") as f:
        f.write(meta)

    typer.echo("Your file has been created {post_file_path}".format(post_file_path=post_file_path))

@app.command()
def export(mode: str = "") -> None:
    """Export posts using the available options"""
    exporters = {
        "rss": export_rss_feed,
        "json": export_as_json
    }

    mode = mode.strip().lower()

    if not mode:
        typer.echo("Which format do you want to export all posts to? (rss/json/all)")
        mode = typer.prompt(typer.style("Choose export mode", fg="green")).strip().lower()

    if mode == "all":
        export_rss_feed()
        export_as_json()
        return

    exporter = exporters.get(mode)
    if exporter is None:
        typer.echo(f"Error: invalid export mode: {mode} Use 'rss', 'json' or 'all'.", err=True)
        raise typer.Exit(1)

    exporter()

def export_as_json() -> None:
    """Export all posts into json format"""
    ctx = __init_full_context()
    generate_json_export(ctx)
    typer.echo("All posts are exported into json format.")

def export_rss_feed() -> None:
    """Export all posts into RSS feed XML format"""
    ctx = __init_context()
    ctx.all_posts = load_posts(ctx.config)
    generate_rss_feed(ctx.all_posts, site=ctx.config.site)
    typer.echo("RSS Feed Generated.")

@app.command()
def sync(output_dir: str = OUTPUT_DIR) -> None:
    """Compile SCSS and sync static assets from theme to output/static/."""
    ctx = __init_context()
    try:
        sync_assets(ctx.config.site.theme, output_dir=output_dir)
    except ThemeNotFoundError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(1)

def _full_rebuild() -> None:
    """Rebuild everything - used as the callback for the file watcher."""
    ctx = __init_full_context()
    build_all_sections(ctx)
    sync_assets(ctx.config.site.theme)

@app.command()
def server(
    port: int = 8000,
    host: str = "localhost",
    output_dir: str = OUTPUT_DIR,
    watch: bool = True
) -> None:
    """Start a dev server with hot-reload on file changes."""
    try:
        typer.echo(f"Serving website on http://{host}:{port} on your browser.", err=False)
        serve(
            output_dir=output_dir,
            host=host,
            port=port,
            watch=watch,
            rebuild_fn=_full_rebuild if watch else None
        )
    except FileNotFoundError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(1)

@app.callback(invoke_without_command=True)
def root(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        typer.echo("Hello from inkflow!")


@app.command("version")
def show_version() -> None:
    from . import __version__
    typer.echo(__version__)

def main() -> None:
    app()