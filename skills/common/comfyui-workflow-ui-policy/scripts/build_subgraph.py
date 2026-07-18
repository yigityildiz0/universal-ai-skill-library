# -*- coding: utf-8 -*-
"""
build_subgraph.py — EXPERIMENTAL flat -> subgraph nest helper for ComfyUI (frontend 1.44).

Moves a chosen set of "tech" node IDs into ONE definitions.subgraphs[] entry, rewires
links (internal / input-port / output-port), creates the outer instance node with
proxyWidgets, and removes the inner nodes from the outer graph.

CANNOT be tested without loading in ComfyUI. ALWAYS:
  1. back up the source file first,
  2. run validate_wf.py + validate_ui.py on the output,
  3. test-load in ComfyUI before trusting it.

Schema reference: references/subgraph-pattern.md (verified vs upstream Head Swap, frontend 1.44).

Usage (as a library):
    from build_subgraph import nest
    nest(src_json, dst_json, inner_ids=[...], name="Klein Engine",
         proxy=[("126","unet_name"),("197","steps")], instance_pos=[400,300])
"""
import json, uuid, copy, sys


def _links_index(wf):
    """Return {link_id: [id, origin_id, origin_slot, target_id, target_slot, type]} for outer array links."""
    out = {}
    for l in wf.get("links", []):
        if isinstance(l, list):
            out[l[0]] = list(l)
        else:
            out[l["id"]] = [l["id"], l["origin_id"], l.get("origin_slot", 0),
                            l["target_id"], l.get("target_slot", 0), l.get("type")]
    return out


def nest(src, dst, inner_ids, name="Subgraph", proxy=None, instance_pos=None, instance_size=None):
    wf = json.load(open(src, encoding="utf-8"))
    inner = set(inner_ids)
    nodes = {n["id"]: n for n in wf["nodes"]}
    if not inner.issubset(set(nodes)):
        missing = inner - set(nodes)
        raise SystemExit(f"inner_ids not in workflow: {missing}")

    links = _links_index(wf)
    sg_id = str(uuid.uuid4())

    inner_nodes = [n for n in wf["nodes"] if n["id"] in inner]
    outer_nodes = [n for n in wf["nodes"] if n["id"] not in inner]

    sg_links = []          # internal object links
    sg_inputs = []         # subgraph input ports
    sg_outputs = []        # subgraph output ports
    inst_inputs = []       # instance node inputs (outer side)
    inst_outputs = []      # instance node outputs (outer side)
    new_outer_links = []   # rebuilt outer links (array form)
    next_link = (max(links) if links else 0) + 1

    def new_lid():
        nonlocal next_link
        v = next_link; next_link += 1; return v

    # group inner->outer outputs by (inner_node, slot) so one port can fan out
    out_ports = {}   # (oid,oslot,type) -> port dict
    in_ports = {}    # (outer_src_id,src_slot,type) -> port dict  (dedupe shared sources)

    for lid, (_, oid, oslot, tid, tslot, ltype) in links.items():
        o_in = oid in inner; t_in = tid in inner
        if o_in and t_in:
            sg_links.append({"id": lid, "origin_id": oid, "origin_slot": oslot,
                             "target_id": tid, "target_slot": tslot, "type": ltype})
        elif (not o_in) and t_in:
            # external -> inner : becomes subgraph INPUT port
            key = (oid, oslot, ltype)
            if key not in in_ports:
                pid = str(uuid.uuid4())
                port = {"id": pid, "name": ltype.lower() if ltype else "in",
                        "type": ltype, "linkIds": [], "pos": [0, 0]}
                in_ports[key] = port; sg_inputs.append(port)
                inst_inputs.append({"name": port["name"], "type": ltype, "link": None})
            port = in_ports[key]
            inner_lid = new_lid()
            port["linkIds"].append(inner_lid)
            sg_links.append({"id": inner_lid, "origin_id": -10,
                             "origin_slot": sg_inputs.index(port), "target_id": tid,
                             "target_slot": tslot, "type": ltype})
            # outer link: external source -> instance input (index = port index)
            new_outer_links.append([lid, oid, oslot, "INSTANCE", sg_inputs.index(port), ltype])
        elif o_in and (not t_in):
            key = (oid, oslot, ltype)
            if key not in out_ports:
                pid = str(uuid.uuid4())
                port = {"id": pid, "name": (ltype or "out").upper(),
                        "type": ltype, "linkIds": [], "pos": [0, 0]}
                out_ports[key] = port; sg_outputs.append(port)
                inst_outputs.append({"name": port["name"], "type": ltype, "links": []})
            port = out_ports[key]
            inner_lid = new_lid()
            port["linkIds"].append(inner_lid)
            sg_links.append({"id": inner_lid, "origin_id": oid, "origin_slot": oslot,
                             "target_id": -20, "target_slot": sg_outputs.index(port), "type": ltype})
            # outer link: instance output -> external target
            new_outer_links.append([lid, "INSTANCE", sg_outputs.index(port), tid, tslot, ltype])
        else:
            new_outer_links.append([lid, oid, oslot, tid, tslot, ltype])  # untouched

    inst_id = max(nodes) + 1
    for l in new_outer_links:
        if l[1] == "INSTANCE":
            l[1] = inst_id
        if l[3] == "INSTANCE":
            l[3] = inst_id
        if l[1] == inst_id:
            inst_outputs[l[2]]["links"].append(l[0])
        if l[3] == inst_id:
            inst_inputs[l[4]]["link"] = l[0]

    inner_max_node = max(inner) if inner else 0
    inner_max_link = max([sl["id"] for sl in sg_links], default=0)

    # CRITICAL: inner nodes must reference the NEW internal link ids (not stale outer ids),
    # else ComfyUI cannot resolve the subgraph's internal wiring.
    sg_nodes = [copy.deepcopy(n) for n in inner_nodes]
    for n in sg_nodes:
        for slot, inp in enumerate(n.get("inputs") or []):
            m = next((L for L in sg_links if L["target_id"] == n["id"] and L["target_slot"] == slot), None)
            inp["link"] = m["id"] if m else None
        for slot, out in enumerate(n.get("outputs") or []):
            out["links"] = [L["id"] for L in sg_links if L["origin_id"] == n["id"] and L["origin_slot"] == slot]

    subgraph = {
        "id": sg_id, "name": name, "version": 1, "revision": 0, "config": {},
        "state": {"lastGroupId": 0, "lastNodeId": inner_max_node,
                  "lastLinkId": inner_max_link, "lastRerouteId": 0},
        "inputNode": {"id": -10, "bounding": [-400, 0, 120, 200]},
        "outputNode": {"id": -20, "bounding": [1600, 0, 120, 200]},
        "inputs": sg_inputs, "outputs": sg_outputs, "widgets": [],
        "nodes": sg_nodes, "links": sg_links, "groups": [],
        "extra": {"workflowRendererVersion": "LG", "ue_links": [], "links_added_by_ue": []},
    }

    instance = {
        "id": inst_id, "type": sg_id, "pos": instance_pos or [600, 200],
        "size": instance_size or [320, 200], "flags": {}, "order": 0, "mode": 0,
        "inputs": inst_inputs, "outputs": inst_outputs,
        "properties": {"proxyWidgets": [[str(a), b] for (a, b) in (proxy or [])],
                       "cnr_id": "comfy-core", "ver": "0.15.1"},
        "widgets_values": [], "title": name,
    }

    wf["nodes"] = outer_nodes + [instance]
    wf["links"] = new_outer_links
    wf.setdefault("definitions", {}).setdefault("subgraphs", []).append(subgraph)
    wf["last_node_id"] = max(wf["last_node_id"], inst_id)
    wf["last_link_id"] = max(wf.get("last_link_id", 0), next_link - 1)

    json.dump(wf, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"WROTE {dst}")
    print(f"  subgraph '{name}' id={sg_id}  inner={len(inner_nodes)} nodes  "
          f"inputs={len(sg_inputs)} outputs={len(sg_outputs)} internal_links={len(sg_links)}")
    print(f"  instance node id={inst_id} proxyWidgets={len(instance['properties']['proxyWidgets'])}")
    print("  REMINDER: validate_wf.py + validate_ui.py, then TEST-LOAD in ComfyUI.")


if __name__ == "__main__":
    print(__doc__)
    print("Import and call nest(); this module is a library, not a CLI.")
