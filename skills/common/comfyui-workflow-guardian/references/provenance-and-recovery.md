# Provenance and Recovery

## Distinguish workflow forms

Confirm whether an input is executable API-format workflow JSON or an editor/layout JSON. Do not rewrite one form into the other without a verified conversion path. Preserve the original file and record the exact input format.

## Before a run

- Verify output node/path, required models, LoRAs, custom nodes, and input assets.
- Record workflow hash, model/checkpoint names, LoRA names, seed, key sampler settings, and source asset hashes when available.
- Treat missing items as blockers or explicit substitutions; do not silently use a near-name match.

## After a timeout or interrupted UI

Inspect ComfyUI history/queue/output folders before submitting another long run. Confirm whether a job completed, failed, was cancelled, or merely lost its browser response. Preserve completed output and diagnostics before retrying.

## Before delivery

Verify output existence, dimensions, format, node provenance, and that the result comes from the intended workflow/version. Report unknown provenance rather than guessing.
