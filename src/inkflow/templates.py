"""Jinja2 env setup and render helpers"""

from __future__ import annotations

import dataclasses
from typing import Any
from jinja2 import Environment, FileSystemLoader, Template

from inkflow.config import SiteConfig
from inkflow.types import MenuItem, Post

TEMPLATES_DIR = "templates"

def create_jinja_env(site: SiteConfig) -> Environment:
    """Create jinja environment

    Uses FileSystemLoader to load jinja templates for better compatibility with the new src layout.
    """
    template_dir = f"{TEMPLATES_DIR}/{site.theme}"
    return Environment(loader=FileSystemLoader(template_dir))

def render_post(
    template: Template,
    post: Post,
    content_directory: str,
    generate_meta: bool,
    site_dict: dict[str, Any],
    menu: list[MenuItem]
) -> str:
    """Render post template"""
    return template.render(
        post=post,
        content_directory=content_directory,
        generate_meta=generate_meta,
        page={
            "title": post["title"],
            "description": post.get("summary", ""),
            "url": post["link"]
        },
        site_dict=site_dict,
        menu=menu
    )

def site_config_to_dict(site: SiteConfig) -> dict[str, Any]:
    """Convert site config to dict"""
    return dataclasses.asdict(site)