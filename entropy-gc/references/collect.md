# Collect

Use this reference when performing one entropy cleanup slice.

## Collect goal

Reduce future drift with a small, validated change. A collect task should leave
the repo easier for the next agent to understand.

## Slice selection

Choose one slice from the entropy report:

- Consolidate duplicated helpers behind one public utility.
- Replace guessed external data shapes with validated boundaries.
- Move durable domain or architecture knowledge into repo docs.
- Add a check for a repeated review finding.
- Split an oversized file only when it improves ownership or review.
- Archive stale plans and update the current handoff.
- Improve logging, metrics, traces, or diagnostics for a recurring failure.

Avoid slices that mix unrelated cleanup, formatting, and behavior changes.

## Before editing

Confirm:

- The public behavior that must not change.
- The files and boundaries likely affected.
- The validation command.
- Whether runtime evidence is needed.
- The rollback path if the cleanup is wrong.

If behavior must change, treat the task as feature or bugfix work and use the
project's TDD and review rules.

## Guardrail upgrade

For every cleanup, ask what would prevent recurrence:

- Test.
- Lint rule.
- Architecture check.
- Docs rule.
- Scan pattern.
- CI gate.
- Review checklist.

Add the smallest practical guardrail in the same slice when it is low risk. If
not practical, record the follow-up in the debt tracker.

## Completion checklist

Before final handoff or PR:

- The cleanup is scoped to one coherent finding or cluster.
- Tests or validation ran, or known failures are documented.
- Runtime evidence exists when static tests cannot prove behavior.
- The entropy report, quality score, or debt tracker is updated.
- A recurrence guardrail exists or a follow-up is recorded.
- The final note lists remaining entropy risks.

## PR note

Use this shape when no project template exists:

```markdown
## Entropy finding
[What drift was found and why it matters.]

## Cleanup
[What changed.]

## Guardrail
[Test, script, doc, lint, CI, or follow-up.]

## Verification
[Commands and runtime evidence.]

## Remaining debt
[What is still intentionally left.]
```
