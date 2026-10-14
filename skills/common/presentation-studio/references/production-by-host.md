# Production route per host

The design rules are the same everywhere; only the mechanics change. Check what the host can do
(shell? Node? Python? file output? image viewing?) before choosing. Never claim a render or a file
you could not produce: say which step the host could not run and what the user should run locally.

## Capability check (30 seconds)

1. Can I run code? Which: Node (`node -v`), Python (`python -c "import pptx"`)?
2. Can I write files the user can download/open?
3. Can I view images (to inspect renders)?
4. Is PowerPoint available (Windows, `render_pptx.ps1`) or a LibreOffice/host renderer?
5. Is a native presentation skill available (Anthropic `pptx`, OpenAI Presentations)? Use it for
   mechanics if you prefer, but keep this skill's sizes, fonts, layouts, notes and QA.

## Routes

| Host | Build | Render / inspect | Notes |
|---|---|---|---|
| Claude Code (Windows desktop) | JS kit: `npm install pptxgenjs@4` in a work folder, copy `assets/deck-kit/*.js` | `render_pptx.ps1` (PowerPoint COM) → `contact_sheet.py` → view sheets | best route; full QA |
| claude.ai web / Claude app with code execution | JS kit (pptxgenjs is usually preinstalled) or Python kit | host LibreOffice render → view images | use Calibri/Arial only; LibreOffice metrics ≈ PowerPoint for these |
| Codex desktop (ChatGPT app) | JS kit in the project folder, or the OpenAI Presentations plugin for mechanics | `render_pptx.ps1` on Windows or the plugin's render step | Presentations defaults (42/32/17 pt) must be overridden by the brief's sizes |
| ChatGPT web (code tool) | Python kit: upload `assets/deck-kit-py/deck_kit.py` + `deck.json` + images, run `python deck_kit.py deck.json out.pptx` | render via `soffice --headless --convert-to pdf` if present, else deliver with "not visually checked" and ask the user to send screenshots | python-pptx is normally available there |
| Gemini CLI | JS or Python kit (needs Node or python-pptx) | PowerPoint COM on Windows | skills live in `~/.gemini/skills/<name>/` |
| Gemini app (web) | no reliable file building: produce brief, slide plan and a complete `deck.json`, then tell the user to build with the kit locally (one command) or in Claude/ChatGPT | — | Gemini Skills accept md/txt/py/json/csv/pdf/images; JS files are not uploaded |
| OpenCode / DeepSeek Harness / other shell agents | JS or Python kit | PowerPoint COM (Windows) or the bundled LibreOffice renderer | keep the ledger: these hosts compact context often |

## Install lines (Windows)

```bash
# JS kit (once per work folder)
npm init -y && npm install pptxgenjs@4
node build.js deck.json "Konu - Sunum.pptx"

# Python kit
python -m pip install python-pptx
python deck_kit.py deck.json "Konu - Sunum.pptx"

# Render + sheets + audit
powershell -ExecutionPolicy Bypass -File render_pptx.ps1 -Pptx "Konu - Sunum.pptx" -OutDir render-r1 -Pdf "Konu - Sunum.pdf"
python contact_sheet.py render-r1
python pptx_audit.py "Konu - Sunum.pptx" --min 36 --target 30-45
```

Use the skill folder's absolute path for the scripts. Keep build files in a work folder, not in
the user's course folder.

## Using a host's own presentation skill

If you build with Anthropic `pptx` or OpenAI Presentations instead of the kit:
- Set slide size 13.333 × 7.5 in (16:9 wide), theme fonts Calibri/Calibri.
- Apply the type-role table, layout families, anti-pattern list and notes template from this skill.
- Name shapes like the kit (`Kaynak satiri`, `Kaynakca`, `Slayt no`, `Gorsel kredisi`) so
  `pptx_audit.py` recognises exception roles; otherwise it flags them as body text.
- Run `pptx_audit.py` at the end regardless of the builder.

## Model-specific advice

- **GPT models:** they default to prose slides. Insist on the slide plan with a layout + visual per
  slide before any code, show 2–4 reference slide images when available, and have a separate
  critique pass on rendered sheets ("score each slide against qa-and-delivery.md; fix the worst 5").
  Reasoning "high" is enough; more effort does not replace the design system.
- **Claude models:** strong at layout; main risks are context bloat in long sessions and claiming
  compliance without measuring. Start production in a clean session with brief + claims + plan,
  and copy numbers from the audit output.
- **Any model:** when switching model or session mid-job, hand over `brief.md`, `claims.json`,
  `deck-plan.md`, `deck.json`, `ledger.md` — not the raw chat log.
