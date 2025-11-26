#!/usr/bin/env python3
"""Normalize content/media filenames and emit an asset map.

Current behavior is intentionally light-touch: it reports which files already
conform to slug-case naming and records their absolute + relative paths so other
scripts can update references or perform uploads. Future enhancements can add
actual renaming once the team signs off on the canonical slugs per release.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

SLUG_RE = re.compile(r"^[a-z0-9]+([\-_][a-z0-9]+)*$")
ALLOWED_CONTENT_SUFFIXES = {".md", ".html", ".ipynb"}
ALLOWED_MEDIA_SUFFIXES = {".mp3", ".wav", ".flac", ".aiff", ".aif", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}


def slugify(name: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", name.lower())
    cleaned = base.strip("-")
    return cleaned or "asset"


def ensure_unique(target: Path, slug: str) -> Path:
    candidate = target.with_name(f"{slug}{target.suffix}")
    suffix = 1
    while candidate.exists():
        candidate = target.with_name(f"{slug}-{suffix}{target.suffix}")
        suffix += 1
    return candidate


def collect_content(content_root: Path, apply: bool) -> Tuple[List[Dict], int]:
    entries: List[Dict] = []
    renamed = 0
    for path in sorted(content_root.rglob("*")):
        if not path.is_file() or path.suffix not in ALLOWED_CONTENT_SUFFIXES:
            continue
        slug_ok = SLUG_RE.match(path.stem) is not None
        slug = path.stem if slug_ok else slugify(path.stem)
        current_path = path
        needs = not slug_ok
        if apply and needs:
            target = ensure_unique(path, slug)
            target.parent.mkdir(parents=True, exist_ok=True)
            path.rename(target)
            current_path = target
            needs = False
            renamed += 1
        entries.append(
            {
                "type": "content",
                "relative_path": str(current_path.relative_to(content_root.parent)),
                "slug": slug,
                "needs_rename": needs,
            }
        )
    return entries, renamed


def collect_media(media_root: Path, apply: bool) -> Tuple[List[Dict], int]:
    entries: List[Dict] = []
    renamed = 0
    for path in sorted(media_root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in ALLOWED_MEDIA_SUFFIXES:
            continue
        slug_ok = SLUG_RE.match(path.stem) is not None
        slug = path.stem if slug_ok else slugify(path.stem)
        current_path = path
        needs = not slug_ok
        if apply and needs:
            target = ensure_unique(path, slug)
            target.parent.mkdir(parents=True, exist_ok=True)
            path.rename(target)
            current_path = target
            needs = False
            renamed += 1
        entries.append(
            {
                "type": "media",
                "relative_path": str(current_path.relative_to(media_root.parent)),
                "slug": slug,
                "needs_rename": needs,
            }
        )
    return entries, renamed


def main() -> None:
    parser = argparse.ArgumentParser(description="Normalize EverLight archive assets")
    parser.add_argument("--content", type=Path, default=Path("content/lyrics"), help="Content root to scan")
    parser.add_argument("--media", type=Path, default=Path("media"), help="Media root to scan")
    parser.add_argument("--output", type=Path, default=Path("dist/asset_map.json"), help="Where to write the asset map JSON")
    parser.add_argument("--apply", action="store_true", help="Rename files to match slug-case automatically")
    args = parser.parse_args()

    content_root = args.content.resolve()
    media_root = args.media.resolve()
    output_path = args.output.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    content_entries, content_renamed = collect_content(content_root, args.apply)
    media_entries, media_renamed = collect_media(media_root, args.apply)
    payload = content_entries + media_entries

    with output_path.open("w", encoding="utf-8") as fh:
        json.dump({"assets": payload}, fh, indent=2)

    renames = [a for a in payload if a["needs_rename"]]
    if args.apply:
        total = content_renamed + media_renamed
        print(f"[normalize_assets] Renamed {total} files. See {output_path} for updated map.")
    elif renames:
        print(f"[normalize_assets] {len(renames)} entries want slug-case filenames. See {output_path} for details.")
    else:
        print("[normalize_assets] All scanned files already follow slug-case naming.")


if __name__ == "__main__":
    main()
