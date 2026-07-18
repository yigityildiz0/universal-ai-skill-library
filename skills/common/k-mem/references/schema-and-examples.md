# K-Mem schema and examples

## Hot-cache marker

```markdown
<!-- k-mem:start -->
## K-Mem hot cache

### People
| Alias | Canonical identity | Why relevant |
|---|---|---|

### Terms
| Term | Meaning | Scope |
|---|---|---|

### Active projects
| Project | State | Next decision |
|---|---|---|

### Preferences
- ...

Full index: `.k-mem/index.md`
<!-- k-mem:end -->
```

## Deep-memory entry metadata

Use plain Markdown. Add a small evidence block when the fact could change:

```markdown
# Project Phoenix

- Status: active
- Last verified: 2026-07-10
- Source: user statement in current task
- Aliases: Phoenix, migration project

## Context
...

## Decisions
- 2026-07-10 — Chose PostgreSQL migration path because ...
```

## Conflict handling

```text
Current memory: Todd = Finance lead (verified 2026-03-01)
New source: Todd = Revenue Operations (message dated 2026-07-08)

Do not overwrite silently. Present:
- keep old role as historical and update current role;
- mark the new claim unverified;
- leave unchanged.
```

## Cross-host rule

Keep one source of truth. A Claude-specific rule file may point to the same `.k-mem/` directory, but it must not contain a second copy of people, terms, or decisions.
