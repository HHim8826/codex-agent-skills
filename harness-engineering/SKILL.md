---
name: harness-engineering
description: Use when starting or maintaining an agent-first software project, planning feature or bugfix work, or adding guardrails for TDD, docs, agent/appreadability, worktrees, git checkpoints, review, PR feedback, validation,handoff, commit, or push workflows.
---

# Harness Engineering

## Overview

Harness engineering designs the repo, tools, docs, tests, observability, and
quality gates that let coding agents work safely and verifiably. Treat the repo
as the agent's operating environment, not just a place where code happens to
live.

The core loop is:

1. Make project intent and constraints visible in versioned files.
2. Give agents deterministic commands for setup, testing, validation, and local
   product inspection.
3. Add guardrails that enforce architectural and product invariants.
4. Make the app readable at runtime through UI inspection, logs, metrics,
   traces, seed data, and worktree-local instances.
5. Capture repeated human feedback as docs, tests, lint rules, or scripts.

## Mandatory Git finalization

For any task that may write repository files, load
`references/git-checkpoints.md` before the first edit. This requirement is
additive and overrides any instruction below to stop loading references once
the workflow appears sufficient.

Record the starting HEAD and dirty state. Commit each coherent GREEN slice
after relevant validation. Before the final response, inspect Git again. Do not
claim completion while task-owned changes remain staged, unstaged, or
untracked. Report the new commit hash, or report the exact attempted commit
blocker and mark the task partial or blocked. A missing remote or upstream can
block a push, but it cannot block a local commit.

## Mandatory zero-start planning interview

When starting from an empty repository, a new product idea, or an otherwise
underspecified project, load `references/zero-to-harness.md`. Draft a
provisional harness-aware plan, then run its built-in planning interview before
implementation. Do not require the user to invoke `$grill-me` separately.

Ask only about decisions that repository inspection and supplied context cannot
answer. Ask one question at a time, include a recommendation and tradeoff, and
state what the answer unlocks. Do not begin implementation until the interview
exit criteria are met and the user approves the finalized plan. The user can
explicitly skip the interview.

## Choose the workflow

Read only the workflow reference that matches the current task. Load one
workflow reference first and another only when the task explicitly needs it.
The mandatory Git reference above remains required for every repo-writing task.

| Situation | Read |
| --- | --- |
| Empty repo, no docs, vague project start | `references/zero-to-harness.md` |
| Agent must understand business/domain knowledge from the repo | `references/agent-readability.md` |
| Agent must inspect UI, logs, metrics, traces, or worktree app instances | `references/app-readability.md` |
| Project kickoff or stage planning | `references/lifecycle.md` |
| Planning must produce repo artifacts | `references/planning-output-contract.md` |
| Building a new feature | `references/feature-development.md` |
| Feature or bugfix implementation needs test-first discipline | `references/tdd-integration.md` |
| Review, PR feedback, or second-agent verification matters | `references/review-loop.md` |
| Any task may write repo files, or commit, push, branch, checkpoint, or worktree safety matters | `references/git-checkpoints.md` |
| Short context handoff is needed between sessions | `references/handoff.md` |
| Post-launch upkeep, drift, quality debt | `references/maintenance.md` |
| Defining "done", PR checks, CI gates | `references/quality-gates.md` |

If multiple situations apply, prefer this order and stop as soon as the loaded
references are sufficient:
`zero-to-harness.md`, `agent-readability.md`, `app-readability.md`,
`lifecycle.md`, `planning-output-contract.md`, `feature-development.md`,
`tdd-integration.md`, `review-loop.md`, `git-checkpoints.md`,
`quality-gates.md`, `handoff.md`, `maintenance.md`.

Do not use this stop rule to skip `git-checkpoints.md` for a repo-writing task.

## Operating principles

- Keep `AGENTS.md` short. Use it as an index to durable project docs, not as a
  giant manual.
- Prefer versioned repo files over chat memory, meeting notes, or private
  assumptions. If an agent needs to know it, put it in the repo.
- Optimize the codebase for agent readability. Domain language, workflows,
  invariants, schemas, plans, and operational evidence must be discoverable
  from version-controlled artifacts.
- Build vertical slices. Do not ask agents to build a whole product in one
  prompt.
- During planning, do not stop at a chat-only plan unless the user explicitly
  asks for discussion only. Persist the right planning artifact or handoff.
- For feature work and bug fixes, use the built-in TDD gate before
  implementation unless the user explicitly opts out. Select one observable
  behavior and write one failing test before implementation code.
- Apply mandatory Git finalization to every repo-writing task. Inspect repo,
  branch, upstream, dirty state, and worktree context before editing and before
  commit or push.
- When the user or project workflow expects direct pushes, task completion
  includes pushing the shareable checkpoint. Do not silently stop after local
  edits or a local commit; push, ask for the needed approval, or record the
  exact blocker.
- Enforce invariants with tests, lint, scripts, architecture checks, and CI.
  Do not rely on repeated human review comments for recurring rules.
- For non-trivial changes, close the loop with spec, harness, and architecture
  review before final handoff or PR completion.
- Give agents runtime visibility: local app commands, browser verification,
  logs, metrics, traces, seed data, and reproducible bug reports.
- Make runtime surfaces Codex-readable. UI state, logs, metrics, traces, and
  app instance details should be inspectable without relying on human QA.
- Convert every repeated mistake into a stronger harness: better docs, a test,
  a script, a check, or a clearer boundary.

## Default project artifacts

When no better project-specific pattern exists, use these names as the catalog
for harness artifacts:

```text
AGENTS.md
ARCHITECTURE.md
docs/
  domain/
    glossary.md
    workflows.md
    invariants.md
  product-specs/
  design-docs/
  exec-plans/
    active/
    completed/
  generated/
  references/
  QUALITY_SCORE.md
  RELIABILITY.md
  SECURITY.md
scripts/
  check-architecture
  check-docs
  inspect-runtime
  run-local
  run-worktree
  validate-feature
```

Adapt names to the stack and repo conventions. The important property is that
future agents can find the project rules, run the product, verify changes, and
update durable knowledge. This is not a mandatory first commit; start with the
smallest useful subset and expand when the work exposes a real need.

## Common mistakes

- Writing a long article instead of agent-operational instructions.
- Creating docs without commands that verify the docs still match reality.
- Leaving durable product, domain, or design knowledge only in chats, external
  documents, or people's heads.
- Letting feature work begin before setup, validation, and local run commands
  are discoverable.
- Treating UI, logs, metrics, or traces as human-only surfaces instead of
  agent-readable evidence.
- Asking agents to infer architecture from scattered files instead of writing
  the dependency rules down.
- Treating a fixed bug as complete before asking why the harness allowed the
  bug to survive.
- Treating review as a one-time comment pass instead of a feedback loop that
  ends with evidence, fixes, or documented blockers.
- Recording every task in durable docs. Every task needs recoverability; only
  durable knowledge belongs in long-lived project documentation.
- Refusing to push only because the current branch is `main` or `master` when
  the user or project policy expects direct pushes. Still do not push from
  detached HEAD, an unknown upstream, unrelated dirty state, or a half-finished
  RED state.
- Claiming completion while task-owned changes remain uncommitted, or calling
  an unattempted commit a blocker.

## Skill maintenance validation

After editing this skill, run
`python scripts/check_workflow_contract.py` from the skill directory, followed
by the standard skill structure validator.
