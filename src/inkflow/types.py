from __future__ import annotations

from typing import Any, TypedDict

# Separator used for multiple categories (e.g: Python + Javascript)
CATEGORY_SEPARATOR = "+"


class CategoryLink(TypedDict):
    title: str
    link: str

def build_category_link(category_title: str, slug: str) -> CategoryLink:
    """Build a category link dict from a title and slug."""
    return CategoryLink(title=category_title, link=f"/category/{slug}/")

class Post(TypedDict):
    section: str
    title: str
    link: str
    date: str
    date_alt: str
    year: str
    date_raw: str
    slug: str
    category: str
    categories: list[CategoryLink]
    summary: str
    reading_time: str
    preview_image_url: str
    filename: str
    status: str
    content: Any
    index: int

class MenuItem(TypedDict):
    link: str
    title: str

class CategoryWithPosts(TypedDict):
    title: str
    slug: str
    link: str
    posts: list[list[Post]] # grouped by year via archive_posts
    count: int

class PaginationLink(TypedDict):
    url: str
    page: int
    has_dots: bool
