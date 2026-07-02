---
name: entropy-gc
description: >-
  Use when a repository shows entropy, drift, stale docs, duplicated helpers,
  divergent patterns, repeated review feedback, quality debt, stale plans, or
  when installing recurring cleanup, golden principles, quality scoring,
  scheduled audits, or targeted refactor PR workflows.
---

# Entropy GC

## Overview

Entropy GC keeps agent-heavy repositories legible by turning repeated cleanup
work into repo-local checks, quality scores, and small targeted refactor slices.
The skill does not run as a scheduler by itself. It helps Codex install and run
the repository mechanisms that make recurring cleanup observable and reviewable.

The core loop is:

1. Capture golden principles in versioned repo artifacts.
2. Scan for deviations and drift signals.
3. Rank findings by user risk and agent confusion.
4. Fix one small, high-signal slice.
5. Promote recurring findings into docs, tests, scripts, lint, or CI.
6. Update quality scores, debt trackers, and the next scheduled check.

## Choose the workflow

Read only the reference that matches the current task. Load another reference
only when the work explicitly needs it.

| Situation | Read |
| --- | --- |
| Need a drift map or entropy report | `references/audit.md` |
| Need to install a recurring GC loop in a repo | `references/install.md` |
| Need to perform one cleanup or refactor slice | `references/collect.md` |
| Need cadence, CI, cron, or scheduler guidance | `references/schedule.md` |
| Need to define repo taste and anti-drift rules | `references/golden-principles.md` |

For a quick mechanical scan, run:

```text
python .agents/skills/entropy-gc/scripts/entropy_scan.py <repo>
```

Treat script output as evidence, not truth. Confirm findings against the code
and project intent before changing behavior.

## Operating rules

- Prefer small, reviewable cleanup PRs over broad rewrites.
- Fix at most one to three related entropy findings per slice.
- Do not change user behavior during cleanup unless the plan and tests make the
  behavior change explicit.
- Convert repeated review feedback into a guardrail. A recurring comment should
  become a doc, test, script, lint rule, architecture check, or CI gate.
- Keep cleanup work repo-local. The durable truth belongs in versioned docs,
  scripts, checks, and quality trackers.
- Do not rely only on static scans. Use tests, runtime inspection, logs, or
  review when the cleanup touches behavior.
- Record false positives and tune the scanner or checklist rather than ignoring
  the same noise repeatedly.
- Leave a handoff or PR note with findings, chosen slice, validation, and
  remaining debt.

## Default repo artifacts

Create or improve only the artifacts the repo needs:

```text
docs/
  golden-principles.md
  QUALITY_SCORE.md
  tech-debt-tracker.md
scripts/
  scan-entropy
  check-architecture
  check-docs
.github/workflows/
  entropy-gc.yml
```

Adapt names to local conventions. Start with an audit and one actionable next
step before adding scheduled automation.

## Common mistakes

- Running a broad cleanup without a ranked report.
- Treating scanner warnings as automatic truth.
- Opening a giant refactor PR that mixes unrelated concerns.
- Fixing drift once without adding a guardrail for recurrence.
- Creating a schedule before the repo has useful checks to run.
- Updating quality scores without recording the next action.
- Deleting or moving code before understanding its public behavior.
