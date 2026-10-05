#!/usr/bin/env python3
"""Small, local stylometry helper for consented writing samples.

This measures mechanical text signals. It does not identify authors, infer traits,
or decide whether two texts have the same author.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


WORD_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)?", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?])(?:[\"'”’»)]*)\s+|\n{2,}")
PARAGRAPH_RE = re.compile(r"\n\s*\n+")
PUNCTUATION = {
    "comma": ",",
    "semicolon": ";",
    "colon": ":",
    "dash": "—",
    "hyphen": "-",
    "ellipsis": "…",
    "exclamation": "!",
    "question": "?",
}


def read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "utf-16", "cp1254", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def split_sentences(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_RE.split(text) if WORD_RE.search(part)]


def safe_mean(values: list[float]) -> float:
    return round(statistics.mean(values), 2) if values else 0.0


def analyze_text(text: str) -> dict[str, Any]:
    words = [word.casefold() for word in WORD_RE.findall(text)]
    sentences = split_sentences(text)
    paragraphs = [part.strip() for part in PARAGRAPH_RE.split(text.strip()) if WORD_RE.search(part)]
    counts = Counter(words)
    word_count = len(words)
    sentence_lengths = [len(WORD_RE.findall(sentence)) for sentence in sentences]
    paragraph_lengths = [len(WORD_RE.findall(paragraph)) for paragraph in paragraphs]
    punctuation_per_100 = {
        label: round((text.count(char) * 100 / word_count), 2) if word_count else 0.0
        for label, char in PUNCTUATION.items()
    }
    frequent_words = [
        {"word": word, "count": count}
        for word, count in counts.most_common(12)
        if len(word) > 2
    ]
    return {
        "characters": len(text),
        "words": word_count,
        "sentences": len(sentences),
        "paragraphs": len(paragraphs),
        "unique_words": len(counts),
        "lexical_diversity": round(len(counts) / word_count, 3) if word_count else 0.0,
        "average_word_length": round(safe_mean([len(word) for word in words]), 2),
        "average_sentence_words": safe_mean(sentence_lengths),
        "sentence_length_spread": round(statistics.pstdev(sentence_lengths), 2) if len(sentence_lengths) > 1 else 0.0,
        "average_paragraph_words": safe_mean(paragraph_lengths),
        "punctuation_per_100_words": punctuation_per_100,
        "frequent_nontrivial_words": frequent_words,
        "confidence_note": confidence_note(word_count, len(sentences)),
    }


def confidence_note(words: int, sentences: int) -> str:
    if words < 150 or sentences < 8:
        return "Low confidence: the sample is small; use only as a rough signal."
    if words < 500:
        return "Moderate confidence: compare more than one representative sample before forming a profile."
    return "Mechanical signals are reasonably stable, but content, audience, language, and editing can still dominate them."


def compare_metrics(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    numeric_keys = (
        "average_word_length",
        "average_sentence_words",
        "sentence_length_spread",
        "average_paragraph_words",
        "lexical_diversity",
    )
    differences = {
        key: round(abs(float(left[key]) - float(right[key])), 3)
        for key in numeric_keys
    }
    punctuation_differences = {
        key: round(
            abs(
                float(left["punctuation_per_100_words"][key])
                - float(right["punctuation_per_100_words"][key])
            ),
            3,
        )
        for key in PUNCTUATION
    }
    return {
        "mechanical_differences": differences,
        "punctuation_differences_per_100_words": punctuation_differences,
        "interpretation": (
            "These are mechanical differences, not authorship evidence. Compare samples with similar language, audience, and format."
        ),
    }


def print_human(label: str, result: dict[str, Any]) -> None:
    print(label)
    for key in (
        "characters",
        "words",
        "sentences",
        "paragraphs",
        "unique_words",
        "lexical_diversity",
        "average_word_length",
        "average_sentence_words",
        "sentence_length_spread",
        "average_paragraph_words",
    ):
        print(f"  {key}: {result[key]}")
    print("  punctuation_per_100_words:")
    for key, value in result["punctuation_per_100_words"].items():
        print(f"    {key}: {value}")
    print(f"  confidence: {result['confidence_note']}")


def run_selftest() -> int:
    sample_a = "Merhaba dünya. Bu kısa bir örnek metindir.\n\nİkinci paragraf daha uzundur, fakat ölçülebilir kalır."
    sample_b = "Merhaba! Bu başka bir örnek mi? Evet, daha kısa cümleler kullanır."
    a = analyze_text(sample_a)
    b = analyze_text(sample_b)
    comparison = compare_metrics(a, b)
    assert a["words"] > 5
    assert a["sentences"] >= 2
    assert "comma" in a["punctuation_per_100_words"]
    assert "mechanical_differences" in comparison
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "sample.txt"
        path.write_text(sample_a, encoding="utf-8")
        assert read_text(path).startswith("Merhaba")
    print("selftest OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Local, consented stylometry helper.")
    parser.add_argument("files", nargs="*", help="One file to analyze or two files to compare.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of a readable summary.")
    parser.add_argument("--selftest", action="store_true", help="Run a harmless built-in test.")
    args = parser.parse_args()

    if args.selftest:
        return run_selftest()
    if len(args.files) not in (1, 2):
        parser.error("provide one authorized text file to analyze or two to compare")

    paths = [Path(value).expanduser() for value in args.files]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        parser.error("file not found: " + ", ".join(missing))

    results = {str(path): analyze_text(read_text(path)) for path in paths}
    payload: dict[str, Any] = {"samples": results}
    if len(paths) == 2:
        payload["comparison"] = compare_metrics(results[str(paths[0])], results[str(paths[1])])

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    for path in paths:
        print_human(str(path), results[str(path)])
    if "comparison" in payload:
        print("comparison:")
        print(json.dumps(payload["comparison"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
