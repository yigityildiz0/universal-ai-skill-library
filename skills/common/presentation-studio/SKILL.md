---
name: presentation-studio
description: "Build complete, editable PowerPoint presentations end to end: brief and course rules, slide plan with layout and visual per slide, real licensed photos, designed PPTX via a deck kit, speaker notes with abbreviation pronunciations, timing, rendered visual QA, automatic audit, PDF and a pre-talk reading guide. Academic (lecture, seminar, article, case, thesis) and general decks. Turkish triggers: sunum hazırla, slayt hazırla, PowerPoint yap, pptx, ders sunumu, seminer sunumu, makale sunumu, vaka sunumu, konuşmacı notu, sunum notları, slaytı düzelt, sunumu güzelleştir."
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


# Presentation Studio

Owns every request for a slide deck, PowerPoint/PPTX, speaker notes or presenter guide, academic or
not. `html-slides` is used only when the user explicitly wants an HTML/web presentation.
`academic-study-coach` supplies scientific argument help; `medical-evidence-research` finds and
appraises literature; this skill turns it into the deck.

Why this skill exists: on the same topic and sources, one model produced 59 near-identical
title-plus-paragraph slides with every text at one size, decorative stripes and almost no photos;
another produced a varied, photo-led, rendered-and-fixed deck. The difference was not intelligence:
it was an explicit design system, real images, role-based type sizes, and a render → inspect → fix
loop. Everything below makes that repeatable on any model (GPT, Claude, Gemini, DeepSeek, local).

## Defaults apply unless the user says otherwise — and conflicts are asked

The rules in `references/brief-and-rules.md` (fonts, ≥36 pt floor, exceptions, density, sources,
notes, delivery) apply automatically. Do not ask about them.

**Conflict protocol.** When the user asks for something that contradicts a rule here or in the course
profile (smaller text, a non-safe font, no sources, a decorative style, AI images as photos, a
different notes format…), stop and ask ONE short question before building:

> Skill kuralı: «36 pt altı yazı yok (kaynak satırı hariç)». Senin isteğin: «madde metni 28 pt».
> Hangisini uygulayayım? 1) Kural  2) Senin isteğin, yalnız bu sunumda  3) Senin isteğin, kalıcı (brief'e yazarım)

Record the answer in `brief.md` (section "Kullanıcı kararları") and apply it everywhere. Never
silently pick one. Ask nothing else unless a missing fact would change the result (talk length,
course, template); otherwise continue with defaults and list assumptions in the delivery message.

## Workflow (gates in bold)

1. **Brief** — fill `templates/brief.md`: topic, audience, course profile (`references/course-profiles.md`),
   time, slide range, rules + exceptions, sources policy, delivery formats, user decisions.
2. **Sources** — verify every reference (PubMed/DOI/Crossref) and record claims in
   `templates/claims.json` (claim → source → number → population/protocol → limitation → slide).
3. **Slide plan** — `templates/deck-plan.md`: one row per slide = claim title, teaching goal,
   layout, visual (what it must show), source, note focus. Check: no layout 3× in a row, every
   content slide has a visual, time budget fits. The plan is where text-only habits get caught.
4. **Images** — real photos first (`references/visuals-and-images.md`, `scripts/find_images.py`),
   licences in `img/LICENSES.csv`, cropped to the teaching point; schematic only as labelled fallback.
5. **Content file** — write `deck.json` for the deck kit (schema: `assets/deck-kit/deck.example.json`).
   The model writes content; the kit owns geometry, sizes, fonts, source lines, numbering, notes layout.
6. **Sample gate** — build 4 representative slides, render, inspect, fix the system. Then build all.
7. **Build** — `node build.js deck.json out.pptx` (JS kit) or `python deck_kit.py deck.json out.pptx`
   (Python kit). Fix every build warning (overflow, density, missing source/notes, forbidden phrase).
8. **Render + visual QA** — render every slide with the user's PowerPoint (`scripts/render_pptx.ps1`)
   or the host renderer, make contact sheets (`scripts/contact_sheet.py`), inspect each slide
   against `references/qa-and-delivery.md`. First render always has defects; fix → re-render the
   changed slides → stop when clean.
9. **Audit** — `python scripts/pptx_audit.py out.pptx --min 36 --target A-B`; zero HARD findings.
   Delivery claims (font sizes, timing) are copied from this output, never from memory.
10. **Deliver** (the reading guide and any extra PDF follow the `pdf-studio` page rules: no split tables, no stranded headings) — PPTX + PDF + pre-talk reading guide (`scripts/make_reading_guide.py`), files named
    and placed per brief, a short message: what was made, assumptions, exceptions, what was not checked.

## Choose the production route for the host

| Host | Route |
|---|---|
| Claude Code / Claude desktop | JS kit (`assets/deck-kit`, pptxgenjs) or Anthropic's built-in `pptx` skill for mechanics; this skill's rules win on design, sizes, notes |
| claude.ai (web) | built-in file creation + JS kit; render with its tools; fonts Calibri/Arial only |
| ChatGPT / Codex desktop | Codex: JS kit (Node) or OpenAI Presentations plugin for mechanics with this skill's sizes; ChatGPT web: Python kit (`assets/deck-kit-py`) in the code tool |
| Gemini | Gemini CLI: JS or Python kit; Gemini web without file tools: write `deck.json` + plan, build locally |
| OpenCode / DeepSeek Harness / any agent with a shell | JS or Python kit; render via PowerPoint (Windows) or bundled LibreOffice |

Details, install lines and fallbacks: `references/production-by-host.md`.

## Files

| Need | File |
|---|---|
| Default rules, sizes, fonts, density, sources, language, forbidden phrases | `references/brief-and-rules.md` |
| Course profiles (lecture, seminar/article, clinical case, general) | `references/course-profiles.md` |
| Layout families, type roles, colour, anti-patterns, sample gate | `references/design-system.md` |
| Real images, licences, cropping, honest schematics, charts, video | `references/visuals-and-images.md` |
| Speaker notes template, abbreviations, research block, timing | `references/speaker-notes.md` |
| Academic content: argument, claims, statistics wording, article/case/thesis structures, FTR practical slides | `references/academic-content.md` |
| Non-academic decks (project, pitch, report, school) | `references/general-presentations.md` |
| Host routes, installs, rendering fallbacks | `references/production-by-host.md` |
| QA checklist, audit, delivery package, folders, Drive | `references/qa-and-delivery.md` |
| User guide in Turkish (how to ask, what happens, how to correct) | `KULLANIM-KILAVUZU.md` |
| Deck kit (JS) / (Python) | `assets/deck-kit/`, `assets/deck-kit-py/` |
| Scripts | `scripts/pptx_audit.py`, `render_pptx.ps1`, `contact_sheet.py`, `find_images.py`, `make_reading_guide.py` |
| Templates | `templates/brief.md`, `deck-plan.md`, `claims.json`, `ledger.md` |

## Non-negotiables

- Editable PPTX (real text, native charts/tables); never a deck of screenshots; never HTML when PPTX was asked.
- Safe font family only (Calibri default, Arial fallback); one family for titles and body.
- Type by role; floor 36 pt except declared exceptions (source line, references, slide number, image credit).
- Every content slide: one message, one visual, a source line when it states a scientific fact.
- Real, licensed images for anything physical; AI images never presented as clinical photographs.
- Notes for every slide in the agreed template; abbreviations with pronunciation and expansion.
- Rendered and inspected before delivery; audit with zero HARD findings; state what was not checked.
- Long jobs keep `templates/ledger.md` updated (done steps, final file path, open items) so a new
  session or a model switch continues instead of restarting.
