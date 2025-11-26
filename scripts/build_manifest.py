#!/usr/bin/env python3
"""Create a unified manifest for lyrics, media, and catalogs.

This is an initial scaffold: it walks the new repo layout, captures useful metadata,
and emits a JSON document (and optionally a Parquet file if pandas/pyarrow are
installed). Downstream exporters + AI pipelines can depend on the manifest
without touching raw folders.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

ALLOWED_CONTENT_SUFFIXES = {".md", ".html", ".ipynb"}
ALLOWED_MEDIA_SUFFIXES = {".mp3", ".wav", ".flac", ".aiff", ".aif", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}


def read_front_matter(path: Path) -> Dict:
    """Very small YAML-ish parser for the top of Markdown files."""
    if path.suffix not in {".md", ".html"}:
        return {}
    content = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    if not content or content[0].strip() != "---":
        return {}
    data: Dict[str, str] = {}
    for line in content[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def collect_content(content_root: Path) -> List[Dict]:
    entries: List[Dict] = []
    for path in sorted(content_root.rglob("*")):
        if not path.is_file() or path.suffix not in ALLOWED_CONTENT_SUFFIXES:
            continue
        rel = path.relative_to(content_root.parent)
        fm = read_front_matter(path)
        entries.append(
            {
                "path": str(rel),
                "release": rel.parts[2] if len(rel.parts) > 2 else None,
                "title": fm.get("title"),
                "type": "notebook" if path.suffix == ".ipynb" else "lyric",
                "checksum": path.stat().st_mtime_ns,
            }
        )
    return entries


def collect_media(media_root: Path) -> List[Dict]:
    entries: List[Dict] = []
    for path in sorted(media_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in ALLOWED_MEDIA_SUFFIXES:
            continue
        rel = path.relative_to(media_root.parent)
        entries.append(
            {
                "path": str(rel),
                "size": path.stat().st_size,
                "checksum": path.stat().st_mtime_ns,
            }
        )
    return entries


def collect_catalogs(data_root: Path) -> List[Dict]:
    entries: List[Dict] = []
    for path in sorted(data_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".csv", ".json"}:
            continue
        rel = path.relative_to(data_root.parent)
        entries.append(
            {
                "path": str(rel),
                "size": path.stat().st_size,
            }
        )
    return entries


def maybe_write_parquet(manifest: List[Dict], path: Optional[Path]) -> None:
    if path is None:
        return
    try:
        import pandas as pd  # type: ignore
    except Exception as exc:  # pragma: no cover - optional dependency
        print(f"[build_manifest] Skipping Parquet export ({exc})")
        return
    df = pd.json_normalize(manifest)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the EverLight manifest")
    parser.add_argument("--content", type=Path, default=Path("content/lyrics"))
    parser.add_argument("--media", type=Path, default=Path("media"))
    parser.add_argument("--data", type=Path, default=Path("data"))
    parser.add_argument("--output", type=Path, default=Path("dist/manifest.json"))
    parser.add_argument("--parquet", type=Path, default=None)
    args = parser.parse_args()

    content_entries = collect_content(args.content.resolve())
    media_entries = collect_media(args.media.resolve())
    catalog_entries = collect_catalogs(args.data.resolve())

    manifest = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "counts": {
            "content": len(content_entries),
            "media": len(media_entries),
            "catalogs": len(catalog_entries),
        },
        "content": content_entries,
        "media": media_entries,
        "catalogs": catalog_entries,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    maybe_write_parquet(manifest["content"], args.parquet)
    print(f"[build_manifest] Wrote manifest with {manifest['counts']['content']} content entries → {args.output}")


if __name__ == "__main__":
    main()
