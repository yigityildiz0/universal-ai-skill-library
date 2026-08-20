#!/usr/bin/env python3
"""List sibling skill name/description metadata without loading full skill bodies."""
from __future__ import annotations
import json
from pathlib import Path


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    out: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line[:1].isspace():
            continue
        key, value = line.split(":", 1)
        if key in {"name", "description"}:
            out[key] = value.strip().strip("'\"")
    return out


def main() -> None:
    skills_root = Path(__file__).resolve().parents[2]
    items = []
    for skill_file in sorted(skills_root.glob("*/SKILL.md")):
        meta = frontmatter(skill_file)
        if meta.get("name") and meta.get("description"):
            items.append(meta)
    print(json.dumps(items, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
