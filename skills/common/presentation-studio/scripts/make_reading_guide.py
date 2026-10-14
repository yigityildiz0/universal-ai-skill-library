#!/usr/bin/env python3
"""Build the pre-talk reading guide ("Sunum öncesi okuma") from deck.json. Standard library only.

Usage:
  python make_reading_guide.py deck.json --out "Konu - Sunum öncesi okuma.pdf" [--brief brief.md] [--claims claims.json]
Writes an HTML file next to the output and converts it to PDF with Microsoft Edge or Chrome
(headless) when one is installed; otherwise keeps the HTML and says so.

Sections: rules and how the deck meets them (from the brief), timing plan, glossary with
pronunciations, slide-by-slide guide (what to say, why the slide exists, research and how to
interpret it), article cards (from claims.json), likely questions, rehearsal checklist.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys

CSS = """
@page { size: A4; margin: 16mm 15mm; }
body { font-family: Calibri, Arial, sans-serif; font-size: 11.5pt; color: #1f2733; line-height: 1.45; }
h1 { font-size: 22pt; margin: 0 0 4mm; color: #1b2430; }
h2 { font-size: 15pt; margin: 9mm 0 3mm; color: #b0303f; border-bottom: 1px solid #d9dee5; padding-bottom: 1mm; }
h3 { font-size: 12.5pt; margin: 5mm 0 1.5mm; color: #1b2430; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0; font-size: 10.5pt; }
th, td { border: 1px solid #d9dee5; padding: 1.5mm 2mm; vertical-align: top; text-align: left; }
th { background: #1b2430; color: #fff; }
tr:nth-child(even) td { background: #f4f5f8; }
.slide { page-break-inside: avoid; border-left: 3px solid #0f6e8c; padding: 1mm 0 1mm 4mm; margin: 3mm 0; }
.meta { color: #5b6676; font-size: 10pt; }
.box { background: #f4f5f8; padding: 2mm 3mm; border-radius: 2mm; margin: 1.5mm 0; }
pre { white-space: pre-wrap; font-family: inherit; margin: 0; }
"""


def words(t: str) -> int:
    return len(re.sub(r"\([^)]*\)", " ", t or "").split())


def fmt(sec: float) -> str:
    return f"{int(sec // 60)}:{int(round(sec % 60)):02d}"


def esc(s) -> str:
    return html.escape(str(s or "")).replace("**", "")


def timing(deck: dict):
    meta = deck.get("meta", {})
    wpm, pause = meta.get("wordsPerMinute", 112), meta.get("pausePerSlide", 7)
    out = []
    for s in deck["slides"]:
        n = s.get("notes")
        if s["layout"] == "references":
            out.append(5)
            continue
        if not n:
            out.append(10 if s["layout"] == "section" else pause)
            continue
        if isinstance(n, str):
            sw = words(n)
        else:
            sw = words(n.get("say")) + words(n.get("summary")) + words(n.get("transition"))
            rs = n.get("research") or []
            for r in (rs if isinstance(rs, list) else [rs]):
                if isinstance(r, str):
                    sw += words(r)
                else:
                    sw += words(r.get("what")) + words(r.get("interpret")) + 0.5 * words(r.get("why"))
        out.append(max(5, round((sw / wpm * 60 + pause) / 5) * 5))
    return out


def find_browser() -> str | None:
    cands = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for c in cands:
        if os.path.exists(c):
            return c
    for name in ("msedge", "google-chrome", "chromium", "chromium-browser", "chrome"):
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
    ap.add_argument("deck")
    ap.add_argument("--out", required=True)
    ap.add_argument("--brief")
    ap.add_argument("--claims")
    a = ap.parse_args()
    deck = json.load(open(a.deck, encoding="utf-8"))
    meta = deck.get("meta", {})
    abbr, names = deck.get("abbreviations", {}), deck.get("names", {})
    secs = timing(deck)
    total = sum(secs)
    H = [f"<html><head><meta charset='utf-8'><style>{CSS}</style><title>{esc(meta.get('title'))}</title></head><body>"]
    H.append(f"<h1>{esc(meta.get('title', 'Sunum'))} — sunum öncesi okuma</h1>")
    H.append(f"<p class='meta'>{esc(meta.get('author', ''))} · {len(deck['slides'])} slayt · tahmini anlatım {fmt(total)} "
             f"({meta.get('wordsPerMinute', 112)} kelime/dk + slayt başına {meta.get('pausePerSlide', 7)} sn). "
             "Hesaplanan süre prova değildir; bir kez saat tutarak prova et.</p>")

    if a.brief and os.path.exists(a.brief):
        H.append("<h2>1. Kurallar ve sunumdaki karşılıkları</h2><div class='box'><pre>")
        H.append(esc(open(a.brief, encoding="utf-8").read()))
        H.append("</pre></div>")

    H.append("<h2>2. Zaman planı</h2><table><tr><th>#</th><th>Başlık</th><th>Süre</th><th>Bitişte</th></tr>")
    acc = 0
    for i, (s, sec) in enumerate(zip(deck["slides"], secs), 1):
        acc += sec
        H.append(f"<tr><td>{i}</td><td>{esc(s.get('title', s['layout']))}</td><td>{fmt(sec)}</td><td>{fmt(acc)}</td></tr>")
    H.append("</table>")

    H.append("<h2>3. Kısaltmalar, okunuşlar ve terimler</h2><table><tr><th>Kısaltma / ad</th><th>Okunuş</th><th>Açılım / anlam</th></tr>")
    for ab, (say, full) in sorted(abbr.items(), key=lambda x: x[0].lower()):
        H.append(f"<tr><td>{esc(ab)}</td><td>{esc(say)}</td><td>{esc(full)}</td></tr>")
    for nm, say in sorted(names.items()):
        H.append(f"<tr><td>{esc(nm)}</td><td>{esc(say)}</td><td>özel ad</td></tr>")
    seen_terms = set()
    for s in deck["slides"]:
        n = s.get("notes")
        if isinstance(n, dict):
            for t in n.get("terms") or []:
                key = t if isinstance(t, str) else t.get("term")
                if key in seen_terms or (not isinstance(t, str) and t.get("term") in abbr):
                    continue
                seen_terms.add(key)
                if isinstance(t, str):
                    H.append(f"<tr><td colspan='3'>{esc(t)}</td></tr>")
                else:
                    H.append(f"<tr><td>{esc(t.get('term'))}{' (' + esc(t.get('english')) + ')' if t.get('english') else ''}</td>"
                             f"<td>{esc(t.get('say', ''))}</td><td>{esc(t.get('full', ''))} {esc(t.get('def', ''))}</td></tr>")
    H.append("</table>")

    H.append("<h2>4. Slayt slayt anlatım</h2>")
    questions = []
    for i, s in enumerate(deck["slides"], 1):
        n = s.get("notes") or {}
        H.append(f"<div class='slide'><h3>{i}. {esc(s.get('title', s['layout']))}</h3>")
        bits = []
        if s.get("image"):
            bits.append(f"Görsel: {esc(s['image'].get('alt', s['image'].get('file')))}")
        if s.get("source"):
            bits.append(f"Kaynak: {esc(s['source'])}")
        if bits:
            H.append(f"<p class='meta'>{' · '.join(bits)}</p>")
        if isinstance(n, str):
            H.append(f"<p>{esc(n)}</p>")
        else:
            if n.get("say"):
                H.append(f"<p>{esc(n['say'])}</p>")
            if n.get("summary"):
                H.append(f"<div class='box'><b>Özetle:</b> {esc(n['summary'])}</div>")
            rs = n.get("research") or []
            for r in (rs if isinstance(rs, list) else [rs]):
                if isinstance(r, str):
                    H.append(f"<div class='box'><b>Araştırma:</b> {esc(r)}</div>")
                else:
                    H.append(f"<div class='box'><b>Araştırma — {esc(r.get('cite'))}</b><br>"
                             f"Neden burada: {esc(r.get('why'))}<br>Ne yapılmış, ne bulunmuş: {esc(r.get('what'))}<br>"
                             f"Nasıl yorumlanır: {esc(r.get('interpret'))}</div>")
            if n.get("question"):
                questions.append((i, n["question"]))
            if n.get("transition"):
                H.append(f"<p class='meta'>→ Geçiş: {esc(n['transition'])}</p>")
        H.append("</div>")

    if a.claims and os.path.exists(a.claims):
        cl = json.load(open(a.claims, encoding="utf-8")).get("claims", [])
        if cl:
            H.append("<h2>5. Makale ve iddia kartları</h2><table><tr><th>Kaynak</th><th>İddia / değer</th><th>Örneklem · yöntem</th><th>Sınırlılık</th><th>Slayt</th></tr>")
            for c in cl:
                doi = c.get("doi_or_pmid", "")
                link = f"<br><span class='meta'>{esc(doi)}</span>" if doi else ""
                H.append(f"<tr><td>{esc(c.get('source'))}{link}</td><td>{esc(c.get('claim'))}<br><b>{esc(c.get('value'))}</b></td>"
                         f"<td>{esc(c.get('population'))} · {esc(c.get('protocol'))} · {esc(c.get('design'))}</td>"
                         f"<td>{esc(c.get('limitation'))} ({esc(c.get('status'))})</td><td>{esc(', '.join(map(str, c.get('slides', []))))}</td></tr>")
            H.append("</table>")

    H.append("<h2>6. Olası sorular</h2>")
    if questions:
        H.append("<ul>" + "".join(f"<li><b>Slayt {i}:</b> {esc(q)}</li>" for i, q in questions) + "</ul>")
    else:
        H.append("<p>Notlarda soru tanımlanmadı. Sık sorulanlar: Bu çalışmadan ne öğrendin? Sınırlılıkları neler? "
                 "Sen yapsan neyi farklı yapardın? Bu sayı hangi popülasyonda geçerli?</p>")

    H.append("<h2>7. Prova kontrol listesi</h2><ul>"
             "<li>Bir kez saat tutarak baştan sona prova; uzun süren slaytları işaretle.</li>"
             "<li>Sunucu görünümünde notları kontrol et (Alt+F5).</li>"
             "<li>Sunum bilgisayarında dosyayı aç: yazı tipi, görseller, videolar.</li>"
             "<li>PDF yedeğini ve PPTX'i ayrı bir yerde (USB/bulut) tut.</li>"
             "<li>Kısaltmaların okunuşlarını bir kez sesli oku.</li></ul>")
    H.append("</body></html>")

    out_pdf = os.path.abspath(a.out)
    out_html = os.path.splitext(out_pdf)[0] + ".html"
    with open(out_html, "w", encoding="utf-8") as fh:
        fh.write("\n".join(H))
    br = find_browser()
    if not br:
        print(f"HTML written: {out_html} (no Edge/Chrome found for PDF; print it to PDF manually)")
        return 0
    import pathlib
    import tempfile
    prof = tempfile.mkdtemp(prefix="guide-browser-")
    cmd = [br, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={prof}", "--no-pdf-header-footer",
           f"--print-to-pdf={out_pdf}", pathlib.Path(out_html).as_uri()]
    r = subprocess.run(cmd, check=False, timeout=180, capture_output=True, text=True)
    shutil.rmtree(prof, ignore_errors=True)
    if not os.path.exists(out_pdf) and r.stderr:
        print(r.stderr[-800:])
    if os.path.exists(out_pdf):
        os.remove(out_html)
        print(f"PDF written: {out_pdf}")
        return 0
    print(f"PDF conversion failed; HTML kept: {out_html}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
