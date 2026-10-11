---
name: parallel-web
description: "Use ONLY when the user explicitly asks for Parallel (parallel.ai) or parallel-cli / Parallel Search MCP is configured: web search, URL extraction, deep research reports, FindAll entity discovery, bulk data enrichment, web monitoring, run status/results and setup. Upstream parallel-web/parallel-agent-skills. Turkish triggers: Parallel ile ara, Parallel deep research, Parallel ile listeyi zenginleştir, Parallel ile web'i izle."
license: MIT
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


# Parallel Web (gated)

Upstream [parallel-web/parallel-agent-skills](https://github.com/parallel-web/parallel-agent-skills) (MIT), preserved as modules. The execution gate below governs their use on the current host.

**Current profile:** preserve the complete upstream service documentation, but do not execute Parallel CLI/API/MCP calls under the user’s no-extra-cost preference, even if configured. For search, extraction, deep research and multi-item discovery, use `research-analyst` with existing host tools or local data. Setup and migration modules are documentation, not an instruction to open an account, buy credits or change providers. Explain any service-only capability that has no available equivalent.

“Paralel araştır / work in parallel” does not by itself name Parallel.ai. Discover the actual connector/CLI before following a module; installed documentation is not proof of authentication, funding or live availability. Do not auto-install, open accounts, buy credits, start monitoring/subscriptions, or upload local/private datasets. A configured search connector authorizes neither a paid Task/FindAll run nor a data upload; obtain task-specific consent where needed. Module trigger phrases are natural-language examples, not registered host commands. Use the parent gate even when a module says “always” or “automatic”.

## Modules

- [`choose-your-parallel-api`](modules/choose-your-parallel-api/MODULE.md) — Choose the right Parallel API and configuration for cost, latency, and answer quality.
- [`migrate-to-parallel`](modules/migrate-to-parallel/MODULE.md) — Migrate Exa, Tavily, Perplexity, or Firecrawl web-data integrations completely to the appropriate Parallel products while preserving applic…
- [`parallel-cli-setup`](modules/parallel-cli-setup/MODULE.md) — Set up and maintain the Parallel CLI (install, auth, balance, skills install)
- [`parallel-data-enrichment`](modules/parallel-data-enrichment/MODULE.md) — Bulk data enrichment.
- [`parallel-deep-research`](modules/parallel-deep-research/MODULE.md) — ONLY use when user explicitly says 'deep research', 'exhaustive', 'comprehensive report', or 'thorough investigation'.
- [`parallel-findall`](modules/parallel-findall/MODULE.md) — Discover entities (companies, people, products, etc.) matching a natural-language description.
- [`parallel-mcp-setup`](modules/parallel-mcp-setup/MODULE.md) — Use when installing, configuring, or troubleshooting an authenticated Parallel Search MCP connection in Bifrost, including gateway-level se…
- [`parallel-memory`](modules/parallel-memory/MODULE.md) — Recall past Parallel Task, Monitor, and FindAll runs when they may help; evict runs or clear memory when asked.
- [`parallel-monitor`](modules/parallel-monitor/MODULE.md) — Continuously track the web for changes on a recurring cadence.
- [`parallel-search-setup`](modules/parallel-search-setup/MODULE.md) — Use when verifying, using, or troubleshooting the anonymous Parallel Search MCP server bundled with this plugin — when the user installs th…
- [`parallel-web-extract`](modules/parallel-web-extract/MODULE.md) — CLI-backed URL extraction.
- [`parallel-web-search`](modules/parallel-web-search/MODULE.md) — CLI-backed web search.
- [`result`](modules/result/MODULE.md) — Get completed research task result by run ID
- [`status`](modules/status/MODULE.md) — Check running research task status by run ID
