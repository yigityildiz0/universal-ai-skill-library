#!/usr/bin/env python3
"""Inventory a skill directory or ZIP without executing or extracting it."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath


TEXT_LIMIT = 2 * 1024 * 1024
MAX_ENTRY_SIZE = 1024 * 1024 * 1024
MAX_RATIO = 1000
EXECUTABLE_SUFFIXES = {
    ".bat", ".cmd", ".com", ".dll", ".exe", ".jar", ".msi", ".ps1",
    ".scr", ".sh", ".so", ".vbs",
}
TEXT_SUFFIXES = {
    ".cfg", ".ini", ".json", ".jsonc", ".md", ".ps1", ".py", ".sh",
    ".toml", ".txt", ".yaml", ".yml",
}
PATTERNS = {
    "process_execution": re.compile(r"\b(subprocess\.|os\.system\s*\(|Start-Process\b|Invoke-Expression\b|child_process\b)", re.I),
    "dynamic_code": re.compile(r"\b(eval|exec)\s*\(|\bInvoke-Expression\b|\bIEX\b", re.I),
    "network_access": re.compile(r"\b(requests\.|urllib\.|fetch\s*\(|Invoke-WebRequest\b|curl\b|wget\b|https?://)", re.I),
    "credential_access": re.compile(r"(api[_ -]?key|access[_ -]?token|client[_ -]?secret|credentials?|cookies?|\.ssh|\.aws|\.env\b)", re.I),
    "persistence": re.compile(r"(scheduled task|schtasks\b|startup folder|runonce|systemd|launchd|crontab|registry.*\\run)", re.I),
    "destructive_operation": re.compile(r"(rm\s+-rf\b|Remove-Item\b.*-Recurse|rmdir\s+/s\b|shutil\.rmtree\s*\(|format\s+[a-z]:)", re.I),
    "instruction_override": re.compile(r"(ignore (all |any )?(previous|prior|higher)[ -]?(instructions|rules)|reveal (the )?(system prompt|secrets?)|bypass (safety|policy|permissions?))", re.I),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def unsafe_archive_name(name: str) -> list[str]:
    normalized = name.replace("\\", "/")
    path = PurePosixPath(normalized)
    flags: list[str] = []
    if path.is_absolute() or re.match(r"^[A-Za-z]:", normalized):
        flags.append("absolute_or_drive_path")
    if ".." in path.parts:
        flags.append("path_traversal")
    if any(":" in part for part in path.parts):
        flags.append("colon_or_ads_path")
    return flags


def scan_text(name: str, data: bytes) -> list[dict[str, str]]:
    if Path(name).suffix.lower() not in TEXT_SUFFIXES or len(data) > TEXT_LIMIT:
        return []
    text = data.decode("utf-8", errors="replace")
    findings: list[dict[str, str]] = []
    for label, pattern in PATTERNS.items():
        match = pattern.search(text)
        if match:
            findings.append({"type": label, "path": name, "evidence": match.group(0)[:160]})
    return findings


def inspect_zip(path: Path) -> dict[str, object]:
    entries: list[dict[str, object]] = []
    findings: list[dict[str, str]] = []
    total_compressed = 0
    total_uncompressed = 0
    with zipfile.ZipFile(path) as archive:
        for info in archive.infolist():
            name = info.filename
            mode = (info.external_attr >> 16) & 0o177777
            item_flags = unsafe_archive_name(name)
            if stat.S_ISLNK(mode):
                item_flags.append("symlink_entry")
            if info.file_size > MAX_ENTRY_SIZE:
                item_flags.append("very_large_entry")
            ratio = info.file_size / max(info.compress_size, 1)
            if ratio > MAX_RATIO and info.file_size > 1024 * 1024:
                item_flags.append("extreme_compression_ratio")
            if Path(name).suffix.lower() in EXECUTABLE_SUFFIXES:
                item_flags.append("executable_or_script")
            for flag in item_flags:
                findings.append({"type": flag, "path": name, "evidence": "archive metadata"})
            digest = None
            if not info.is_dir() and info.file_size <= TEXT_LIMIT:
                data = archive.read(info)
                digest = sha256_bytes(data)
                findings.extend(scan_text(name, data))
            entries.append({
                "path": name,
                "size": info.file_size,
                "compressed_size": info.compress_size,
                "sha256_if_read": digest,
                "flags": sorted(set(item_flags)),
            })
            total_compressed += info.compress_size
            total_uncompressed += info.file_size
    return {
        "artifact_type": "zip",
        "artifact_sha256": sha256_file(path),
        "entries": entries,
        "entry_count": len(entries),
        "compressed_bytes": total_compressed,
        "uncompressed_bytes": total_uncompressed,
        "findings": findings,
    }


def inspect_directory(path: Path) -> dict[str, object]:
    entries: list[dict[str, object]] = []
    findings: list[dict[str, str]] = []
    tree_rows: list[str] = []
    for root, dirs, files in os.walk(path, followlinks=False):
        root_path = Path(root)
        for dirname in list(dirs):
            full = root_path / dirname
            if full.is_symlink():
                rel = full.relative_to(path).as_posix()
                findings.append({"type": "symlink_entry", "path": rel, "evidence": str(os.readlink(full))})
                entries.append({"path": rel, "type": "symlink_directory", "target": str(os.readlink(full)), "flags": ["symlink_entry"]})
                dirs.remove(dirname)
        for filename in files:
            full = root_path / filename
            rel = full.relative_to(path).as_posix()
            flags: list[str] = []
            if full.is_symlink():
                flags.append("symlink_entry")
                target = str(os.readlink(full))
                findings.append({"type": "symlink_entry", "path": rel, "evidence": target})
                entries.append({"path": rel, "type": "symlink_file", "target": target, "flags": flags})
                continue
            size = full.stat().st_size
            digest = sha256_file(full)
            tree_rows.append(f"{rel}\0{digest}\0{size}")
            if full.suffix.lower() in EXECUTABLE_SUFFIXES:
                flags.append("executable_or_script")
                findings.append({"type": "executable_or_script", "path": rel, "evidence": full.suffix.lower()})
            if size <= TEXT_LIMIT:
                findings.extend(scan_text(rel, full.read_bytes()))
            entries.append({"path": rel, "type": "file", "size": size, "sha256": digest, "flags": flags})
    tree_hash = sha256_bytes("\n".join(sorted(tree_rows)).encode("utf-8"))
    return {
        "artifact_type": "directory",
        "artifact_sha256": tree_hash,
        "entries": entries,
        "entry_count": len(entries),
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="Directory or ZIP to inspect")
    parser.add_argument("--json", type=Path, dest="json_path", help="Write the report to this path")
    args = parser.parse_args()

    artifact = args.artifact.expanduser().resolve()
    if not artifact.exists():
        parser.error(f"artifact does not exist: {artifact}")
    if artifact.is_dir():
        report = inspect_directory(artifact)
    elif artifact.is_file() and zipfile.is_zipfile(artifact):
        report = inspect_zip(artifact)
    else:
        parser.error("artifact must be a directory or ZIP file")

    report["artifact"] = str(artifact)
    report["finding_count"] = len(report["findings"])
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_path:
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(rendered + "\n", encoding="utf-8")
    else:
        sys.stdout.write(rendered + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
