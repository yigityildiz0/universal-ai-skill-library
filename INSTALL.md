# Installation guide

<p align="center"><a href="INSTALL.tr.md"><strong>Türkçe</strong></a> · <a href="README.md">Back to README</a> · <a href="CATALOG.md">Browse skills</a> · <a href="https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest">Latest release</a></p>

This guide covers individual skills, platform bundles, Windows/macOS/Linux paths, updates, uninstalling, checksum verification, and common mistakes.

## Clinical literature packages

1. Download the current [`medical-evidence-research`](CATALOG.md) and [`physio-clinical-copilot`](CATALOG.md) single-skill ZIPs for your host. Their names remain unchanged; GPT/Codex and Claude have separate discovery metadata and the same research/safety coverage.
2. For Codex, extract each GPT/Codex skill folder under `~/.agents/skills/`. For Claude Code use `~/.claude/skills/`; OpenCode can use the portable common packages in its native skill root.
3. For Claude.ai, upload each Claude single-skill ZIP separately using its supported custom-skill setting. The archive contains one `<name>/SKILL.md` root and all references/licenses. Do not upload a two-skill folder bundle as one Claude custom skill.
4. ChatGPT web/mobile plugin distribution needs a separate plugin archive, not an assumption that a filesystem skill ZIP installs account-wide. Use the currently supported import/install flow if your account exposes it. The platform package itself does not create an account installation, network permission, paid connector or scheduled watch.
5. Back up older same-named local folders before replacement. Prefer the consolidated pair instead of also installing the older `research-medical-evidence`, `physio-evidence-search`, `physio-study-appraisal` and broad hub for the same purpose. Legacy names remain downloadable and preserve standalone fallback behavior; when installed together their routing selects one primary workflow.
6. Confirm the final folder/ZIP shape, source identity and SHA256; test a real query and check actual provenance/access. Source/package validation is separate from Claude, GPT or connector runtime verification. No cloud-account installation is certified by this repository update.

The October 2026 update adds PEDro-native search syntax, source/provider and pagination logs, design-specific appraisal, between-group effects, independent human final eligibility for formal reviews, and recoverable literature-watch checkpoints. A watch requires a separately authorized alert/automation; the skill alone does not run later.

## Choose what to download

| Goal | Download |
|---|---|
| Install one specific skill | Open [CATALOG.md](CATALOG.md), find the skill, and use its platform download link. |
| Install the recommended starter library | Use the curated bundle for your agent below. |
| Keep everything offline | Use an expanded bundle from the [latest release](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest). |

> Do not use GitHub's green **Code → Download ZIP** button when you want an install-ready bundle. That button downloads the repository source.

## Platform roots

| Agent | Personal — macOS/Linux | Personal — Windows | Project |
|---|---|---|---|
| Claude Code | `~/.claude/skills/` | `%USERPROFILE%\.claude\skills\` | `.claude/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `%USERPROFILE%\.agents\skills\` | `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `%USERPROFILE%\.config\opencode\skills\` | `.opencode/skills/` |

On Windows, `~` means your user folder, normally `C:\Users\<username>`.

OpenCode also scans compatible skills from Claude and Codex skill roots. The dedicated OpenCode bundle uses `.opencode/skills` so its installation remains explicit.

## Install a curated bundle

| Agent | Bundle |
|---|---|
| Claude Code | [⬇ Download](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-claude.zip) |
| OpenAI Codex | [⬇ Download](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-codex.zip) |
| OpenCode | [⬇ Download](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-opencode.zip) |

### Personal installation

1. Download the bundle matching your agent.
2. Inspect the ZIP and back up any same-named skill folders you customized.
3. Extract the ZIP into your user/home folder. The archive already contains `.claude/skills`, `.agents/skills`, or `.opencode/skills`.
4. Confirm that the final tree contains `<skills-root>/<skill-name>/SKILL.md`.
5. Restart the host if the new skills do not appear.

Windows PowerShell example for Codex:

```powershell
Expand-Archive -LiteralPath "$env:USERPROFILE\Downloads\universal-ai-skill-library-codex.zip" -DestinationPath $env:USERPROFILE
```

macOS/Linux example for Codex:

```bash
unzip ~/Downloads/universal-ai-skill-library-codex.zip -d "$HOME"
```

### Project installation

Extract the matching bundle into the project root instead of your home folder. Commit project-scoped skills only if their licenses and your repository policy allow it.

## Install one skill

1. Open [CATALOG.md](CATALOG.md).
2. Find the skill and click the download for your platform.
3. Open the ZIP and inspect `SKILL.md`, scripts, dependencies, and external-service requirements.
4. Extract the skill folder under the correct personal or project root.
5. Confirm this exact shape:

```text
<skills-root>/
└── skill-name/
    ├── SKILL.md
    ├── references/   optional
    ├── scripts/      optional
    └── assets/       optional
```

- Wrong: `<skills-root>/skill-name/skill-name/SKILL.md`
- Correct: `<skills-root>/skill-name/SKILL.md`

## Verify metadata and safety

- `SKILL.md` must use that exact uppercase filename.
- The YAML frontmatter must contain a valid `name` and `description`.
- The folder name should match the frontmatter `name`.
- Read scripts before execution; do not assume a ZIP is safe because it is listed here.
- Review package installation, network/API access, credentials, privileged actions, deletion, and publication requirements.
- A catalog platform mapping is not proof that every dependency was tested on that host.

## Verify the checksum

Windows PowerShell:

```powershell
Get-FileHash .\universal-ai-skill-library-codex.zip -Algorithm SHA256
```

macOS/Linux:

```bash
sha256sum universal-ai-skill-library-codex.zip
```

Compare the result with [manifests/SHA256SUMS.txt](manifests/SHA256SUMS.txt). Release bundles are listed under `release-assets/` in that file.

## Update a skill or bundle

1. Download the new version.
2. Compare it with your installed copy, especially if you made local edits.
3. Back up the exact skill folder you are replacing.
4. Replace only that verified folder or extract the updated bundle after reviewing name conflicts.
5. Restart the host if it does not reload the change automatically.

Do not blindly overwrite customized skills.

## Uninstall

1. Resolve the exact skill folder: `<skills-root>/<skill-name>/`.
2. Confirm it contains the skill you intend to remove.
3. Delete only that folder using your file manager or a platform-native command you understand.
4. Do not delete the entire skill root.
5. Restart the host if the removed skill remains cached.

## Troubleshooting

### The skill does not appear

- Check that you used the correct agent root.
- Check for double nesting.
- Check that the filename is exactly `SKILL.md`.
- Validate YAML frontmatter and make sure `name` matches the folder.
- Restart the agent, especially if you created its skill root for the first time.

### The skill appears but cannot run

- Read its platform note in [CATALOG.md](CATALOG.md).
- Check required local tools, runtimes, environment variables, external services, and permissions.
- Treat format compatibility and runtime readiness as separate questions.

### Hundreds of skills make discovery noisy

Use the curated bundle or install individual skills. The expanded archive is intended for deliberate offline/audit use.

### A ZIP or link is missing

Open the [latest release](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest), confirm the asset name, and report a reproducible issue with the broken URL.

## Official platform references

- [Claude Code — where skills live](https://code.claude.com/docs/en/skills#where-skills-live)
- [OpenAI Codex — where to save skills](https://developers.openai.com/codex/skills/#where-to-save-skills)
- [OpenCode — Agent Skills](https://opencode.ai/docs/skills)

Before redistribution, read [LICENSE.md](LICENSE.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
