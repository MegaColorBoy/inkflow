"""RSS Feed generation"""
from __future__ import annotations

import logging
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import format_datetime

from inkflow.builder import OUTPUT_DIR, logger
from inkflow.config import SiteConfig
from inkflow.types import Post
from inkflow.utils import create_directory

def _post_date_to_rfc822(post: Post) -> str:
    """Convert a post's date_raw (YYYY-MM-DD) to RFC 822 format for RSS.

    Falls back to the raw date string if date_raw is missing or unparseable.
    """
    date_raw = post.get("date_raw", "")

    if date_raw:
        try:
            dt = datetime.fromisoformat(date_raw).replace(tzinfo=timezone.utc)
            return format_datetime(dt, usegmt=True)
        except (ValueError, OverflowError):
            pass

    # Fallback: return the human-readable date as-is
    return post.get("date", "")

def _build_absolute_url(site_url: str, path: str) -> str:
    """Combine site URL and relative path into an absolute URL."""
    base = site_url.rstrip("/")
    path = path.lstrip("/")
    return f"{base}/{path}"

def generate_rss_feed(
    posts: list[Post],
    output_dir: str = OUTPUT_DIR,
    site: SiteConfig | None = None,
) -> None:
    """Generate an RSS feed XML file using ElementTree.

    Produces well-formed XML with proper escaping and RFC 822 dates.
    """
    if site is None:
        logger.error("SiteConfig is required for RSS feed generation")
        return

    create_directory(output_dir + "/")

    # Build the XML tree
    rss = ET.Element("rss", version="2.0")
    rss.set("xmlns:atom", "http://www.w3.org/2005/Atom")

    channel = ET.SubElement(rss, "channel")

    rss_title = site.rss_title if site.rss_title else site.name

    ET.SubElement(channel, "title").text = rss_title
    ET.SubElement(channel, "link").text = site.url
    ET.SubElement(channel, "description").text = site.rss_description

    atom_link = ET.SubElement(channel, "atom:link")
    atom_link.set("href", site.url)
    atom_link.set("rel", "self")
    atom_link.set("type", "application/rss+xml")

    for post in posts:
        item = ET.SubElement(channel, "item")

        ET.SubElement(item, "title").text = post["title"]

        absolute_url = _build_absolute_url(site.url, post["link"])
        ET.SubElement(item, "link").text = absolute_url

        guid = ET.SubElement(item, "guid")
        guid.set("isPermaLink", "true")
        guid.text = absolute_url

        ET.SubElement(item, "pubDate").text = _post_date_to_rfc822(post)

        raw_summary = post.get("summary", "")
        ET.SubElement(item, "description").text = raw_summary if raw_summary else post["title"]

    ET.indent(rss, space="  ")
    tree = ET.ElementTree(rss)

    file_path = output_dir + "/rss.xml"
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

    logger.info("RSS Feed Generated.")