"""Built-in dev server with file-watching and auto-rebuild.

Replaces the need for `live-server <output_dir>`.
"""

from __future__ import annotations

import contextlib
import functools
import logging
import os
import threading
from collections.abc import Callable
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

from inkflow.builder import OUTPUT_DIR

logger = logging.getLogger(__name__)


class _QuietHandler(SimpleHTTPRequestHandler):
    """HTTP handler that serves from a configurable directory and suppresses routine logs."""

    def __init__(self, *args: object, directory: str = OUTPUT_DIR, **kwargs: object) -> None:
        super().__init__(*args, directory=directory, **kwargs)  # type: ignore[arg-type]

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        # Only log errors (status >= 400), not every 200/304
        if args and isinstance(args[1], str) and not args[1].startswith(("4", "5")):
            return
        super().log_message(format, *args)

    def do_GET(self) -> None:
        # Serve index.html for directory paths (clean URLs)
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            index = os.path.join(path, "index.html")
            if os.path.isfile(index):
                self.path = self.path.rstrip("/") + "/index.html"
        super().do_GET()


def _collect_mtimes(directories: list[str], extensions: set[str]) -> dict[str, float]:
    """Walk directories and collect file modification times."""
    mtimes: dict[str, float] = {}
    for directory in directories:
        for root, _dirs, files in os.walk(directory):
            for filename in files:
                if any(filename.endswith(ext) for ext in extensions):
                    filepath = os.path.join(root, filename)
                    with contextlib.suppress(OSError):
                        mtimes[filepath] = os.path.getmtime(filepath)
    return mtimes


def _watch_and_rebuild(
    watch_dirs: list[str],
    rebuild_fn: Callable[[], None],
    interval: float = 1.0,
    stop_event: threading.Event | None = None,
) -> None:
    """Poll for file changes and trigger a rebuild callback."""
    extensions = {".md", ".html", ".toml", ".json", ".scss", ".css"}
    existing_dirs = [d for d in watch_dirs if os.path.isdir(d)]

    if not existing_dirs:
        logger.warning("No watch directories found, file watching disabled.")
        return

    prev_mtimes = _collect_mtimes(existing_dirs, extensions)
    _stop = stop_event or threading.Event()

    while not _stop.is_set():
        _stop.wait(interval)
        if _stop.is_set():
            break

        curr_mtimes = _collect_mtimes(existing_dirs, extensions)

        if curr_mtimes != prev_mtimes:
            changed = set(curr_mtimes.keys()) ^ set(prev_mtimes.keys())
            for filepath in set(curr_mtimes.keys()) & set(prev_mtimes.keys()):
                if curr_mtimes[filepath] != prev_mtimes[filepath]:
                    changed.add(filepath)

            if changed:
                short_names = [os.path.basename(f) for f in list(changed)[:5]]
                suffix = f" (+{len(changed) - 5} more)" if len(changed) > 5 else ""
                logger.info("Change detected: %s%s", ", ".join(short_names), suffix)
                logger.info("Rebuilding...")

                try:
                    rebuild_fn()
                    logger.info("Rebuild complete. Refresh your browser.")
                except Exception:
                    logger.exception("Rebuild error")

            prev_mtimes = curr_mtimes


def serve(
    output_dir: str = OUTPUT_DIR,
    port: int = 8000,
    host: str = "localhost",
    watch: bool = True,
    rebuild_fn: Callable[[], None] | None = None,
) -> None:
    """Start an HTTP dev server, optionally watching for file changes.

    Args:
        output_dir: Directory to serve (default: OUTPUT_DIR).
        port: Port to bind to (default: 8000).
        host: Host to bind to (default: "localhost").
        watch: Whether to watch for file changes and auto-rebuild.
        rebuild_fn: Callable to invoke on file changes. If None, watching is disabled.
    """
    output_path = Path(output_dir)
    if not output_path.is_dir():
        raise FileNotFoundError(f"Output directory '{output_dir}' not found. Run `ssg build --mode all` first.")

    handler = functools.partial(_QuietHandler, directory=str(output_path.resolve()))
    server = HTTPServer((host, port), handler)

    stop_event = threading.Event()
    watcher_thread: threading.Thread | None = None

    if watch and rebuild_fn is not None:
        watch_dirs = ["content", "templates", "data", "."]
        watcher_thread = threading.Thread(
            target=_watch_and_rebuild,
            args=(watch_dirs, rebuild_fn, 1.0, stop_event),
            daemon=True,
        )
        watcher_thread.start()
        logger.info("File watching enabled (content/, templates/, data/, site.toml)")

    logger.info("Serving %s/ at http://%s:%d/", output_dir, host, port)
    logger.info("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        stop_event.set()
        server.shutdown()
        if watcher_thread is not None:
            watcher_thread.join(timeout=2)
