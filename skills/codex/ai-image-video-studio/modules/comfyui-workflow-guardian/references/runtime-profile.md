# Runtime Profile

Resolve machine-specific values at runtime. Do not persist a person's username, home directory, hardware inventory, model filenames, or private workflow names in the reusable skill.

## Runtime Discovery

Before changing a ComfyUI installation, determine only the values required for the current task:

- operating system and relevant GPU/backend family
- ComfyUI root directory
- launcher or startup command, if troubleshooting startup
- exact workflow file explicitly selected by the user
- model, VAE, text-encoder, LoRA, and custom-node paths referenced by that workflow
- optional backup/archive destination selected for the current operation

Prefer values supplied by the user or discovered from the active workspace. If discovery is ambiguous, do not guess a path from a previous machine.

## Path Examples

Use generic placeholders in reusable instructions:

```text
<COMFYUI_ROOT>
<COMFYUI_LAUNCHER>
<WORKFLOW_PATH>
<BACKUP_DIRECTORY>
```

On Windows, a command may look like:

```powershell
python scripts/check_comfyui_workflow.py "<WORKFLOW_PATH>" --comfy-root "<COMFYUI_ROOT>"
```

## Runtime Guardrails

- Treat hardware- or backend-specific workarounds as conditional, not universal defaults.
- Verify a workaround against the installed ComfyUI/PyTorch/backend versions before applying it.
- Prefer conservative startup and memory settings when stability is the stated priority.
- If visual artifacts appear, identify the active attention/backend path before changing workflow structure.

## Local Editing Rules

- Edit only the workflow the user explicitly names.
- Back up the workflow before edits.
- Do not replace the user's primary model stack unless evidence shows corruption, incompatibility, or the user requests a change.
- Do not treat a frontend popup as proof of a workflow bug; inspect backend health first.
- Keep machine-specific facts in runtime context, not in this reusable skill package.
