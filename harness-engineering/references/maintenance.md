# Maintenance

Use this reference after feature work, after release, or when the project shows
signs of drift.

For recurring entropy scans, golden principles, quality score gardening, or
targeted cleanup PRs, use `$entropy-gc`. Keep this reference for general
maintenance routing; let `$entropy-gc` own the garbage-collection loop.

## Maintenance loop

1. Inspect drift.
2. Rank risk by user impact and agent confusion.
3. Fix small items immediately.
4. Turn recurring issues into harness improvements.
5. Update the quality score and docs.

## Drift signals

Look for:

- `AGENTS.md` that no longer points to the right commands or docs.
- Specs that describe old behavior.
- Architecture docs that do not match imports or runtime boundaries.
- Multiple helpers that solve the same problem differently.
- Tests that pass while important user journeys are untested.
- Logs that exist but do not help diagnose failures.
- Bug reports that cannot be reproduced from repo-local instructions.
- Product or domain decisions that exist only in chats, external docs, or
  people's heads.
- Runtime behavior that cannot be inspected through UI, logs, metrics, traces,
  or reproducible seed data.
- Review comments that repeat across PRs.

## Documentation gardening

Run a regular pass over docs:

- Delete stale placeholders.
- Update links and command names.
- Move durable decisions out of chats into docs.
- Promote external-only domain knowledge into repo-local artifacts.
- Keep generated artifacts separate from authored docs.
- Ensure active plans are still active.
- Archive completed plans with outcome notes.

Do not expand `AGENTS.md` for every detail. Add links from `AGENTS.md` to the
right detailed document.

## Architecture gardening

Run or add checks for:

- Forbidden imports.
- Circular dependencies.
- Boundary-crossing calls.
- Domain terms that have multiple names.
- Domain workflows or invariants that are only implied by code.
- Shared utilities that hide business logic.
- Oversized files that harm review or agent context.

When a check cannot be automated yet, document the invariant and add a manual
review checklist until automation is practical.

## Quality score

Keep `docs/QUALITY_SCORE.md` short and current. Score each domain or major
surface on:

- Test confidence.
- Runtime observability.
- Agent readability of domain docs and navigation.
- App readability of UI, logs, metrics, traces, and local instances.
- Documentation freshness.
- Architecture fit.
- Security and privacy risk.
- Known debt and next action.

Scores are useful only when they lead to action. Include the next smallest
improvement for each weak area.

## Bug aftermath

After fixing a bug, ask:

- Which missing test would have caught this?
- Which doc or spec misled the agent?
- Which log, metric, or trace would have shortened diagnosis?
- Which UI/runtime evidence would have let an agent verify the fix without
  human QA?
- Which repo-local doc should have contained the missing domain knowledge?
- Which architecture rule was absent or unenforced?
- Which command should reproduce this failure next time?

Add the smallest durable harness improvement that answers one of those
questions.
