# Git checkpoints

Use this reference when a task involves commits, pushes, branches, handoff, or
worktree safety.

## Core rule

Use git checkpoints for recoverability, not noise.

- Treat a local commit as the default completion checkpoint for every task that
  writes repository files, even when the user did not mention Git.
- Commit after each coherent vertical slice or completed harness update.
- Push at task completion when the user or project workflow expects direct
  pushes and the branch is in a shareable state.
- Do not push every small step.
- Do not push while in a TDD RED step unless the user explicitly asks for a
  remote checkpoint and the failure is documented.

## Completion protocol

Every repo-writing task follows the local commit steps below. When direct pushes
are expected, do not finish the task with only a local commit.

At completion:

1. Compare the current Git context with the starting HEAD and dirty state.
2. Run relevant validation, or document known failures.
3. Stage only changes that belong to the current task.
4. Commit the coherent checkpoint after validation, unless the user asked for
   no commit.
5. Confirm no task-owned changes remain staged, unstaged, or untracked.
6. Push the current branch when shareable-state checks pass.
7. If there is no upstream, ask or make the intended upstream explicit before
   pushing.
8. If commit or push needs approval, network access, or authentication, request
   it. Do
   not silently skip push.
9. In the final response or handoff, report the commit hash and push result, or
   the exact blocker.

## Completion gate

Do not claim completion while task-owned changes remain staged, unstaged, or
untracked. If a commit cannot be created, record the attempted command's exact
failure and mark the task partial or blocked. Never describe a commit as
blocked when no commit was attempted.

Stop and finalize Git when any of these red flags appears:

- The final `git status --short` lists task-owned files.
- The final response has no new commit hash and no explicit no-commit request.
- A validation or usage-limit failure is used as a commit blocker without a
  failed commit attempt.
- A missing remote or upstream is used as a reason to skip a local commit.

## Inspect git context first

Before committing or pushing, inspect:

```text
git rev-parse --show-toplevel
git rev-parse --git-common-dir
git worktree list --porcelain
git branch --show-current
git status --short
git rev-parse --abbrev-ref --symbolic-full-name @{u}
```

If an upstream does not exist, do not invent one silently. Ask the user or make
the intended remote branch explicit before pushing.

## Worktree safety

If the checkout is a worktree:

- Confirm the repo root and current worktree path.
- Confirm the current branch is the intended branch for this task. This may be
  `main` or `master` when the user or project policy expects direct pushes.
- Confirm the branch is not detached HEAD.
- Confirm no other worktree is using the same branch. If it is, stop and ask.
- Commit only changes for the current task.
- Do not clean, reset, remove, or modify other worktrees.

If the checkout is not a worktree, still apply the branch and dirty-state
checks before committing or pushing.

## Commit timing

Commit when all are true:

- The slice has a coherent purpose.
- Relevant tests or validation have passed, or known failures are documented.
- Docs, handoff, or plans are updated when needed.
- The diff does not include unrelated user changes.
- The commit message can describe behavior or harness value, not just file
  churn.

Good commit boundaries:

- One GREEN TDD behavior.
- A refactor completed while tests are green.
- One feature vertical slice.
- One bug fix with reproduction and validation.
- One harness/doc/checkpoint update.

Avoid commits for:

- Half-written implementation.
- RED tests without explicit checkpoint intent.
- Mixed unrelated changes.
- Formatting churn combined with behavior changes unless unavoidable.

## Push timing

At task completion, push when the branch is shareable:

- Validation has run, or known failures are recorded in the handoff.
- The task is not in the middle of a RED step.
- Session handoff is updated when work may continue elsewhere.
- The branch is the intended branch for this work and has a clear upstream.
- The next action is clear.

Push at natural handoff points:

- Feature completion.
- End of session.
- Before creating a PR.
- Before handing work to another agent.
- After a meaningful harness migration.

Block push when:

- Detached HEAD.
- Unknown upstream.
- Shared or protected branches when direct pushes are not authorized by the
  user or project policy.
- Dirty states containing unrelated changes.

Do not block a push solely because the current branch is `main` or `master`.
Apply the same shareable-state checks, then push when direct pushes are the
expected workflow.

## Handoff checklist

Before ending a session, record:

- Current branch.
- Whether direct pushes to this branch are expected.
- Whether this checkout is a worktree.
- Last commit hash, if any.
- Whether the branch was pushed.
- Push blocker, if push did not happen.
- Validation command and result.
- Uncommitted changes and why they remain.
- Next recommended action.

## User approval triggers

Ask before:

- Creating or changing upstream branch tracking.
- Pushing to a protected/shared branch when direct pushes are not already
  authorized by the user or project policy.
- Pushing known failing work.
- Committing unrelated existing changes.
- Performing destructive commands such as reset, clean, checkout overwrite, or
  worktree removal.
