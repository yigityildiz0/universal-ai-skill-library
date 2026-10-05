---
name: research-add-fields
description: "Add field definitions to existing research outline. Use with an existing /research outline. Turkish triggers: araştırmaya alan ekle, yeni kriter ekle."
---

# Research Add Fields - Supplement Research Fields

## Trigger
`/research-add-fields`

## Workflow

### Step 1: Auto-locate Fields File
Find `*/fields.yaml` file in current working directory, auto-read existing fields definitions.

### Step 2: Get Supplement Source
Ask user to choose:
- **A. User direct input**: User provides field names and descriptions
- **B. Web Search**: Launch agent to search common fields in this domain

### Step 3: Display and Confirm
- Display suggested new fields list
- User confirms which fields to add
- User specifies field category and detail_level

### Step 4: Save Update
Append confirmed fields to fields.yaml, save file.

## Output
Updated `{topic}/fields.yaml` file (in-place modification, requires user confirmation)

## Host notes (added for Yiğit's setup)

- If this host has no background web-search agent or subagents (for example ChatGPT/Claude web or mobile), run the same prompt template yourself for each item — sequentially, or with the host's parallel tools — and write the same outputs.
- The validator is `validate_json.py` inside the `research` skill folder. If the path shown above does not exist on this host, locate that file next to the `research` skill and run it from there (requires `pip install pyyaml`).
- Yiğit prefers few interruptions: put all confirmation questions of a step into one message, and when he says "devam" or "varsayılanla", use defaults (time range: last 12 months; batch_size 3; items_per_agent 2).
