# Zero to harness

Use this reference when the repo is empty, undocumented, or too unclear for
agents to work reliably.

## Goal

Create the smallest agent-ready project environment before building product
features. The first deliverable is not the app; it is a repo where an agent can
understand intent, run checks, and make a small verified change.

## Built-in planning interview

Use this interview for an empty repository, a new product idea, or a project
whose product and engineering constraints are not yet actionable. It is built
into `harness-engineering`; do not require a separate `$grill-me` invocation.

Before asking questions, inspect the available repository and user context.
Draft a provisional harness-aware plan that covers the applicable items below:

- Product goal, target users, core workflows, and non-goals.
- Acceptance criteria and hard product or operational constraints.
- Architecture boundaries, data ownership, persistence, and configuration.
- Runtime, packaging, deployment, and supported environments.
- Documentation, tests, validation commands, runtime evidence, and quality
  gates.
- Security, reliability, maintenance risks, and unresolved decisions.

Omit irrelevant sections. For example, do not force a polling or diff strategy
onto a product that has no synchronization workflow.

After the provisional plan, ask exactly one unresolved decision question at a
time. Each question must contain:

- **Recommended answer:** the default choice and why it fits the known
  constraints.
- **Tradeoff:** the meaningful cost or alternative.
- **Unlocks:** the decision the answer unlocks in the plan.

Resolve questions in dependency order. Explore the repository instead of
asking the user when code, docs, configuration, or runtime evidence can answer
the question. Treat an accepted recommendation as a resolved decision, update
the plan, and continue with the next unresolved branch.

End the interview only when every plan-critical choice has an answer, an
accepted recommendation, or an explicit documented assumption; acceptance
criteria and validation are concrete; and remaining questions are
non-blocking. Then finalize the plan under
`references/planning-output-contract.md` and request approval.

Do not start implementation during the interview. Start only after the user
approves the finalized plan, unless the user explicitly asks to skip the
interview. If the supplied brief already resolves every plan-critical choice,
report that the interview found no unresolved decisions and proceed to plan
approval instead of inventing questions.

## Minimum viable harness

Create only the smallest set of artifacts needed for the first verified slice:

1. `AGENTS.md`: short entry point with working rules, command index, and links.
2. `ARCHITECTURE.md`: initial layers, dependency direction, module ownership,
   and allowed cross-boundary communication.
3. `docs/product-specs/index.md`: product goal, target user, non-goals, and
   first vertical slice.
4. `docs/exec-plans/active/`: plans for work that is too large for one direct
   edit.
5. `scripts/run-local`: start the app or say exactly what is missing.
6. `scripts/validate-feature`: run the smallest trustworthy validation suite.

Add more harness only when the first slice needs it or a risk is already known.
Do not create empty docs just to satisfy a catalog.

## Expansion catalog

Add these artifacts when the project has the matching need:

- `docs/domain/glossary.md`: business terms are ambiguous or reused across
  features.
- `docs/domain/workflows.md`: business flows, actors, states, or edge cases
  matter.
- `docs/domain/invariants.md`: business rules must survive future changes.
- `docs/design-docs/core-beliefs.md`: product principles or tradeoffs recur.
- `docs/QUALITY_SCORE.md`: quality gaps need tracking across domains.
- `docs/RELIABILITY.md`: local run expectations, failure modes, logging, or
  recovery assumptions matter.
- `docs/SECURITY.md`: auth, secrets, data handling, or dependency risk matters.
- `scripts/run-worktree`: isolated worktree app instances are practical.
- `scripts/inspect-runtime`: agents need a stable way to inspect app URL, logs,
  runtime health, or diagnostics.
- `scripts/check-docs`: links, required docs, or stale placeholders need
  mechanical checks.
- `scripts/check-architecture`: import, layer, or dependency rules need
  enforcement.

## AGENTS.md shape

Keep `AGENTS.md` small enough to scan in one minute:

```markdown
# Agent guide

## Mission
[One paragraph product mission.]

## Start here
- Architecture: ARCHITECTURE.md
- Product specs: docs/product-specs/
- Active plans: docs/exec-plans/active/
- Domain docs: docs/domain/ (when present)
- Quality score: docs/QUALITY_SCORE.md (when present)

## Commands
- Run locally: scripts/run-local
- Run worktree app: scripts/run-worktree
- Inspect runtime: scripts/inspect-runtime
- Validate feature: scripts/validate-feature
- Check docs: scripts/check-docs
- Check architecture: scripts/check-architecture

## Rules
- Update docs when behavior or architecture changes.
- Prefer vertical slices.
- Run validation before claiming completion.
```

## Architecture starter

Document dependency direction even if implementation is tiny:

```text
Types -> Config -> Repository -> Service -> Runtime -> UI
```

Adjust the names to the stack. The invariant matters more than the exact
labels: dependencies flow in one direction, domain boundaries are explicit, and
shared providers are the only approved cross-domain entry points.

## Minimum validation

Before product code begins, the repo must answer these questions:

- How does an agent install dependencies?
- How does an agent start the app?
- How does an agent start or identify an app instance for the current worktree?
- How does an agent run tests?
- How does an agent inspect the app in a browser or equivalent runtime?
- How does an agent find logs, metrics, traces, or runtime diagnostics?
- Where are domain terms, workflows, and invariants documented?
- Where should feature plans go?
- Where should new product decisions be recorded?
- Which checks fail when architecture or docs drift?

If an answer needed for the next slice is missing, fill that gap before
expanding product scope. Defer unrelated catalog items until they protect real
work.
