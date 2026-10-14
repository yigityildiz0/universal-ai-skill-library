#!/usr/bin/env python3
"""HTML -> PDF with headless Edge/Chrome. Standard library only.

Usage:
  python build_pdf.py document.html out.pdf [--size A4|Letter|A5] [--orientation portrait|landscape]
                      [--margin "19mm 18mm 21mm 18mm"] [--wait 8] [--no-audit]

* Injects the page size/orientation/margins as a final <style> in a temp copy (the source HTML is untouched).
* Waits for fonts and images (virtual time budget), prints without browser header/footer.
* Runs html_lint.py first (errors stop the build) and pdf_audit.py afterwards when available.
Fallbacks if no Edge/Chrome is found: see references/engines.md (WeasyPrint, wkhtmltopdf, LibreOffice).
"""
from __future__ import annotations

import argparse
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent


def find_browser() -> str | None:
    cands = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for c in cands:
        if os.path.exists(c):
            return c
    for name in ("msedge", "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        p = shutil.which(name)
        if p:
            return p
    return None


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html")
    ap.add_argument("pdf")
    ap.add_argument("--size", default="A4")
    ap.add_argument("--orientation", default="portrait", choices=["portrait", "landscape"])
    ap.add_argument("--margin", default=None)
    ap.add_argument("--wait", type=int, default=8, help="seconds of virtual time for fonts/images")
    ap.add_argument("--no-audit", action="store_true")
    a = ap.parse_args()

    src = pathlib.Path(a.html).resolve()
    out = pathlib.Path(a.pdf).resolve()
    if not src.is_file():
        print("HTML not found:", src)
        return 1
    if not a.no_audit or True:
        lint = HERE / "html_lint.py"
        if lint.exists():
            r = subprocess.run([sys.executable, str(lint), str(src)], capture_output=True, text=True, encoding="utf-8")
            print(r.stdout.strip())
            if r.returncode:
                print("html_lint reported ERRORS — fix them before building.")
                return 2
    br = find_browser()
    if not br:
        print("No Edge/Chrome/Chromium found. Install one or use a fallback from references/engines.md.")
        return 3

    css = f"@page {{ size: {a.size} {a.orientation};" + (f" margin: {a.margin};" if a.margin else "") + " }"
    text = src.read_text(encoding="utf-8")
    inj = f"<style id=\"pdf-studio-page\">{css}</style>"
    text = text.replace("</head>", inj + "\n</head>", 1) if "</head>" in text else inj + text
    tmp = src.with_name(".__pdfstudio_" + src.name)
    tmp.write_text(text, encoding="utf-8")
    prof = tempfile.mkdtemp(prefix="pdfstudio-browser-")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            out.unlink()
        cmd = [br, "--headless=new", "--disable-gpu", "--no-first-run", "--hide-scrollbars", f"--user-data-dir={prof}",
               "--no-pdf-header-footer", "--allow-file-access-from-files", f"--virtual-time-budget={a.wait * 1000}",
               f"--print-to-pdf={out}", tmp.as_uri()]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=240)
        if not out.exists():
            print("Browser did not produce a PDF.", (r.stderr or "")[-600:])
            return 4
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass
        shutil.rmtree(prof, ignore_errors=True)
    print(f"PDF written: {out} ({out.stat().st_size // 1024} KB)")
    if not a.no_audit:
        audit = HERE / "pdf_audit.py"
        if audit.exists():
            r = subprocess.run([sys.executable, str(audit), str(out)], capture_output=True, text=True, encoding="utf-8")
            print(r.stdout.strip())
            return 0 if r.returncode in (0, 1) else r.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
