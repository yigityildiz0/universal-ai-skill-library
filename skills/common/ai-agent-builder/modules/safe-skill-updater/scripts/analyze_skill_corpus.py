"""Deterministic, read-only analysis of local SKILL.md trees.

This is intentionally conservative: it flags possible consolidation work but
never changes a source skill.  The generated CSV files are an audit trail for
human review before a canonical corpus is built.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


ROOTS = {
    "codex": Path.home() / ".codex" / "skills",
    "agents": Path.home() / ".agents" / "skills",
}

VENDOR_PATTERNS = {
    "anthropic_claude": r"\b(?:anthropic|claude(?:\s+code)?|sonnet|opus|haiku)\b",
    "openai_chatgpt": r"\b(?:openai|chatgpt|codex|gpt(?:[- ]?\d[\w.\-]*)?|o[1-9](?:[-\w.]*)?)\b",
    "google_gemini": r"\b(?:google|gemini)\b",
    "other_model_provider": r"\b(?:deepseek|qwen|kimi|mistral|llama|grok|perplexity|copilot)\b",
}
MODEL_DIRECTIVE = re.compile(
    r"(?im)^.*\b(?:use|select|choose|switch|set|must|only|always)\b.*\b(?:model|gpt|claude|sonnet|opus|haiku|gemini|qwen|deepseek|kimi|llama|grok)\b.*$"
)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalized(text: str) -> str:
    text = text.removeprefix("\ufeff")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in text.split("\n")).strip() + "\n"


def parse_frontmatter(text: str) -> tuple[str, dict[str, str], str]:
    """Return status, simple scalar fields, and body; no YAML dependency needed."""
    text = text.removeprefix("\ufeff")
    if not text.startswith("---"):
        return "absent", {}, text
    lines = text.replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return "absent", {}, text
    end = next((idx for idx, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
    if end is None:
        return "unterminated", {}, text
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            key, value = match.groups()
            fields[key] = value.strip("\"'")
    return "valid", fields, "\n".join(lines[end + 1 :])


def linked_or_junction(path: Path) -> bool:
    try:
        is_junction = getattr(path, "is_junction", lambda: False)()
        return path.is_symlink() or is_junction or bool(path.lstat().st_file_attributes & 0x400)
    except (AttributeError, OSError):
        return path.is_symlink()


@dataclass
class Skill:
    root: str
    path: str
    relative_path: str
    folder: str
    is_system: bool
    is_linked_folder: bool
    name: str
    description: str
    frontmatter_status: str
    content_sha256: str
    body_sha256: str
    bytes: int
    lines: int
    words: int
    approx_tokens: int
    sidecar_files: int
    sidecar_bytes: int
    modified_utc: str
    name_matches_folder: bool
    name_is_kebab_case: bool
    has_verification: bool
    has_safety: bool
    has_todo: bool
    model_directive_count: int
    anthropic_claude_refs: int
    openai_chatgpt_refs: int
    google_gemini_refs: int
    other_model_provider_refs: int
    quality_score: int
    audit_flags: str


def count_matches(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def score_skill(frontmatter: str, words: int, has_verify: bool, has_safety: bool, has_todo: bool, flags: list[str]) -> int:
    score = 0
    if frontmatter == "valid":
        score += 3
    if 120 <= words <= 5500:
        score += 2
    elif words < 40:
        score -= 3
    if has_verify:
        score += 2
    if has_safety:
        score += 1
    if has_todo:
        score -= 2
    if "missing_name" in flags or "name_folder_mismatch" in flags:
        score -= 3
    if "model_specific_directive" in flags:
        score -= 1
    return score


def iter_skills(root_label: str, root: Path) -> Iterable[Skill]:
    if not root.exists():
        return
    for skill_file in sorted(root.rglob("SKILL.md"), key=lambda p: str(p).lower()):
        try:
            raw = skill_file.read_text(encoding="utf-8", errors="replace")
            raw_bytes = skill_file.stat().st_size
        except OSError:
            continue
        frontmatter_status, fields, body = parse_frontmatter(raw)
        folder = skill_file.parent.name
        relative = skill_file.relative_to(root).as_posix()
        is_system = relative.startswith(".system/")
        name = fields.get("name", "")
        description = fields.get("description", "")
        sidecars = [p for p in skill_file.parent.rglob("*") if p.is_file() and p != skill_file]
        sidecar_bytes = sum(p.stat().st_size for p in sidecars if p.exists())
        has_verify = bool(re.search(r"\b(?:verify|validation|validate|test(?:ing)?|checklist|smoke test)\b", body, re.I))
        has_safety = bool(re.search(r"\b(?:safety|safe|risk|approval|permission|backup|reversible)\b", body, re.I))
        has_todo = bool(re.search(r"\b(?:TODO|TBD|FIXME|placeholder|coming soon)\b", raw, re.I))
        model_directives = len(MODEL_DIRECTIVE.findall(raw))
        flags: list[str] = []
        if frontmatter_status != "valid":
            flags.append(f"frontmatter_{frontmatter_status}")
        if not name:
            flags.append("missing_name")
        elif name != folder:
            flags.append("name_folder_mismatch")
        if name and not NAME_RE.fullmatch(name):
            flags.append("name_not_kebab_case")
        if model_directives:
            flags.append("model_specific_directive")
        if has_todo:
            flags.append("todo_or_placeholder")
        if len(raw.split()) < 40:
            flags.append("very_short")
        quality = score_skill(frontmatter_status, len(raw.split()), has_verify, has_safety, has_todo, flags)
        yield Skill(
            root=root_label,
            path=str(skill_file),
            relative_path=relative,
            folder=folder,
            is_system=is_system,
            is_linked_folder=linked_or_junction(skill_file.parent),
            name=name,
            description=description,
            frontmatter_status=frontmatter_status,
            content_sha256=digest(normalized(raw)),
            body_sha256=digest(normalized(body)),
            bytes=raw_bytes,
            lines=len(raw.splitlines()),
            words=len(raw.split()),
            approx_tokens=math.ceil(len(raw) / 4),
            sidecar_files=len(sidecars),
            sidecar_bytes=sidecar_bytes,
            modified_utc=datetime.fromtimestamp(skill_file.stat().st_mtime, tz=timezone.utc).isoformat(),
            name_matches_folder=bool(name) and name == folder,
            name_is_kebab_case=bool(name) and bool(NAME_RE.fullmatch(name)),
            has_verification=has_verify,
            has_safety=has_safety,
            has_todo=has_todo,
            model_directive_count=model_directives,
            anthropic_claude_refs=count_matches(VENDOR_PATTERNS["anthropic_claude"], raw),
            openai_chatgpt_refs=count_matches(VENDOR_PATTERNS["openai_chatgpt"], raw),
            google_gemini_refs=count_matches(VENDOR_PATTERNS["google_gemini"], raw),
            other_model_provider_refs=count_matches(VENDOR_PATTERNS["other_model_provider"], raw),
            quality_score=quality,
            audit_flags=";".join(flags),
        )


def preference(skill: Skill) -> tuple[int, int, str]:
    # User-owned common corpus wins over aliases, then higher audit score.
    root_priority = {"agents": 5, "codex": 4, "claude": 3, "opencode": 2}.get(skill.root, 0)
    if skill.is_system:
        root_priority -= 3
    if skill.is_linked_folder:
        root_priority -= 1
    return root_priority, skill.quality_score, skill.path.lower()


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    columns = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("work/skill-audit"))
    parser.add_argument(
        "--root",
        action="append",
        metavar="LABEL=PATH",
        help="Optional audit root; repeatable. If omitted, the four user skill roots are used.",
    )
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)

    roots = ROOTS
    if args.root:
        roots = {}
        for item in args.root:
            if "=" not in item:
                raise SystemExit(f"Invalid --root {item!r}; expected LABEL=PATH")
            label, raw_path = item.split("=", 1)
            roots[label] = Path(raw_path)

    skills = [skill for label, root in roots.items() for skill in iter_skills(label, root)]
    records = [asdict(skill) for skill in skills]
    write_csv(out / "all_skills.csv", records)

    by_content: dict[str, list[Skill]] = defaultdict(list)
    by_body: dict[str, list[Skill]] = defaultdict(list)
    by_name: dict[str, list[Skill]] = defaultdict(list)
    for skill in skills:
        by_content[skill.content_sha256].append(skill)
        by_body[skill.body_sha256].append(skill)
        by_name[(skill.name or f"__missing__:{skill.folder}").lower()].append(skill)

    exact_rows: list[dict] = []
    for checksum, group in sorted(by_content.items(), key=lambda item: (-len(item[1]), item[0])):
        group_roots = {skill.root for skill in group}
        if len(group) < 2 or len(group_roots) < 2:
            continue
        canonical = max(group, key=preference)
        exact_rows.append({
            "content_sha256": checksum,
            "copies": len(group),
            "roots": ";".join(sorted(group_roots)),
            "canonical_candidate": canonical.path,
            "canonical_root": canonical.root,
            "all_paths": " | ".join(skill.path for skill in sorted(group, key=lambda s: s.path.lower())),
            "recommendation": "Do not delete yet; retain canonical candidate and disable/archive other physical copies after a load-path test.",
        })
    write_csv(out / "exact_duplicate_groups.csv", exact_rows)

    conflict_rows: list[dict] = []
    for name, group in sorted(by_name.items()):
        contents = {skill.content_sha256 for skill in group}
        if len(group) < 2 or len(contents) < 2:
            continue
        preferred = max(group, key=preference)
        conflict_rows.append({
            "name": name,
            "copies": len(group),
            "distinct_contents": len(contents),
            "roots": ";".join(sorted({skill.root for skill in group})),
            "preferred_review_candidate": preferred.path,
            "all_variants": " | ".join(f"{skill.root}:{skill.path} (score={skill.quality_score})" for skill in sorted(group, key=lambda s: s.path.lower())),
            "recommendation": "Manual merge/selection required; same name has divergent instructions.",
        })
    write_csv(out / "same_name_conflicts.csv", conflict_rows)

    vendor_rows = []
    for skill in skills:
        references = skill.anthropic_claude_refs + skill.openai_chatgpt_refs + skill.google_gemini_refs + skill.other_model_provider_refs
        if references or skill.model_directive_count:
            row = asdict(skill)
            row["recommendation"] = (
                "Review context before changing names. Generalize only prescriptive model/provider selection; preserve factual or integration references."
            )
            vendor_rows.append(row)
    write_csv(out / "vendor_model_review.csv", vendor_rows)

    issue_rows = []
    for skill in skills:
        if skill.audit_flags or skill.quality_score <= 0:
            row = asdict(skill)
            row["recommendation"] = "Review before migration; this is a diagnostic flag, not an automatic removal decision."
            issue_rows.append(row)
    write_csv(out / "quality_and_format_review.csv", issue_rows)

    root_counts = Counter(skill.root for skill in skills)
    summary = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "roots": {name: str(path) for name, path in roots.items()},
        "total_skills": len(skills),
        "skill_count_by_root": dict(sorted(root_counts.items())),
        "system_skills_in_codex": sum(1 for skill in skills if skill.is_system),
        "linked_or_junction_skill_folders": sum(1 for skill in skills if skill.is_linked_folder),
        "cross_root_exact_duplicate_groups": len(exact_rows),
        "same_name_divergent_groups": len(conflict_rows),
        "format_or_quality_flags": len(issue_rows),
        "vendor_or_model_reference_skills": len(vendor_rows),
        "model_directive_skills": sum(1 for skill in skills if skill.model_directive_count),
        "output_files": [
            "all_skills.csv",
            "exact_duplicate_groups.csv",
            "same_name_conflicts.csv",
            "vendor_model_review.csv",
            "quality_and_format_review.csv",
        ],
        "interpretation": "Scores and flags are triage aids. No source file was modified by this audit.",
    }
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
