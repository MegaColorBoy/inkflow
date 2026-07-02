"""Parsing of markdown content and loading of posts"""
from __future__ import annotations
import logging
from datetime import datetime
from pathlib import Path

import markdown2
from dateutil.parser import parse

from inkflow.config import Config, SectionConfig
from inkflow.types import Post, build_category_link, CATEGORY_SEPARATOR
from inkflow.utils import get_file_index, convert_to_raw_date, generate_slug, estimate_reading_time

logger = logging.getLogger(__name__)

REQUIRED_METADATA_KEYS = ("title", "date", "slug", "category")
CONTENT_DIR = "content"

def load_posts(config: Config) -> list[Post]:
    """Load all posts from content directories defined in config."""
    return _get_posts(config.sections)

def _get_posts(sections: list[SectionConfig]) -> list[Post]:
    """Parse markdown files from all sections into post dicts."""
    posts: list[Post] = []
    extras = ["metadata", "code-friendly", "fenced-code-blocks"]

    for section in sections:
        if section.page_type in "archive":
            continue

        # Skip if empty
        if not section.content_directory:
            continue

        # The directory of the targeted section
        content_path = Path(CONTENT_DIR) / section.content_directory

        # Ensure that the directory exists
        if not content_path.is_dir():
            logger.warning("Content directory does not exist: %s", content_path)
            continue

        for md_file in sorted(content_path.iterdir()):
            # Ensure that it's a valid markdown file
            if not md_file.is_file() or md_file.suffix != ".md":
                continue

            post = _parse_post(md_file, section, extras)
            if post is not None:
                posts.append(post)

    # Sort posts by date (most recent first)
    posts.sort(key=lambda post: post["date_raw"], reverse=True)
    return posts

def _parse_post(file_path: Path, section: SectionConfig, extras: list[str]) -> Post | None:
    """Parse markdown file into post dict.

    Returns None for posts that are missing required metadata keys or if the date is unparseable.
    or if the posts are inactive/drafted.
    """
    with open(file_path) as f:
        post_content = markdown2.markdown(f.read(), extras=extras)

    metadata = getattr(post_content, "metadata", {})
    if metadata is None:
        metadata = {}

    status = metadata.get("status", "active")
    if status != "active":
        return None

    missing = [key for key in REQUIRED_METADATA_KEYS if key not in metadata]
    if missing:
        logger.warning("Skipping %s: Missing required metadata: %s", file_path, ", ".join(missing))
        return None

    try:
        index = get_file_index(str(file_path))
    except ValueError:
        logger.warning("Skipping %s: could not extract file index", file_path)
        return None

    title = metadata["title"]
    post_date = metadata["date"]

    try:
        date_raw = convert_to_raw_date(post_date)
        parsed_date = parse(post_date)
        date_alt = f"{parsed_date:%d}.{parsed_date:%m}.{parsed_date.year}"
        post_year = datetime.fromisoformat(date_raw).strftime("%Y")
    except (ValueError, OverflowError) as exc:
        logger.warning("Skipping %s: could not parse date %r: %s", file_path, post_date, exc)
        return None

    slug = metadata["slug"]
    category = metadata["category"]

    categories_list = [
        build_category_link(cat.strip(), generate_slug(cat.strip()))
        for cat in category.split(CATEGORY_SEPARATOR)
    ]

    summary = metadata.get("summary", "")
    reading_time = estimate_reading_time(str(post_content))
    preview_image_url = metadata.get("preview_image_url", "")

    # e.g: about/ or resume/
    if section.page_type in ("single", "custom"):
        post_url = section.content_directory
    # e.g: writings/posts/hello-world
    else:
        post_url = "/".join([section.content_directory, "posts", slug])

    return Post(
        section=section.content_directory,
        title=title,
        link=post_url,
        date=post_date,
        date_alt=date_alt,
        year=post_year,
        date_raw=date_raw,
        slug=slug,
        category=category,
        categories=categories_list,
        summary=summary,
        reading_time=reading_time,
        preview_image_url=preview_image_url,
        filename=str(file_path),
        status=status,
        content=post_content,
        index=index,
    )

def get_posts_by_content_directory(
    all_posts: list[Post],
    content_directories: list[str]
) -> list[Post]:
    """Filter posts by content directory/section."""
    return [post for post in all_posts if post["section"] in content_directories]

def get_recent_articles(all_posts: list[Post], sections: list[SectionConfig]) -> list[Post]:
    """Get posts from sections marked as show_in_recent_articles."""
    content_directories = [s.content_directory for s in sections if s.show_in_recent_articles]
    return get_posts_by_content_directory(all_posts, content_directories)