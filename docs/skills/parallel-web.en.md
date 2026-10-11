# parallel-web

[English](parallel-web.en.md) · [Türkçe](parallel-web.tr.md) · [Library](../../README.md)

**Retain Parallel service documentation while routing this edition to existing no-extra-cost research tools.**

## Try it

> Research several sources without adding a paid research service.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Use ONLY when the user explicitly asks for Parallel (parallel.ai) or parallel-cli / Parallel Search MCP is configured: web search, URL extraction, deep research reports, FindAll entity discovery, bulk data enrichment, web monitoring, run status/results and setup. Upstream parallel-web/parallel-agent-skills. Turkish triggers: Parallel ile ara, Parallel deep research, Parallel ile listeyi zenginleştir, Parallel ile web'i izle.

</details>

## How it works

Identify the research need; use available host search/fetch or local data; keep vendor-only examples as references; disclose unavailable capabilities.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/parallel-web/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [choose-your-parallel-api](../../skills/common/parallel-web/modules/choose-your-parallel-api/MODULE.md) | Choose the right Parallel API and configuration for cost, latency, and answer quality. Use when adding live web data to an app: current events and prices, a cited answer in a chat, |
| [migrate-to-parallel](../../skills/common/parallel-web/modules/migrate-to-parallel/MODULE.md) | Migrate Exa, Tavily, Perplexity, or Firecrawl web-data integrations completely to the appropriate Parallel products while preserving application behavior. Use when replacing these  |
| [parallel-cli-setup](../../skills/common/parallel-web/modules/parallel-cli-setup/MODULE.md) | Set up and maintain the Parallel CLI (install, auth, balance, skills install) |
| [parallel-data-enrichment](../../skills/common/parallel-web/modules/parallel-data-enrichment/MODULE.md) | Bulk data enrichment. Adds web-sourced fields (CEO names, funding, contact info) to lists of companies, people, or products. Use for enriching CSV files or inline data. Supports mu |
| [parallel-deep-research](../../skills/common/parallel-web/modules/parallel-deep-research/MODULE.md) | ONLY use when user explicitly says 'deep research', 'exhaustive', 'comprehensive report', or 'thorough investigation'. Slower and more expensive than parallel-web-search. For norma |
| [parallel-findall](../../skills/common/parallel-web/modules/parallel-findall/MODULE.md) | Discover entities (companies, people, products, etc.) matching a natural-language description. Use when the user asks to 'find all X' or 'list every Y that…' — e.g., 'Find AI start |
| [parallel-mcp-setup](../../skills/common/parallel-web/modules/parallel-mcp-setup/MODULE.md) | Use when installing, configuring, or troubleshooting an authenticated Parallel Search MCP connection in Bifrost, including gateway-level search settings and downstream tool access. |
| [parallel-memory](../../skills/common/parallel-web/modules/parallel-memory/MODULE.md) | Recall past Parallel Task, Monitor, and FindAll runs when they may help; evict runs or clear memory when asked. |
| [parallel-monitor](../../skills/common/parallel-web/modules/parallel-monitor/MODULE.md) | Continuously track the web for changes on a recurring cadence. Use when the user asks to 'monitor', 'track changes to', 'watch', or 'alert me when' something on the web changes — e |
| [parallel-search-setup](../../skills/common/parallel-web/modules/parallel-search-setup/MODULE.md) | Use when verifying, using, or troubleshooting the anonymous Parallel Search MCP server bundled with this plugin — when the user installs the plugin, says "set up Parallel Search",  |
| [parallel-web-extract](../../skills/common/parallel-web/modules/parallel-web-extract/MODULE.md) | CLI-backed URL extraction. Use when the user explicitly invokes this skill, needs CLI-only controls or saved JSON output, or no Parallel web_fetch MCP tool is available. When the b |
| [parallel-web-search](../../skills/common/parallel-web/modules/parallel-web-search/MODULE.md) | CLI-backed web search. Use when the user explicitly invokes this skill, needs CLI-only controls or saved JSON output, or no Parallel web_search MCP tool is available. When the bund |
| [result](../../skills/common/parallel-web/modules/result/MODULE.md) | Get completed research task result by run ID |
| [status](../../skills/common/parallel-web/modules/status/MODULE.md) | Check running research task status by run ID |
