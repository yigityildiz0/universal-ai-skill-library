# Identity Mechanisms — Example Face-Transfer Workflow (late 2025/early 2026 research)

## Ranked mechanisms (illustrative 12 GB GPU/model setup; benchmark locally)

| Rank | Mechanism | Time/img | Identity Strength | Notes |
|---|---|---|---|---|
| 1 | ReferenceLatentPlus (shootthesound) + auto face crop | 25-35s | Strong | Per-image sigma gating, MediaPipe face mask. NOT installed. |
| 2 | Identity Feature Transfer V3 (Flux2Klein-Enhancer) | 35-45s | Cleanest at CFG=1 | INSTALLED. preset=MIDUM_LOCK or HARD_LOCK. |
| 3 | **PuLID-Flux2 Klein V2** (iFayens) | 40-55s | Strongest single mechanism | INSTALLED. `pulid_flux2_klein_v2.safetensors` present. |
| 4 | BFS Head V1 LoRA (Alissonerdx civitai 2027766) | 30s | Strong head identity | INSTALLED. **Requires 2 image inputs (body+face crop) + `head_swap:` prompt prefix**. |
| 5 | FaceDetailer (Impact Pack) + face_yolov8m | +15-25s post-pass | Refines only | Best as second-pass detail, NOT primary identity. |
| 6 | Reactor / InstantID Flux | varies | Low quality on Klein | Skip — inswapper-128 quality, degrades skin. |

## PuLID Flux2 Klein V2 — Critical Settings

### Strength
- **0.85-1.05** (research-confirmed)
- **NEVER 1.4** — README "recommended" value burns at 4-step distilled
- Strength widget range: 0.0-2.0, default 1.0
- For 4-step distilled (steps=8 in master test), use 0.95 as sweet spot

### NO sigma gating
- PuLID-Flux2 node exposes ONLY `strength`, `face_index`, `debug_mode`
- NO sigma_start/sigma_end inputs (verified from source `pulid_flux2.py`)
- Patch applies uniformly per-step

### NO ReferenceLatent collision
- PuLID injects into double_blocks (image stream)
- ReferenceLatent stored in `reference_latents` metadata
- Different paths until single_blocks merge → safe to combine

### Placement
- Apply PuLID BEFORE Power LoRA in MODEL chain:
  ```
  UNETLoader → ApplyPuLIDFlux2 → Power LoRA → CFGGuider
  ```
- This lets LoRA shape/dampen identity if needed

### File required
- `pulid_flux2_klein_v2.safetensors` (Klein V2, recommended over V1)
- Place in `<COMFYUI_ROOT>/models/pulid/`
- Place the required InsightFace model under `<COMFYUI_ROOT>/models/insightface/models/`

## BFS Head V1 LoRA — Usage Requirements

### File
`bfs_head_v1_flux-klein_9b_step3500_rank128.safetensors` (or step3750_rank64)

### Strength
- 0.85-1.0 (rank128)
- 0.6-0.85 (rank64)
- Above 1.1 → head-mismatch artifacts

### CRITICAL: Prompt Prefix
LoRA trained on this exact prompt structure:
```
head_swap: start with Picture 1 as the base image... replace head from Picture 2...
```
Without `head_swap:` prefix → LoRA does NOTHING useful. Must update CLIPTextEncode positive prompt to include this template.

### CRITICAL: 2 Image Inputs Required
BFS is an image-edit LoRA. Needs:
- image_1: body/scene reference
- image_2: face crop reference
Both as ReferenceLatent or via MultiReferenceLatent (latent_1 + latent_2).

For single-ref user upload, derive face crop via Ultralytics + Crop chain (see "Auto Face Crop" below).

### Compatibility
- CFG=1.0 distilled: ✓
- Pair with PuLID: ✓ (different mechanism, complementary)
- Pair with consistency LoRA: ✓

### Source
- HuggingFace: `Alissonerdx/BFS-Best-Face-Swap`
- Civitai: model 2027766

## Identity Feature Transfer V3 — Klein Enhancer

### Node
`IdentityFeatureTransferV3` (class), display "IFT V3"

### Presets
- `MIDUM_LOCK` — balanced (recommended default)
- `HARD_LOCK` — strong lock, risk of over-fit
- `SOFT_LOCK` — gentle
- `custom` — manual block schedule

### Placement
After Power LoRA, before CFGGuider:
```
Power LoRA → IdentityFeatureTransferV3 → CFGGuider
```

### Inputs
Takes MODEL only (reference comes via positive conditioning chain)

### CFG=1 safe
Designed for distilled flow matching. No CFG bump needed.

### VERIFIED 2026-05-30 (from example_workflow/iden_transfer_v3.json, ver 3.2.0)
- JSON node `type` = **`IdentityFeatureTransferV3`** (NODE_CLASS_MAPPINGS key; display "FLUX.2 Klein Identity Feature Transfer V3").
- inputs: `model` (MODEL, required) + `subject_mask` (MASK, optional — leave unconnected for whole-image).
- outputs: `MODEL`.
- `widgets_values` for MIDUM_LOCK default (copy verbatim):
  `["MIDUM_LOCK", 0, "0-3:mid=0.25; 4:mid=0.35; 5:mid=0.65; 6-7:mid=0.45", "0:mid=0.35; 1:mid=0.25; 2-10:mid=0.30; 11-19:mid=0.25; 20:mid=0.08; 21:mid=0.10; 22:mid=0.15; 23:mid=0.20", 0.02, 0.02, 0.035, 2, 0.5, 0.25, false]`
  - widget[0]=preset (MIDUM_LOCK / HARD_LOCK / SOFT_LOCK / custom). Schedule strings + floats apply when custom.
- properties: `{"cnr_id":"comfyui-flux2klein-enhancer","ver":"3.2.0","Node name for S&R":"IdentityFeatureTransferV3"}`.
- Reference is read from the POSITIVE conditioning's ReferenceLatent (must be present). subject_mask optional.
- Verdict: this IS the user's "hard/medium/soft lock" node. "soft kötü" = SOFT_LOCK drifted / wiring. Start MIDUM_LOCK → HARD_LOCK if identity drifts.

## MultiReferenceLatent (Flux2Klein-Enhancer)

### Node
`Flux2KleinMultiReferenceLatent`

### Inputs
- conditioning (required)
- latent_1 (required)
- latent_2..latent_8 (optional)

### Behavior
Stacks all provided latents into `reference_latents` metadata. Method "index".

### Replaces
Multiple ReferenceLatent chain. Cleaner: one node, up to 8 refs.

## Auto Face Crop Chain (single user ref → body + face latents)

Required nodes (all installed):
1. `LoadImage` → user ref
2. `ImageScaleToTotalPixels` 1MP → body latent path
3. `VAEEncode` (body) → latent_1
4. `UltralyticsDetectorProvider` (`bbox/face_yolov8m.pt`) → BBOX_DETECTOR
5. `BboxDetectorSEGS` (detector, image, threshold=0.5, dilation=10, crop_factor=1.5) → SEGS
6. (option A) `SegsToImageList` → IMAGE[] → take first → face crop
   (option B) `Impact Edit SEGS` → cropped images
7. `ImageScaleToTotalPixels` 1MP → face crop scaled
8. `VAEEncode` (face crop) → latent_2
9. `Flux2KleinMultiReferenceLatent` (conditioning, latent_1=body, latent_2=face)

## Recommended v4 Architecture (research-driven)

```
LoadImage (user ref, single)
 ├─ branch A: ImageScale → VAEEncode → latent_1 (body)
 └─ branch B: UltralyticsDetect → BboxSEGS → SegsToImage → ImageScale → VAEEncode → latent_2 (face)

UNETLoader
 → ApplyPuLIDFlux2 (model, pulid_klein_v2, eva_clip, insightface, image=LoadImage, strength=0.95)
 → Power LoRA (anatomy 3.0, snofs 1.0, realism 0.8, consistency 0.5, BFS OFF default)
 → IdentityFeatureTransferV3 (preset=MIDUM_LOCK)
 → CFGGuider.model

CLIPTextEncode (positive) → Flux2KleinMultiReferenceLatent (latent_1, latent_2) → CFGGuider.positive
CLIPTextEncode (negative) → CFGGuider.negative

CFGGuider → SamplerCustomAdvanced (euler, simple, 8 steps, CFG 1.0) → VAEDecode → output
```

Optional second pass (FaceDetailer):
```
VAEDecode IMAGE → FaceDetailer (face_yolov8m, denoise=0.40, guide_size=512, bbox_crop_factor=1.5)
 → Final image
```

## Illustrative time budget (hardware/model dependent)

| Configuration | Time |
|---|---|
| Master (no identity boost) | ~90s |
| Master + PuLID Klein V2 only | ~100-110s |
| Master + PuLID + IFT V3 | ~115-130s |
| Master + PuLID + IFT V3 + auto face crop multi-ref | ~120-140s |
| Master + PuLID + IFT V3 + multi-ref + FaceDetailer | ~140-160s |

## Sources

- [GitHub iFayens/ComfyUI-PuLID-Flux2](https://github.com/iFayens/ComfyUI-PuLID-Flux2)
- [GitHub iFayens issue #11 — strength burns at 1.4](https://github.com/iFayens/ComfyUI-PuLID-Flux2/issues/11)
- [GitHub capitan01R/ComfyUI-Flux2Klein-Enhancer](https://github.com/capitan01R/ComfyUI-Flux2Klein-Enhancer)
- [GitHub shootthesound/comfyui-ReferenceLatentPlus](https://github.com/shootthesound/comfyui-ReferenceLatentPlus)
- [Civitai BFS Head Flux Klein 9B](https://civitai.com/models/2027766)
- [HuggingFace Alissonerdx/BFS-Best-Face-Swap README](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap)
- [HuggingFace Fayens/Pulid-Flux2](https://huggingface.co/Fayens/Pulid-Flux2)
