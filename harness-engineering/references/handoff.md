# Handoff

Use this reference when work may continue in a later chat or with another
agent. This is especially useful when conversations end every few tasks.

## Core rule

Every task needs recoverability. Only durable knowledge needs formal
documentation.

Write a short handoff at task boundaries when there is useful state that is not
obvious from committed docs and code. Keep it short enough for the next agent to
read immediately.

## Default location

Use the repo convention if it exists. Otherwise use:

```text
docs/exec-plans/active/session-handoff.md
```

## Template

```markdown
# Session handoff

## Current state
- Done:
- In progress:
- Blocked:

## Files changed
- path: reason

## Decisions
- decision:
- reason:

## Next task
- recommended next step:
- validation needed:

## Git checkpoint
- branch:
- last commit:
- pushed:
- push blocker:
- uncommitted changes:

## Runtime evidence
- app URL:
- seed/reset state:
- browser evidence:
- logs/metrics/traces:
```

## What belongs here

- Current state that is not obvious from docs.
- Incomplete work and blockers.
- Files changed and why.
- Decisions not yet promoted to durable docs.
- Next recommended validation command.
- Current branch, last checkpoint commit, push status, and uncommitted changes
  when git state matters for continuation.
- Exact push blocker when direct push was expected but did not happen.
- App URL, seed/reset state, browser evidence, or log/metric/trace evidence
  when runtime behavior matters for continuation.

## What does not belong here

- Full chat transcript.
- Low-value command logs.
- Details obvious from the diff.
- Long-term architecture decisions that belong in `ARCHITECTURE.md`.
- Product behavior that belongs in `docs/product-specs/`.

## Promotion rule

At the end of every few tasks, scan the handoff and promote durable knowledge
into formal docs. Delete or shorten stale handoff entries after promotion.
