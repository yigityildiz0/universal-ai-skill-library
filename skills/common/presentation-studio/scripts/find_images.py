#!/usr/bin/env python3
"""Search openly licensed REAL photos/figures and download them with licence records.

Sources (free, no API key): Wikimedia Commons, Openverse.
Usage:
  python find_images.py search "hand held dynamometer knee" [--source commons|openverse|all] [--limit 12]
  python find_images.py get "<file-url-or-commons-title>" --out img/protokol.jpg [--name protokol]
Every download appends a row to img/LICENSES.csv: file, title, author, licence, licence_url, source_page.
Only use results whose licence permits reuse with attribution (CC0, PD, CC BY, CC BY-SA; CC BY-NC
only for non-commercial teaching and say so). Put the credit on the slide (credit/source line).
For journal figures use the article's own licence (PMC open-access subset, CC BY) and cite the article.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.parse
import urllib.request

UA = "presentation-studio/1.0 (teaching use; contact via repository)"
OK_LIC = re.compile(r"(cc0|public domain|pd|cc[- ]by(?![- ]?nd)|cc[- ]by[- ]sa)", re.I)


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def commons(query: str, limit: int) -> list[dict]:
    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
        "gsrsearch": query + " filetype:bitmap", "gsrlimit": limit, "prop": "imageinfo",
        "iiprop": "url|size|extmetadata", "iiurlwidth": 1600})
    data = get_json(api)
    out = []
    for p in (data.get("query", {}).get("pages", {}) or {}).values():
        ii = (p.get("imageinfo") or [{}])[0]
        md = ii.get("extmetadata", {})
        out.append({"source": "commons", "title": p.get("title"), "url": ii.get("thumburl") or ii.get("url"),
                    "w": ii.get("width"), "h": ii.get("height"),
                    "license": strip_html(md.get("LicenseShortName", {}).get("value")),
                    "license_url": md.get("LicenseUrl", {}).get("value", ""),
                    "author": strip_html(md.get("Artist", {}).get("value"))[:120],
                    "page": ii.get("descriptionurl")})
    return out


def openverse(query: str, limit: int) -> list[dict]:
    api = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode({"q": query, "page_size": limit})
    data = get_json(api)
    out = []
    for r in data.get("results", []):
        lic = (r.get("license") or "").upper()
        out.append({"source": "openverse", "title": r.get("title"), "url": r.get("url"), "w": r.get("width"),
                    "h": r.get("height"), "license": f"CC {lic} {r.get('license_version') or ''}".strip(),
                    "license_url": r.get("license_url", ""), "author": (r.get("creator") or "")[:120],
                    "page": r.get("foreign_landing_url")})
    return out


def cmd_search(a) -> int:
    res = []
    if a.source in ("commons", "all"):
        try:
            res += commons(a.query, a.limit)
        except Exception as e:  # noqa: BLE001
            print("commons error:", e)
    if a.source in ("openverse", "all"):
        try:
            res += openverse(a.query, a.limit)
        except Exception as e:  # noqa: BLE001
            print("openverse error:", e)
    for i, r in enumerate(res, 1):
        flag = "OK " if OK_LIC.search(r["license"] or "") else "?? "
        print(f"{i:2}. {flag}[{r['source']}] {r['title']}  {r['w']}x{r['h']}  {r['license']}  by {r['author']}")
        print(f"     url:  {r['url']}\n     page: {r['page']}")
    if not res:
        print("no results — try English anatomical/clinical terms, the device brand, or the article figure route")
    return 0


def cmd_get(a) -> int:
    target = a.target
    meta = {"title": target, "author": "", "license": "", "license_url": "", "page": target}
    if target.startswith("File:") or "commons.wikimedia.org/wiki/File:" in target:
        title = target.split("/wiki/")[-1]
        api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
            "action": "query", "format": "json", "titles": urllib.parse.unquote(title), "prop": "imageinfo",
            "iiprop": "url|extmetadata", "iiurlwidth": 2000})
        p = next(iter(get_json(api)["query"]["pages"].values()))
        ii = p["imageinfo"][0]
        md = ii.get("extmetadata", {})
        target = ii.get("thumburl") or ii["url"]
        meta = {"title": p["title"], "author": strip_html(md.get("Artist", {}).get("value"))[:120],
                "license": strip_html(md.get("LicenseShortName", {}).get("value")),
                "license_url": md.get("LicenseUrl", {}).get("value", ""), "page": ii.get("descriptionurl")}
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    req = urllib.request.Request(target, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r, open(a.out, "wb") as fh:
        fh.write(r.read())
    for k in ("author", "license", "license_url", "page"):
        if getattr(a, k, None):
            meta[k] = getattr(a, k)
    lic_file = os.path.join(os.path.dirname(os.path.abspath(a.out)), "LICENSES.csv")
    new = not os.path.exists(lic_file)
    with open(lic_file, "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["file", "title", "author", "license", "license_url", "source_page"])
        w.writerow([os.path.basename(a.out), meta["title"], meta["author"], meta["license"], meta["license_url"], meta["page"]])
    print(f"saved {a.out}  licence: {meta['license'] or 'UNKNOWN — check the page before use'}")
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--source", default="all", choices=["commons", "openverse", "all"])
    s.add_argument("--limit", type=int, default=10)
    g = sub.add_parser("get")
    g.add_argument("target", help="direct image URL, Commons File: title or Commons file page URL")
    g.add_argument("--out", required=True)
    g.add_argument("--author")
    g.add_argument("--license")
    g.add_argument("--license_url")
    g.add_argument("--page", help="source page (article or landing page) for the licence record")
    a = ap.parse_args()
    return cmd_search(a) if a.cmd == "search" else cmd_get(a)


if __name__ == "__main__":
    sys.exit(main())
