# Speaker notes and timing

Notes are read live from PowerPoint's presenter view. They must be short enough to read at a glance,
complete enough to answer a lecturer's follow-up question, and timed so the whole talk fits.

## 1. Template (the presenter accepted this exact structure)

```
[7/55]  Hedef ≈ 0:55 · Bitişte ≈ 6:10 / 38:48

<2–5 short spoken sentences in the presenter's own voice; abbreviations with (okunuş; açılım);
units written as words>

ÖZETLE: <technical slides only — what we must understand from this slide, 1–2 sentences>

ARAŞTIRMA — Yazar ve ark., yıl
• Neden burada: <why this study is on this slide, 1 sentence>
• Ne yapılmış, ne bulunmuş: <sample, method, main number>
• Nasıl yorumlanır: <threshold + meaning + limitation>

TERİMLER:
• ICC (ay-si-si): sınıf içi korelasyon katsayısı (intraclass correlation coefficient): iki ölçüm
  arasındaki tutarlılık; 0–1; < 0,50 zayıf, 0,50–0,75 orta, 0,75–0,90 iyi, > 0,90 mükemmel

→ Geçiş: <one bridge sentence to the next slide>
```

The JS and Python kits assemble this from `deck.json` fields: `say`, `summary`, `research` (object or
list: `cite`, `why`, `what`, `interpret`), `terms` (strings or `{term, say, full, english, def}`),
`question` (likely lecturer question + short answer), `transition`.

## 2. Rules (from the presenter's feedback)

1. **Short and readable.** Spoken part ≈ 80–100 words per slide; soft limit 120, hard limit 160
   (terms and pronunciations excluded). The presenter adds a few words live; do not write an essay.
2. **No raw numbers.** Every number in a research block gets its threshold and meaning: ICC (Koo &
   Li bands), r (correlation size, "ilişki nedensellik değildir"), p (< 0,05 = anlamlı; says nothing
   about size), SEM/MDC/MCID (error vs real change vs clinically important change), effect size.
   "Direkt veri vermişsin, ben yorumlayacakmışım gibi" was a rejected pattern.
3. **Abbreviations every time.** In notes, each abbreviation is followed by (okunuş; açılım) at every
   mention (default `abbreviationMode: "every"`), inside the research block too. Proper names get
   their pronunciation at first mention (`Jamar (ceymar)`, `Koo ve Li (ku ve li)`). r and p are
   abbreviations too: `r (ar; korelasyon katsayısı)`, `p (pe; anlamlılık değeri)`.
4. **Terms** at the bottom: what it is, what it measures, superficially, one line each; English
   original when useful. Short definitions also for slogans the slide uses ("uyum sınırı ne?").
5. **Units as words** in spoken text: "60 newton", "5 santimetre", "newton-metre".
6. **Relative links only in notes.** "Geçen hafta [arkadaşın adı] ölçüm hatasını anlatmıştı…" or "4 hafta
   sonraki sunumda…" — never on the slide. If a topic was covered earlier: "detaylı anlatmayacağım"
   and move on.
7. **No date-bound greetings** ("İyi akşamlar", "bugün") even in notes; start with content.
8. **Explain the why.** Why this slide, why this study, why this calculation, what the standard is.
9. **Too technical?** Simplify on the slide, keep the depth in ÖZETLE + research; or remove the slide
   if the point was already made.
10. **Likely questions** (seminar especially): what did you learn, limitations, what would you do —
    put short answers in `question` or in the reading guide.

## 3. Timing

- Read-aloud speed: **112 words/min**; **+7 s** per slide for showing/transition; section slide 10 s;
  references 2–8 s; spoken words exclude parentheses; the "why" line counts half.
- Target time T = lower-middle of the allowed range (e.g. 30–45 → 35–38 min). Notes reading time ≈
  0.85 × T (the presenter adds words live).
- Content slides N ≈ T × (0.9–1.2), respecting the profile minimum; never force a count.
- Per-slide budget ≈ (0.85 × T × 60 / N − 7) × 112 / 60 words (T = 35, N = 35 → ≈ 82 words).
- Each note starts with `[i/N] Hedef ≈ m:ss · Bitişte ≈ m:ss / toplam` so the presenter can check
  pace while talking.
- Calculated timing is not a rehearsal: say so in the delivery message and in the reading guide
  (rehearsal plan: one timed run, mark slides that ran long).

## 4. Pre-talk reading guide (PDF)

`scripts/make_reading_guide.py deck.json --brief brief.md --out "<Konu> - Sunum öncesi okuma.pdf"`
produces: course rules and how the deck meets them; timing plan; glossary with pronunciations and
English originals; slide-by-slide explanation (what to say, what the visual shows, why it is there);
article cards with DOI links (design, sample, main result, limitation); likely lecturer questions
with answers; rehearsal checklist. It extends the notes; it does not repeat them verbatim.
