# context7-mcp

[English](context7-mcp.en.md) · [Türkçe](context7-mcp.tr.md) · [Library](../../README.md)

**Retrieve current library documentation through an available Context7 integration.**

## Try it

> Check the current documented API before changing this React integration.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Context7 MCP compatibility guide for explicit Context7 requests, library-ID resolution, query tuning, or hosts without find-docs. General library/framework/API documentation questions route to find-docs first; do not load both for the same lookup. TR: Context7 kullan, Context7 kütüphane kimliği, doküman sorgusunu iyileştir.

</details>

## How it works

Resolve the exact library/version; ask a focused documentation question; ground the implementation in retrieved examples.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/context7-mcp/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Standalone root workflow; references are linked by the entry point.
