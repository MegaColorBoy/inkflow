from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

if sys.version_info >= (3, 10):
    import tomllib
else:
    try:
        import tomli as tomllib
    except ImportError as exc:
        raise ImportError("Python <3.10 requires the tomli package: pip install tomli") from exc


@dataclass
class SeoConfig:
    title: str
    description: str

@dataclass
class TemplateConfig:
    single: str | None = None
    listing: str | None = None
    main: str | None = None
    archive: str | None = None
    custom: str | None = None

@dataclass
class SectionConfig:
    title: str
    url: str
    page_type: str
    seo: SeoConfig
    content_directory: str = ""
    data_type: str = "markdown"
    display_in_menu: bool = False
    enable_listing: bool = False
    enable_pagination: bool = False
    show_in_recent_articles: bool = False
    template: TemplateConfig | None = None

@dataclass
class SiteConfig:
    name: str
    url: str
    author: str
    theme: str
    logo: str
    pagination_limit: int = 8
    enable_archive: bool = True
    enable_tags: bool = False
    export_rss_feed: bool = False
    export_json: bool = False
    rss_title: str = ""
    rss_description: str = "Writings, experiements & ideas."
    meta_template: str = ""

@dataclass
class Config:
    site: SiteConfig
    sections: list[SectionConfig] = field(default_factory=list)

def _parse_section(raw: dict[str, Any]) -> SectionConfig:
    """Parse a raw TOML section dict into a SectionConfig"""
    seo_raw = raw.get("seo", {})
    seo = SeoConfig(**seo_raw)
    
    template_raw = raw.get("template")
    template = TemplateConfig(**template_raw) if template_raw else None

    # pass the remaining keys (exclude seo and template)
    remaining = {k: v for k,v in raw.items() if k not in ("seo", "template")}

    return SectionConfig(seo=seo, template=template, **remaining)

def load_config(config_path: Path | str = "site.toml") -> Config:
    """Load and validate configuration from a TOML file."""
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")


    with open(config_path, "rb") as f:
        raw = tomllib.load(f)

    site_raw = raw.get("site")
    if not site_raw:
        raise KeyError("Missing required [site] table in config")

    site = SiteConfig(**site_raw)

    sections_raw = raw.get("sections", [])
    sections = [_parse_section(s) for s in sections_raw]

    return Config(site=site, sections=sections)




