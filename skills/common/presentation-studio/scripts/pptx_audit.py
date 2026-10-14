#!/usr/bin/env python3
"""Audit any .pptx against the presentation contract. Standard library only.

Usage:
  python pptx_audit.py deck.pptx [--min 36] [--allow "source=12,references=12,slideNumber=10,kicker=18,credit=10"]
                                 [--fonts "Arial,Calibri"] [--wpm 112] [--pause 7] [--target 30-45]
                                 [--forbid "bu akşam,lorem"] [--json report.json]

Checks (hard = exit code 1):
  hard  text below the floor size outside a declared exception role
  hard  shape outside the slide, forbidden phrase on a slide, unreadable file
  warn  non-safe font, inherited (unknown) size, text-only slide, same layout 3x in a row,
        content slide without a source line, missing speaker notes, decorative full-width
        bar or title underline, very dense slide, timing outside target
Roles are inferred from shape names (kit names: "Kaynak satiri", "Kaynakca", "Slayt no",
"Ust etiket", "Gorsel kredisi") or text patterns ("Kaynak:", "Source:", references slide).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
EMU = 914400
SAFE = ["Arial", "Calibri", "Cambria", "Times New Roman", "Georgia", "Verdana", "Tahoma"]
ROLE_PATTERNS = [
    ("source", re.compile(r"kaynak sat|source|citation|atıf", re.I)),
    ("references", re.compile(r"kaynakça|kaynakca|references|bibliograph", re.I)),
    ("slideNumber", re.compile(r"slayt no|slide number|sldnum", re.I)),
    ("kicker", re.compile(r"ust etiket|üst etiket|baslik etiketi|başlık etiketi|kicker|eyebrow", re.I)),
    ("credit", re.compile(r"kredi|credit|telif", re.I)),
]
DEFAULT_ALLOW = {"source": 16, "references": 16, "slideNumber": 14, "kicker": 20, "credit": 14}


def q(tag: str) -> str:
    ns, t = tag.split(":")
    return "{%s}%s" % (NS[ns], t)


def slide_order(z: zipfile.ZipFile) -> list[str]:
    pres = ET.fromstring(z.read("ppt/presentation.xml"))
    rels = ET.fromstring(z.read("ppt/_rels/presentation.xml.rels"))
    rid = {r.get("Id"): r.get("Target") for r in rels}
    out = []
    for s in pres.iter(q("p:sldId")):
        t = rid[s.get(q("r:id"))]
        out.append("ppt/" + t.lstrip("/").replace("ppt/", "") if not t.startswith("/") else t.lstrip("/"))
    return out


def notes_text(z: zipfile.ZipFile, slide_path: str) -> str:
    rel = slide_path.replace("slides/", "slides/_rels/") + ".rels"
    if rel not in z.namelist():
        return ""
    for r in ET.fromstring(z.read(rel)):
        if r.get("Type", "").endswith("/notesSlide"):
            npath = "ppt/notesSlides/" + r.get("Target").split("/")[-1]
            root = ET.fromstring(z.read(npath))
            parts = []
            for sp in root.iter(q("p:sp")):
                ph = sp.find(".//" + q("p:ph"))
                if ph is not None and ph.get("type") in ("body", None) and ph.get("type") != "sldNum":
                    parts.append(" ".join(t.text or "" for t in sp.iter(q("a:t"))))
            return "\n".join(parts).strip()
    return ""


def shape_role(name: str, text: str, is_ref_slide: bool) -> str | None:
    for role, pat in ROLE_PATTERNS:
        if pat.search(name or ""):
            return role
    if re.match(r"^\s*(kaynak|kaynaklar|source|sources|görsel|foto|photo)\s*[:：]", text or "", re.I):
        return "source"
    if is_ref_slide and len(text or "") > 30:
        return "references"
    if re.fullmatch(r"\s*\d{1,3}\s*", text or ""):
        return "slideNumber"
    return None


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pptx")
    ap.add_argument("--min", type=float, default=36)
    ap.add_argument("--allow", default="")
    ap.add_argument("--fonts", default=",".join(SAFE))
    ap.add_argument("--wpm", type=float, default=112)
    ap.add_argument("--pause", type=float, default=7)
    ap.add_argument("--target", default="")
    ap.add_argument("--forbid", default="bu akşam,lorem,ipsum,TODO,xxx,[insert")
    ap.add_argument("--json", default="")
    a = ap.parse_args()

    allow = dict(DEFAULT_ALLOW)
    for kv in filter(None, a.allow.split(",")):
        k, v = kv.split("=")
        allow[k.strip()] = float(v)
    safe = [f.strip().lower() for f in a.fonts.split(",") if f.strip()]
    forbid = [f.strip().lower() for f in a.forbid.split(",") if f.strip()]

    try:
        z = zipfile.ZipFile(a.pptx)
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
    except Exception as e:  # noqa: BLE001
        print("HARD: cannot open:", e)
        return 1
    sz = pres.find(q("p:sldSz"))
    cx, cy = int(sz.get("cx")), int(sz.get("cy"))
    hard, warn = [], []
    fonts_used: dict[str, int] = {}
    layouts, total_sec, per_slide = [], 0.0, []
    seen_small: set = set()
    theme_fonts = {}
    for n in z.namelist():
        if n.startswith("ppt/theme/theme") and n.endswith(".xml"):
            t = ET.fromstring(z.read(n))
            for key, tag in (("major", "a:majorFont"), ("minor", "a:minorFont")):
                el = t.find(".//" + q(tag) + "/" + q("a:latin"))
                if el is not None:
                    theme_fonts.setdefault(key, el.get("typeface"))
            break

    for idx, sp_path in enumerate(slide_order(z), 1):
        root = ET.fromstring(z.read(sp_path))
        all_text = " ".join(t.text or "" for t in root.iter(q("a:t")))
        title_guess = all_text[:60]
        is_ref = bool(re.search(r"\b(kaynakça|kaynaklar|references|bibliography)\b", all_text[:200], re.I))
        pics = len(root.findall(".//" + q("p:pic")))
        frames = root.findall(".//" + q("p:graphicFrame"))
        visual = pics + len(frames)
        has_source = False
        layout_marker = None
        words = 0
        for sp in root.iter(q("p:sp")):
            nv = sp.find(".//" + q("p:cNvPr"))
            name = nv.get("name", "") if nv is not None else ""
            if name.startswith("layout:"):
                layout_marker = name[7:]
                continue
            off = sp.find(".//" + q("a:off"))
            ext = sp.find(".//" + q("a:ext"))
            if off is not None and ext is not None:
                x, y, w, h = int(off.get("x")), int(off.get("y")), int(ext.get("cx")), int(ext.get("cy"))
                if x < -EMU * 0.05 or y < -EMU * 0.05 or x + w > cx + EMU * 0.05 or y + h > cy + EMU * 0.05:
                    hard.append(f"slide {idx}: shape '{name}' extends outside the slide")
                geom = sp.find(".//" + q("a:prstGeom"))
                txt = "".join(t.text or "" for t in sp.iter(q("a:t"))).strip()
                if geom is not None and not txt and w > cx * 0.9 and h < EMU * 0.15 and y < cy * 0.2:
                    warn.append(f"slide {idx}: full-width thin bar '{name}' — decorative bars read as template filler")
            stext = "".join(t.text or "" for t in sp.iter(q("a:t"))).strip()
            if not stext:
                continue
            role = shape_role(name, stext, is_ref)
            if role == "source":
                has_source = True
            if role is None:
                words += len(stext.split())
            for para in sp.iter(q("a:p")):
                ppr = para.find(q("a:pPr"))
                dsz = None
                if ppr is not None and ppr.find(q("a:defRPr")) is not None:
                    dsz = ppr.find(q("a:defRPr")).get("sz")
                for r in para.findall(q("a:r")):
                    t = (r.findtext(q("a:t")) or "").strip()
                    if not t:
                        continue
                    rpr = r.find(q("a:rPr"))
                    s = rpr.get("sz") if rpr is not None and rpr.get("sz") else dsz
                    if rpr is not None:
                        lat = rpr.find(q("a:latin"))
                        if lat is not None:
                            f = lat.get("typeface")
                            fonts_used[f] = fonts_used.get(f, 0) + 1
                    if s is None:
                        warn.append(f"slide {idx}: '{t[:30]}' size inherited from layout — verify in render")
                        continue
                    pt = int(s) / 100
                    floor = allow.get(role, a.min) if role else a.min
                    if pt + 0.01 < floor and (idx, name, pt) not in seen_small:
                        seen_small.add((idx, name, pt))
                        hard.append(f"slide {idx}: {pt:g} pt < {floor:g} pt ({role or 'body'}) in '{name}': \"{t[:40]}\"")
            low = stext.lower()
            for fbd in forbid:
                if fbd and fbd in low:
                    hard.append(f"slide {idx}: forbidden phrase '{fbd}' in \"{stext[:50]}\"")
        if layout_marker:
            layouts.append(layout_marker)
        notes = notes_text(z, sp_path)
        nw = len(re.sub(r"\([^)]*\)", " ", notes).split())
        sec = nw / a.wpm * 60 + a.pause
        total_sec += sec
        per_slide.append({"slide": idx, "layout": layout_marker, "visuals": visual, "slideWords": words,
                          "noteWords": nw, "seconds": round(sec), "source": has_source, "start": title_guess})
        content = idx > 1 and not is_ref and layout_marker not in ("cover", "section", "closing", "quote", "agenda", "references")
        if content and visual == 0 and layout_marker not in ("agenda", "cards", "compare", "process", "stat", "photoSteps"):
            warn.append(f"slide {idx}: text-only slide (no picture, chart, table or diagram)")
        if content and not has_source:
            warn.append(f"slide {idx}: no source line")
        if idx > 1 and not notes and not is_ref:
            warn.append(f"slide {idx}: no speaker notes")
        if words > 45:
            warn.append(f"slide {idx}: {words} words on the slide — move detail to notes")
    for i in range(2, len(layouts)):
        if layouts[i] == layouts[i - 1] == layouts[i - 2] and layouts[i] != "references":
            warn.append(f"slides {i - 1}-{i + 1}: layout '{layouts[i]}' three times in a row")
    for k in ("major", "minor"):
        f = theme_fonts.get(k)
        if f:
            fonts_used.setdefault(f + " (theme)", 0)
    for f in fonts_used:
        base = f.replace(" (theme)", "")
        if base.lower() not in safe and not base.startswith("+"):
            warn.append(f"font '{base}' is not in the safe list ({', '.join(SAFE)}) — may change on another computer")
    if a.target:
        lo, hi = (float(x) for x in a.target.split("-"))
        if not lo <= total_sec / 60 <= hi:
            warn.append(f"estimated talk {total_sec / 60:.1f} min outside target {a.target} min")

    report = {"file": a.pptx, "slides": len(per_slide), "slideSize_in": [round(cx / EMU, 2), round(cy / EMU, 2)],
              "estimatedMinutes": round(total_sec / 60, 1), "fonts": fonts_used, "hard": hard, "warnings": warn,
              "perSlide": per_slide}
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=2)
    print(f"{a.pptx}: {len(per_slide)} slides, {cx / EMU:.2f}x{cy / EMU:.2f} in, ~{total_sec / 60:.1f} min talk")
    print("fonts:", ", ".join(f"{k}×{v}" for k, v in fonts_used.items()) or "-")
    print(f"HARD ({len(hard)}):")
    for h in hard:
        print("  -", h)
    print(f"WARN ({len(warn)}):")
    for w in warn:
        print("  -", w)
    print("RESULT:", "FAIL" if hard else ("PASS with warnings" if warn else "PASS"))
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
