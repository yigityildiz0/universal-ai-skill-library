# Visuals: real images first, honest modelling second

The visual must teach the slide's point. For anything physical — a test position, a device, a
grip, hand placement, stabilisation, an exercise, an anatomical landmark, a clinical sign — the
audience must SEE the real thing. A labelled rectangle standing in for a dynamometer teaches nothing.

## 1. Decide the visual per slide (in the slide plan)

For each slide write one line: `visual: <type> — <what it must show>`.

| Content | Best visual | Acceptable fallback |
|---|---|---|
| test position, manual technique, exercise | real photo of that exact position, cropped to the contact point | article figure (open licence) → drawn schematic labelled "şematik" |
| device | real product/device photo | article figure, manufacturer press image only with permission |
| anatomy / mechanism | open atlas or article figure | clean vector schematic (shapes in PPTX) |
| numbers, comparisons | native chart or big-number callout | table ≤5 rows |
| sequence / protocol | numbered steps + photo | process diagram |
| concept / definition | quote/definition slide with one icon or photo | cards |

## 2. Search order for real images (free sources, licence recorded)

1. **The study you cite.** Open-access articles (PMC open-access subset, journals under CC BY) often
   contain the exact protocol photo. Check the licence line on the article page; CC BY / CC BY-SA
   allow reuse with attribution. Cite "Görsel: Yazar ve ark., yıl (CC BY 4.0)".
2. **Wikimedia Commons** and **Openverse**: `python scripts/find_images.py search "<English terms>"`
   then `python scripts/find_images.py get <url|File:title> --out img/<name>.jpg`. Licences go to
   `img/LICENSES.csv` automatically. Search in English with anatomical/clinical words
   ("hand-held dynamometer knee extension seated", "goniometer elbow flexion").
3. **Public-domain institutional media** (U.S. federal agencies such as CDC/NIH/Army: public domain;
   check the page).
4. **User-supplied photos** (their own, a classmate's with consent, course material only for
   internal use) — ask before showing identifiable people.

Do not use: images without a visible licence, watermarked stock, screenshots of paywalled figures
for a public deck, images of identifiable patients without consent, CC BY-NC material in anything
commercial, CC BY-ND material that you crop or annotate (cropping is a modification).

## 3. Preparing images

- Crop to the teaching point (contact point of the sensor, hand placement, joint angle). A close-up
  inset next to the full position is often best.
- Minimum ~1000 px wide for half-slide use, ~1600 px for full-bleed. Never upscale small images.
- Keep aspect ratio (kit `image()` contain/cover). Remove borders/captions baked into the figure only
  if the licence allows modification, and keep the citation.
- Add arrows/labels as PPTX shapes on top of the photo (editable), not burned into the image.
- Alt text: one sentence describing what is shown (kit `alt`).
- Credit line on the slide (14–16 pt, exception role) + full reference on the references slide.

## 4. When no real image exists: model it honestly

1. Draw a clean schematic with PPTX shapes (segments, joints, arrows, angle arcs) or a simple vector
   (SVG) and label it **"şematik / öğretim modeli"** in the credit line.
2. Show what matters: body segment positions, joint angle, axis, force direction, sensor/hand
   location, stabilisation straps. Use the deck colours, no shading or 3-D.
3. If an image-generation tool is available and the user agrees, a generated illustration may be
   used ONLY as an illustration, labelled "yapay zekâ ile üretilmiş çizim — klinik fotoğraf değildir",
   never as evidence and never for anatomy that must be exact.
4. Do not reuse the same schematic for different points; each schematic answers one question.

## 5. Charts and numbers

- Use native PowerPoint charts (editable), labelled values, axis titles with units, ≤5 categories.
- One chart = one message; the takeaway sentence sits beside or under it.
- Re-check every number against `claims.json` (source, population, unit, direction).
- Illustrative (invented) numbers are allowed only as "öğretim örneği" and labelled as such.

## 6. Video

If the lecturer wants video: embed the file (not a link) only after testing playback in the target
PowerPoint; keep a link + a still frame as backup; note the duration in the speaker notes. Never
assume a classroom computer has internet.
