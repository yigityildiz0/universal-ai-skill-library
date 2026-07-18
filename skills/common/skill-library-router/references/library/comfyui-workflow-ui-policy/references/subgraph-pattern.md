# Subgraph Pattern (from 08 - Pixaroma Subgraph Compact)

## JSON Structure

A workflow with subgraphs has:

```json
{
  "id": "<workflow-uuid>",
  "nodes": [ ... outer nodes ... ],
  "links": [ ... outer links ... ],
  "groups": [ ... outer groups ... ],
  "definitions": {
    "subgraphs": [
      {
        "id": "<subgraph-uuid>",
        "name": "<display name>",
        "version": 1,
        "state": { "lastGroupId": 0, "lastNodeId": N, "lastLinkId": M, "lastRerouteId": 0 },
        "revision": 0,
        "config": {},
        "inputNode": { "id": -10, "bounding": [x,y,w,h] },
        "outputNode": { "id": -20, "bounding": [x,y,w,h] },
        "inputs": [
          { "id": "<uuid>", "name": "image", "type": "IMAGE", "linkIds": [N], "localized_name": "image", "pos": [x,y] }
        ],
        "outputs": [
          { "id": "<uuid>", "name": "IMAGE", "type": "IMAGE", "linkIds": [N], "localized_name": "IMAGE", "pos": [x,y] }
        ],
        "widgets": [],
        "nodes": [ ... inner nodes (full ComfyUI node objects) ... ],
        "links": [ ... internal links + IO links ... ],
        "groups": [],
        "extra": { "workflowRendererVersion": "LG", "ue_links": [] }
      }
    ]
  }
}
```

## Subgraph Instance Node (in outer `nodes`)

The instance node uses the subgraph UUID as its `type`:

```json
{
  "id": <instance_node_id>,
  "type": "<subgraph-uuid>",
  "pos": [x, y],
  "size": [w, h],
  "flags": { "collapsed": true },
  "inputs": [ ... match subgraph inputs by index/name ... ],
  "outputs": [ ... match subgraph outputs by index/name ... ],
  "properties": {
    "proxyWidgets": [
      ["<inner_node_id>", "<widget_name>"],
      ...
    ],
    "cnr_id": "comfy-core",
    "ver": "0.15.1"
  },
  "widgets_values": []
}
```

## Internal Links Format

Inner links use object format (NOT array):

```json
{
  "id": 262,
  "origin_id": 213,
  "origin_slot": 1,
  "target_id": 6,
  "target_slot": 0,
  "type": "CLIP"
}
```

IO links use virtual IDs:
- `origin_id: -10` → input from outside
- `target_id: -20` → output to outside

## proxyWidgets Mechanics

ProxyWidgets surface specific widgets from inner nodes to the outer subgraph node's widget panel. User edits the widget on the outer node, value propagates to inner node.

Format: `[inner_node_id_as_string, widget_name]`

Example from 08:
```json
"proxyWidgets": [
  ["6", "text"],           // CLIPTextEncode text
  ["163", "seed"],         // KSampler seed
  ["163", "steps"],        // KSampler steps
  ["194", "unet_name"],    // UNETLoader file
  ["213", "lora_1"],       // Power LoRA slot 1
  ["213", "lora_2"]        // Power LoRA slot 2
]
```

## Recommended proxyWidgets for Klein 9B Workflows

```json
"proxyWidgets": [
  ["<UNETLoader_id>", "unet_name"],
  ["<UNETLoader_id>", "weight_dtype"],
  ["<CLIPLoader_id>", "clip_name"],
  ["<VAELoader_id>", "vae_name"],
  ["<PowerLoraLoader_id>", "lora_1"],
  ["<PowerLoraLoader_id>", "lora_2"],
  ["<PowerLoraLoader_id>", "lora_3"],
  ["<PowerLoraLoader_id>", "lora_4"],
  ["<PowerLoraLoader_id>", "lora_5"],  // BFS Head
  ["<ApplyPuLIDFlux2_id>", "strength"],
  ["<IdentityFeatureTransferV3_id>", "preset"],
  ["<KSamplerSelect_id>", "sampler_name"]
]
```

## Building Programmatically

Critical steps:

1. **Generate UUID** for subgraph: `str(uuid.uuid4())`
2. **Move tech nodes** from outer `nodes` to `definitions.subgraphs[0].nodes` (keep IDs)
3. **Convert outer links** that endpoint into tech nodes:
   - If both endpoints inside → internal link
   - If src outside, tgt inside → input link (origin_id=-10, target=inner)
   - If src inside, tgt outside → output link (origin=inner, target_id=-20)
4. **Create subgraph IO**:
   - inputs[] and outputs[] arrays with UUIDs
   - inputNode/outputNode boundings
5. **Create subgraph instance node** in outer with type=subgraph_uuid
6. **Rewire outer links** to go to subgraph instance (not the inner nodes directly)
7. **Set proxyWidgets** in instance properties

## Pitfalls

- Internal link format is object, NOT array (outer uses array)
- Subgraph instance inputs/outputs must MATCH subgraph definition inputs/outputs by index
- proxyWidgets refers to inner node IDs as STRINGS (not integers)
- `last_node_id` in main and `state.lastNodeId` in subgraph must be tracked separately
- IO virtual IDs -10 (input) and -20 (output) are hardcoded
