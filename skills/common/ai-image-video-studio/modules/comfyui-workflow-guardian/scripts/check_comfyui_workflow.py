#!/usr/bin/env python3
"""Offline UI/API structure and bounded model-reference checks; never a runtime test.

Exit 0: requested static checks passed; 1: invalid structure/missing model;
2: unreadable input or incomplete model-reference coverage. Layout is advisory.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path, PurePosixPath
from typing import Any


# API input name, UI widget index, standard model directories. Custom schemas
# are deliberately reported as unhandled instead of guessed from arbitrary text.
UNET = ("models/unet", "models/diffusion_models")
CLIP = ("models/clip", "models/text_encoders")
KNOWN_FILE_FIELDS = {
    "UNETLoader": (("unet_name", 0, UNET),),
    "CLIPLoader": (("clip_name", 0, CLIP),),
    "DualCLIPLoader": (("clip_name1", 0, CLIP), ("clip_name2", 1, CLIP)),
    "TripleCLIPLoader": tuple((f"clip_name{i + 1}", i, CLIP) for i in range(3)),
    "VAELoader": (("vae_name", 0, ("models/vae",)),),
    "CheckpointLoaderSimple": (("ckpt_name", 0, ("models/checkpoints",)),),
    "CheckpointLoader": (("ckpt_name", 1, ("models/checkpoints",)),
                         ("config_name", 0, ("models/configs",))),
    "LoraLoader": (("lora_name", 0, ("models/loras",)),),
    "LoraLoaderModelOnly": (("lora_name", 0, ("models/loras",)),),
    "ControlNetLoader": (("control_net_name", 0, ("models/controlnet",)),),
    "DiffControlNetLoader": (("control_net_name", 0, ("models/controlnet",)),),
    "CLIPVisionLoader": (("clip_name", 0, ("models/clip_vision",)),),
    "PuLIDModelLoader": (("pulid_file", 0, ("models/pulid", "models")),),
    "UpscaleModelLoader": (("model_name", 0, ("models/upscale_models",)),),
}
MODEL_SUFFIXES = {".safetensors", ".ckpt", ".pt", ".pth", ".bin", ".gguf", ".onnx"}


def slot(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def identifier(value: Any) -> bool:
    return (isinstance(value, (str, int)) and not isinstance(value, bool)
            and bool(str(value).strip()))


def rectangle(item: dict) -> tuple | None:
    box = item.get("bounding")
    if box is None:
        pos, size = item.get("pos"), item.get("size")
        if isinstance(pos, dict):
            pos = [pos.get("0"), pos.get("1")]
        if isinstance(size, dict):
            size = [size.get("0"), size.get("1")]
        if not isinstance(pos, list) or not isinstance(size, list):
            return None
        box = pos[:2] + size[:2]
    try:
        x, y, w, h = map(float, box[:4])
        if all(math.isfinite(v) for v in (x, y, w, h)) and w >= 0 and h >= 0:
            return x, y, x + w, y + h
    except (TypeError, ValueError):
        pass
    return None


def overlap_pairs(items: list[dict]) -> list:
    pairs = []
    rects = [(n.get("id", n.get("title", i)), rectangle(n)) for i, n in enumerate(items)]
    for i, (aid, a) in enumerate(rects):
        for bid, b in rects[i + 1:]:
            if a and b and not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1]):
                pairs.append([aid, bid])
    return pairs


def resolve_existing_file(filename: str, comfy_root: Path, roots: tuple) -> dict:
    relative = PurePosixPath(filename.replace("\\", "/"))
    if relative.is_absolute() or ".." in relative.parts or ":" in filename:
        return {"status": "invalid_path", "matches": []}
    exact, fallback = set(), set()
    for rel in roots:
        base = (comfy_root / rel).resolve()
        candidate = (base / relative).resolve()
        if not candidate.is_relative_to(base):
            continue
        if candidate.is_file():
            exact.add(str(candidate))
        if base.is_dir():
            for match in base.rglob(relative.name):
                resolved = match.resolve()
                if match.is_file() and resolved.is_relative_to(base):
                    fallback.add(str(resolved))
    matches = sorted(exact or fallback)
    status = ("ambiguous" if len(matches) > 1 else "resolved" if exact else
              "basename_only" if matches else "missing")
    return {"status": status, "matches": matches}


def validate(data: Any, comfy_root: Path | None = None, structure_only: bool = False) -> dict:
    errors, warnings, unhandled, references, bad_links = [], [], [], [], []
    fmt, nodes, groups, links = "unknown", [], [], []
    if not isinstance(data, dict):
        errors.append("Workflow must be a JSON object.")
    elif "nodes" in data:
        fmt = "ui"
        if not isinstance(data["nodes"], list):
            errors.append("UI nodes must be a list.")
        else:
            nodes = data["nodes"]
        links, groups = data.get("links", []), data.get("groups", [])
        if not isinstance(links, list):
            errors.append("UI links must be a list.")
            links = []
        if not isinstance(groups, list) or any(not isinstance(g, dict) for g in groups):
            warnings.append("Invalid group metadata; layout check skipped.")
            groups = []
    else:
        prompt = data.get("prompt", data)
        if isinstance(prompt, dict) and prompt and any(isinstance(n, dict) and "class_type" in n for n in prompt.values()):
            fmt = "api"
            nodes = [dict(n, id=k) if isinstance(n, dict) else n for k, n in prompt.items()]
        else:
            errors.append("Unrecognized or empty workflow: expected UI nodes or API class_type/inputs nodes.")
    if not nodes:
        errors.append("Workflow contains no nodes.")
    index = {}
    for n in nodes:
        if not isinstance(n, dict) or not identifier(n.get("id")):
            errors.append("Node must be an object with a nonempty string/integer ID.")
            continue
        key = str(n["id"])
        if key in index:
            errors.append(f"Duplicate node ID: {key}")
        index[key] = n
        kind = n.get("class_type" if fmt == "api" else "type")
        if not isinstance(kind, str) or not kind.strip():
            errors.append(f"Node {key}: missing node type.")
        if fmt == "api":
            inputs = n.get("inputs")
            if not isinstance(inputs, dict):
                errors.append(f"Node {key}: API inputs must be an object.")
                continue
            for name, value in inputs.items():
                if isinstance(value, list):
                    if len(value) == 2 and identifier(value[0]) and slot(value[1]):
                        links.append([f"{key}:{name}", value[0], value[1], key, name, None])
                    else:
                        errors.append(f"Node {key}.{name}: malformed API connection; list-valued custom inputs require schema-aware validation.")
    normalized, link_ids = [], set()
    for raw in links:
        link = ([raw.get(k) for k in ("id", "origin_id", "origin_slot", "target_id", "target_slot", "type")]
                if isinstance(raw, dict) else raw)
        reason = None
        if not isinstance(link, list) or len(link) < 6 or not identifier(link[0]):
            reason = "Malformed link record"
        elif str(link[0]) in link_ids:
            reason = "Duplicate link ID"
        else:
            link_ids.add(str(link[0]))
            if not identifier(link[1]) or not identifier(link[3]) or str(link[1]) not in index or str(link[3]) not in index:
                reason = "Missing link endpoint"
            elif not slot(link[2]) or (fmt == "ui" and not slot(link[4])):
                reason = "Invalid slot index"
            elif fmt == "ui":
                for end, field, at in ((1, "outputs", 2), (3, "inputs", 4)):
                    ports = index[str(link[end])].get(field)
                    if ports is not None and (not isinstance(ports, list) or link[at] >= len(ports)):
                        reason = "Slot outside declared ports"
        if reason:
            bad_links.append({"link": raw, "error": reason})
        else:
            normalized.append(link)
    errors.extend(item["error"] + ": " + str(item["link"]) for item in bad_links)
    if fmt == "ui":
        by_link = {str(l[0]): l for l in normalized}
        for key, n in index.items():
            for field in ("inputs", "outputs"):
                ports = n.get(field, [])
                if not isinstance(ports, list):
                    errors.append(f"Node {key}: {field} must be a list.")
                    continue
                for position, port in enumerate(ports):
                    if not isinstance(port, dict):
                        errors.append(f"Node {key}: malformed {field} port.")
                        continue
                    ids = [port.get("link")] if field == "inputs" else port.get("links", [])
                    if ids is None:
                        ids = []
                    if not isinstance(ids, list):
                        errors.append(f"Node {key}: malformed output link list.")
                        continue
                    for lid in ids:
                        if lid is None:
                            continue
                        l = by_link.get(str(lid))
                        endpoint, at = (3, 4) if field == "inputs" else (1, 2)
                        if not l or str(l[endpoint]) != key or l[at] != position:
                            errors.append(f"Node {key}: dangling/inconsistent port link {lid}.")
        for l in normalized:
            target = index[str(l[3])].get("inputs")
            source = index[str(l[1])].get("outputs")
            if isinstance(target, list) and isinstance(target[l[4]], dict) and str(target[l[4]].get("link")) != str(l[0]):
                errors.append(f"Link {l[0]}: target port does not reference link.")
            if isinstance(source, list) and isinstance(source[l[2]], dict) and str(l[0]) not in [str(x) for x in source[l[2]].get("links") or []]:
                errors.append(f"Link {l[0]}: source port does not reference link.")
    for key, n in index.items():
        kind = n.get("class_type" if fmt == "api" else "type", "")
        if not isinstance(kind, str):
            continue
        widgets = n.get("widgets_values") or []
        values = n.get("inputs", {}) if fmt == "api" else widgets
        specs = KNOWN_FILE_FIELDS.get(kind)
        candidates = []
        if specs:
            for name, pos, roots in specs:
                value = (values.get(name) if isinstance(values, dict) else
                         values[pos] if isinstance(values, list) and len(values) > pos else None)
                candidates.append((name, value, roots))
        elif kind == "Power Lora Loader (rgthree)" and fmt == "ui" and isinstance(widgets, list):
            candidates = [("lora", w["lora"], ("models/loras",)) for w in widgets
                          if isinstance(w, dict) and w.get("lora") and w.get("on", True)]
        elif "loader" in kind.lower() or "load" in kind.lower() or any(ext in json.dumps(values).lower() for ext in MODEL_SUFFIXES):
            unhandled.append({"node_id": key, "node_type": kind, "reason": "Custom/unmapped file-input schema"})
        for name, value, roots in candidates:
            ref = {"node_id": key, "node_type": kind, "input": name, "file": value}
            if not isinstance(value, str) or not value:
                ref["status"] = "unhandled"
                unhandled.append({**ref, "reason": "Dynamic or absent filename"})
            elif comfy_root is None or structure_only:
                ref["status"] = "not_checked"
            else:
                ref.update(resolve_existing_file(value, comfy_root, roots))
            references.append(ref)
    node_pairs = overlap_pairs(list(index.values())) if fmt == "ui" else []
    group_pairs = overlap_pairs(groups) if fmt == "ui" else []
    if node_pairs or group_pairs:
        warnings.append("Overlaps are layout warnings; nested groups can be intentional.")
    missing = [r for r in references if r["status"] in ("missing", "invalid_path")]
    uncertain = [r for r in references if r["status"] in ("ambiguous", "basename_only", "unhandled")]
    model_status = ("not_checked" if structure_only or comfy_root is None else
                    "failed" if missing else "incomplete" if unhandled or uncertain else "passed_known_references")
    code = 1 if errors or (missing and not structure_only) else 2 if not structure_only and model_status in ("not_checked", "incomplete") else 0
    return {"format": fmt, "nodes": len(nodes), "groups": len(groups), "links": len(links),
            "structural_status": "failed" if errors else "passed", "errors": errors,
            "bad_links": len(bad_links), "bad_link_details": bad_links,
            "node_overlaps": len(node_pairs), "node_overlap_details": node_pairs[:50],
            "group_overlaps": len(group_pairs), "group_overlap_details": group_pairs[:50],
            "warnings": warnings, "missing_files": len(missing), "missing_file_details": missing,
            "model_reference_status": model_status, "file_references": references,
            "unhandled_model_references": unhandled, "runtime_validated": False,
            "scope": "structure_only" if structure_only else "structure_and_known_model_files",
            "limitations": "No custom-node schemas, output type compatibility, extra_model_paths.yaml or inference execution validated.",
            "exit_code": code}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow", type=Path)
    parser.add_argument("--comfy-root", type=Path)
    parser.add_argument("--structure-only", action="store_true", help="Explicitly skip local model existence checks")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.workflow.read_text(encoding="utf-8-sig"))
        if args.comfy_root is not None and not args.comfy_root.is_dir():
            raise ValueError("--comfy-root must be an existing directory")
        result = validate(data, args.comfy_root, args.structure_only)
    except (OSError, ValueError, RecursionError) as exc:
        result = {"errors": [str(exc)], "structural_status": "not_checked", "runtime_validated": False, "exit_code": 2}
    result["workflow"] = str(args.workflow)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
    return result["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
