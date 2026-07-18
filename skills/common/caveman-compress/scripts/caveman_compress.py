#!/usr/bin/env python3
"""Preview-first, provider-neutral prose compression safety gate.

The script never generates a compressed candidate and performs no network
calls. Without --apply it is read-only. Apply requires explicit user approval,
preview hashes, a clean invariant report, a timestamped backup, and an atomic
replacement.
"""

from __future__ import annotations

import argparse
import codecs
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
from typing import Iterable, Sequence


MAX_FILE_SIZE = 1_048_576
ALLOWED_SOURCE_SUFFIXES = {"", ".md", ".markdown", ".txt"}
BACKUP_MARKER = ".caveman-backup."

FENCE_RE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+)$")
LIST_RE = re.compile(r"^([ \t]*)([-+*]|\d+[.)])([ \t]+)")
TABLE_SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
URL_RE = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
QUOTED_PATH_RE = re.compile(
    r"[\"']((?:[A-Za-z]:[\\/]|\\\\|\.{1,2}[\\/]|~[\\/]|/)[^\"'\r\n]+)[\"']"
)
ABSOLUTE_PATH_RE = re.compile(
    r"(?<![\w:])(?:[A-Za-z]:[\\/]|\\\\|\.{1,2}[\\/]|~[\\/]|/)"
    r"[^\s<>\"'`]+"
)
RELATIVE_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9:_-])(?:[A-Za-z0-9_.@+()-]+[\\/])+"
    r"[A-Za-z0-9_.@+()-]+"
)
NUMBER_RE = re.compile(
    r"(?<![\w])(?:"
    r"0x[0-9A-Fa-f]+|"
    r"v?\d+(?:[._:/-]\d+)*"
    r"(?:\s?(?:%|ms|sec|min|h|KB|MB|GB|KiB|MiB|GiB|px|em|rem|kg|mg|g|mL|uL|µL|°C))?"
    r")(?![\w])"
)

NEGATION_TERMS = (
    "must not",
    "may not",
    "do not",
    "does not",
    "did not",
    "is not",
    "are not",
    "was not",
    "were not",
    "should not",
    "cannot",
    "can't",
    "won't",
    "don't",
    "doesn't",
    "didn't",
    "isn't",
    "aren't",
    "wasn't",
    "weren't",
    "shouldn't",
    "mustn't",
    "without",
    "neither",
    "never",
    "none",
    "nor",
    "not",
    "no",
    "değildir",
    "değildi",
    "değil",
    "olmadan",
    "yapmayın",
    "yapma",
    "hayır",
    "asla",
    "hiçbir",
    "hiç",
    "yok",
)

CONSTRAINT_TERMS = (
    "must not",
    "must",
    "required",
    "should not",
    "should",
    "only if",
    "only",
    "unless",
    "except",
    "before",
    "after",
    "always",
    "never",
    "if",
    "when",
    "zorunludur",
    "zorunlu",
    "gerekir",
    "gerekmiyor",
    "yalnızca",
    "sadece",
    "olmadıkça",
    "hariç",
    "önce",
    "sonra",
    "her zaman",
    "asla",
    "eğer",
)


class SafetyError(RuntimeError):
    """Raised when a safety precondition blocks preview or apply."""


@dataclass(frozen=True)
class Document:
    path: Path
    raw: bytes
    text: str
    has_bom: bool
    newline: str
    mode: int


@dataclass(frozen=True)
class Finding:
    code: str
    message: str


@dataclass
class ValidationReport:
    errors: list[Finding] = field(default_factory=list)
    warnings: list[Finding] = field(default_factory=list)
    metrics: dict[str, float | int] = field(default_factory=dict)

    @property
    def is_valid(self) -> bool:
        return not self.errors

    def add_error(self, code: str, message: str) -> None:
        self.errors.append(Finding(code, message))

    def add_warning(self, code: str, message: str) -> None:
        self.warnings.append(Finding(code, message))

    def to_dict(self) -> dict[str, object]:
        return {
            "valid": self.is_valid,
            "errors": [asdict(item) for item in self.errors],
            "warnings": [asdict(item) for item in self.warnings],
            "metrics": self.metrics,
        }


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(131_072), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _reject_backup_name(path: Path) -> None:
    lower = path.name.casefold()
    if BACKUP_MARKER in lower or lower.endswith(".original.md"):
        raise SafetyError(f"backup files are never valid sources: {path}")


def load_document(path_like: str | Path, *, source: bool) -> Document:
    path = Path(path_like).expanduser().absolute()
    if path.is_symlink():
        raise SafetyError(f"symbolic links are not supported: {path}")
    if not path.exists():
        raise SafetyError(f"file not found: {path}")
    if not path.is_file():
        raise SafetyError(f"not a regular file: {path}")
    if source:
        _reject_backup_name(path)
        if path.suffix.casefold() not in ALLOWED_SOURCE_SUFFIXES:
            raise SafetyError(
                "source must be Markdown, plain text, or extensionless: "
                f"{path.suffix or '<none>'}"
            )
    size = path.stat().st_size
    if size > MAX_FILE_SIZE:
        raise SafetyError(
            f"file exceeds {MAX_FILE_SIZE} byte safety limit: {path}"
        )

    raw = path.read_bytes()
    has_bom = raw.startswith(codecs.BOM_UTF8)
    payload = raw[len(codecs.BOM_UTF8) :] if has_bom else raw
    try:
        decoded = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SafetyError(f"file is not valid UTF-8: {path}") from exc

    crlf_count = decoded.count("\r\n")
    lf_count = decoded.count("\n")
    lone_lf_count = lf_count - crlf_count
    lone_cr_count = decoded.count("\r") - crlf_count
    if source and ((crlf_count and lone_lf_count) or lone_cr_count):
        raise SafetyError(f"mixed line endings require manual normalization: {path}")
    newline = "\r\n" if crlf_count else "\n"
    return Document(
        path=path,
        raw=raw,
        text=normalize_newlines(decoded),
        has_bom=has_bom,
        newline=newline,
        mode=stat.S_IMODE(path.stat().st_mode),
    )


def ensure_distinct_files(source: Document, candidate: Document) -> None:
    if source.path.resolve() == candidate.path.resolve():
        raise SafetyError("candidate must be a separate file")
    try:
        if os.path.samefile(source.path, candidate.path):
            raise SafetyError("candidate resolves to the source file")
    except OSError:
        pass


def extract_frontmatter(text: str) -> tuple[str | None, bool]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, False
    for index in range(1, len(lines)):
        if lines[index] in {"---", "..."}:
            return "\n".join(lines[: index + 1]), False
    return None, True


def extract_fenced_blocks(
    text: str,
) -> tuple[list[str], set[int], bool]:
    lines = text.split("\n")
    blocks: list[str] = []
    protected_lines: set[int] = set()
    index = 0
    malformed = False

    while index < len(lines):
        match = FENCE_RE.match(lines[index])
        if not match:
            index += 1
            continue
        fence = match.group(2)
        fence_char = fence[0]
        fence_length = len(fence)
        start = index
        index += 1
        closed = False
        while index < len(lines):
            close = FENCE_RE.match(lines[index])
            if (
                close
                and close.group(2)[0] == fence_char
                and len(close.group(2)) >= fence_length
                and not close.group(3).strip()
            ):
                closed = True
                index += 1
                break
            index += 1
        if not closed:
            malformed = True
            protected_lines.update(range(start, len(lines)))
            break
        protected_lines.update(range(start, index))
        blocks.append("\n".join(lines[start:index]))

    return blocks, protected_lines, malformed


def extract_indented_code(text: str, protected_lines: set[int]) -> list[str]:
    result: list[str] = []
    for index, line in enumerate(text.split("\n")):
        if index in protected_lines:
            continue
        if line.startswith("    ") or line.startswith("\t"):
            result.append(line)
    return result


def extract_inline_code(
    text: str, protected_lines: set[int]
) -> tuple[list[str], bool]:
    lines = text.split("\n")
    masked = "\n".join(
        "" if index in protected_lines else line
        for index, line in enumerate(lines)
    )
    spans: list[str] = []
    malformed = False
    index = 0
    while index < len(masked):
        if masked[index] != "`":
            index += 1
            continue
        end_run = index
        while end_run < len(masked) and masked[end_run] == "`":
            end_run += 1
        delimiter = masked[index:end_run]
        close = masked.find(delimiter, end_run)
        if close == -1:
            malformed = True
            break
        spans.append(masked[index : close + len(delimiter)])
        index = close + len(delimiter)
    return spans, malformed


def _trim_terminal_punctuation(value: str) -> str:
    result = value.rstrip(".,;:!?")
    while result.endswith(")") and result.count(")") > result.count("("):
        result = result[:-1]
    while result.endswith("]") and result.count("]") > result.count("["):
        result = result[:-1]
    return result


def extract_urls(text: str) -> Counter[str]:
    return Counter(_trim_terminal_punctuation(item) for item in URL_RE.findall(text))


def extract_link_destinations(text: str) -> Counter[str]:
    return Counter(match.strip() for match in MARKDOWN_LINK_RE.findall(text))


def extract_paths(text: str) -> Counter[str]:
    without_urls = URL_RE.sub(" ", text)
    found: list[str] = []
    for match in QUOTED_PATH_RE.findall(without_urls):
        found.append(match.strip())
    for regex in (ABSOLUTE_PATH_RE, RELATIVE_PATH_RE):
        for match in regex.findall(without_urls):
            found.append(_trim_terminal_punctuation(match))
    return Counter(found)


def _split_table_cells(line: str) -> list[str]:
    raw = line.strip()
    if raw.startswith("|"):
        raw = raw[1:]
    if raw.endswith("|") and not raw.endswith(r"\|"):
        raw = raw[:-1]

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    backtick_run = 0
    index = 0
    while index < len(raw):
        char = raw[index]
        if escaped:
            current.append(char)
            escaped = False
            index += 1
            continue
        if char == "\\":
            current.append(char)
            escaped = True
            index += 1
            continue
        if char == "`":
            run_end = index
            while run_end < len(raw) and raw[run_end] == "`":
                run_end += 1
            run_length = run_end - index
            if backtick_run == 0:
                backtick_run = run_length
            elif backtick_run == run_length:
                backtick_run = 0
            current.extend(raw[index:run_end])
            index = run_end
            continue
        if char == "|" and backtick_run == 0:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        index += 1
    cells.append("".join(current).strip())
    return cells


def _is_separator_row(line: str) -> bool:
    cells = _split_table_cells(line)
    return len(cells) >= 2 and all(
        TABLE_SEPARATOR_CELL_RE.fullmatch(cell) is not None for cell in cells
    )


def _alignment_signature(separator_line: str) -> tuple[str, ...]:
    result: list[str] = []
    for cell in _split_table_cells(separator_line):
        left = cell.startswith(":")
        right = cell.endswith(":")
        if left and right:
            result.append("center")
        elif right:
            result.append("right")
        elif left:
            result.append("left")
        else:
            result.append("default")
    return tuple(result)


def extract_tables(
    text: str, protected_lines: set[int]
) -> list[tuple[str, int, tuple[int, ...], tuple[str, ...]]]:
    lines = text.split("\n")
    tables: list[tuple[str, int, tuple[int, ...], tuple[str, ...]]] = []
    index = 0
    while index + 1 < len(lines):
        if (
            index in protected_lines
            or index + 1 in protected_lines
            or "|" not in lines[index]
            or not _is_separator_row(lines[index + 1])
        ):
            index += 1
            continue

        rows = [lines[index], lines[index + 1]]
        next_index = index + 2
        while (
            next_index < len(lines)
            and next_index not in protected_lines
            and "|" in lines[next_index]
            and lines[next_index].strip()
        ):
            rows.append(lines[next_index])
            next_index += 1

        tables.append(
            (
                rows[0],
                len(rows),
                tuple(len(_split_table_cells(row)) for row in rows),
                _alignment_signature(rows[1]),
            )
        )
        index = next_index
    return tables


def extract_headings(text: str, protected_lines: set[int]) -> list[str]:
    return [
        line
        for index, line in enumerate(text.split("\n"))
        if index not in protected_lines and HEADING_RE.match(line)
    ]


def extract_list_signature(
    text: str, protected_lines: set[int]
) -> list[tuple[int, str]]:
    signature: list[tuple[int, str]] = []
    for index, line in enumerate(text.split("\n")):
        if index in protected_lines:
            continue
        match = LIST_RE.match(line)
        if match:
            indentation = len(match.group(1).expandtabs(4))
            signature.append((indentation, match.group(2)))
    return signature


def _term_pattern(terms: Sequence[str]) -> re.Pattern[str]:
    alternatives = sorted((re.escape(term) for term in terms), key=len, reverse=True)
    return re.compile(
        r"(?<![\w])(?:" + "|".join(alternatives) + r")(?![\w])",
        re.IGNORECASE,
    )


NEGATION_RE = _term_pattern(NEGATION_TERMS)
CONSTRAINT_RE = _term_pattern(CONSTRAINT_TERMS)


def extract_terms(text: str, pattern: re.Pattern[str]) -> Counter[str]:
    return Counter(
        re.sub(r"\s+", " ", match.group(0)).casefold()
        for match in pattern.finditer(text)
    )


def extract_numbers(text: str) -> Counter[str]:
    return Counter(match.group(0) for match in NUMBER_RE.finditer(text))


def _counter_delta(original: Counter[str], candidate: Counter[str]) -> str:
    lost = list((original - candidate).elements())
    added = list((candidate - original).elements())
    return f"lost={lost[:12]}, added={added[:12]}"


def _compare_sequence(
    report: ValidationReport,
    code: str,
    label: str,
    original: object,
    candidate: object,
) -> None:
    if original != candidate:
        report.add_error(code, f"{label} changed")


def _compare_counter(
    report: ValidationReport,
    code: str,
    label: str,
    original: Counter[str],
    candidate: Counter[str],
) -> None:
    if original != candidate:
        report.add_error(
            code,
            f"{label} changed: {_counter_delta(original, candidate)}",
        )


def validate_documents(
    source: Document, candidate: Document
) -> ValidationReport:
    ensure_distinct_files(source, candidate)
    report = ValidationReport()

    source_frontmatter, source_frontmatter_malformed = extract_frontmatter(source.text)
    candidate_frontmatter, candidate_frontmatter_malformed = extract_frontmatter(
        candidate.text
    )
    if source_frontmatter_malformed:
        report.add_error("SOURCE_FRONTMATTER", "source frontmatter is unclosed")
    if candidate_frontmatter_malformed:
        report.add_error("CANDIDATE_FRONTMATTER", "candidate frontmatter is unclosed")
    _compare_sequence(
        report,
        "FRONTMATTER",
        "frontmatter",
        source_frontmatter,
        candidate_frontmatter,
    )

    source_fences, source_protected, source_fences_malformed = extract_fenced_blocks(
        source.text
    )
    candidate_fences, candidate_protected, candidate_fences_malformed = (
        extract_fenced_blocks(candidate.text)
    )
    if source_fences_malformed:
        report.add_error("SOURCE_FENCE", "source contains an unclosed code fence")
    if candidate_fences_malformed:
        report.add_error("CANDIDATE_FENCE", "candidate contains an unclosed code fence")
    _compare_sequence(
        report,
        "FENCED_CODE",
        "fenced code blocks",
        source_fences,
        candidate_fences,
    )

    _compare_sequence(
        report,
        "INDENTED_CODE",
        "indented code lines",
        extract_indented_code(source.text, source_protected),
        extract_indented_code(candidate.text, candidate_protected),
    )

    source_inline, source_inline_malformed = extract_inline_code(
        source.text, source_protected
    )
    candidate_inline, candidate_inline_malformed = extract_inline_code(
        candidate.text, candidate_protected
    )
    if source_inline_malformed:
        report.add_error("SOURCE_INLINE_CODE", "source has unclosed inline code")
    if candidate_inline_malformed:
        report.add_error("CANDIDATE_INLINE_CODE", "candidate has unclosed inline code")
    _compare_sequence(
        report,
        "INLINE_CODE",
        "inline-code spans",
        source_inline,
        candidate_inline,
    )

    _compare_sequence(
        report,
        "HEADINGS",
        "heading text or order",
        extract_headings(source.text, source_protected),
        extract_headings(candidate.text, candidate_protected),
    )
    _compare_sequence(
        report,
        "TABLES",
        "table header or structure",
        extract_tables(source.text, source_protected),
        extract_tables(candidate.text, candidate_protected),
    )
    _compare_sequence(
        report,
        "LISTS",
        "list count, indentation, marker, or order",
        extract_list_signature(source.text, source_protected),
        extract_list_signature(candidate.text, candidate_protected),
    )

    _compare_counter(
        report,
        "URLS",
        "URLs",
        extract_urls(source.text),
        extract_urls(candidate.text),
    )
    _compare_counter(
        report,
        "LINK_TARGETS",
        "Markdown link destinations",
        extract_link_destinations(source.text),
        extract_link_destinations(candidate.text),
    )
    _compare_counter(
        report,
        "PATHS",
        "path-like tokens",
        extract_paths(source.text),
        extract_paths(candidate.text),
    )
    _compare_counter(
        report,
        "NEGATIONS",
        "negation phrases",
        extract_terms(source.text, NEGATION_RE),
        extract_terms(candidate.text, NEGATION_RE),
    )
    _compare_counter(
        report,
        "CONSTRAINTS",
        "condition or obligation phrases",
        extract_terms(source.text, CONSTRAINT_RE),
        extract_terms(candidate.text, CONSTRAINT_RE),
    )
    _compare_counter(
        report,
        "NUMBERS",
        "numeric literals",
        extract_numbers(source.text),
        extract_numbers(candidate.text),
    )

    source_words = len(re.findall(r"\S+", source.text))
    candidate_words = len(re.findall(r"\S+", candidate.text))
    source_chars = len(source.text)
    candidate_chars = len(candidate.text)
    word_ratio = candidate_words / source_words if source_words else 1.0
    char_ratio = candidate_chars / source_chars if source_chars else 1.0
    report.metrics = {
        "source_bytes": len(source.raw),
        "candidate_bytes": len(candidate.raw),
        "source_words": source_words,
        "candidate_words": candidate_words,
        "word_reduction_percent": round((1.0 - word_ratio) * 100.0, 2),
        "character_reduction_percent": round((1.0 - char_ratio) * 100.0, 2),
    }
    if source_words >= 80 and word_ratio < 0.35:
        report.add_warning(
            "AGGRESSIVE_REDUCTION",
            "candidate removed more than 65% of words; semantic review needs extra care",
        )
    if candidate_words >= source_words:
        report.add_warning(
            "NO_WORD_REDUCTION",
            "candidate does not reduce the source word count",
        )
    if source.text == candidate.text:
        report.add_warning("UNCHANGED", "candidate is identical to the source")

    return report


def build_unified_diff(
    source: Document, candidate: Document, max_lines: int
) -> tuple[str, bool]:
    lines = list(
        difflib.unified_diff(
            source.text.splitlines(),
            candidate.text.splitlines(),
            fromfile=str(source.path),
            tofile=str(candidate.path),
            lineterm="",
        )
    )
    truncated = len(lines) > max_lines
    if truncated:
        omitted = len(lines) - max_lines
        lines = lines[:max_lines] + [f"... diff truncated; {omitted} lines omitted ..."]
    return "\n".join(lines), truncated


def inspect_document(source: Document) -> dict[str, object]:
    fences, protected, malformed = extract_fenced_blocks(source.text)
    inline, inline_malformed = extract_inline_code(source.text, protected)
    frontmatter, frontmatter_malformed = extract_frontmatter(source.text)
    return {
        "mode": "inspect",
        "source": str(source.path),
        "source_sha256": sha256_bytes(source.raw),
        "source_bytes": len(source.raw),
        "frontmatter": frontmatter is not None,
        "frontmatter_malformed": frontmatter_malformed,
        "fenced_code_blocks": len(fences),
        "fenced_code_malformed": malformed,
        "inline_code_spans": len(inline),
        "inline_code_malformed": inline_malformed,
        "urls": sum(extract_urls(source.text).values()),
        "paths": sum(extract_paths(source.text).values()),
        "tables": len(extract_tables(source.text, protected)),
        "list_items": len(extract_list_signature(source.text, protected)),
        "negations": sum(extract_terms(source.text, NEGATION_RE).values()),
        "constraints": sum(extract_terms(source.text, CONSTRAINT_RE).values()),
        "numeric_literals": sum(extract_numbers(source.text).values()),
    }


def preview(
    source: Document, candidate: Document, max_diff_lines: int
) -> dict[str, object]:
    report = validate_documents(source, candidate)
    diff, truncated = build_unified_diff(source, candidate, max_diff_lines)
    return {
        "mode": "preview",
        "source_unchanged": True,
        "source": str(source.path),
        "candidate": str(candidate.path),
        "source_sha256": sha256_bytes(source.raw),
        "candidate_sha256": sha256_bytes(candidate.raw),
        "validation": report.to_dict(),
        "diff_truncated": truncated,
        "diff": diff,
    }


def _encode_candidate_for_source(source: Document, candidate: Document) -> bytes:
    normalized = candidate.text
    if source.newline == "\r\n":
        normalized = normalized.replace("\n", "\r\n")
    payload = normalized.encode("utf-8")
    return codecs.BOM_UTF8 + payload if source.has_bom else payload


def _new_backup_path(source: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    suffix = source.suffix
    base = source.name[: -len(suffix)] if suffix else source.name
    candidate = source.with_name(f"{base}{BACKUP_MARKER}{stamp}{suffix}")
    counter = 1
    while candidate.exists():
        candidate = source.with_name(
            f"{base}{BACKUP_MARKER}{stamp}-{counter}{suffix}"
        )
        counter += 1
    return candidate


def _assert_hash(label: str, actual: str, expected: str | None) -> None:
    if not expected:
        raise SafetyError(f"{label} hash from preview is required")
    if not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
        raise SafetyError(f"{label} hash must be 64 hexadecimal characters")
    if actual.casefold() != expected.casefold():
        raise SafetyError(f"{label} changed after preview; run preview again")


def apply_candidate(
    source: Document,
    candidate: Document,
    *,
    user_approved: bool,
    expected_source_sha256: str | None,
    expected_candidate_sha256: str | None,
) -> dict[str, object]:
    if not user_approved:
        raise SafetyError(
            "write blocked: explicit user approval flag --user-approved-write is required"
        )
    ensure_distinct_files(source, candidate)
    source_hash = sha256_bytes(source.raw)
    candidate_hash = sha256_bytes(candidate.raw)
    _assert_hash("source", source_hash, expected_source_sha256)
    _assert_hash("candidate", candidate_hash, expected_candidate_sha256)

    report = validate_documents(source, candidate)
    if not report.is_valid:
        codes = ", ".join(item.code for item in report.errors)
        raise SafetyError(f"write blocked by invariant failures: {codes}")

    _assert_hash("source", sha256_file(source.path), expected_source_sha256)
    _assert_hash("candidate", sha256_file(candidate.path), expected_candidate_sha256)

    backup_path = _new_backup_path(source.path)
    shutil.copy2(source.path, backup_path)

    temp_path: Path | None = None
    try:
        _assert_hash("source", sha256_file(source.path), expected_source_sha256)
        _assert_hash("candidate", sha256_file(candidate.path), expected_candidate_sha256)
        replacement = _encode_candidate_for_source(source, candidate)
        with tempfile.NamedTemporaryFile(
            mode="wb",
            prefix=f".{source.path.name}.caveman-",
            suffix=".tmp",
            dir=source.path.parent,
            delete=False,
        ) as handle:
            temp_path = Path(handle.name)
            handle.write(replacement)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp_path, source.mode)

        _assert_hash("source", sha256_file(source.path), expected_source_sha256)
        _assert_hash("candidate", sha256_file(candidate.path), expected_candidate_sha256)
        os.replace(temp_path, source.path)
        temp_path = None
    except Exception:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
        raise

    final_hash = sha256_file(source.path)
    return {
        "mode": "apply",
        "applied": True,
        "source": str(source.path),
        "backup": str(backup_path),
        "source_sha256_before": source_hash,
        "candidate_sha256": candidate_hash,
        "source_sha256_after": final_hash,
        "validation": report.to_dict(),
    }


def _print_findings(title: str, findings: Iterable[dict[str, str]]) -> None:
    items = list(findings)
    if not items:
        return
    print(f"{title}:")
    for item in items:
        print(f"  - {item['code']}: {item['message']}")


def print_human(payload: dict[str, object]) -> None:
    mode = payload["mode"]
    if mode == "inspect":
        print("Mode: INSPECT (read-only)")
        for key, value in payload.items():
            if key != "mode":
                print(f"{key}: {value}")
        return

    if mode == "preview":
        print("Mode: PREVIEW (source unchanged)")
        print(f"Source: {payload['source']}")
        print(f"Candidate: {payload['candidate']}")
        print(f"Source SHA256: {payload['source_sha256']}")
        print(f"Candidate SHA256: {payload['candidate_sha256']}")
        validation = payload["validation"]
        assert isinstance(validation, dict)
        print(f"Validation: {'PASS' if validation['valid'] else 'FAIL'}")
        _print_findings("Errors", validation["errors"])
        _print_findings("Warnings", validation["warnings"])
        print("Metrics:")
        for key, value in validation["metrics"].items():
            print(f"  {key}: {value}")
        print("Unified diff:")
        print(payload["diff"] or "(no changes)")
        print("Write remains blocked until explicit user approval.")
        return

    print("Mode: APPLY")
    print(f"Applied: {payload['source']}")
    print(f"Backup: {payload['backup']}")
    print(f"Final SHA256: {payload['source_sha256_after']}")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate and preview a provider-neutral text-compression candidate."
    )
    parser.add_argument("source", help="UTF-8 Markdown or plain-text source")
    parser.add_argument(
        "--candidate",
        help="separate UTF-8 candidate file; omission performs inspect only",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="replace source after all safety gates; preview is the default",
    )
    parser.add_argument(
        "--user-approved-write",
        action="store_true",
        help="attest that the user explicitly approved this exact overwrite",
    )
    parser.add_argument("--expected-source-sha256")
    parser.add_argument("--expected-candidate-sha256")
    parser.add_argument(
        "--max-diff-lines",
        type=int,
        default=400,
        help="maximum unified-diff lines shown in preview (default: 400)",
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.max_diff_lines < 20:
            raise SafetyError("--max-diff-lines must be at least 20")
        source = load_document(args.source, source=True)
        if not args.candidate:
            if args.apply:
                raise SafetyError("--apply requires --candidate")
            payload = inspect_document(source)
        else:
            candidate = load_document(args.candidate, source=False)
            ensure_distinct_files(source, candidate)
            if args.apply:
                payload = apply_candidate(
                    source,
                    candidate,
                    user_approved=args.user_approved_write,
                    expected_source_sha256=args.expected_source_sha256,
                    expected_candidate_sha256=args.expected_candidate_sha256,
                )
            else:
                payload = preview(source, candidate, args.max_diff_lines)

        if args.as_json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print_human(payload)

        if payload["mode"] == "preview":
            validation = payload["validation"]
            assert isinstance(validation, dict)
            return 0 if validation["valid"] else 2
        return 0
    except SafetyError as exc:
        if args.as_json:
            print(
                json.dumps(
                    {"mode": "blocked", "error": str(exc)},
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(f"Blocked: {exc}", file=sys.stderr)
        return 3
    except OSError as exc:
        if args.as_json:
            print(
                json.dumps(
                    {"mode": "error", "error": str(exc)},
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
