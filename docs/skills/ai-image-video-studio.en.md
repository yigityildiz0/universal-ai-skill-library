# ai-image-video-studio

[English](ai-image-video-studio.en.md) · [Türkçe](ai-image-video-studio.tr.md) · [Library](../../README.md)

**Plan and troubleshoot image/video production, including local ComfyUI workflows.**

## Try it

> Diagnose this ComfyUI workflow and propose a reproducible fix.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

AI image and video production: ComfyUI workflow design and repair (FLUX, SDXL, SD3, Wan, Hunyuan, LTXV, LoRA, ControlNet, IPAdapter, PuLID, inpaint, upscale, img2vid; missing nodes or models, Failed to fetch, VRAM, identity drift), AI product photography, source-preserving image edits and rendered-video QA. Turkish triggers: ComfyUI workflow yap, iş akışını düzelt, node eksik, model bulunamadı, VRAM hatası, ürün fotoğrafı, görseli düzenle, arka planı değiştir, rötuş ve varyasyon, videoyu kontrol et. More triggers: güvenli onarım, workflow'u bozmadan modül ekle, ışık ve kompozisyon, çekim listesi, çözünürlük/ses/kare kontrolü.

</details>

## How it works

Identify the media task and available runtime; inspect workflow/model compatibility; plan or repair; check the actual output.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/ai-image-video-studio/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [comfyui-workflow](../../skills/common/ai-image-video-studio/modules/comfyui-workflow/MODULE.md) | Automatically design or substantially modify a ComfyUI workflow when the user wants a new image/video pipeline or capability for FLUX, SDXL, SD3, Wan, Hunyuan, LTXV, Mochi, Cosmos, |
| [comfyui-workflow-guardian](../../skills/common/ai-image-video-studio/modules/comfyui-workflow-guardian/MODULE.md) | Automatically audit, repair, refactor, and stabilize an existing ComfyUI workflow or Windows runtime when the user shares workflow JSON, an error/screenshot, or reports startup/que |
| [image-editing-workflow](../../skills/common/ai-image-video-studio/modules/image-editing-workflow/MODULE.md) | Apply a source-preserving workflow to plan, execute, and verify image edits with the active host's approved image-editing capability. Use when the user asks for this workflow or ne |
| [product-photography](../../skills/common/ai-image-video-studio/modules/product-photography/MODULE.md) | Plan, generate, edit, or review AI product photography for e-commerce, packaging, ads, catalogs, and product launches. Use for product photos, packshots, hero images, lifestyle sce |
| [video-delivery-qa](../../skills/common/ai-image-video-studio/modules/video-delivery-qa/MODULE.md) | Inspect, validate, and prepare video deliverables for export or handoff using available local tools such as ffprobe, frame sampling, waveform/audio inspection, captions, and visual |
