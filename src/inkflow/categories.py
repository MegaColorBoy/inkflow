"""Category generation"""
from collections import defaultdict

from inkflow.builder import OUTPUT_DIR, logger
from inkflow.context import SiteContext
from inkflow.types import Post, CATEGORY_SEPARATOR, CategoryWithPosts, build_category_link
from inkflow.utils import delete_directory, create_directory, write_to_file, generate_slug, archive_posts


def generate_categories(ctx: SiteContext) -> None:
    """Collect category metadata and render category pages"""
    _collect_categories(ctx)
    _render_category_pages(ctx)

def _collect_categories(ctx: SiteContext) -> None:
    """Bucket posts by category and store results on the site context.

    Sets ctx.categories (list of names) and ctx.categories_with_posts (list of dicts, sorted by count descending).
    """
    if not ctx.all_posts:
        ctx.categories = []
        ctx.categories_with_posts = []
        logger.info("No posts - skipping category collection")
        return

    category_posts: dict[str, list[Post]] = defaultdict(list)
    for post in ctx.all_posts:
        for cat in post["category"].split(CATEGORY_SEPARATOR):
            cat = cat.strip()
            category_posts[cat].append(post)

    if not category_posts:
        logger.info("No categories - skipping category collection")
        return

    categories_with_posts: list[CategoryWithPosts] = []
    for cat_title, posts in category_posts.items():
        slug = generate_slug(cat_title)
        categories_with_posts.append(CategoryWithPosts(
            title=cat_title,
            slug=slug,
            link=build_category_link(cat_title, slug)["link"],
            posts=archive_posts(posts),
            count=len(posts),
        ))

    # Sort by count descending
    categories_with_posts.sort(key=lambda x: x["count"], reverse=True)

    ctx.categories = list(category_posts.keys())
    ctx.categories_with_posts = categories_with_posts

    logger.info("Collected %d category/categories from %d posts", len(ctx.categories), len(ctx.all_posts))


def _render_category_pages(ctx: SiteContext) -> None:
    """Write an HTML index page for each category."""
    if not ctx.categories_with_posts:
        return

    category_dir = f"{OUTPUT_DIR}/category/"
    delete_directory(category_dir)

    template = ctx.env.get_template("category.html")

    for category in ctx.categories_with_posts:
        directory = f"{category_dir}{category['slug']}/"

        rendered_html = template.render(
            body_class="",
            posts=category["posts"],
            page={
                "title": category["title"],
                "description": f"There are <b>{category['count']}</b> posts linked to this category.",
                "count": category["count"],
            },
            pagination=False,
            site=ctx.site_dict,
            menu=ctx.menu,
        )

        create_directory(directory)
        write_to_file(f"{directory}/index.html", rendered_html.encode("utf-8"))

    logger.info("Rendered %d category page(s)", len(ctx.categories_with_posts))