# Research 2026-05 — ComfyUI UI/Layout + Identity (RTX 5070 12GB, Flux 2 Klein 9B)

Authoritative findings backing the UI-policy skill. Verified against the user's install.

## Versions (verified on disk)
- ComfyUI backend `0.22.0`, frontend `comfyui-frontend-package==1.44.19`.
- Subgraph feature needs frontend ≥ **1.24.3** → available.
- Edit subgraph widgets from outer **parameters panel** (no entering): ComfyUI ≥ **v0.3.66** / modern frontend → available.
- → Subgraph nesting + external widget editing = FULLY supported here.

## Subgraph (official)
- Create: select nodes → toolbar subgraph icon → auto-infers I/O. Right-click slot to rename/delete exposed port.
- **Nested** subgraphs supported; navigation bar shows hierarchy level.
- Widgets of inner nodes can be surfaced/ordered/hidden from the outer parameters panel.
- Schema (confirmed from `_archive/_upstream/Head Swap V1...`): see `subgraph-pattern.md`. Key facts:
  - `definitions.subgraphs[]`: keys = id,name,version,revision,config,state,inputNode,outputNode,inputs,outputs,widgets,nodes,links,groups,extra.
  - `state` = {lastGroupId,lastNodeId,lastLinkId,lastRerouteId}.
  - `inputNode {id:-10,bounding:[x,y,w,h]}`, `outputNode {id:-20,bounding}`.
  - `inputs[]/outputs[]` = {id:uuid, name, type, linkIds:[], label, pos}.
  - inner links = **object** form {id,origin_id,origin_slot,target_id,target_slot,type}; IO uses origin_id:-10 / target_id:-20.
  - outer instance node: `type` = subgraph UUID; `properties.proxyWidgets` = [["innerNodeId(str)","widget_name"], ...].
  - `extra.workflowRendererVersion: "LG"`.
- Limitation: "convert subgraph back to nodes" partial; unpack exists.

## Nodes 2.0 (the "düğümler 2.0" setting)
- Vue-based node rendering replacing LiteGraph canvas. **BETA.**
- Toggle: top banner "Try it out" OR ComfyUI logo menu → "Nodes 2.0".
- **Breaks** some custom-node mappings (Comfy-Org/ComfyUI_frontend #10988) → rgthree / Flux2Klein-Enhancer / Power Lora at risk.
- POLICY: author/ship workflows in **classic LiteGraph** (stable, all custom nodes work). Document 2.0 as optional/experimental.

## Node geometry (LiteGraph)
- Node JSON: `pos:[x,y]` (top-left of body, BELOW its titlebar), `size:[w,h]`, `flags.collapsed`.
- Titlebar height ≈ 30px (above pos). Collapsed node renders ≈ 30px tall bar (stored size stays expanded).
- Group: `bounding:[x,y,w,h]`, title band ≈ 24-34px at top.
- Collapse: gray dot top-left / right-click → Collapse. Settings: Ctrl+,.
- Min sane node width ≈ 120-140px.
- LAYOUT RULES (enforced by validate_ui.py geometry block):
  - No node-node AABB overlap (rendered, collapse-aware).
  - No group-group overlap unless one fully contains another (nested).
  - Each node center inside exactly ONE group.
  - Node top must be below its group's title band (pos.y ≥ group.y + ~34).
  - Minimal-but-safe gaps (~16-40px), column-aligned, symmetric; not flat single-row.

## rgthree toggles (module on/off + perf)
- **Fast Groups Muter**: toggles group nodes ALWAYS↔NEVER (mute = skipped at execution).
- **Fast Groups Bypasser**: toggles BYPASS (node passes input→output, weights not run).
- **Mute/Bypass Repeater**: one node dispatches mode to many; feed into a Fast Muter/Bypasser for a single dashboard toggle.
- Disabled group = **zero compute cost** → ideal for optional modules (BFS pass, IFT lock, extra LoRAs, A/B recipe branches).
- Mute vs Bypass: mute fully skips (downstream may error if it needed the output); bypass passes-through (safer when a model-patch node should be neutralized).

## Identity methods (Flux 2 Klein 9B) — current verdicts
- **BFS head-swap** (MODIFIYELI): post-gen 2-pass; best in user tests (face+anatomy). Keep. Tune steps 4→6.
- **IFT V3** (Flux2Klein-Enhancer, installed): model-level identity LOCK, single-pass, CFG=1. The "hard/medium/soft lock" node. New #3 workflow on **distilled** klein (no grain).
- **PuLID** (installed): fragile (dark/green/dep-sensitive), ~12 failed user attempts → DON'T use.
- **True-v2 + turbo lora** (old TRUE TURBO): weak face + film-grain + perspective distortion in user tests → ABANDON for identity.

## Test feedback lessons (Ece/Zeynep/Irmak, seconds)
- ANA(112-116) ≈ SAF(95-101): identical results, only clip differs → merge to one (fp8mixed).
- MODIFIYELI(65-103): FAVORITE, strongest identity+anatomy.
- TRUE TURBO(74): fast but weak face + grain/film-grain (AI tell) + perspective (short-wide). → distilled+IFT avoids grain.

## Sources
- docs.comfy.org/interface/features/subgraph ; comfyui-wiki subgraph ; blog.comfy.org Nodes 2.0 ; Comfy-Org/ComfyUI_frontend#10988
- github.com/rgthree/rgthree-comfy (Fast Groups Muter/Bypasser)
- github.com/capitan01R/ComfyUI-Flux2Klein-Enhancer (IFT V3)
- _archive/_upstream/Head Swap V1 Flux 2 Klein 4b_9b (base_distill).json (subgraph schema + BFS upstream recipe)
