[English](./README.md) | [繁體中文](./README.zh-TW.md)

# Codex agent skills

This repository contains reusable skills for keeping agent-driven software
projects understandable, verifiable, and maintainable. Each skill follows the
Agent Skills directory format and includes a `SKILL.md` entry point.

## Choose a skill

The two skills solve related problems at different stages of a repository's
lifecycle:

- Use [`harness-engineering`](./harness-engineering/SKILL.md) to establish or
  improve the operating environment in which coding agents plan, implement,
  inspect, validate, review, and hand off work.
- Use [`entropy-gc`](./entropy-gc/SKILL.md) to find accumulated drift, rank it,
  clean up one focused slice, and prevent the same problem from returning.

## Harness engineering

`harness-engineering` treats the repository as the agent's operating
environment. It makes project intent, commands, architecture, runtime evidence,
validation, and Git state explicit enough for an agent to work safely.

### Capabilities

The skill provides workflows and reference material for these areas:

- **Zero-to-harness planning:** Inspect an empty or unclear repository, draft a
  provisional plan, resolve one decision at a time, and create only the minimum
  useful agent-ready artifacts.
- **Agent readability:** Keep domain terms, workflows, invariants,
  architecture, product specifications, and active plans in discoverable,
  version-controlled files.
- **App readability:** Make local URLs, worktree instances, seed data, UI
  state, logs, metrics, traces, and diagnostics inspectable by an agent.
- **Feature development:** Define a short feature brief, split work into
  vertical slices, check required harness support, and update durable docs with
  behavior changes.
- **Test-driven development:** Select one observable behavior, write one
  failing test, implement the smallest passing behavior, and repeat.
- **Quality gates:** Define stable validation commands and require evidence for
  behavior, architecture, tests, runtime state, documentation, and risk.
- **Review loops:** Run focused specification, harness, and architecture review
  passes, then turn recurring feedback into tests, scripts, or rules.
- **Git checkpoints:** Record the starting state, commit coherent green slices,
  protect worktree boundaries, push when required, and report exact blockers.
- **Session handoffs:** Preserve only the current state, decisions, Git
  checkpoint, runtime evidence, blockers, and next action needed to resume.
- **Maintenance:** Detect stale documentation, architecture drift, weak
  observability, missing runtime evidence, and repeated review findings.

### Workflow

A typical feature or repository-improvement workflow follows these steps:

1. Inspect the repository, documentation, runtime entry points, and Git state.
2. Select the reference that matches the task, such as zero-start planning,
   feature development, app readability, or maintenance.
3. Resolve any plan-critical decisions and persist the smallest useful brief or
   execution plan.
4. Choose one observable behavior and complete a red-green-refactor vertical
   slice.
5. Validate tests, architecture, documentation, and runtime behavior with
   reproducible evidence.
6. Review specification compliance, harness quality, and architecture drift.
7. Commit the coherent result, push when the workflow requires it, and leave a
   concise handoff only when work remains.

### Examples

Use an explicit prompt when you want to force the skill to load. For a new
repository, ask Codex to create the minimum viable harness before product code:

```text
Use $harness-engineering to turn this empty repository into an agent-ready
project. Inspect the available context, run the built-in planning interview,
and propose the minimum validation and runtime inspection commands.
```

For feature work in an existing project, include the expected completion
contract:

```text
Use $harness-engineering to add a billing health-check endpoint. Create a short
feature brief, implement one vertical TDD slice, verify the endpoint at runtime,
run the review and quality gates, then commit and push the green checkpoint.
```

The second example causes the skill to inspect the existing repo, define the
observable endpoint behavior, add only the harness support the feature needs,
capture validation evidence, and finish with an explicit Git result.

## Entropy GC

`entropy-gc` turns repository cleanup into an evidence-based maintenance loop.
It treats scanner results as signals to inspect, not as automatic permission to
refactor.

### Capabilities

The skill provides focused cleanup and anti-drift workflows:

- **Mechanical audits:** Scan for large files, stale markers, type or lint
  escape hatches, repeated helper names, missing harness artifacts, and
  documentation placeholders.
- **Manual audits:** Inspect repeated review feedback, divergent helpers,
  inconsistent domain language, stale plans, weak tests, and poor diagnostics.
- **Risk ranking:** Prioritize user-visible and data risks first, followed by
  security, reliability, agent confusion, review cost, and cleanup cost.
- **Focused collection:** Select one finding or a cluster of up to three
  related findings without mixing broad formatting or unrelated behavior.
- **Guardrail upgrades:** Convert recurring drift into a test, lint rule,
  architecture check, documentation rule, scan pattern, CI gate, or review
  checklist.
- **Golden principles:** Record three to seven concrete repository rules, each
  connected to an enforcement path or a planned automation step.
- **Quality tracking:** Maintain an actionable quality score and technical-debt
  tracker with evidence, risk, owner or area, and the next smallest cleanup.
- **Recurring schedules:** Add manual, CI, or cron-based scans only after the
  local command is stable and false positives have a review path.

### Workflow

A complete entropy-GC cycle follows these steps:

1. Run the bundled scanner and inspect its evidence.
2. Perform manual passes for drift that static patterns cannot detect.
3. Rank findings by user risk, operational risk, agent confusion, and cost.
4. Record false positives and choose one small, high-signal cleanup slice.
5. Preserve public behavior, implement the cleanup, and add a recurrence
   guardrail when practical.
6. Run the relevant validation and update the entropy report, quality score, or
   debt tracker.
7. Record remaining debt and add a schedule only when the scan is stable.

### Examples

Ask for an audit when you need a ranked report before changing code:

```text
Use $entropy-gc to audit this repository. Run the conservative scanner, confirm
the findings against the code and project intent, rank the risks, and recommend
one small cleanup slice without implementing it.
```

Run the bundled scanner directly from a repository that has this skill
installed at `.agents/skills`:

```shell
python .agents/skills/entropy-gc/scripts/entropy_scan.py .
python .agents/skills/entropy-gc/scripts/entropy_scan.py . --json
```

Ask for a focused collection pass after confirming a finding:

```text
Use $entropy-gc to consolidate the duplicated API response adapters identified
in the entropy report. Preserve public behavior, add a regression guardrail,
run the relevant validation, and record the remaining debt.
```

## Installation

To install all skills for one project, clone this repository into that
project's `.agents/skills` directory:

```shell
git clone https://github.com/HHim8826/codex-agent-skills.git .agents/skills
```

If `.agents/skills` already exists, clone the repository elsewhere and copy
only the skill directories you need. Keep each `SKILL.md` at
`.agents/skills/<skill-name>/SKILL.md`.

## Invoking a skill

Codex loads a skill when your request matches the trigger in its `description`
frontmatter. You can also name a skill directly by using
`$harness-engineering` or `$entropy-gc` in your prompt.

Open the selected skill's `SKILL.md` to review its operating rules. Load only
the referenced workflow file that matches the current task.

## Repository validation

Run these checks from this repository's root before publishing changes:

```shell
python harness-engineering/scripts/check_workflow_contract.py
python -m py_compile harness-engineering/scripts/check_workflow_contract.py
python -m py_compile entropy-gc/scripts/entropy_scan.py
python entropy-gc/scripts/entropy_scan.py --help
```

## License

This repository is available under the [MIT License](./LICENSE).
