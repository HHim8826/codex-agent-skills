# Quality gates

Use this reference when defining completion criteria, PR checks, CI, or local
validation for agent-driven work.

## Done definition

A feature is not done until the project can show evidence for these claims:

- The user-facing behavior matches the spec.
- The implementation respects architecture boundaries.
- Tests cover the meaningful success and failure paths.
- UI or runtime behavior has been inspected when relevant.
- Logs or diagnostics are adequate for likely failures.
- Docs reflect changed behavior, commands, or architecture.
- Domain knowledge needed for the change is repo-local and navigable.
- Runtime evidence is captured when tests cannot prove the behavior.
- Review findings are resolved, converted into harness improvements, or
  recorded as blockers.
- Known risks and rollback notes are recorded for risky changes.
- Recoverability is handled by a short handoff or by an explicit statement that
  no non-obvious continuation state remains.
- Task-owned changes are committed unless the user explicitly requested no
  commit, or an attempted commit failed with an exact recorded blocker.
- The final response reports the new commit hash and push result, or accurately
  marks the task partial or blocked.

## Local validation command

Prefer one project-level command that agents can run before claiming success:

```text
scripts/validate-feature
```

The command can call stack-specific tools, but the entry point should be stable.
Typical checks:

- Format.
- Lint.
- Type check.
- Unit tests.
- Integration tests.
- Architecture checks.
- Docs checks.
- Critical browser or runtime smoke test.
- Agent-readability checks for required domain docs.
- Runtime inspection checks for app URL, logs, or diagnostics when relevant.

If one command is too slow, provide fast and full variants with clear names.

Do not put a clean-tree requirement inside the pre-commit validation command.
Run Git finalization after validation so the command can validate working-tree
changes before they are committed.

## Finalization gate

After validation, load `references/git-checkpoints.md` and complete these
steps:

1. Compare the current HEAD and dirty state with the task-start snapshot.
2. Stage only task-owned changes.
3. Commit the coherent checkpoint.
4. Confirm no task-owned changes remain dirty.
5. Push when the established workflow expects direct pushes.
6. Report the new commit hash and push result, or the exact attempted blocker.

Do not claim completion when step 3 was skipped. A passing validation command
does not replace a commit, and a missing remote affects only the push.

## PR checklist

Use a checklist like this when no project-specific template exists:

```markdown
## Summary
[What changed and why.]

## Verification
- [ ] Format/lint passed
- [ ] Type check passed
- [ ] Tests passed
- [ ] Runtime or browser check completed, if relevant
- [ ] Logs, metrics, traces, or diagnostics inspected, if relevant
- [ ] Docs updated, if behavior or architecture changed
- [ ] Domain terms, workflows, or invariants updated, if relevant
- [ ] Git context checked before commit/push
- [ ] Task-owned changes committed, or exact attempted commit blocker recorded
- [ ] New commit hash recorded
- [ ] Branch pushed only from a shareable state
- [ ] Push completed, or exact push blocker documented
- [ ] Review loop completed, or reason it was skipped documented

## Harness impact
- [ ] New invariant captured as test/script/doc, if discovered
- [ ] Observability updated for new failure modes, if relevant
- [ ] Repeated review finding converted into a guardrail, if practical
- [ ] Quality score updated for known gaps, if relevant

## Risk
[Migration, rollout, rollback, or compatibility notes.]
```

## CI gates

Start small and make failures actionable:

- Fail on missing required docs for new modules or domains.
- Fail on broken links in core docs.
- Fail on forbidden imports and circular dependencies.
- Fail on tests, type errors, and lint errors.
- Fail on stale generated artifacts when generation is deterministic.

Each CI failure should tell the agent how to reproduce and fix it locally.

## Review loop

For non-trivial changes, run `references/review-loop.md` before final handoff or
PR completion. At minimum, record:

- Review passes performed.
- Whether independent review was required, used, skipped, or unavailable.
- Findings fixed.
- Harness improvements added.
- Findings deferred, rejected, or blocked, with reasons.
- Validation rerun after review fixes.

## Recoverability gate

Before final response, run the handoff decision in `references/handoff.md`.
Create or update the handoff when continuation state would otherwise live only
in chat, local runtime state, or unpushed Git state. If no handoff is written,
record that no non-obvious continuation state remains.

## Runtime evidence

For UI or service behavior, tests alone may not be enough. Ask for evidence:

- Browser screenshot, DOM assertion, or accessibility tree for UI changes.
- Logs or trace IDs for backend behavior.
- Metric or diagnostic query result for operational behavior.
- Seed data or fixture used for reproduction.
- Exact command sequence used to validate.

Do not require screenshots for every tiny change. Require runtime evidence when
static tests cannot prove the product experience.

## Agent-readable evidence

For changes that rely on product or domain knowledge, record:

- Which repo-local artifact contains the relevant rule.
- Which term, workflow, invariant, schema, or contract changed.
- Whether any external-only knowledge was promoted into the repo.

For changes that rely on running app behavior, record:

- Worktree path and app URL, if relevant.
- DOM, screenshot, accessibility, log, metric, trace, or diagnostic evidence.
- Seed/reset state used for reproduction.

## Git evidence

For handoff, PR, or remote checkpoint work, record:

- Current branch and whether it is a task branch.
- Whether the checkout is a worktree.
- Last validation command and result.
- Last commit hash, if committed.
- Remote branch or reason no push happened.

## Guardrail escalation

When a human repeats the same review comment, escalate it:

| Repeated comment | Better harness |
| --- | --- |
| "Docs are stale" | docs check or required docs template |
| "Wrong layer import" | architecture check |
| "Forgot failure state" | acceptance criteria and test helper |
| "Cannot reproduce" | seed data and reproduction script |
| "Logs are useless" | structured log field and diagnostics guide |
| "Visual regression" | browser smoke test or screenshot diff |

The best review comment is the one no one needs to write again.
