---
name: ai-agent-builder
description: "Builds and maintains AI tooling: writes, merges, ports and audits skills and plugins, security-checks downloaded skill packages, builds MCP servers and ChatGPT Apps SDK apps, converts Claude Code agent kits for Codex, audits context and skill budgets, and compares AI models, providers and subscriptions for a task. Turkish triggers: skill yaz/düzenle/birleştir, eklenti kur, bu skill güvenli mi, MCP sunucusu yap, ChatGPT app, hangi model daha iyi, Claude mu ChatGPT mi, context şişti. More triggers: becerileri karşılaştır, tetikleyiciyi düzelt, kaliteyi koruyarak güncelle, skill senkronla, guardrail ve komutları uyarla, API karşılaştır, yerel mi bulut mu."
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


# AI Agent Builder

Build and maintain AI tooling: skills, plugins, MCP servers, ChatGPT apps, agent configuration and model choice.

## Choose the module

| Need | Module |
|---|---|
| Write, edit, split, merge or port a skill | `writing-skills` |
| Compare, repair or improve existing skill variants without regressions | `safe-skill-updater` |
| Trust and security check of a downloaded skill, plugin, ZIP or repo before installing | `skill-package-security-audit` |
| Build an MCP server | `mcp-builder` |
| ChatGPT Apps SDK app (MCP server + widget) | `chatgpt-apps` |
| Convert a Claude Code agent kit to Codex (or back) | `codex-agent-dev-kit` |
| Context, skill or tool budget audit | `context-budget` |
| Which AI model, provider or subscription for a task | `ai-model-route-evaluator` |

## Host installation and maintenance

Read the collection's INSTALL.md and verify the current host documentation. Use a user-selected source repository and output directory. Edit source, regenerate selected editions, then validate before installation. Do not assume an existing local deployment, cloud upload, agent account or shared configuration.

## Rules

- Respect the user's archive-retention preference. Validate source and targets before deployment; do not create backups when `keep_backups` is false.
- Never execute downloaded scripts merely to inspect them.
- Test triggering with a few realistic prompts after changing a description.

## Module map

Open only the module(s) the request needs and read the module file completely before acting. Several modules may combine in one task.

| Module | Use when | File |
|---|---|---|
| `writing-skills` | Create, edit, split, merge, port, or validate agent skills and SKILL.md packages. | [MODULE.md](modules/writing-skills/MODULE.md) |
| `safe-skill-updater` | Audit, compare, merge, repair, or improve user-owned Codex and ChatGPT skill variants while preserving proven behavior. | [MODULE.md](modules/safe-skill-updater/MODULE.md) |
| `skill-package-security-audit` | Perform a static, read-only security and trust preflight on a downloaded or third-party skill, plugin, ZIP, repository, installer, or update. | [MODULE.md](modules/skill-package-security-audit/MODULE.md) |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. | [MODULE.md](modules/mcp-builder/MODULE.md) |
| `chatgpt-apps` | Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. | [MODULE.md](modules/chatgpt-apps/MODULE.md) |
| `codex-agent-dev-kit` | Convert Claude Code agent-kit setups into Codex-compatible skills, project instructions, guardrail scripts, command workflows, and subagent guidance. | [MODULE.md](modules/codex-agent-dev-kit/MODULE.md) |
| `context-budget` | Audit actual context consumption and routing overhead across instructions, skill metadata and bodies, tool schemas, agent definitions, conversation output, and project f… | [MODULE.md](modules/context-budget/MODULE.md) |
| `ai-model-route-evaluator` | Compare current AI models, providers, gateways, subscriptions, local routes, and free/paid endpoints for a concrete task. | [MODULE.md](modules/ai-model-route-evaluator/MODULE.md) |

Supporting files (open only when the module points to them):

- `writing-skills`: [anthropic-best-practices.md](modules/writing-skills/anthropic-best-practices.md), [CLAUDE_MD_TESTING.md](modules/writing-skills/examples/CLAUDE_MD_TESTING.md), [persuasion-principles.md](modules/writing-skills/persuasion-principles.md), [testing-skills-with-subagents.md](modules/writing-skills/testing-skills-with-subagents.md)
- `safe-skill-updater`: [evaluation-and-rule-promotion.md](modules/safe-skill-updater/references/evaluation-and-rule-promotion.md), [model-provider-policy.md](modules/safe-skill-updater/references/model-provider-policy.md), [quality-preservation-rubric.md](modules/safe-skill-updater/references/quality-preservation-rubric.md); scripts: `modules/safe-skill-updater/scripts/analyze_skill_corpus.py`
- `skill-package-security-audit`: [review-checklist.md](modules/skill-package-security-audit/references/review-checklist.md); scripts: `modules/skill-package-security-audit/scripts/inspect_skill_package.py`
- `mcp-builder`: [evaluation.md](modules/mcp-builder/reference/evaluation.md), [mcp_best_practices.md](modules/mcp-builder/reference/mcp_best_practices.md), [node_mcp_server.md](modules/mcp-builder/reference/node_mcp_server.md), [python_mcp_server.md](modules/mcp-builder/reference/python_mcp_server.md); scripts: `modules/mcp-builder/scripts/connections.py`, `modules/mcp-builder/scripts/evaluation.py`
- `chatgpt-apps`: [app-archetypes.md](modules/chatgpt-apps/references/app-archetypes.md), [apps-sdk-docs-workflow.md](modules/chatgpt-apps/references/apps-sdk-docs-workflow.md), [interactive-state-sync-patterns.md](modules/chatgpt-apps/references/interactive-state-sync-patterns.md), [repo-contract-and-validation.md](modules/chatgpt-apps/references/repo-contract-and-validation.md), [search-fetch-standard.md](modules/chatgpt-apps/references/search-fetch-standard.md), [upstream-example-workflow.md](modules/chatgpt-apps/references/upstream-example-workflow.md), [window-openai-patterns.md](modules/chatgpt-apps/references/window-openai-patterns.md)
- `codex-agent-dev-kit`: [claude-to-codex-map.md](modules/codex-agent-dev-kit/references/claude-to-codex-map.md), [codex-plugin-layout.md](modules/codex-agent-dev-kit/references/codex-plugin-layout.md)
- `ai-model-route-evaluator`: [evaluation-scorecard.md](modules/ai-model-route-evaluator/references/evaluation-scorecard.md)
