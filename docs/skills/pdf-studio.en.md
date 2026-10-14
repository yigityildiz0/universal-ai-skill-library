# pdf-studio

[English](pdf-studio.en.md) · [Türkçe](pdf-studio.tr.md) · [Library](../../README.md)

**Make reliable PDFs: intake questions first, print-safe HTML/CSS with design languages, rendered pages audited for split tables, stranded headings, overflow and broken letters.**

## Try it

> Make an A4 portrait PDF study guide from these notes, clean clinical design, with references.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Make clean, reliable PDFs (study guides, reports, handouts, summaries, CVs, brochures, forms of any topic): asks the right questions first (orientation, purpose, design language, sources), builds from HTML/CSS with print rules so tables, headings and figures never split badly and nothing overflows, then renders and audits every page. Turkish triggers: PDF hazırla, PDF yap, PDF oluştur, rapor PDF, çalışma kılavuzu, el notu, özet PDF, PDF düzenle, sayfa bölünüyor, tablo ikiye bölündü.

</details>

## How it works

Ask orientation, purpose, design language and sources; build from the print kit; lint the HTML; render with Edge/Chrome; audit and read every page; deliver with checks listed.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/pdf-studio/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Standalone root workflow; references are linked by the entry point.
