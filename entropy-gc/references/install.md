# Install

Use this reference when adding a recurring entropy GC loop to a repository.

## Install goal

Install the smallest repo-local loop that can find drift, rank it, and create
small cleanup work. Do not add a schedule until the repo has a useful scan or
check to run.

## Minimal loop

Start with these artifacts:

1. `docs/golden-principles.md`: opinionated anti-drift rules.
2. `docs/tech-debt-tracker.md`: known debt, owner or area, next action.
3. `docs/QUALITY_SCORE.md`: current quality by domain or surface.
4. `scripts/scan-entropy`: project-local wrapper around scans and checks.

If the repo already has equivalent artifacts, update those instead of adding
new names.

## Scan wrapper

Create a repo-local command that agents can run without remembering skill paths:

```text
scripts/scan-entropy
```

The wrapper may call:

- The bundled `entropy_scan.py`.
- Existing lint, type, architecture, docs, or test commands.
- Repo-specific checks for forbidden imports, stale generated docs, or quality
  score coverage.

Keep the wrapper read-only by default. Cleanup should happen in explicit collect
tasks, not hidden inside scans.

## Quality score

Track only scores that lead to action:

- Domain or surface.
- Current confidence.
- Evidence used.
- Top entropy risk.
- Next smallest cleanup.
- Last updated date.

Do not create a scorecard that is only decorative.

## Golden principles

Load `references/golden-principles.md` before writing the first principles file.
Start with three to seven rules. Each rule needs an enforcement path:

- Existing test or script.
- Planned check.
- Manual review checklist.
- Reason enforcement is not practical yet.

## Automation threshold

Add scheduled automation only after:

- `scripts/scan-entropy` runs locally.
- The output is stable enough to review.
- False positives have a place to be recorded.
- The team knows what should happen when findings appear.

Use `references/schedule.md` for cadence and CI guidance.
