# Provenance

- Upstream: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Declared skill version (skill.json): 2.6.2
- Git tag pointing at the source commit: v2.10.2
- CLI package version (cli/package.json): 2.5.0
- Source commit: 12b486b22e67f5d887962ef8351c1ac863bfaeb9
- Retrieved: 2026-07-10
- License: MIT

The upstream repository contains inconsistent version metadata at this commit, so the declared skill version, Git tag, and CLI package version are recorded separately instead of presenting one as universally authoritative.

The canonical package uses the complete upstream data and Python search engine rather than pointer stubs. It intentionally excludes draft.csv and design.csv because upstream marks them as design backup/reference files that are not read by the search engine and they duplicate production data in Chinese.

Verified production data counts:

| Dataset | Records |
|---|---:|
| Styles | 84 |
| Color palettes and products | 192 |
| Font pairings | 74 |
| UX guidelines | 99 |
| Chart patterns | 25 |
| Google Fonts | 1,923 |
| Icon records | 105 |
| Technology stacks | 22 |

Curated changes are limited to provider-neutral instructions, accurate counts, portable skill-relative paths, English production text, and host-agnostic output wording. Functional CSV schemas and search behavior remain compatible with upstream 2.6.2.
