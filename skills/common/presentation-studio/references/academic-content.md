# Academic content

Use with `academic-study-coach` (argument, terminology) and `medical-evidence-research` (search,
appraisal). This file turns evidence into teachable slides.

## 1. Argument

- Audience, time, the one claim the talk defends, the questions it answers.
- Action titles: each title is the slide's takeaway as a claim. Ghost-deck test: titles alone tell
  a defensible story.
- Each results slide: one primary exhibit + one interpretation. Secondary evidence → notes/appendix.
- Separate result, interpretation, limitation, speculation. Keep sample sizes, comparators, units.
- Methods: enough for credibility, not a protocol transcript — except when the protocol IS the
  teaching point (measurement and technique talks), then show it step by step with a photo.
- End with conclusions and the next question; no empty "Teşekkürler/Sorular?" slide.

## 2. Claims file (`templates/claims.json`)

One entry per number or factual claim used anywhere (slide, notes, guide):
`id, claim, source (APA short + DOI/PMID), value + unit, population (n, age, condition),
protocol/device/test, design, limitation, status (standard | guideline | single study | author
proposal | calculation), slides[]`. Verify against the full text; mark what came only from an
abstract. A claim without a verified source is removed or labelled clearly as uncertain.

## 3. Statistics wording (slides short, notes interpreted)

| Statistic | Say | Interpret with |
|---|---|---|
| ICC | consistency between measurements/raters | Koo & Li 2016: < 0,50 poor, 0,50–0,75 moderate, 0,75–0,90 good, > 0,90 excellent; report model and 95 % CI |
| r / ρ | strength of association | ±0,1 small, ±0,3 moderate, ±0,5 large (Cohen); association ≠ causation |
| p | probability of data this extreme if no effect | < 0,05 conventionally significant; says nothing about size or importance |
| SEM | typical measurement error | same unit as the measure |
| MDC (MDC95) | smallest change beyond error | 1,96 × √2 × SEM |
| MCID | smallest change that matters to patients | population- and anchor-specific; never universal |
| LoA (Bland–Altman) | range of agreement between methods | bias ± 1,96 SD; clinically acceptable width decided beforehand |
| Effect size (d, g) | size of difference | 0,2 small, 0,5 medium, 0,8 large |
| Sensitivity / specificity | detecting true positives / true negatives | with prevalence context |

Thresholds are conventions; say whose and for what.

## 4. Structures

**Lecture topic (teaching classmates).** Agenda as questions → why it matters (big number/clinical
problem) → concepts with units → devices/tools (real photos) → standardised protocol (photoSteps per
test) → error sources and how to control them → interpretation (norms, MDC/MCID, asymmetry) →
clinical use cases → summary answering the agenda → references.

**Article presentation (seminar).** Per article: first page screenshot (journal, year, authors,
country, impact) → aim/hypothesis → design, participants, method (photo/figure of the protocol) →
assessments/outcomes → results (one chart or table) → discussion and limitations → "what I learned /
what I would do differently". Research week: synthesis slide comparing ≥ 8 articles (table/matrix).

**Clinical case.** Short theory (≤ 10–15 slides) → case: demographics, history, complaint (with
consent, anonymised) → ICF-based assessment with both sides compared and reference values → problem
list → goals → treatment with the reason for each choice (photos/videos of the patient with consent)
→ progress/outcome measures → current evidence → summary; group task split anonymised.

**Thesis / conference.** Problem → gap → aim → method → key results (one exhibit each) → discussion →
limitations → conclusion → next question; backup slides for expected questions.

## 5. Physiotherapy practical slides (tests, techniques, exercises)

Every practical slide shows, with a real photo or honest schematic:
1. starting position and body segment alignment,
2. stabilisation (who/what fixes which segment),
3. contact point / sensor or hand placement (landmark + distance),
4. movement or force direction (arrow) and joint angle,
5. command and duration ("5 sn maksimal itme"), number of trials and rest,
6. common errors and how to avoid them,
7. what the result means (unit, norm/MDC, side comparison).
Missing any of these makes the slide decorative rather than teachable.

## 6. Accuracy traps seen in real decks

- Device family vs test type ("isokinetic dynamometer" used for an isometric test).
- Population-specific cut-offs presented as universal (MCID of one group for all).
- Test–retest numbers mislabelled as inter-rater (or vice versa); LoA confused with reliability.
- Rounded numbers drifting between slide, notes and guide — always pull from `claims.json`.
- Teaching (invented) numbers mixed with study results — keep them visibly separate.
