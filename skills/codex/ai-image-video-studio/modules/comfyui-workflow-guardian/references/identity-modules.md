# Identity Modules

Use this file when working on BFS, BFSC-style head-swap LoRAs, PuLID, LanPaint-style stage-2 transfer, or any identity-preservation branch.

## Identity Module Classes

Treat these as different tools with different jobs:

- **General LoRAs**: shape the base image before sampling
- **Model identity layers**: modify the final model directly, then feed the main sampler
- **Stage-2 face transfer**: take a generated base image and apply identity transfer afterward

Do not assume one class can replace another.

## Stable Architecture Rules

- Put general LoRAs before the base sampler.
- If an identity module works by modifying the final model, place it after the general LoRA chain.
- If an identity module works by face transfer or inpainting, use it as a second pass after the base image exists.
- Keep each identity system independently switchable.
- Test these modes separately:
  - all off
  - BFS-only
  - PuLID-only
  - BFS plus PuLID

Do not assume the combined mode is best.

## Head-Swap Stage Rules

For BFS-style stage-2 systems:

- Use the generated image as the base image.
- Use the user reference image as the face source only if the model card for that module explicitly expects that ordering.
- Preserve from the base image:
  - scene
  - body pose
  - accessories
  - hands
  - props
  - expression
  - mouth state
  - lighting
- Transfer from the reference image:
  - stable identity anchors only
  - face shape
  - facial proportions
  - hairline
  - eye and brow identity
  - nose
  - jawline
  - natural hair color and fiber type

Do not let the face source overwrite props, hands, or expression unless the module explicitly requires it.

## PuLID Rules

- Use PuLID as a model-layer identity option, not as a universal fix for every identity problem.
- Start with conservative strength.
- Raise strength only after verifying the branch logic is correct.
- If quality softens or colors drift, test a lower strength before changing the rest of the workflow.

## Decision Rule

If a stage-2 identity pass copies hats, hands, props, mouth shape, or expression from the reference image, the transfer is too broad. Narrow the transfer logic before raising strength.
