"""Pure utility functions extracted from ssg.py"""

from __future__ import annotations

import os
import re
import shutil
from datetime import date
from itertools import groupby
from typing import Any
from dateutil.parser import parse

def generate_slug(title: str) -> str:
    """Generate a slug based on the post title"""
    cleaned = "".join(c for c in title if c.isalnum() or c in (" ", "-"))
    return cleaned.lower().strip().replace(" ", "-")

def date_suffix(day: int) -> str:
    """Return day with ordinal suffix (e.g: 1st, 2nd, 3rd, 4th, etc.)"""
    return str(day) + ("th" if 4 <= day % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th"))

def format_date(dt: date, fmt: str) -> str:
    """Format a date with ordinal day suffix. Use {S} as a placeholder for the suffixed day."""
    return dt.strftime(fmt).replace('{S}', date_suffix(dt.day))

def convert_to_raw_date(date_time_str: str) -> str:
    """Convert a date string to YYYY-MM-DD format"""
    return "{0.year}-{0:%m}-{0:%d}".format(parse(date_time_str))

def get_file_index(path: str) -> int:
    """Extract the numeric index from a content file path.

    Raises ValueError if the path doesn't match the expected pattern.
    """
    match = re.search(r"content[\\/]\w+[\\/](\d+).*", path, re.IGNORECASE)
    if match is None:
        raise ValueError(f"Cannot extract file index from path: {path}")
    return int(match.group(1))


def generate_file_path(dt: date, directory: str, slug: str) -> str:
    """Generate a file path for a new blog post."""
    file_number = generate_file_number(directory)
    file_name = "_".join(["{:0>2}", "{}", "{:0>2}", "{:0>2}", "{}.md"])
    return directory + file_name.format(file_number, dt.year, dt.month, dt.day, slug)


def generate_file_number(path: str) -> int:
    """Generate the next sequential file number for a content directory."""
    from glob import glob

    existing_files = glob(path + "*.md")

    if not existing_files:
        return 1

    indexes = [get_file_index(filename) for filename in existing_files]
    return max(indexes) + 1


def estimate_reading_time(content: str) -> str:
    """Estimate the reading time of HTML content"""
    wpm = 200
    text = _extract_visible_text(content)
    word_count = len(text.split())
    minutes = max(1, round(word_count / wpm))
    return f"{minutes} minutes read" if minutes > 1 else "1 minute read"

def _extract_visible_text(html: str) -> str:
    """Extract visible text from HTML content"""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["style", "script", "head", "title", "pre", "code"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)

def archive_posts(posts: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    """Group posts by year in reverse chronological order."""
    sorted_posts = sorted(posts, key=lambda x: x["date_raw"], reverse=True)
    return [
        list(group)
        for _, group in groupby(sorted_posts, key=lambda y: y["date_raw"][:4])
    ]

def write_to_file(path: str, content: bytes) -> None:
    """Write content to a file"""
    with open(path, "wb") as f:
        f.write(content)

def create_directory(directory: str) -> None:
    """Create a directory (and parents) if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)

def delete_directory(directory: str) -> None:
    """Delete a directory if it exists"""
    if os.path.exists(directory):
        shutil.rmtree(directory)

def delete_file(filepath: str) -> None:
    """Delete a file if it exists"""
    if os.path.exists(filepath):
        os.remove(filepath)