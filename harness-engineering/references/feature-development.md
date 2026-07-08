# Feature development

Use this reference when adding a new feature to an agent-ready project.

## Feature loop

1. Load `references/git-checkpoints.md`, then record the starting HEAD and dirty
   state before the first edit.
2. Write or update the feature brief.
3. Create an execution plan for anything larger than a small direct edit.
4. Check whether the feature needs new harness support.
5. For a non-trivial slice, write a sprint contract before coding.
6. Use `references/tdd-integration.md` to choose the first observable behavior
   and write the first failing test.
7. Implement the smallest vertical slice.
8. Verify with tests and runtime inspection.
9. Commit the coherent GREEN slice.
10. Run the review loop for every non-trivial change.
11. Load `references/quality-gates.md`, capture reusable learning, rerun the
    relevant validation, and commit review fixes.
12. Run the recoverability check and update the handoff when useful state would
    otherwise remain only in chat or local runtime state.
13. Inspect Git again and report the commit hash and push result, or the exact
    attempted blocker.

## Feature brief

Put the brief in `docs/product-specs/` or the repo's equivalent location. Include:

- User and problem.
- Desired outcome.
- Non-goals.
- Acceptance criteria.
- Data, permissions, and failure states.
- UX or API contract.
- Risks and rollback considerations.

Keep the brief short enough that an agent can use it during implementation.

## Execution plan

Use `docs/exec-plans/active/` for complex work. A good plan has vertical slices:

```markdown
# Plan: [feature]

## Goal
[Outcome, not implementation.]

## Constraints
[Architecture, security, UX, compatibility.]

## Slices
1. Data model and tests
2. Service behavior and tests
3. UI/API path and runtime verification
4. Docs, quality gates, and cleanup

## Done
[Commands, browser checks, docs updates, PR notes.]
```

## Harness check

Before implementation, ask whether this feature needs:

- New or updated product docs.
- New or updated domain terms, workflows, invariants, schemas, or contracts.
- New architecture boundary or provider.
- New seed data, fixture, mock, or local service.
- New observability field, log event, metric, or trace.
- New runtime inspection path for UI, logs, metrics, traces, or diagnostics.
- New validation command or CI check.
- New browser flow or screenshot verification.
- New security or reliability note.

If yes, add the harness support as part of the feature slice.

## Sprint contract

Before coding a non-trivial slice, write a short contract that bridges the
feature brief and implementation. The contract must make "done" testable
without over-specifying internal implementation.

Record the contract in the active plan, feature brief, or handoff. Include:

- Slice goal and non-goals.
- User-visible behavior or public interface.
- Acceptance criteria and failure states.
- First RED behavior or test.
- Runtime, browser, API, data, or log evidence required.
- Review criteria and known edge cases.

When independent review is available, have the reviewer check the contract
before implementation. Iterate until the implementing agent and reviewer agree
on what will be built and how it will be verified. If no reviewer is available,
run the same check yourself and record the limitation.

## Implementation rules

- Build one vertical slice at a time.
- Do not start a non-trivial slice until its sprint contract is concrete enough
  to verify.
- Do not write implementation code before the first RED step unless the user
  explicitly opts out. Use `references/tdd-integration.md` as the built-in TDD
  gate.
- Test behavior through public interfaces. Avoid tests coupled to internal
  implementation details.
- Use one test -> minimal implementation -> next test. Do not write all tests
  first and then all implementation.
- Keep boundary contracts typed and validated.
- Use existing patterns before inventing a new abstraction.
- Update docs in the same change when behavior or architecture changes.
- Prefer deterministic tests over broad manual inspection.
- Use browser or runtime tools for UI behavior, not static code reading alone.
- Promote durable external knowledge into repo-local artifacts before relying
  on it for implementation.

## Feature completion gate

Treat `references/git-checkpoints.md` and `references/quality-gates.md` as
required sub-skills for feature completion. Do not claim that implementation is
complete while task-owned changes remain staged, unstaged, or untracked.

If the final aggregate validation cannot run, preserve the last coherent GREEN
slice in a commit and document the missing validation. Do not convert a
validation or usage-limit failure into a commit blocker unless a commit was
actually attempted and failed.

## Review loop

For non-trivial feature work, load `references/review-loop.md` after local
validation. Use it to check spec compliance, harness quality, and architecture
drift, then rerun the relevant validation after review fixes. Record whether
independent review was required, used, skipped, or unavailable.

## Recoverability check

Before finalization, load `references/handoff.md` when continuation state,
blockers, skipped validation or review, runtime evidence, or push state would
otherwise be lost. If no handoff is written, make sure no non-obvious
continuation state remains.

## Merge learning capture

Before considering the feature complete, capture durable learning:

- Move completed plans from `active/` to `completed/` if that is the local
  convention.
- Update product specs when behavior changed.
- Update architecture docs when boundaries changed.
- Add a quality note if a gap remains.
- Convert repeated review feedback into a check when practical.
