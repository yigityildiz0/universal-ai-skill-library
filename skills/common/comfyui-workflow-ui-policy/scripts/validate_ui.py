"""ComfyUI Workflow UI Policy Validator.
Checks workflow JSON against the UI policy rules.

Usage:
    python validate_ui.py <workflow.json>
"""
import sys, io, json, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Knob node types (never collapse)
KNOB_TYPES = {
    'LoadImage',
    'PrimitiveStringMultiline',
    'PrimitiveBoolean',
    'PrimitiveInt',
    'PrimitiveFloat',
    'Power Lora Loader (rgthree)',
    'Power Primitive (rgthree)',
    'PreviewImage',
    'SaveImage',
    'Image Comparer (rgthree)',
    'MarkdownNote',
    'Note',
    'Fast Groups Bypasser (rgthree)',
}

# Tech node types (must be collapsed)
TECH_TYPES = {
    'UNETLoader',
    'CLIPLoader',
    'VAELoader',
    'CLIPTextEncode',
    'ReferenceLatent',
    'Flux2KleinMultiReferenceLatent',
    'VAEEncode',
    'VAEDecode',
    'ImageScaleToTotalPixels',
    'GetImageSize',
    'RandomNoise',
    'KSamplerSelect',
    'Flux2Scheduler',
    'EmptyFlux2LatentImage',
    'CFGGuider',
    'SamplerCustomAdvanced',
    'StringConcatenate',
    'ComfySwitchNode',
    'ApplyPuLIDFlux2',
    'PuLIDInsightFaceLoader',
    'PuLIDEVACLIPLoader',
    'PuLIDModelLoader',
    'IdentityFeatureTransferV3',
    'IdentityFeatureTransferV3Advanced',
    'UltralyticsDetectorProvider',
    'BboxDetectorSEGS',
    'SAMLoader',
    'FaceDetailer',
}

# Tech nodes that hold a user-adjustable control -> allowed to stay EXPANDED (not collapsed)
ALLOW_EXPANDED = {'KSamplerSelect', 'IdentityFeatureTransferV3'}

# Required colors per group title pattern
COLOR_RULES = {
    '1.': ['#6d5aa3'],  # User Inputs - purple
    '2.': ['#2f6f89'],  # Model loading - blue
    '3.': ['#2f6f89'],  # Reference processing - blue
    '4.': ['#4f7a45'],  # Conditioning - green
    '5.': ['#6a54a3'],  # Sampling - dark purple
    '6.': ['#3d7e86'],  # Output - cyan
    'KONTROL': ['#2a2a5a'],  # Control panel
}


def validate(path):
    d = json.load(open(path, encoding='utf-8'))
    issues = []
    warnings = []

    nodes = d.get('nodes', [])
    links = d.get('links', [])
    groups = d.get('groups', [])

    # Link integrity
    node_ids = {n['id'] for n in nodes}
    link_ids = {l[0] for l in links}
    for n in nodes:
        for i in n.get('inputs', []):
            if i.get('link') is not None and i['link'] not in link_ids:
                issues.append(f"N{n['id']} input '{i.get('name')}' → missing link {i['link']}")
        for o in n.get('outputs', []):
            for l in (o.get('links') or []):
                if l not in link_ids:
                    issues.append(f"N{n['id']} output → missing link {l}")
    for l in links:
        if l[1] not in node_ids or l[3] not in node_ids:
            issues.append(f"L{l[0]} endpoint missing {l[1]}→{l[3]}")

    # last_node_id / last_link_id consistency
    if nodes:
        max_node = max(n['id'] for n in nodes)
        if d.get('last_node_id', 0) < max_node:
            warnings.append(f"last_node_id ({d.get('last_node_id')}) < actual max ({max_node})")
    if links:
        max_link = max(l[0] for l in links)
        if d.get('last_link_id', 0) < max_link:
            warnings.append(f"last_link_id ({d.get('last_link_id')}) < actual max ({max_link})")

    # Collapse policy
    collapsed_violations = []
    uncollapsed_violations = []
    for n in nodes:
        t = n.get('type', '')
        collapsed = n.get('flags', {}).get('collapsed', False)
        if t in KNOB_TYPES and collapsed:
            collapsed_violations.append(f"N{n['id']} ({t}) — knob should NOT be collapsed")
        if t in TECH_TYPES and t not in ALLOW_EXPANDED and not collapsed:
            uncollapsed_violations.append(f"N{n['id']} ({t}) — tech should be collapsed")

    # Group title format + color
    for g in groups:
        title = g.get('title', '')
        color = g.get('color', '')
        for pattern, valid_colors in COLOR_RULES.items():
            if pattern in title:
                if color not in valid_colors:
                    warnings.append(f"Group '{title}' has color {color}, expected {valid_colors}")
                break

    # Power LoRA BFS check
    for n in nodes:
        if n.get('type') == 'Power Lora Loader (rgthree)':
            wv = n.get('widgets_values', [])
            bfs_on = False
            for w in wv:
                if isinstance(w, dict) and 'bfs' in str(w.get('lora', '')).lower():
                    if w.get('on'):
                        bfs_on = True
                        break
            if bfs_on:
                # Check MarkdownNote for head_swap: mention
                has_warning = False
                for nn in nodes:
                    if nn.get('type') == 'MarkdownNote':
                        wv2 = nn.get('widgets_values', [])
                        if any('head_swap' in str(w).lower() for w in wv2):
                            has_warning = True
                            break
                if not has_warning:
                    issues.append("BFS Head LoRA is ON but no MarkdownNote mentions 'head_swap:' prompt prefix requirement")

    # PuLID strength check
    for n in nodes:
        if n.get('type') == 'ApplyPuLIDFlux2':
            wv = n.get('widgets_values', [])
            if wv and isinstance(wv[0], (int, float)):
                strength = wv[0]
                if strength > 1.05:
                    issues.append(f"ApplyPuLIDFlux2 N{n['id']} strength={strength} — burns at 4-step distilled. Use 0.85-1.05.")
                elif strength < 0.6:
                    warnings.append(f"ApplyPuLIDFlux2 N{n['id']} strength={strength} — too low, identity weak")

    # ---------- GEOMETRY CHECKS (overlap / spacing / title-bar / size) ----------
    # Geometry constants (LiteGraph, frontend 1.44)
    TITLE_PAD = 34      # group title band height; nodes must start below this
    GROUP_TITLE_H = 30  # node titlebar height (expanded)
    COLLAPSED_H = 30    # rendered height of a collapsed node
    MIN_NODE_W = 120    # minimum sane node width
    MIN_GAP = 8         # nodes closer than this (but not overlapping) = too cramped
    EXCESS_GAP = 220    # neighbour gap larger than this inside a group = wasteful

    def node_box(n):
        """Effective rendered AABB [x,y,w,h]. Collapsed nodes render as a short bar."""
        pos = n.get('pos') or [0, 0]
        size = n.get('size') or [200, 100]
        x, y = float(pos[0]), float(pos[1])
        w = float(size[0]) if size and size[0] else 200.0
        collapsed = n.get('flags', {}).get('collapsed', False)
        h = COLLAPSED_H if collapsed else (float(size[1]) if len(size) > 1 and size[1] else 100.0)
        return [x, y - GROUP_TITLE_H, w, h + GROUP_TITLE_H]  # include node titlebar above pos

    def group_box(g):
        b = g.get('bounding')
        if b and len(b) == 4:
            return [float(b[0]), float(b[1]), float(b[2]), float(b[3])]
        pos = g.get('pos') or [0, 0]; size = g.get('size') or [400, 200]
        return [float(pos[0]), float(pos[1]), float(size[0]), float(size[1])]

    def aabb_overlap(a, b):
        ax, ay, aw, ah = a; bx, by, bw, bh = b
        ix = max(0.0, min(ax + aw, bx + bw) - max(ax, bx))
        iy = max(0.0, min(ay + ah, by + bh) - max(ay, by))
        return ix * iy

    def center(box):
        return (box[0] + box[2] / 2, box[1] + box[3] / 2)

    def in_group(nb, gb):
        cx, cy = center(nb)
        return gb[0] <= cx <= gb[0] + gb[2] and gb[1] <= cy <= gb[1] + gb[3]

    geo = []  # geometry findings (warnings-level unless overlap)
    real_nodes = [n for n in nodes if n.get('pos') and n.get('type') not in ('Note',)]

    # 1) node-node overlap (rendered)
    boxes = {n['id']: node_box(n) for n in real_nodes}
    ids_sorted = [n['id'] for n in real_nodes]
    overlaps = 0
    for i in range(len(ids_sorted)):
        for j in range(i + 1, len(ids_sorted)):
            a, b = boxes[ids_sorted[i]], boxes[ids_sorted[j]]
            ov = aabb_overlap(a, b)
            if ov > 200:  # meaningful overlap (px^2)
                overlaps += 1
                if overlaps <= 8:
                    geo.append(f"NODE OVERLAP: N{ids_sorted[i]} ∩ N{ids_sorted[j]} (~{int(ov)}px2)")
    if overlaps:
        issues.append(f"{overlaps} node-node overlap(s) — nodes must not visually overlap")

    # 2) group-group overlap (excluding nested: one fully inside another is OK)
    gboxes = [(g.get('title', '?'), group_box(g)) for g in groups]
    def contains(outer, inner):
        return (outer[0] <= inner[0] and outer[1] <= inner[1] and
                outer[0] + outer[2] >= inner[0] + inner[2] and
                outer[1] + outer[3] >= inner[1] + inner[3])
    for i in range(len(gboxes)):
        for j in range(i + 1, len(gboxes)):
            (t1, g1), (t2, g2) = gboxes[i], gboxes[j]
            if aabb_overlap(g1, g2) > 400 and not contains(g1, g2) and not contains(g2, g1):
                warnings.append(f"GROUP OVERLAP (not nested): '{t1}' ∩ '{t2}'")

    # 3) node under group title band  +  4) multi-group membership
    for n in real_nodes:
        nb = node_box(n)
        member_of = [(t, gb) for (t, gb) in gboxes if in_group(nb, gb)]
        if len(member_of) > 1:
            warnings.append(f"N{n['id']} ({n.get('type')}) center inside {len(member_of)} groups: {[t for t,_ in member_of]}")
        for (t, gb) in member_of:
            node_top = float((n.get('pos') or [0, 0])[1]) - GROUP_TITLE_H
            if node_top < gb[1] + TITLE_PAD:
                geo.append(f"N{n['id']} ({n.get('type')}) under group title band of '{t}' (top {int(node_top)} < {int(gb[1]+TITLE_PAD)})")

    # 5) min node width
    for n in real_nodes:
        size = n.get('size') or [200, 100]
        if size and float(size[0]) < MIN_NODE_W and not n.get('flags', {}).get('collapsed'):
            geo.append(f"N{n['id']} ({n.get('type')}) width {size[0]} < min {MIN_NODE_W}")

    if geo:
        warnings.extend(geo[:15])

    # Master file protection
    if 'ANA WORKFLOW.json' in os.path.basename(path) and 'v' not in os.path.basename(path).lower():
        warnings.append("EDITING MASTER FILE — must NEVER be modified per policy. Edit a versioned copy instead.")

    # Report
    print(f"\n{'='*60}")
    print(f"UI Policy Validation: {os.path.basename(path)}")
    print(f"{'='*60}")
    print(f"Nodes: {len(nodes)}")
    print(f"Links: {len(links)}")
    print(f"Groups: {len(groups)}")
    print(f"\n[ISSUES] {len(issues)}")
    for i in issues:
        print(f"  ✗ {i}")
    print(f"\n[COLLAPSE POLICY VIOLATIONS]")
    print(f"  Knob collapsed: {len(collapsed_violations)}")
    for v in collapsed_violations[:5]:
        print(f"    ! {v}")
    print(f"  Tech NOT collapsed: {len(uncollapsed_violations)}")
    for v in uncollapsed_violations[:5]:
        print(f"    ! {v}")
    print(f"\n[WARNINGS] {len(warnings)}")
    for w in warnings:
        print(f"  ⚠ {w}")

    total_issues = len(issues) + len(collapsed_violations) + len(uncollapsed_violations)
    if total_issues == 0 and not warnings:
        print(f"\n✓ PASS — All checks clean.")
        return 0
    elif total_issues == 0:
        print(f"\n△ PASS with {len(warnings)} warnings.")
        return 0
    else:
        print(f"\n✗ FAIL — {total_issues} policy violations.")
        return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: validate_ui.py <workflow.json>")
        sys.exit(2)
    sys.exit(validate(sys.argv[1]))
