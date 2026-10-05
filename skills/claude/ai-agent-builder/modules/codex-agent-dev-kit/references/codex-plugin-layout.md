# Codex Local Plugin Layout

Use this when a user wants a Claude-style plugin converted into a Codex local plugin.

## Required Files

```text
plugins\<plugin-name>\
  .codex-plugin\plugin.json
```

For a useful skill plugin, also include:

```text
plugins\<plugin-name>\
  skills\
    <skill-name>\
      SKILL.md
      agents\openai.yaml
      scripts\
      references\
  assets\
```

Repo marketplace entry:

```text
.agents\plugins\marketplace.json
```

## Minimal Manifest

```json
{
  "name": "agent-dev-kit",
  "version": "0.1.0",
  "description": "Codex agent development kit with skills, guardrails, and plugin packaging guidance.",
  "author": {
    "name": "Local"
  },
  "license": "MIT",
  "keywords": ["codex", "skills", "agents", "plugins"],
  "skills": "./skills/",
  "interface": {
    "displayName": "Agent Dev Kit",
    "shortDescription": "Codex skills, guardrails, and plugin setup",
    "longDescription": "A local Codex plugin that packages reusable agent-development workflows as skills.",
    "developerName": "Local",
    "category": "Productivity",
    "capabilities": ["Write"],
    "defaultPrompt": [
      "Set up a Codex skill and local plugin bundle."
    ],
    "brandColor": "#8B5CF6"
  }
}
```

## Marketplace Entry

Append an entry like this to `.agents\plugins\marketplace.json`:

```json
{
  "name": "agent-dev-kit",
  "source": {
    "source": "local",
    "path": "./plugins/agent-dev-kit"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

## Validation Checklist

- Folder name equals `plugin.json` `name`.
- `skills` points to `./skills/`.
- Every bundled skill has a valid `SKILL.md`.
- Marketplace path resolves from the repo root.
- Do not include Claude-only `.claude/settings.json` as a runtime config.
