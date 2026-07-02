# Project lifecycle

Use this reference when planning how harness work changes across project stages.

## Kickoff

At kickoff, reduce ambiguity before optimizing speed.

- Write the product mission, target user, first user journey, and non-goals.
- Define the smallest architecture with explicit dependency direction.
- Add setup, local run, test, and validation commands.
- Create a place for active execution plans and completed plans.
- Decide what must be true before a PR can be called done.

Avoid premature infrastructure. Add only what helps agents understand, run,
verify, or safely change the project.

## Early development

In early development, make agents successful on small vertical slices.

- Keep features narrow and end-to-end.
- Prefer mocks, providers, and seed data over unavailable external services.
- Add tests around the first real user journeys.
- Write docs when terms, boundaries, or decisions appear.
- Record why rejected approaches were rejected when the tradeoff will recur.

Good early prompts mention the exact slice, constraints, docs to update, and
validation commands to run.

## Middle development

In middle development, convert taste and review feedback into enforceable
rules.

- Add architecture checks for forbidden imports and boundary violations.
- Add lint or tests for repeated code review comments.
- Standardize error handling, data validation, logging, and naming.
- Keep generated docs separate from human-authored design docs.
- Add browser or runtime verification for important flows.
- Split large files when context size hurts agent reliability.

This stage is where the harness begins to compound. Do not repeat the same
manual review comment three times; encode it.

## Late development

In late development, focus on full-loop verification.

- Ensure each branch or worktree can run independently.
- Add realistic seed data and reset commands.
- Make logs, metrics, traces, or structured diagnostics queryable.
- Require before/after screenshots or browser checks for visual changes.
- Document rollback, migration, and operational risk for risky PRs.
- Track quality by domain, not only by global test count.

The agent should be able to reproduce a bug, inspect runtime evidence, change
code, rerun validation, and explain the evidence for the fix.

## After release

After release, the harness protects the project from decay.

- Schedule docs and architecture gardening.
- Remove or update stale execution plans.
- Search for duplicated helpers and divergent patterns.
- Upgrade repeated review findings into scripts, tests, or docs.
- Keep `QUALITY_SCORE.md` honest and action-oriented.
- Revisit `AGENTS.md` only when navigation or top-level rules change.

Maintenance is not separate from harness engineering. It is the feedback loop
that keeps future agent work reliable.
