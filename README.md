<p align="center"><img src="assets/library-hero.svg" alt="Universal Agent Skill Library compatibility switchboard" width="100%"></p>

<p align="center"><a href="README.tr.md">Türkçe</a> · <a href="https://yigityildiz0.github.io/universal-ai-skill-library/">Search all skills</a> · <a href="CATALOG.md">Full table</a> · <a href="INSTALL.md">Install guide</a> · <a href="THIRD_PARTY_NOTICES.md">Licenses</a></p>

# Universal Agent Skill Library

A bilingual, searchable library of **531 unique Agent Skill names** for Claude Code, OpenAI Codex, and OpenCode. It preserves a common core, small host overlays, individual ZIP downloads, curated platform bundles, a progressive-disclosure router, and 21 conflicting embedded variants without silently merging them.

| Claude Code | OpenAI Codex | OpenCode | Catalog | Unspecified license signal |
|---:|---:|---:|---:|---:|
| 524 | 530 | 525 | 531 | 405 |

## Recommended downloads

[⬇ Claude Code](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-claude.zip) · [⬇ OpenAI Codex](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-codex.zip) · [⬇ OpenCode](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-opencode.zip)

These curated bundles contain **100 Claude**, **106 Codex**, or **101 OpenCode** top-level skills. Each includes `skill-library-router`, which exposes the embedded catalog progressively instead of flooding the host's initial skill list.

## Expanded bundles

[⬇ Claude Code expanded](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-claude-expanded.zip) · [⬇ OpenAI Codex expanded](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-codex-expanded.zip) · [⬇ OpenCode expanded](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-opencode-expanded.zip)

Expanded bundles install every compatible name directly (524 / 530 / 525). They are convenient for offline archives, but installing hundreds of direct skills can crowd discovery metadata. Prefer the curated bundle or individual downloads.

## Find the right skill

- [Interactive English/Turkish catalog](https://yigityildiz0.github.io/universal-ai-skill-library/) — search, category, platform, risk, and license filters.
- [Complete English table](CATALOG.md) — every skill, platform note, capability signal, risk signal, license status, and download.
- [Complete Turkish table](CATALOG.tr.md) — aynı kataloğun Türkçe açıklamaları.
- Machine-readable [JSON](manifests/catalog.json) and [CSV](manifests/catalog.csv).

## Architecture

```text
skills/common/                 portable common core
skills/platforms/codex/        Codex metadata or full host-only skills
skills/platforms/opencode/     OpenCode-only skills
skills/archive-variants/       conflicting embedded versions, never auto-merged
packages/common/               individual portable ZIPs
packages/<platform>/           matching host variants
release-assets/                local release files; published through GitHub Releases
```

## Trust boundary

The source catalog's `hosts` field is not treated as proof of runtime compatibility. The table separately exposes host terms, MCP/slash-command signals, package-install commands, privileged operations, destructive patterns, network/API use, and license gaps. Review before enabling tools.

**Licensing warning:** many supplied packages do not contain a local license or upstream provenance marker. The repository's MIT license covers only the catalog, docs, site, and packaging code—not skill content. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
