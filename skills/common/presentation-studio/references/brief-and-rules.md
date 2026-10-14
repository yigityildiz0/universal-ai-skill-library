# Default rules and the brief

These defaults come from the presenter's lecturers (recorded course rules), the presenter's own
feedback on earlier AI-made decks, and presentation practice. They apply without asking. A user
request that contradicts one triggers the conflict question in SKILL.md.

## 1. The brief (`templates/brief.md`) — always first

Fill from the conversation, course files and the course profile; ask only for facts that change the
result and are missing (time limit, course, mandatory template, group or solo).

- Topic and the 3–6 questions the talk answers.
- Audience and level: master's level content explained so that someone new to it understands.
- Course profile (`course-profiles.md`) and any written course rules in the user's files. The
  course's own lecturer overrides other courses; borrowed rules are labelled as borrowed.
- Time target and slide range (formula in `speaker-notes.md`).
- Type floor and exceptions, font, theme.
- Sources policy (which source types are accepted, recency, reference style).
- Deliverables, file names, folder, upload destination.
- "Kullanıcı kararları": every answer to a conflict question, dated.

## 2. Typography (defaults)

| Rule | Default |
|---|---|
| Font | **Calibri** for everything (titles bold); fallback **Arial**. One family in the whole deck. |
| Never | Segoe UI, Aptos, Montserrat, Roboto, Poppins, any downloaded/decorative font, WordArt |
| Floor | **36 pt** for every text on a slide (body, bullets, steps, labels, captions, table cells, chart labels and axes, callouts, chips) |
| Title | 40–44 pt bold, left aligned, same position on every content slide |
| Cover / section titles | 48–60 pt; section number 96–110 pt |
| Big numbers | 60–96 pt (up to 110 for section numbers) |
| Exceptions (only these) | source line 14–16 pt (bottom left), references slide 14–16 pt, slide number 12–16 pt, image credit 12–16 pt |
| Off by default | small section labels / kickers (20 pt) — ask before using; otherwise make it a ≥36 pt subtitle or drop it |
| Not text | screenshots of an article's first page or figures are images; the floor does not apply but they must be legible enough for their purpose |

When text does not fit at the floor: shorten → split the slide → move detail to notes. Never shrink.

## 3. Density

- ≤ 6 lines per slide at 36 pt (lecturers asked for 5–7); ≤ 8–10 words per line; no paragraphs.
- One message per slide; every slide teaches something new.
- Bullets are phrases, not long sentences; the explanation is spoken (notes), not printed.
- Technical slides get a short "Özetle" box (one line: what we must understand from this slide).
- Visual slides: the image is big and alone with ≤ 2 short labels; do not dwell on it.
- Clinical-case profile may carry more informative on-slide text (still ≤ 7 lines) if the user asks.

## 4. Sources

- Scientific claim on a slide → short source line bottom left: `Kaynak: Yazar ve ark., yıl`.
  Agenda, section, summary and purely structural slides carry none.
- Only peer-reviewed articles or textbooks (international preferred); no blogs, random websites,
  YouTube, AI chats. Lecture notes are never cited with page numbers as a scientific source.
- Every reference verified (PubMed/DOI/Crossref) and every critical number checked in the full text.
- Reliability is checked but never written on the slide ("güvenilir kaynak" etc. is not printed).
- A schematic built from a concept: `Kavram kaynağı: Yazar, yıl`. No "öğretim örneği" label; do not
  show a weak or wrong source as an example.
- Full references at the end: APA 7, one consistent style, DOI/URL, alphabetical.
- Research boxes on slides only for key findings; the research story goes into the notes.
- Turkish studies are highlighted when they exist ("Türkiye'den de bir çalışma var").

## 5. Language and wording

- The presenter's own Turkish; natural, short, no translation-smell, no ChatGPT-sounding filler
  ("önemli bir rol oynar", "kritik öneme sahiptir", "bu bağlamda"). Lecturers penalise copy-paste
  and translated-sounding sentences.
- Correct professional terminology (fleksiyon, ekstansiyon, abdüksiyon…) instead of lay phrases.
- Titles are claims ("Sensörün yeri torku değiştirir"), not topic labels ("Tork").
- Abbreviations: on the slide, give a short Turkish expansion at first appearance; pronunciations
  go only into the notes.
- No open-ended rules or numbers: every rule/number states its basis — standard, guideline, one
  author's proposal, or a calculation — and why.

## 6. Forbidden on slides (build + audit check these)

- Time-bound phrases: "bu akşam", "bugün", "iyi akşamlar", "geçen hafta", "haftaya" — the deck must
  stay valid as a study file. Relative links to classmates' talks go only in the notes.
- Classmates' names and dates on slides.
- A "Tartışalım" / "Sorular?" invitation slide. (Seminar profile: content slide "Ne öğrendik /
  sınırlılıklar / ben yapsam" instead; closing courtesy sentence goes in the notes.)
- "öğretim örneği", reliability remarks, placeholders (lorem, TODO, xxx).
- Animations and transitions (a separate animated copy only on request).
- Patient-identifiable images without consent; names in group task lists (use "A kişisi, B kişisi").

## 7. Structure defaults

- Cover: title, subtitle, presenter, course, date; course lecturer line only if the course profile
  says so (default: small "Ders sorumlusu" line on the cover only for course talks).
- Agenda with the questions → section dividers (dark) → content → summary that answers the agenda →
  references.
- Section rhythm: dark cover/section/closing, light content.
- Slide count follows time, never a forced number (see `speaker-notes.md` timing).

## 8. Deliverables (default)

`<Konu> - Sunum.pptx`, `<Konu> - Sunum.pdf`, `<Konu> - Sunum öncesi okuma.pdf` in the course folder.
Working files, renders and scripts stay in an "AI çalışmaları" area, never mixed into the user's
course folder. Details: `qa-and-delivery.md`.
