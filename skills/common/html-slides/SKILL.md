---
name: html-slides
description: "Create strategic HTML/web presentations with Chart.js, design tokens, responsive layouts, copywriting formulas and contextual slide strategies. Only for decks that must run in a browser; PowerPoint/PPTX decks and speaker notes belong to presentation-studio. Turkish triggers: HTML sunum, web sunumu, tarayıcıda çalışan slayt, Chart.js sunum."
metadata:
  author: claudekit
  version: "1.0.0"
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


# Slides

Strategic HTML presentation design with data visualization.

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content

## Subcommands

| Subcommand | Description | Reference |
|------------|-------------|-----------|
| `create` | Create strategic presentation slides | `references/create.md` |

## Script Paths

Resolve `<SKILL_DIR>` to the directory containing this file. The bundled helpers and CSV databases live in `yigit/scripts/` and `yigit/data/`; no sibling skill is required. Run helpers by absolute path with the working directory at the target project root. Read [yigit/YIGIT-WORKFLOW.md](yigit/YIGIT-WORKFLOW.md) for the narrative workflow and helper usage; its `<skill-dir>` means `<SKILL_DIR>/yigit`.

## Output routing

- This skill builds HTML decks. For an explicitly requested editable `.pptx`, use an available PowerPoint/presentation tool and its actual schema; do not rename HTML to PPTX or imply an export was tested.
- Academic, thesis, conference, seminar and FTR teaching talks route first to `academic-study-coach`; return here only for a requested HTML rendering of the approved academic outline.
- Infer format from the request; ask only if HTML versus editable PPTX materially changes the deliverable. Do not generate an image, PDF or extra file merely to answer a planning question.

## References (Knowledge Base)

| Topic | File |
|-------|------|
| Layout Patterns | `references/layout-patterns.md` |
| HTML Template | `references/html-template.md` |
| Copywriting Formulas | `references/copywriting-formulas.md` |
| Slide Strategies | `references/slide-strategies.md` |

## Routing

1. Use the user's request directly; `$ARGUMENTS` is optional host syntax.
2. For creation, read `references/create.md` and execute it directly.
3. Read only the additional references required by the deliverable.

## the user's working rules (added)

The upstream HTML workflow is retained with local script-path and output-routing adaptations. the user's earlier customized workflow for this skill is kept in [yigit/YIGIT-WORKFLOW.md](yigit/YIGIT-WORKFLOW.md). Read it as well; where it is stricter (keep the existing stack, no new dependencies, verify accessibility and the rendered result, preserve brand assets), follow it. Otherwise the upstream instructions apply.
