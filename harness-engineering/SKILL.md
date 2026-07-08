---
name: harness-engineering
description: >-
  Use when starting or maintaining an agent-first software project, planning
  feature or bugfix work, or adding guardrails for TDD, docs, agent/app
  readability, long-running coding sessions, worktrees, git checkpoints,
  sub-agent review, PR feedback, validation, handoff, commit, or push
  workflows.
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

## Mandatory review gate

For feature, bugfix, harness, skill, agent workflow, architecture, data,
security, reliability, migration, CI, validation, or user-visible behavior
changes, load `references/review-loop.md` before finalization. This requirement
is additive and overrides the progressive-disclosure stop rule below.

Run or attempt independent review for non-trivial changes and for any workflow
change that future agents will copy. Use an available sub-agent or review tool
when policy and permissions allow. If independent review cannot be used, record
the exact limitation in the handoff or final response, then run the spec,
harness, and architecture self-review passes from `references/review-loop.md`.

Do not call the task complete until important review findings are fixed,
converted into harness improvements, or recorded as explicit blockers.

## Mandatory recoverability check

Before the final response, decide whether the next agent can recover the task
from committed code, durable docs, and the final response alone. Load
`references/handoff.md` and create or update the handoff when useful state
would otherwise stay only in chat or local runtime state.

Create or update a handoff when work may continue later, blockers or known
failures remain, validation or runtime evidence is not obvious from committed
artifacts, commit/push/review was skipped or blocked, or the next step depends
on transient state. If no handoff is written, the final response must make it
clear that no non-obvious continuation state remains.

## Choose the workflow

Read only the workflow reference that matches the current task. Load one
workflow reference first and another only when the task explicitly needs it.
The mandatory Git, review, and recoverability references above remain required
when their gates apply.

| Situation | Read |
| --- | --- |
| Empty repo, no docs, vague project start | `references/zero-to-harness.md` |
| Agent must understand business/domain knowledge from the repo | `references/agent-readability.md` |
| Agent must inspect UI, logs, metrics, traces, or worktree app instances | `references/app-readability.md` |
| Project kickoff or stage planning | `references/lifecycle.md` |
| Planning must produce repo artifacts | `references/planning-output-contract.md` |
| Building a new feature | `references/feature-development.md` |
| Feature or bugfix implementation needs test-first discipline | `references/tdd-integration.md` |
| Feature, bugfix, harness, skill, workflow, PR feedback, or second-agent verification | `references/review-loop.md` |
| Any task may write repo files, or commit, push, branch, checkpoint, or worktree safety matters | `references/git-checkpoints.md` |
| Recoverability, blocker, continuation state, or session handoff is needed | `references/handoff.md` |
| Long-running work hits context pressure, compaction, reset, or continuation risk | `references/handoff.md` |
| Post-launch upkeep, drift, quality debt, model upgrade, or harness cost review | `references/maintenance.md` |
| Defining "done", PR checks, CI gates | `references/quality-gates.md` |

If multiple situations apply, prefer this order and stop as soon as the loaded
references are sufficient:
`zero-to-harness.md`, `agent-readability.md`, `app-readability.md`,
`lifecycle.md`, `planning-output-contract.md`, `feature-development.md`,
`tdd-integration.md`, `review-loop.md`, `git-checkpoints.md`,
`quality-gates.md`, `handoff.md`, `maintenance.md`.

Do not use this stop rule to skip `git-checkpoints.md` for a repo-writing task,
`review-loop.md` when the review gate applies, or `handoff.md` when the
recoverability check says useful state would otherwise be lost.

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
- For long-running work, keep each slice anchored by a testable contract and a
  recoverable handoff. Reset context with a structured handoff when context
  pressure makes the agent wrap up early or lose coherence.
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
  review before final handoff or PR completion. Use independent review when
  policy and permissions allow; otherwise document the limitation and run the
  focused self-review passes.
- At task boundaries, run the recoverability check. Write a short handoff when
  state, blockers, validation evidence, runtime details, or next steps would
  otherwise live only in the chat.
- Give agents runtime visibility: local app commands, browser verification,
  logs, metrics, traces, seed data, and reproducible bug reports.
- Make runtime surfaces Codex-readable. UI state, logs, metrics, traces, and
  app instance details should be inspectable without relying on human QA.
- Convert every repeated mistake into a stronger harness: better docs, a test,
  a script, a check, or a clearer boundary.
- Stress-test harness complexity over time. Each harness component encodes an
  assumption about what the current model cannot do reliably; re-check those
  assumptions after model upgrades, high-cost runs, or repeated workflow drag.

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
- Letting a long-running agent drift, wrap up early, or continue after context
  loss without a structured handoff.
- Treating UI, logs, metrics, or traces as human-only surfaces instead of
  agent-readable evidence.
- Asking agents to infer architecture from scattered files instead of writing
  the dependency rules down.
- Treating a fixed bug as complete before asking why the harness allowed the
  bug to survive.
- Treating review as a one-time comment pass instead of a feedback loop that
  ends with evidence, fixes, or documented blockers.
- Trusting a reviewer that only praises the work. Evaluator prompts and rubrics
  need calibration when they miss real bugs, accept shallow testing, or approve
  generic output.
- Treating sub-agent review as optional for non-trivial harness, workflow,
  architecture, or user-visible changes without recording why independent
  review was unavailable.
- Recording every task in durable docs. Every task needs recoverability; only
  durable knowledge belongs in long-lived project documentation.
- Skipping the handoff decision because the work feels finished. Either create
  or update the handoff, or make sure no non-obvious continuation state remains.
- Refusing to push only because the current branch is `main` or `master` when
  the user or project policy expects direct pushes. Still do not push from
  detached HEAD, an unknown upstream, unrelated dirty state, or a half-finished
  RED state.
- Claiming completion while task-owned changes remain uncommitted, or calling
  an unattempted commit a blocker.
- Keeping planner, sprint, evaluator, or reset machinery after it stops adding
  measurable lift for the current model and project.

## Skill maintenance validation

After editing this skill, run these commands from the skill directory:

```text
python scripts/check_workflow_contract.py
python -c "from pathlib import Path; import ast; ast.parse(Path('scripts/check_workflow_contract.py').read_text())"
```
