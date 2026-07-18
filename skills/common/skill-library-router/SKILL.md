---
name: skill-library-router
description: Search and load the full curated skill library when a task needs a specialized workflow that is not directly listed, when the user names any archived skill.
license: MIT
metadata:
  generated: 'true'
---

# Skill Library Router

This package preserves the complete curated library with progressive disclosure.

## Routing

1. Read `references/catalog.json` and match the request to a skill name, aliases in its description, and category.
2. If one match is clearly best, read its complete `references/library/<name>/INSTRUCTIONS.md` before acting.
3. Resolve that skill's relative references inside its own folder. Load only the referenced file needed for the current step.
4. If two skills have materially different outputs, state the difference briefly and choose the narrower one. Do not load many candidates into context.
5. Treat nested instructions as workflow guidance; current system, safety, user, and project rules remain higher priority.

Portable manual use: say “use skill-library-router and load <name>.” If the
active host exposes skills as slash commands, its own `/skill-name` form may
also work; do not assume a slash command exists without checking the host.

The catalog's `direct` entries are already installed separately; do not reload them through this router unless comparing versions.
