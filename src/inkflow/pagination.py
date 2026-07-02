"""Pagination logic."""

from __future__ import annotations

import math

from inkflow.types import PaginationLink


def calculate_page_count(total_posts: int, per_page: int) -> int:
    """Calculate total number of pages needed."""
    if per_page <= 0:
        return 1
    return math.ceil(total_posts / per_page)


def build_page_url(base_directory: str, page_number: int) -> str:
    """Build the URL for a given page number."""

    base = base_directory.strip("/")

    if page_number <= 1:
        return f"/{base}/" if base else "/"

    return f"/{base}/pages/{page_number}" if base else f"/pages/{page_number}"


def generate_pagination_links(base_directory: str, current: int, total_pages: int) -> list[PaginationLink]:
    """Generate pagination link dicts with optional ellipsis markers."""
    delta = 2
    left = current - delta
    right = current + delta + 1

    # Collect the page numbers that should be shown
    visible_pages: list[int] = []
    for i in range(1, total_pages + 1):
        if i == 1 or i == total_pages or (left <= i < right):
            visible_pages.append(i)

    # Build links, inserting ellipsis markers for gaps
    links: list[PaginationLink] = []
    prev_page: int | None = None

    for page in visible_pages:
        if prev_page is not None:
            gap = page - prev_page
            if gap == 2:
                # Single missing page — show it directly instead of dots
                links.append(
                    PaginationLink(
                        url=build_page_url(base_directory, prev_page + 1),
                        page=prev_page + 1,
                        has_dots=False,
                    )
                )
            elif gap > 2:
                # Multiple missing pages — show dots
                links.append(
                    PaginationLink(
                        url=build_page_url(base_directory, prev_page + 1),
                        page=prev_page + 1,
                        has_dots=True,
                    )
                )

        links.append(
            PaginationLink(
                url=build_page_url(base_directory, page),
                page=page,
                has_dots=False,
            )
        )

        prev_page = page

    return links
