#!/usr/bin/env python3
"""Make web-sized previews from source PNGs.

Usage:
    python3 scripts/make_previews.py SRC DST [--width 1200] [--quality 85]
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("src", type=Path)
    parser.add_argument("dst", type=Path)
    parser.add_argument("--width", type=int, default=1200)
    parser.add_argument("--quality", type=int, default=85)
    args = parser.parse_args()

    with Image.open(args.src) as im:
        im = im.convert("RGB")
        if im.width > args.width:
            height = round(im.height * args.width / im.width)
            im = im.resize((args.width, height), Image.Resampling.LANCZOS)
        args.dst.parent.mkdir(parents=True, exist_ok=True)
        im.save(args.dst, "WEBP", quality=args.quality, method=6)
    print(f"{args.dst}  {args.dst.stat().st_size // 1024} KiB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
