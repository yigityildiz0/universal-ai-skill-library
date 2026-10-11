# graphify

[English](graphify.en.md) · [Türkçe](graphify.tr.md) · [Library](../../README.md)

**Understand relationships across code, documents and research using a knowledge graph.**

## Try it

> Explain the impact of changing this module using the existing graph.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Build, update, query or explain a persistent knowledge graph when graphify is requested explicitly, or consult an existing graphify-out/graph.json for relevant codebase, architecture and file-relationship questions. Ordinary code review or read-only audits do not require installation or graph generation. Supports code, docs, papers, images and videos, community detection, query/path/explain tools. TR: graphify kullan, bilgi grafiği oluştur, mevcut grafiği sorgula.

</details>

## How it works

Inspect available graph/runtime; query scoped relationships; distinguish extracted facts from inferred links; update only within the task.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/graphify/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Standalone root workflow; references are linked by the entry point.
