# ai-agent-builder

[English](ai-agent-builder.en.md) · [Türkçe](ai-agent-builder.tr.md) · [Library](../../README.md)

**Build, audit and maintain skills, agent workflows and MCP integrations.**

## Try it

> Review this skill package and improve its routing without losing features.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Builds and maintains AI tooling: writes, merges, ports and audits skills and plugins, security-checks downloaded skill packages, builds MCP servers and ChatGPT Apps SDK apps, converts Claude Code agent kits for Codex, audits context and skill budgets, and compares AI models, providers and subscriptions for a task. Turkish triggers: skill yaz/düzenle/birleştir, eklenti kur, bu skill güvenli mi, MCP sunucusu yap, ChatGPT app, hangi model daha iyi, Claude mu ChatGPT mi, context şişti. More triggers: becerileri karşılaştır, tetikleyiciyi düzelt, kaliteyi koruyarak güncelle, skill senkronla, guardrail ve komutları uyarla, API karşılaştır, yerel mi bulut mu.

</details>

## How it works

Select the writing, update, security or integration module; inspect the host; make a bounded change; validate the result.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/ai-agent-builder/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [ai-model-route-evaluator](../../skills/common/ai-agent-builder/modules/ai-model-route-evaluator/MODULE.md) | Compare current AI models, providers, gateways, subscriptions, local routes, and free/paid endpoints for a concrete task. Evaluate exact model identity, modality, Turkish and multi |
| [chatgpt-apps](../../skills/common/ai-agent-builder/modules/chatgpt-apps/MODULE.md) | Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools. Turkish triggers: ChatGPT  |
| [codex-agent-dev-kit](../../skills/common/ai-agent-builder/modules/codex-agent-dev-kit/MODULE.md) | Convert Claude Code agent-kit setups into Codex-compatible skills, project instructions, guardrail scripts, command workflows, and subagent guidance. Use when migrating an agent ki |
| [context-budget](../../skills/common/ai-agent-builder/modules/context-budget/MODULE.md) | Audit actual context consumption and routing overhead across instructions, skill metadata and bodies, tool schemas, agent definitions, conversation output, and project files. Use w |
| [mcp-builder](../../skills/common/ai-agent-builder/modules/mcp-builder/MODULE.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers  |
| [safe-skill-updater](../../skills/common/ai-agent-builder/modules/safe-skill-updater/MODULE.md) | Audit, compare, merge, repair, or improve user-owned Codex and ChatGPT skill variants while preserving proven behavior. Use for skill regression analysis, semantic diffs, trigger r |
| [skill-package-security-audit](../../skills/common/ai-agent-builder/modules/skill-package-security-audit/MODULE.md) | Perform a static, read-only security and trust preflight on a downloaded or third-party skill, plugin, ZIP, repository, installer, or update. Use before import, installation, execu |
| [writing-skills](../../skills/common/ai-agent-builder/modules/writing-skills/MODULE.md) | Create, edit, split, merge, port, or validate agent skills and SKILL.md packages. Use for skill architecture, trigger descriptions, supporting references/scripts, host variants, re |
