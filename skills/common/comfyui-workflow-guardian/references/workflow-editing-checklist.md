# Workflow Editing Checklist

Use this file before and after modifying any ComfyUI workflow JSON.

## Before Editing

- Confirm the exact workflow path.
- Create a timestamped backup next to the target file.
- Run the workflow checker script.
- Record:
  - node count
  - link count
  - missing file count
  - node overlap count
  - group overlap count

## Editing Rules

- Prefer small, local edits over large rewrites.
- Keep the user's existing working sections intact unless the request targets them.
- If you add quick controls, keep the original nodes in place and wire the quick controls to them.
- Keep notes short and functional.
- Do not leave oversized empty note boxes.
- Do not leave overlapping groups or nodes.
- Use clear Turkish titles if they do not break node behavior.

## Model and LoRA Rules

- Verify every referenced model and LoRA file exists on disk.
- Do not leave stale model names in notes after changing node values.
- Do not keep conflicting LoRAs enabled by default.
- Keep broadly useful, low-risk LoRAs in the main chain.
- Keep scenario-specific or aggressive LoRAs disabled by default.

## After Editing

- Run the workflow checker again.
- Confirm there are no invalid links.
- Confirm there are no node overlaps.
- Confirm there are no group overlaps.
- Confirm quick controls and original controls still point to the same live values.
- Summarize the changed nodes and default values.
