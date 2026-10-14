#!/usr/bin/env python3
"""Audit a finished PDF for the faults AI-made documents usually have.

Usage:  python pdf_audit.py file.pdf [--render OUTDIR] [--dpi 80] [--min-pt 8] [--margin-mm 8]
Needs PyMuPDF for the full audit:  python -m pip install pymupdf
Without it, a reduced stdlib check (header, page count, font embedding hints) runs and says so.

Reports (ERROR fails, exit 1; WARN needs a look):
  ERROR  text outside the page or inside the unsafe edge band, text clipped by the page
  ERROR  missing-glyph characters (U+FFFD, .notdef boxes) in extracted text
  ERROR  overlapping text blocks (one on top of another)
  WARN   heading stranded at the bottom of a page (orphan heading)
  WARN   table/figure cut by a page break (table bbox touching the bottom, same table continuing on the next page)
  WARN   table continued without a repeated header row
  WARN   fonts not embedded, text smaller than --min-pt, blank or almost blank pages, mixed page sizes,
         low-resolution images, missing title metadata
--render writes PNGs so you can LOOK at every page (reading the images is part of the job).
"""
from __future__ import annotations

import argparse
import os
import re
import statistics
import sys

try:
    import pymupdf as fitz  # PyMuPDF >= 1.24
except ImportError:  # pragma: no cover
    try:
        import fitz  # older PyMuPDF
    except ImportError:
        fitz = None


def stdlib_check(path: str) -> int:
    data = open(path, "rb").read()
    print(f"pdf_audit (reduced, PyMuPDF missing): {os.path.basename(path)} {len(data) // 1024} KB")
    if not data.startswith(b"%PDF-"):
        print("  ERROR: not a PDF header")
        return 1
    pages = len(re.findall(rb"/Type\s*/Page[^s]", data))
    print(f"  pages ≈ {pages}")
    fonts = len(re.findall(rb"/Type\s*/Font\b", data))
    files = len(re.findall(rb"/FontFile[23]?\b", data))
    print(f"  fonts ≈ {fonts}, embedded font files ≈ {files}" + ("  WARN: some fonts may not be embedded" if files < fonts else ""))
    print("  install PyMuPDF (python -m pip install pymupdf) for geometry checks: cut tables, orphan headings, overflow, overlaps")
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--render", default=None)
    ap.add_argument("--dpi", type=int, default=80)
    ap.add_argument("--min-pt", type=float, default=8.0)
    ap.add_argument("--margin-mm", type=float, default=8.0, help="unsafe edge band: text closer than this to the page edge is an error")
    a = ap.parse_args()
    if fitz is None:
        return stdlib_check(a.pdf)
    doc = fitz.open(a.pdf)
    E, W = [], []
    mm = 72 / 25.4
    band = a.margin_mm * mm
    sizes = {(round(p.rect.width), round(p.rect.height)) for p in doc}
    if len(sizes) > 1:
        W.append(f"mixed page sizes {sorted(sizes)} — intended only for deliberate landscape sections")
    if not (doc.metadata or {}).get("title"):
        W.append("no title metadata (set <title>)")
    all_sizes = []
    page_info = []
    for pno, page in enumerate(doc, 1):
        rect = page.rect
        blocks = page.get_text("dict")["blocks"]
        tb = [b for b in blocks if b["type"] == 0]
        text = page.get_text()
        if len(text.strip()) < 12 and not page.get_images():
            W.append(f"p{pno}: blank or almost blank page (stray break?)")
        if "�" in text or "�" in text:
            E.append(f"p{pno}: missing-glyph character (U+FFFD) in text — a font lacks a letter (Turkish ı ğ ş İ?)")
        spans = []
        for b in tb:
            for ln in b["lines"]:
                for sp in ln["spans"]:
                    if sp["text"].strip():
                        spans.append(sp)
                        all_sizes.append(sp["size"])
                        x0, y0, x1, y1 = sp["bbox"]
                        if x0 < -1 or y0 < -1 or x1 > rect.width + 1 or y1 > rect.height + 1:
                            E.append(f"p{pno}: text outside the page: “{sp['text'][:40]}”")
                        elif x0 < band or x1 > rect.width - band or y0 < band * 0.8 or y1 > rect.height - band * 0.8:
                            if not re.fullmatch(r"\s*\d+\s*(/\s*\d+)?\s*", sp["text"]):   # page numbers may sit in the margin
                                E.append(f"p{pno}: text inside the unsafe edge band (<{a.margin_mm:g} mm): “{sp['text'][:40]}”")
                        if sp["size"] < a.min_pt and not re.fullmatch(r"\s*\d+\s*(/\s*\d+)?\s*", sp["text"]):
                            W.append(f"p{pno}: text {sp['size']:.1f} pt < {a.min_pt:g} pt: “{sp['text'][:30]}”")
        # overlapping text blocks
        rects = [fitz.Rect(b["bbox"]) for b in tb]
        for i in range(len(rects)):
            for j in range(i + 1, len(rects)):
                inter = rects[i] & rects[j]
                if inter.is_empty:
                    continue
                ar = min(rects[i].get_area(), rects[j].get_area())
                if ar > 0 and inter.get_area() / ar > 0.25:
                    E.append(f"p{pno}: overlapping text blocks near y={inter.y0:.0f}")
                    break
        # fonts
        for f in page.get_fonts(full=True):
            xref, ext, name = f[0], f[1], f[3]
            if ext in ("n/a", "") and not re.match(r"(Helvetica|Times|Courier|Symbol|ZapfDingbats)", name or "") and name:
                W.append(f"p{pno}: font {name} not embedded — may change on another computer")
        # images: effective dpi
        for im in page.get_images(full=True):
            try:
                for r in page.get_image_rects(im[0]):
                    w_in = r.width / 72
                    if w_in > 0.5 and im[2] / w_in < 110:
                        W.append(f"p{pno}: image {im[2]}px over {w_in:.1f} in ≈ {im[2] / w_in:.0f} dpi — blurry in print")
            except Exception:  # noqa: BLE001
                pass
        page_info.append((page, tb, spans))
    body = statistics.median(all_sizes) if all_sizes else 11
    # orphan heading: last text line on page is heading-like (bigger/bold) and nothing follows on that page
    for pno, (page, tb, spans) in enumerate(page_info, 1):
        if not spans:
            continue
        content = [sp for sp in spans if sp["bbox"][3] < page.rect.height - band * 2.2]
        if not content:
            continue
        last = max(content, key=lambda s: s["bbox"][3])
        heading_like = last["size"] >= body * 1.18 or (("bold" in last["font"].lower() or last["flags"] & 16) and last["size"] >= body * 1.05 and len(last["text"]) < 90)
        if heading_like and pno < len(page_info) and last["bbox"][3] > page.rect.height * 0.80:
            W.append(f"p{pno}: heading “{last['text'][:50]}” is stranded at the bottom — keep it with the next block (break-after: avoid)")
    # tables
    try:
        for pno, (page, tb, spans) in enumerate(page_info, 1):
            tabs = page.find_tables().tables
            for t in tabs:
                bottom_gap = page.rect.height - t.bbox[3]
                if bottom_gap < band * 2.6 and pno < len(page_info):
                    nxt = page_info[pno][0]
                    cont = nxt.find_tables().tables
                    if cont and abs(cont[0].bbox[0] - t.bbox[0]) < 12 and cont[0].bbox[1] < band * 4.5:
                        first = ""
                        try:
                            first = " ".join((t.extract()[0] or [""])[:3])
                            nfirst = " ".join((cont[0].extract()[0] or [""])[:3])
                        except Exception:  # noqa: BLE001
                            nfirst = ""
                        if first and first == nfirst:
                            continue  # header repeated: acceptable split between rows
                        W.append(f"p{pno}-{pno + 1}: table continues on the next page without a repeated header row; check rows are not cut")
                    elif bottom_gap < band * 1.4 and not cont:
                        W.append(f"p{pno}: table ends flush with the bottom edge — a row may be clipped or cut; look at the page")
    except Exception:  # noqa: BLE001
        W.append("table analysis unavailable in this PyMuPDF version (upgrade to ≥1.23)")
    if a.render:
        os.makedirs(a.render, exist_ok=True)
        for pno, page in enumerate(doc, 1):
            page.get_pixmap(dpi=a.dpi).save(os.path.join(a.render, f"page-{pno:02d}.png"))
    # de-duplicate, keep order
    def uniq(xs):
        seen, out = set(), []
        for x in xs:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out
    E, W = uniq(E), uniq(W)
    print(f"pdf_audit: {os.path.basename(a.pdf)}: {len(doc)} page(s), body ≈ {body:.1f} pt, {len(E)} error(s), {len(W)} warning(s)")
    for e in E[:40]:
        print("  ERROR:", e)
    for w in W[:60]:
        print("  warn: ", w)
    if a.render:
        print(f"  rendered pages → {a.render} (open and read every page)")
    print("RESULT:", "FAIL" if E else ("PASS with warnings" if W else "PASS"))
    return 1 if E else 0


if __name__ == "__main__":
    sys.exit(main())
