"""Assets synchorization -- replacement for syncAssets.sh

Compile SCSS files (if sass CLI is available) and copies static assets
from the theme directory into output/static/
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from pathlib import Path

from inkflow.builder import OUTPUT_DIR
from inkflow.templates import TEMPLATES_DIR

logger = logging.getLogger(__name__)

# Directories to copy from theme to output/static/
ASSET_DIRS = (
    "css",
    "fonts",
    "vendor",
    "til_images",
    "js",
    "projects",
    "favicon",
    "images"
)

class ThemeNotFoundError(Exception):
    """Raised when the theme directory is not found."""

def _find_scss_files(theme_dir: Path) -> list[tuple[Path, Path]]:
    """Discover SCSS files and their corresponding CSS output paths"""
    scss_dir = theme_dir / "scss"
    css_dir = theme_dir / "css"
    pairs: list[tuple[Path, Path]] = []

    if not scss_dir.is_dir():
        return pairs

    for scss_file in sorted(scss_dir.glob("*.scss")):
        # Skip partials
        if scss_file.name.startswith("_"):
            continue
        css_file = css_dir / scss_file.with_suffix(".css").name
        pairs.append((scss_file, css_file))

    return pairs

def compile_scss(theme_dir: Path) -> bool:
    """Compile SCSS files and their corresponding CSS output paths using SASS CLI
    Return True if success
    Return False if sass is not available and if the files exist.
    """
    pairs = _find_scss_files(theme_dir)
    if not pairs:
        logger.info("No SCSS files found in theme directory, skipping compilation.")
        return True

    # Check if SASS is installed on the system
    sass_cmd = shutil.which("sass")
    if sass_cmd is None:
        logger.warning("'sass' is not installed, skipping compilation. Install it with: npm install -g sass")
        return False

    # Ensure CSS output directory exists
    css_dir = theme_dir / "css"
    css_dir.mkdir(parents=True, exist_ok=True)

    for scss_src, css_dst in pairs:
        logger.info("Compiling %s -> %s", scss_src.name, css_dst.name)
        result = subprocess.run(
            [sass_cmd, str(scss_src), str(css_dst), "--style=compressed"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            logger.error("Error compiling %s:\n%s", scss_src.name, result.stderr)
            return False

    return True

def sync_assets(theme: str, output_dir: str = OUTPUT_DIR) -> None:
    theme_dir = Path(TEMPLATES_DIR) / theme
    static_dir = Path(output_dir) / "static"

    if not theme_dir.is_dir():
        raise ThemeNotFoundError(f"Theme directory '{theme_dir}' not found.")

    # Step 1: Compile SCSS
    logger.info("Compiling SCSS...")
    compile_scss(theme_dir)

    # Step 2 & 3: Remove stale directories and copy fresh
    for dirname in ASSET_DIRS:
        src = theme_dir / dirname
        dst = static_dir / dirname

        print(src, dst)

        if dst.exists():
            shutil.rmtree(dst)

        if src.is_dir():
            logger.info("Copying %s/", dirname)
            shutil.copytree(src, dst)
        else:
            logger.info("Skipping %s/ (not found in theme)", dirname)

    # Step 4: Copy individual assets
    for filename in _find_root_assets(theme_dir):
        src = theme_dir / filename
        dst = static_dir / filename
        dst.parent.mkdir(parents=True, exist_ok=True)
        logger.info("Copying %s/", filename)
        shutil.copy2(src, dst)

    # Step 5: Copy custom files
    # shutil.copy2(theme_dir / "resume.pdf", static_dir / "resume.pdf")
    # shutil.copy2(theme_dir / "logo.png", static_dir / "logo.png")
    # shutil.copy2(theme_dir / "logo.gif", static_dir / "logo.gif")

    logger.info("Assets synced.")

def _find_root_assets(theme_dir: Path) -> list[str]:
    """Find all assets under theme directory"""
    asset_extensions = {".png", ".gif", ".ico", ".svg", ".jpg", ".jpeg", ".webp", ".pdf"}
    assets: list[str] = []
    for entry in sorted(theme_dir.iterdir()):
        if entry.is_file() and entry.suffix.lower() in asset_extensions:
            assets.append(entry.name)
    return assets