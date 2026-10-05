#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


KNOWN_FILE_FIELDS = {
    "UNETLoader": ("models/unet", "models/diffusion_models"),
    "CLIPLoader": ("models/clip", "models/text_encoders"),
    "VAELoader": ("models/vae",),
    "LoraLoaderModelOnly": ("models/loras",),
    "PuLIDModelLoader": ("models",),
    "UpscaleModelLoader": ("models/upscale_models",),
}


def rect_from_node(node: dict[str, Any]) -> tuple[float, float, float, float] | None:
    pos = node.get("pos")
    size = node.get("size")
    if not isinstance(pos, list) or len(pos) < 2 or not isinstance(size, list) or len(size) < 2:
        return None
    x, y = float(pos[0]), float(pos[1])
    w, h = float(size[0]), float(size[1])
    return (x, y, x + w, y + h)


def rect_from_group(group: dict[str, Any]) -> tuple[float, float, float, float] | None:
    box = group.get("bounding")
    if isinstance(box, list) and len(box) >= 4:
        x, y, w, h = map(float, box[:4])
        return (x, y, x + w, y + h)
    pos = group.get("pos")
    size = group.get("size")
    if isinstance(pos, list) and len(pos) >= 2 and isinstance(size, list) and len(size) >= 2:
        x, y = float(pos[0]), float(pos[1])
        w, h = float(size[0]), float(size[1])
        return (x, y, x + w, y + h)
    return None


def overlaps(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def resolve_existing_file(filename: str, comfy_root: Path, roots: tuple[str, ...]) -> Path | None:
    for rel in roots:
        candidate = comfy_root / rel / filename
        if candidate.exists():
            return candidate
    for rel in roots:
        base = comfy_root / rel
        if base.exists():
            matches = list(base.rglob(filename))
            if matches:
                return matches[0]
    return None


def collect_file_refs(node: dict[str, Any], comfy_root: Path) -> list[dict[str, str]]:
    refs: list[dict[str, str]] = []
    node_type = node.get("type")
    widgets = node.get("widgets_values") or []

    if node_type in KNOWN_FILE_FIELDS and widgets:
        filename = widgets[0]
        if isinstance(filename, str) and filename and not resolve_existing_file(filename, comfy_root, KNOWN_FILE_FIELDS[node_type]):
            refs.append(
                {
                    "node_id": str(node["id"]),
                    "node_type": node_type,
                    "title": node.get("title") or node_type,
                    "file": filename,
                }
            )

    if node_type == "Power Lora Loader (rgthree)":
        for item in widgets:
            if isinstance(item, dict) and item.get("lora"):
                filename = item["lora"]
                if not resolve_existing_file(filename, comfy_root, ("models/loras",)):
                    refs.append(
                        {
                            "node_id": str(node["id"]),
                            "node_type": node_type,
                            "title": node.get("title") or node_type,
                            "file": filename,
                        }
                    )

    return refs


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ComfyUI workflow structure and file references.")
    parser.add_argument("workflow", help="Path to workflow JSON")
    parser.add_argument("--comfy-root", required=True, help="ComfyUI root path")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    workflow_path = Path(args.workflow)
    comfy_root = Path(args.comfy_root)
    data = json.loads(workflow_path.read_text(encoding="utf-8"))

    nodes = data.get("nodes", [])
    groups = data.get("groups", [])
    links = data.get("links", [])
    node_ids = {n["id"] for n in nodes}

    bad_links = [l for l in links if l[1] not in node_ids or l[3] not in node_ids]

    node_rects = [(n["id"], rect_from_node(n)) for n in nodes]
    node_overlaps: list[tuple[int, int]] = []
    for i, (id_a, rect_a) in enumerate(node_rects):
        if rect_a is None:
            continue
        for id_b, rect_b in node_rects[i + 1 :]:
            if rect_b is None:
                continue
            if overlaps(rect_a, rect_b):
                node_overlaps.append((id_a, id_b))

    group_rects = [(g.get("title") or g.get("name") or f"group-{idx}", rect_from_group(g)) for idx, g in enumerate(groups)]
    group_overlaps: list[tuple[str, str]] = []
    for i, (name_a, rect_a) in enumerate(group_rects):
        if rect_a is None:
            continue
        for name_b, rect_b in group_rects[i + 1 :]:
            if rect_b is None:
                continue
            if overlaps(rect_a, rect_b):
                group_overlaps.append((str(name_a), str(name_b)))

    missing_files: list[dict[str, str]] = []
    for node in nodes:
        missing_files.extend(collect_file_refs(node, comfy_root))

    summary = {
        "workflow": str(workflow_path),
        "nodes": len(nodes),
        "groups": len(groups),
        "links": len(links),
        "bad_links": len(bad_links),
        "node_overlaps": len(node_overlaps),
        "group_overlaps": len(group_overlaps),
        "missing_files": len(missing_files),
        "bad_link_details": bad_links,
        "node_overlap_details": node_overlaps[:50],
        "group_overlap_details": group_overlaps[:50],
        "missing_file_details": missing_files[:100],
    }

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    print(f"Workflow: {workflow_path}")
    print(f"Nodes: {summary['nodes']}")
    print(f"Groups: {summary['groups']}")
    print(f"Links: {summary['links']}")
    print(f"Bad links: {summary['bad_links']}")
    print(f"Node overlaps: {summary['node_overlaps']}")
    print(f"Group overlaps: {summary['group_overlaps']}")
    print(f"Missing files: {summary['missing_files']}")

    if bad_links:
        print("\nBad link details:")
        for item in bad_links[:20]:
            print(item)

    if node_overlaps:
        print("\nNode overlap details:")
        for item in node_overlaps[:20]:
            print(item)

    if group_overlaps:
        print("\nGroup overlap details:")
        for item in group_overlaps[:20]:
            print(item)

    if missing_files:
        print("\nMissing file details:")
        for item in missing_files[:40]:
            print(item)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
