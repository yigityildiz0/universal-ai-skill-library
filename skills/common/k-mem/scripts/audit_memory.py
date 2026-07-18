"""Read-only health audit for K-Mem-compatible project memory."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic_api_key": re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*[^\s<>{}\[\]]{8,}"),
    "github_token": re.compile(r"\bgh[opusr]_[A-Za-z0-9_]{20,}\b"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
}

START = "<!-- k-mem:start -->"
END = "<!-- k-mem:end -->"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()

    candidates = [root / "AGENTS.md", root / "CLAUDE.md"]
    memory_roots = [root / ".k-mem", root / "memory", root / ".ai-handoff"]
    files = [p for p in candidates if p.is_file()]
    for memory_root in memory_roots:
        if memory_root.is_dir():
            files.extend(p for p in memory_root.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt"})

    findings: list[dict[str, object]] = []
    marker_files = []
    for path in sorted(set(files), key=lambda p: str(p).lower()):
        text = path.read_text(encoding="utf-8", errors="replace")
        if START in text or END in text:
            marker_files.append(str(path))
            if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
                findings.append({"severity": "error", "code": "invalid_markers", "path": str(path)})
        for code, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                findings.append({"severity": "error", "code": code, "path": str(path)})
        if "\ufffd" in text or re.search(r"(?:Ã.|Â.|â€|ðŸ)", text):
            findings.append({"severity": "warning", "code": "encoding_damage", "path": str(path)})

    if len(marker_files) > 1:
        findings.append({"severity": "warning", "code": "multiple_hot_caches", "path": "; ".join(marker_files)})

    report = {
        "root": str(root),
        "files_scanned": len(set(files)),
        "marker_files": marker_files,
        "findings": findings,
        "file_hashes": {str(path): sha256(path) for path in sorted(set(files), key=lambda p: str(p).lower())},
        "read_only": True,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"K-Mem audit: {report['files_scanned']} files, {len(findings)} findings")
        for item in findings:
            print(f"[{item['severity']}] {item['code']}: {item['path']}")
    return 1 if any(item["severity"] == "error" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
