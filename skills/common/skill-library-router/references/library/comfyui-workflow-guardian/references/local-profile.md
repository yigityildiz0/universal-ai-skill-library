# Local Profile Template

Populate this profile only at runtime from the current user's verified environment. Do not publish a filled personal profile or assume these values across machines.

## Runtime fields

- Operating system and GPU/VRAM
- ComfyUI root and launch method
- Exact workflow path(s) placed in scope
- Protected master/workflow allowlist
- Backup/archive directory
- Installed model, encoder and VAE identifiers relevant to the workflow
- Listener/port and custom-node availability when needed

## Runtime guardrails

- Force safe Windows loading for large safetensors by disabling mmap.
- Prefer conservative Windows startup flags over aggressive memory/offload shortcuts when stability is the priority.
- If line artifacts appear on Blackwell-class GPUs, confirm whether the current install already forces a safe attention backend before changing the workflow.

## Local Editing Rules

- Edit only the workflow the user explicitly names.
- Back up the workflow before edits.
- Do not replace the user's primary model stack unless there is evidence that the current files are corrupt or incompatible.
- Do not treat a frontend popup as proof of a workflow bug; inspect backend health first.
