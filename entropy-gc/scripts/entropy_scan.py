#!/usr/bin/env python3
"""Conservative repository entropy scanner.

The scanner reports signals that deserve inspection. It does not decide that a
finding is wrong or safe to refactor.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


DEFAULT_IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".next",
    ".nuxt",
    ".pytest_cache",
    ".ruff_cache",
    ".turbo",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "target",
    "vendor",
    "venv",
}

SELF_SKILL_PARTS = (".agents", "skills", "entropy-gc")
SEVERITY_ORDER = {"high": 0, "medium": 1, "low": 2}

TEXT_EXTENSIONS = {
    ".c",
    ".cc",
    ".cs",
    ".css",
    ".go",
    ".h",
    ".hpp",
    ".html",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".kt",
    ".md",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".scss",
    ".swift",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}

MARKER_RE = re.compile(
    r"\b(TODO|FIXME|HACK|XXX|TEMP|WORKAROUND|COPYPASTE|DEPRECATED)\b",
    re.IGNORECASE,
)
ESCAPE_HATCH_RE = re.compile(
    r"(as\s+any|@ts-ignore|@ts-expect-error|eslint-disable|type:\s*ignore|"
    r"pragma:\s*no\s*cover|noqa\b)",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(
    r"\b(TODO|TBD|coming soon|placeholder|fill this in|not documented)\b",
    re.IGNORECASE,
)
HELPER_STEM_RE = re.compile(
    r"(helper|helpers|util|utils|common|shared|adapter|parser|formatter|"
    r"mapper|client|service|constants?)",
    re.IGNORECASE,
)


@dataclass
class Finding:
    category: str
    severity: str
    path: str
    detail: str
    line: int | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan a repo for conservative entropy signals.",
    )
    parser.add_argument(
        "repo",
        nargs="?",
        default=".",
        help="Repository path to scan. Defaults to current directory.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of Markdown.",
    )
    parser.add_argument(
        "--large-file-lines",
        type=int,
        default=500,
        help="Line threshold for large source or doc files.",
    )
    parser.add_argument(
        "--max-findings",
        type=int,
        default=120,
        help="Maximum detailed findings to emit.",
    )
    parser.add_argument(
        "--fail-on-findings",
        action="store_true",
        help="Exit with status 2 when any finding exists.",
    )
    return parser.parse_args()


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS


def iter_files(root: Path) -> Iterable[Path]:
    for current_root, dirs, files in os.walk(root):
        current_path = Path(current_root)
        if contains_sequence(current_path.parts, SELF_SKILL_PARTS):
            dirs[:] = []
            continue
        dirs[:] = [
            d for d in dirs
            if d not in DEFAULT_IGNORE_DIRS and not d.startswith(".git")
        ]
        for name in files:
            path = Path(current_root) / name
            if is_text_file(path):
                yield path


def contains_sequence(parts: tuple[str, ...], sequence: tuple[str, ...]) -> bool:
    lowered = tuple(part.lower() for part in parts)
    target = tuple(part.lower() for part in sequence)
    for index in range(0, len(lowered) - len(target) + 1):
        if lowered[index:index + len(target)] == target:
            return True
    return False


def relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def read_lines(path: Path) -> list[str]:
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8-sig").splitlines()
        except UnicodeDecodeError:
            return []
    except OSError:
        return []


def scan_file(root: Path, path: Path, large_file_lines: int) -> list[Finding]:
    rel = relative(root, path)
    lines = read_lines(path)
    findings: list[Finding] = []

    if len(lines) > large_file_lines:
        findings.append(
            Finding(
                "large-file",
                "medium",
                rel,
                f"{len(lines)} lines; review ownership and split points",
            )
        )

    for number, line in enumerate(lines, start=1):
        marker = MARKER_RE.search(line)
        if marker:
            findings.append(
                Finding(
                    "marker",
                    "low",
                    rel,
                    marker.group(0),
                    number,
                )
            )

        escape = ESCAPE_HATCH_RE.search(line)
        if escape:
            findings.append(
                Finding(
                    "escape-hatch",
                    "medium",
                    rel,
                    escape.group(0),
                    number,
                )
            )

        if path.suffix.lower() == ".md":
            placeholder = PLACEHOLDER_RE.search(line)
            if placeholder:
                findings.append(
                    Finding(
                        "doc-placeholder",
                        "medium",
                        rel,
                        placeholder.group(0),
                        number,
                    )
                )

    return findings


def duplicate_helper_findings(root: Path, files: list[Path]) -> list[Finding]:
    by_stem: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        stem = path.stem.lower()
        if HELPER_STEM_RE.search(stem):
            normalized = re.sub(r"[-_\d]+", "", stem)
            by_stem[normalized].append(path)

    findings: list[Finding] = []
    for stem, paths in sorted(by_stem.items()):
        if len(paths) < 3:
            continue
        examples = ", ".join(relative(root, p) for p in paths[:6])
        extra = "" if len(paths) <= 6 else f", +{len(paths) - 6} more"
        findings.append(
            Finding(
                "repeated-helper-name",
                "medium",
                ".",
                f"{stem}: {examples}{extra}",
            )
        )
    return findings


def missing_harness_findings(root: Path) -> list[Finding]:
    expected = [
        "AGENTS.md",
        "ARCHITECTURE.md",
        "docs/QUALITY_SCORE.md",
        "docs/tech-debt-tracker.md",
    ]
    findings: list[Finding] = []
    for rel in expected:
        if not (root / rel).exists():
            findings.append(
                Finding(
                    "missing-harness-artifact",
                    "low",
                    rel,
                    "missing common entropy-GC artifact",
                )
            )
    return findings


def git_status_findings(root: Path) -> list[Finding]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "status", "--short"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return []

    if result.returncode != 0:
        return []

    untracked_dirs = []
    for line in result.stdout.splitlines():
        if line.startswith("?? ") and line.endswith("/"):
            untracked_dirs.append(line[3:])

    if not untracked_dirs:
        return []

    detail = ", ".join(untracked_dirs[:8])
    if len(untracked_dirs) > 8:
        detail += f", +{len(untracked_dirs) - 8} more"
    return [
        Finding(
            "untracked-directories",
            "low",
            ".",
            detail,
        )
    ]


def summarize(findings: list[Finding]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for finding in findings:
        counts[finding.category] += 1
    return dict(sorted(counts.items()))


def to_markdown(root: Path, findings: list[Finding], max_findings: int) -> str:
    counts = summarize(findings)
    lines = [
        "# Entropy scan report",
        "",
        f"Repo: `{root}`",
        f"Findings: {len(findings)}",
        "",
        "## Summary",
        "",
    ]
    if counts:
        for category, count in counts.items():
            lines.append(f"- {category}: {count}")
    else:
        lines.append("- No conservative entropy signals found.")

    lines.extend(["", "## Findings", ""])
    for finding in findings[:max_findings]:
        location = finding.path
        if finding.line is not None:
            location += f":{finding.line}"
        lines.append(
            f"- [{finding.severity}] {finding.category} `{location}`: "
            f"{finding.detail}"
        )

    if len(findings) > max_findings:
        lines.append("")
        lines.append(f"... truncated {len(findings) - max_findings} findings")

    lines.extend(
        [
            "",
            "## Next step",
            "",
            "Inspect the highest-risk finding, confirm it is real, then choose "
            "one small cleanup slice with validation and a recurrence guardrail.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.repo).resolve()
    if not root.exists():
        print(f"Repo path does not exist: {root}", file=sys.stderr)
        return 1

    files = list(iter_files(root))
    findings: list[Finding] = []
    for path in files:
        findings.extend(scan_file(root, path, args.large_file_lines))
    findings.extend(duplicate_helper_findings(root, files))
    findings.extend(missing_harness_findings(root))
    findings.extend(git_status_findings(root))

    findings.sort(
        key=lambda f: (
            SEVERITY_ORDER.get(f.severity, 99),
            f.category,
            f.path,
            f.line or 0,
        )
    )

    if args.json:
        payload = {
            "repo": str(root),
            "summary": summarize(findings),
            "findings": [asdict(f) for f in findings[: args.max_findings]],
            "truncated": max(0, len(findings) - args.max_findings),
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(to_markdown(root, findings, args.max_findings))

    if findings and args.fail_on_findings:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
