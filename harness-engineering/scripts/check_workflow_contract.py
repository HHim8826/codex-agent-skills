#!/usr/bin/env python3
"""Validate mandatory workflow links in the harness-engineering skill."""

from pathlib import Path
import sys


REQUIRED_TEXT = {
    "SKILL.md": (
        "description: >-",
        "agent/app readability",
        "sub-agent review",
        "validation, handoff",
        "## Mandatory Git finalization",
        "load `references/git-checkpoints.md` before the first edit",
        "Do not claim completion while task-owned changes remain",
        "## Mandatory zero-start planning interview",
        "load `references/zero-to-harness.md`",
        "Do not require the user to invoke `$grill-me` separately",
        "## Mandatory review gate",
        "load `references/review-loop.md` before finalization",
        "Use an available sub-agent or review tool when policy and permissions allow",
        "Do not call the task complete until important review findings are fixed",
        "## Mandatory recoverability check",
        "Load `references/handoff.md` and create or update the handoff",
        "If no handoff is written",
    ),
    "references/zero-to-harness.md": (
        "## Built-in planning interview",
        "Draft a provisional harness-aware plan",
        "ask exactly one unresolved decision question at a time",
        "**Recommended answer:**",
        "tradeoff",
        "decision the answer unlocks",
        "Do not start implementation",
        "skip the interview",
        "no unresolved decisions",
        "approves the finalized plan",
        "artifact trigger rubric",
    ),
    "references/feature-development.md": (
        "record the starting HEAD and dirty",
        "## Feature completion gate",
        "commit was actually attempted and failed",
        "Run the review loop for every non-trivial change",
        "Record whether independent review was required",
        "## Recoverability check",
    ),
    "references/quality-gates.md": (
        "## Finalization gate",
        "Task-owned changes are committed",
        "Do not claim completion when step 3 was skipped",
        "Recoverability is handled by a short handoff",
        "Whether independent review was required",
        "## Recoverability gate",
    ),
    "references/git-checkpoints.md": (
        "## Completion gate",
        "Never describe a commit as",
        "missing remote or upstream is used as a reason to skip a local commit",
    ),
    "agents/openai.yaml": (
        "mandatory Git",
        "exact attempted commit blocker",
        "built-in one-question-at-a-time planning interview",
        "mandatory review gates",
        "recoverability checks",
        "Report independent review status",
    ),
    "references/planning-output-contract.md": (
        "## Artifact trigger rubric",
        "What future agent decision or validation step fails without this artifact?",
        "Do not create empty placeholder artifacts",
        "use the same one-question-at-a-time contract rather than running a second interview",
        "persist the appropriate artifact",
    ),
    "references/review-loop.md": (
        "independent review is part of the completion gate",
        "## Independent review requirement",
        "Use a sub-agent or review tool when policy and permissions allow",
        "The exact reason independent review was skipped or unavailable",
        "Which self-review passes were run instead",
    ),
    "references/handoff.md": (
        "## Recoverability check",
        "Load this reference and create or update a short handoff",
        "If no handoff is written",
        "Do not create empty handoff files just to satisfy the catalog",
    ),
}

PROHIBITED_TEXT = {
    "SKILL.md": (
        "agent/appreadability",
        "validation,handoff",
        "standard skill structure validator",
    ),
}


def main() -> int:
    skill_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for relative_path, required_fragments in REQUIRED_TEXT.items():
        path = skill_root / relative_path
        if not path.is_file():
            errors.append(f"missing file: {relative_path}")
            continue

        content = path.read_text(encoding="utf-8")
        normalized_content = " ".join(content.split())
        for fragment in required_fragments:
            normalized_fragment = " ".join(fragment.split())
            if normalized_fragment not in normalized_content:
                errors.append(f"{relative_path}: missing contract text: {fragment}")

        for fragment in PROHIBITED_TEXT.get(relative_path, ()):
            normalized_fragment = " ".join(fragment.split())
            if normalized_fragment in normalized_content:
                errors.append(f"{relative_path}: prohibited stale text: {fragment}")

    if errors:
        print("Harness workflow contract is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Harness workflow contract is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
