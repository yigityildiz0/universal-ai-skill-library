# Runtime and Performance

Use this file for startup crashes, queue failures, `Failed to fetch`, access violations, and speed regressions.

## Triage Order

1. Confirm the backend is actually alive.
2. Read the backend traceback before editing the workflow.
3. Distinguish:
   - runtime crash
   - model-load crash
   - node execution error
   - frontend disconnect
4. Only then edit the workflow.

## Stable Windows Rules

- Treat `access violation` during model loading as a runtime or file-loading problem first, not a prompt or node-layout problem.
- When large safetensors files crash on Windows during load, prefer the safer non-mmap path.
- When a backend disconnect follows a sampler traceback, inspect logging wrappers and stderr handling before blaming the workflow.

## Performance Rules

Reduce cost in this order:

1. Disable optional identity modules not in use.
2. Disable optional detail/refiner modules not in use.
3. Reduce second-pass face-transfer cost.
4. Reduce sharpening or restoration passes.
5. Only then reduce core generation steps.

Avoid these anti-patterns:

- lowering core quality before trimming post-processing
- enabling multiple identity systems by default
- raising identity strength blindly when the transfer logic itself is wrong
- changing model families and LoRA stacks at the same time

## Timing Strategy

Use a baseline-per-stage mindset:

- Stage 1 generation time
- identity/post-pass time
- refiner/sharpen time

If a workflow becomes much slower, identify which stage grew, then optimize that stage only.

## Documentation to Prefer

- ComfyUI official troubleshooting docs
- model cards or official repos for the exact identity/refiner module
- local launcher flags and local runtime logs
