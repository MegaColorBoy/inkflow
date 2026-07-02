"""Site context - replaces all global mutable state"""
from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from typing import Any

from jinja2 import Environment
from inkflow.config import Config
from inkflow.templates import site_config_to_dict

from inkflow.types import MenuItem, CategoryWithPosts, Post


@dataclass
class SiteContext:
    """Central state object threaded through all build functions."""
    config: Config
    env: Environment
    all_posts: list[Post] = field(default_factory=list)
    menu: list[MenuItem] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    categories_with_posts: list[CategoryWithPosts] = field(default_factory=list)

    @cached_property
    def site_dict(self) -> dict[str, Any]:
        """Site config as a dict for templates - computed once, cached."""
        return site_config_to_dict(self.config.site)