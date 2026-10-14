#!/usr/bin/env python3
"""Static checks on the HTML/CSS before printing. Standard library only.

Usage: python html_lint.py document.html
Exit code 1 when there is at least one ERROR. Warnings never fail the build.
Checks patterns that reliably break print pagination or readability in HTML-to-PDF pipelines.
"""
from __future__ import annotations

import pathlib
import re
import sys
from html.parser import HTMLParser

SAFE_SIZE_PT = 8.0


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.errors, self.warns = [], []
        self.stack, self.lang, self.charset, self.title = [], False, False, False
        self.tables, self.tables_with_thead, self.imgs_no_alt, self.imgs_no_size = 0, 0, 0, 0
        self.cur_table_thead = []
        self.css = []
        self._in_style = False
        self.remote, self.br_runs, self._last_br = [], 0, False
        self.headings = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html" and a.get("lang"):
            self.lang = True
        if tag == "meta" and ("charset" in a or "utf-8" in (a.get("content", "") or "").lower()):
            self.charset = True
        if tag == "style":
            self._in_style = True
        if tag == "table":
            self.tables += 1
            self.cur_table_thead.append(False)
        if tag == "thead" and self.cur_table_thead:
            self.cur_table_thead[-1] = True
        if tag == "img":
            if not a.get("alt"):
                self.imgs_no_alt += 1
            if not (a.get("width") or "width" in (a.get("style") or "") or a.get("class")):
                self.imgs_no_size += 1
            src = a.get("src", "")
            if re.match(r"https?://", src):
                self.remote.append(src)
        if tag in ("link",) and re.match(r"https?://", a.get("href", "") or ""):
            self.remote.append(a["href"])
        if tag in ("script",) and re.match(r"https?://", a.get("src", "") or ""):
            self.remote.append(a["src"])
        if tag == "br":
            if self._last_br:
                self.br_runs += 1
            self._last_br = True
        else:
            self._last_br = False
        if tag in ("h1", "h2", "h3", "h4"):
            self.headings.append(tag)
        style = a.get("style") or ""
        if style:
            self.css.append(("inline style on <%s>" % tag, style))

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False
        if tag == "table" and self.cur_table_thead:
            if self.cur_table_thead.pop():
                self.tables_with_thead += 1

    def handle_data(self, data):
        if self._in_style:
            self.css.append(("<style>", data))


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = pathlib.Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    p = P()
    p.feed(text)
    # also inspect linked local stylesheets
    for m in re.finditer(r'<link[^>]+rel=["\']stylesheet["\'][^>]*href=["\']([^"\']+)["\']', text):
        href = m.group(1)
        if re.match(r"https?://", href):
            continue
        f = (path.parent / href).resolve()
        if f.is_file():
            p.css.append((href, f.read_text(encoding="utf-8", errors="ignore")))
        else:
            p.errors.append(f"stylesheet not found: {href}")
    E, W = p.errors, p.warns
    if not p.lang:
        W.append('missing <html lang="..."> — hyphenation, screen readers and quotes depend on it')
    if not p.charset:
        E.append('missing <meta charset="utf-8"> — Turkish letters will break')
    if "<title>" not in text.lower():
        W.append("missing <title> — becomes the PDF title")
    for src in p.remote:
        W.append(f"remote resource {src[:70]} — renders blank when offline; download it locally")
    if p.imgs_no_alt:
        W.append(f"{p.imgs_no_alt} image(s) without alt text")
    if p.imgs_no_size:
        W.append(f"{p.imgs_no_size} image(s) without width — may overflow or print at the wrong size")
    if p.tables and p.tables_with_thead < p.tables:
        W.append(f"{p.tables - p.tables_with_thead} table(s) without <thead> — header will not repeat across pages")
    if p.br_runs:
        W.append(f"{p.br_runs} run(s) of consecutive <br> used as spacing — use margins/padding (they split unpredictably)")
    if p.headings and p.headings[0] not in ("h1",):
        W.append("document does not start with an <h1>")
    all_css = "\n".join(c for _, c in p.css)
    own_css = "\n".join(c for n, c in p.css if not n.endswith(("print.css", "themes.css")))
    def has(pat, flags=re.I | re.S):
        return re.search(pat, all_css, flags)
    if not has(r"@page"):
        E.append("no @page rule — link print.css (page size, margins, page numbers)")
    if has(r"position\s*:\s*(absolute|fixed)") :
        W.append("position:absolute/fixed found — absolute text is not paginated and overlaps; allowed only for decorations on a cover")
    if has(r"\b\d+\s*(vh|vw|vmin|vmax)\b"):
        W.append("vh/vw units found — they are tied to the browser window, not the printed page; use mm/% or rem")
    if has(r"height\s*:\s*\d+(\.\d+)?\s*(px|mm|cm|pt|in)\s*;[^}]*overflow\s*:\s*hidden|overflow\s*:\s*hidden[^}]*height\s*:\s*\d+(\.\d+)?\s*(px|mm|cm|pt|in)"):
        E.append("fixed height + overflow:hidden — long content is silently cut off; use min-height")
    if has(r"overflow\s*:\s*(auto|scroll)"):
        W.append("overflow:auto/scroll — scroll areas do not print; let content flow")
    for m in re.finditer(r"font-size\s*:\s*([\d.]+)\s*(pt|px)", all_css, re.I):
        v = float(m.group(1)) * (0.75 if m.group(2).lower() == "px" else 1)
        if v < SAFE_SIZE_PT:
            W.append(f"font-size {m.group(0)} ≈ {v:.1f} pt is below {SAFE_SIZE_PT:g} pt — hard to read when printed")
            break
    if re.search(r"display\s*:\s*(flex|grid)", own_css, re.I) and re.search(r"<table|<ul|<ol|<p[ >]", text, re.I):
        W.append("display:flex/grid in use — page-break rules do not work inside flex/grid items; keep paginating content in normal flow "
                 "(tables, lists, paragraphs) and use flex/grid only for small non-splitting widgets")
    if has(r"-webkit-box-decoration-break|text-shadow|filter\s*:") :
        W.append("text-shadow/filter found — often prints as a blurry raster in PDF")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", text):
        W.append("emoji/dingbat characters found — need a colour-emoji font; they often print as empty boxes. Use SVG icons or words")
    if re.search(r"[​­]{3,}", text):
        W.append("many zero-width/soft-hyphen characters found — check for hidden spacing hacks")
    if not has(r"break-inside\s*:\s*avoid|page-break-inside\s*:\s*avoid"):
        W.append("no break-inside:avoid rule — figures/tables/callouts may be split (print.css provides it)")
    if p.tables and not has(r"thead\s*\{[^}]*table-header-group") and "<thead" not in text.lower().replace("<thead>", "", 0)[:0]:
        W.append("no 'thead { display: table-header-group }' — long tables will not repeat the header (browsers repeat <thead> by default, but custom display rules can break it)")
    n_err, n_warn = len(E), len(W)
    print(f"html_lint: {path.name}: {n_err} error(s), {n_warn} warning(s)")
    for e in E:
        print("  ERROR:", e)
    for w in W:
        print("  warn: ", w)
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
