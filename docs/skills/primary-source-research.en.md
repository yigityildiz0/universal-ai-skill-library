# primary-source-research

[English](primary-source-research.en.md) · [Türkçe](primary-source-research.tr.md) · [Library](../../README.md)

**Answer from official documents, specifications, source code and first-party records.**

## Try it

> Verify this API behavior from the official documentation and source.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Answer research questions from primary sources: official docs, specifications, source code and first-party records. Return cited findings in chat; create a repository memo only when requested. TR: resmi dokümandan araştır, API nasıl çalışıyor, birincil kaynaktan doğrula, kaynaklı not dosyası çıkar.

</details>

## How it works

Locate the source that owns the claim; inspect the relevant passage/version; reconcile contradictions; return citations in chat or a requested memo.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/primary-source-research/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Standalone root workflow; references are linked by the entry point.
