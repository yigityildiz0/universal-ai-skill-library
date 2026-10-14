#!/usr/bin/env python3
"""Make labelled contact sheets (default 6 slides per sheet) from rendered slide PNGs.

Usage: python contact_sheet.py RENDER_DIR [--per 6] [--cols 2] [--width 800] [--out RENDER_DIR/sheets]
Needs Pillow. Without Pillow it prints the file list so the model can open images one by one.
"""
from __future__ import annotations
import argparse
import glob
import os
import sys


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("render_dir")
    ap.add_argument("--per", type=int, default=6)
    ap.add_argument("--cols", type=int, default=2)
    ap.add_argument("--width", type=int, default=800, help="tile width in px")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(a.render_dir, "*.png")))
    if not files:
        print("no PNG files in", a.render_dir)
        return 1
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("Pillow not installed; open these images directly:")
        print("\n".join(files))
        return 0
    out = a.out or os.path.join(a.render_dir, "sheets")
    os.makedirs(out, exist_ok=True)
    tw = a.width
    th = int(tw * 9 / 16)
    pad, lab = 10, 22
    for k in range(0, len(files), a.per):
        chunk = files[k:k + a.per]
        rows = (len(chunk) + a.cols - 1) // a.cols
        sheet = Image.new("RGB", (a.cols * (tw + pad) + pad, rows * (th + lab + pad) + pad), "#9aa3ab")
        d = ImageDraw.Draw(sheet)
        for i, f in enumerate(chunk):
            im = Image.open(f).convert("RGB").resize((tw, th))
            x = pad + (i % a.cols) * (tw + pad)
            y = pad + (i // a.cols) * (th + lab + pad)
            d.text((x + 2, y + 4), os.path.basename(f), fill="black")
            sheet.paste(im, (x, y + lab))
        name = os.path.join(out, f"sheet-{k // a.per + 1:02d}.jpg")
        sheet.save(name, quality=88)
        print(name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
