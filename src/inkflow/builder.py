from __future__ import annotations

import json
import logging
import os
from itertools import islice
from types import SimpleNamespace
from typing import Any

from jinja2 import Template

from inkflow.config import SectionConfig
from inkflow.content import get_posts_by_content_directory, get_recent_articles
from inkflow.context import SiteContext
from inkflow.pagination import build_page_url, calculate_page_count, generate_pagination_links
from inkflow.templates import render_post
from inkflow.types import Post
from inkflow.utils import archive_posts, create_directory, delete_directory, write_to_file

logger = logging.getLogger(__name__)

OUTPUT_DIR = "output"


def _resolve_template(ctx: SiteContext, section: SectionConfig, kind: str) -> Template:
    """Resolve the correct template for a section and kind.

    *kind* is one of ``"listing"``, ``"single"``, or ``"custom"``.
    Falls back to sensible defaults when no override is configured.
    """
    defaults: dict[str, str] = {
        "listing": "listing.html",
        "single": "single.html",
        "custom": "listing.html",
    }

    # Page-type overrides that ignore the section's template config
    if kind == "listing":
        if section.page_type == "main":
            return ctx.env.get_template("main.html")
        if section.page_type == "archive":
            return ctx.env.get_template("archive.html")

    # Check section-level template config
    if section.template:
        override = getattr(section.template, kind, None)
        if override:
            return ctx.env.get_template(override)

    return ctx.env.get_template(defaults.get(kind, "listing.html"))


def _base_render_kwargs(ctx: SiteContext, section: SectionConfig) -> dict[str, Any]:
    """Return the kwargs common to every index-page render call."""
    return {
        "page": {
            "title": section.seo.title,
            "description": section.seo.description,
        },
        "generate_meta": True,
        "categories": ctx.categories_with_posts,
        "site": ctx.site_dict,
        "menu": ctx.menu,
    }


def build_all_sections(ctx: SiteContext) -> None:
    """Build every section defined in config."""
    logger.info("Building all sections (%d total)", len(ctx.config.sections))
    for section in ctx.config.sections:
        build_section(ctx, section)
    logger.info("All sections built successfully")


def build_section(ctx: SiteContext, section: SectionConfig) -> None:
    """Build a specific section."""
    logger.info("Building section: %s (type=%s)", section.title, section.page_type)
    if section.data_type == "json":
        generate_json_section(ctx, section)
    elif section.page_type == "main":
        generate_main_page(ctx, section)
    elif section.page_type == "archive":
        generate_archive_page(ctx, section)
    else:
        posts = get_posts_by_content_directory(ctx.all_posts, [section.content_directory])
        generate_pages(ctx, section, posts)


def generate_pages(
    ctx: SiteContext,
    section: SectionConfig,
    posts: list[Post],
) -> None:
    """Generate all pages for a section (index + content)."""
    section_dir = f"{OUTPUT_DIR}/{section.content_directory}/"
    delete_directory(section_dir)

    if section.page_type == "multiple":
        generate_index_page(ctx, section, posts)

    generate_content(ctx, section, posts)


def generate_main_page(ctx: SiteContext, section: SectionConfig) -> None:
    """Generate a main/home page section."""
    posts = get_recent_articles(ctx.all_posts, ctx.config.sections)
    generate_index_with_paginator(ctx, section, posts, ctx.config.site.pagination_limit)


def generate_archive_page(ctx: SiteContext, section: SectionConfig) -> None:
    """Generate archive section."""
    archived = archive_posts(ctx.all_posts)
    generate_index_without_paginator(ctx, section, archived)


def generate_index_page(
    ctx: SiteContext,
    section: SectionConfig,
    posts: list[Post],
) -> None:
    """Generate index/listing page — with or without pagination."""
    if not section.enable_pagination:
        generate_index_without_paginator(ctx, section, posts)
    else:
        generate_index_with_paginator(ctx, section, posts, ctx.config.site.pagination_limit)


def generate_index_with_paginator(
    ctx: SiteContext,
    section: SectionConfig,
    posts: list[Post],
    posts_per_page: int,
) -> None:
    """Generate index page with pagination links."""
    template = _resolve_template(ctx, section, "listing")
    total_number_of_posts = len(posts)
    number_of_pages = calculate_page_count(total_number_of_posts, posts_per_page)

    is_main = section.page_type == "main"
    root_directory = f"{OUTPUT_DIR}/" if is_main else f"{OUTPUT_DIR}/{section.content_directory}/"
    pagination_base = "" if is_main else section.content_directory
    create_directory(root_directory)

    it = iter(posts)
    chunked_posts = list(iter(lambda: tuple(islice(it, posts_per_page)), ()))

    base_kwargs = _base_render_kwargs(ctx, section)

    for page_number in range(number_of_pages):
        current_page_number = page_number + 1

        sub_directory = ""
        if current_page_number > 1:
            sub_directory = f"pages/{current_page_number}/"
            delete_directory(root_directory + sub_directory)
            create_directory(root_directory + sub_directory)

        page_index_file = f"{root_directory}{sub_directory}index.html"

        previous_page = 0 if current_page_number == 1 else current_page_number - 1
        next_page = 0 if current_page_number == number_of_pages else current_page_number + 1
        prev_url = build_page_url(pagination_base, previous_page) if previous_page else ""
        next_url = build_page_url(pagination_base, next_page) if next_page else ""

        rendered_html = template.render(
            body_class="",
            posts=chunked_posts[page_number] if page_number < len(chunked_posts) else (),
            curr=current_page_number,
            prev=previous_page,
            next=next_page,
            prev_url=prev_url,
            next_url=next_url,
            total=number_of_pages,
            pagination_links=generate_pagination_links(pagination_base, current_page_number, number_of_pages),
            pagination=True,
            **base_kwargs,
        )

        write_to_file(page_index_file, rendered_html.encode("utf-8"))

    logger.info("Generated %d paginated index pages(s) for %s", number_of_pages, section.title)


def generate_index_without_paginator(
    ctx: SiteContext,
    section: SectionConfig,
    posts: list[Post] | list[list[Post]],
) -> None:
    """Generate index page without pagination."""
    template = _resolve_template(ctx, section, "listing")

    # For custom page types, use the custom template here instead.
    if section.page_type == "custom":
        template = _resolve_template(ctx, section, "custom")

    first_post = posts[0] if posts else {}

    base_kwargs = _base_render_kwargs(ctx, section)

    rendered_html = template.render(
        body_class="details-page" if len(posts) == 1 else "",
        posts=posts,
        post=first_post,
        pagination=False,
        **base_kwargs,
    )

    section_dir = f"{OUTPUT_DIR}/{section.content_directory}/"
    create_directory(section_dir)
    file_path = os.path.join(section_dir, "index.html")
    write_to_file(file_path, rendered_html.encode("utf-8"))
    logger.info("Generated index page for %s", section.title)


def generate_content(
    ctx: SiteContext,
    section: SectionConfig,
    posts: list[Post],
) -> None:
    """Generate content pages (single posts)."""
    template = _resolve_template(ctx, section, "single")

    if section.page_type == "multiple":
        posts_directory = f"{OUTPUT_DIR}/{section.content_directory}/posts/"
    else:
        posts_directory = f"{OUTPUT_DIR}/{section.content_directory}/"

    create_directory(posts_directory)

    if section.page_type == "multiple":
        for post in posts:
            rendered_html = render_post(template, post, section.content_directory, True, ctx.site_dict, ctx.menu)
            slug_dir = f"{posts_directory}{post['slug']}/"
            create_directory(slug_dir)
            write_to_file(f"{slug_dir}index.html", rendered_html.encode("utf-8"))
        logger.info("Generated %d post page(s) for %s", len(posts), section.title)
    else:
        if not posts:
            logger.warning("No posts found for section: %s", section.title)
            return
        rendered_html = render_post(template, posts[0], section.content_directory, True, ctx.site_dict, ctx.menu)
        file_path = f"{posts_directory}index.html"
        write_to_file(file_path, rendered_html.encode("utf-8"))
        logger.info("Generated single page for %s", section.title)


def generate_json_section(ctx: SiteContext, section: SectionConfig) -> None:
    """Generate pages from JSON data (e.g. Resume)."""
    if section.data_type != "json":
        return

    json_file = f"data/{section.content_directory}.json"
    if not os.path.exists(json_file):
        logger.error("JSON data for the %s section not found: %s", section.title, json_file)
        return

    with open(json_file) as f:
        json_data = json.load(f)

    template = _resolve_template(ctx, section, "custom")

    # Fix #6: SimpleNamespace instead of anonymous namedtuple
    json_obj = _convert_json_to_namespace(json_data)

    rendered_html = template.render(
        data=json_obj,
        page={
            "title": section.seo.title,
            "description": section.seo.description,
        },
        site=ctx.site_dict,
        menu=ctx.menu,
    )

    section_dir = f"{OUTPUT_DIR}/{section.content_directory}/"
    create_directory(section_dir)
    file_path = os.path.join(section_dir, "index.html")
    write_to_file(file_path, rendered_html.encode("utf-8"))

    logger.info("%s section created", section.title)


def generate_json_export(ctx: SiteContext) -> None:
    """Export all posts to JSON."""
    json_data: dict[str, Any] = {"posts": list(ctx.all_posts)}

    json_directory = f"{OUTPUT_DIR}/json/"
    create_directory(json_directory)

    with open(json_directory + "posts.json", "w") as f:
        json.dump(json_data, f)

    logger.info("JSON export complete")


def _json_to_namespace(json_dict: dict[str, Any]) -> SimpleNamespace:
    """Convert a JSON dict to a SimpleNamespace (dot-accessible)."""
    return SimpleNamespace(**json_dict)


def _convert_json_to_namespace(json_dict: Any) -> Any:
    """Recursively convert nested JSON data to SimpleNamespace objects."""
    return json.loads(json.dumps(json_dict), object_hook=_json_to_namespace)
