# QA and delivery

A deck is done when the rendered file — not the code, not the plan — passes these checks, and the
delivery message reports only measured facts.

## 1. Loop

1. Build → fix every build warning (overflow estimate, density, missing source/notes, forbidden phrase).
2. Render all slides (`render_pptx.ps1` or host renderer) → contact sheets of 6 (`contact_sheet.py`).
3. Look at every sheet fresh, as the audience will. If the host can run a separate reviewer
   (subagent/second pass), let it review the images without reading the code.
4. Fix the cause at the system level (kit helper, theme, layout choice) before patching single slides.
5. Re-render only changed slides; repeat until a pass finds nothing. Expect 2–6 passes on a new deck.
6. `pptx_audit.py` → zero HARD findings; review each WARN and fix or justify it.
7. Open the final file once more in the target app if possible (PowerPoint), including presenter
   view for notes.

## 2. Visual checklist (per slide)

- [ ] Text inside its box and inside the slide; nothing overlapping; nothing cut off.
- [ ] Title on one line (two max), same position as other content slides.
- [ ] Sizes by role: no body text under the floor; source/credit/number only in their places.
- [ ] One message; ≤ 6 lines; no paragraph; no sentence that sounds translated or AI-written.
- [ ] A real visual that teaches (photo cropped to the point, chart, diagram, big number).
- [ ] Image sharp, not stretched, licence credit present; no watermark.
- [ ] Balanced space: no empty half-slide, no cramped corner.
- [ ] Contrast: dark on light / white on dark; no grey on photo.
- [ ] Number + unit on the same line; decimal comma for Turkish (0,978).
- [ ] No stripes, title underlines, edge borders, clip art, animations.
- [ ] Layout differs from the previous two slides.
- [ ] Source line present when the slide states a scientific fact; matches `claims.json`.

## 3. Content checklist (whole deck)

- [ ] Titles read in order tell the argument (ghost-deck test).
- [ ] Agenda questions are all answered; summary repeats the answers.
- [ ] Every number checked against the full text (value, unit, population, protocol, direction).
- [ ] Device/test terms exact (e.g. "isokinetic device, isometric test" when that is what was done).
- [ ] Generalisation limits stated (a cut-off from one population is not universal).
- [ ] Notes on every slide in the template; abbreviations expanded; research interpreted.
- [ ] Timing within target; slide count follows time.
- [ ] Forbidden phrases absent (audit).
- [ ] References complete, consistent APA 7, DOIs resolve.

## 4. Delivery package

| File | Purpose |
|---|---|
| `<Konu> - Sunum.pptx` | editable deck with notes |
| `<Konu> - Sunum.pdf` | exact look on any computer (font safety net) |
| `<Konu> - Sunum öncesi okuma.pdf` | presenter study guide (see `speaker-notes.md` §4) |

- Course folder keeps only these final files. Work files (deck.json, scripts, renders, images,
  ledger) go to the user's AI-work area, e.g. `<Ders>\Yapay zeka çalışmaları\<Konu>\`.
- Old versions are archived, never deleted; one-file folders are not created; user files are renamed
  only when asked and never edited in content.
- Cloud upload (e.g. Google Drive): upload only the final three; old versions as PDF only into an
  archive subfolder. Check the account's "convert uploads" setting first: with conversion on, a PPTX
  becomes Google Slides and fonts/notes may change — keep the PDF as the faithful copy and tell the
  user. Do not change account settings without explicit permission.
- Videos: test playback in the target PowerPoint; keep a still + link fallback.

## 5. Delivery message (short, measured)

1. What was delivered (paths) and slide count / estimated time (from the build or audit output).
2. Rules applied and exceptions used (from the audit: e.g. "body ≥ 36 pt; source line 16 pt;
   references 16 pt").
3. Assumptions made (profile, time target) and user decisions recorded.
4. Not checked: e.g. timed rehearsal, video playback on the classroom PC, Google Slides conversion.
5. Next step suggestion (one line).

## 6. Ledger (`templates/ledger.md`)

Update after every stage: sources verified, images collected (with licences), plan approved, build
version, render pass number and defects fixed, audit result, final file paths + SHA-256, open items.
A new session reads the ledger first and continues; it never re-does finished source analysis.
