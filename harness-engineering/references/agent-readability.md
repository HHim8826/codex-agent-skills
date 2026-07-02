# Agent readability

Use this reference when Codex must understand the product, business domain,
architecture, or design decisions from the repository itself.

## Core rule

If Codex must use a fact to design, implement, test, debug, review, or maintain
the system, that fact must exist in version-controlled repo artifacts.

Knowledge that exists only in chats, Google Docs, issue comments, Slack, or
people's heads is not reliable agent context. External sources may be linked,
but the durable decision must be summarized in the repo.

## Agent-readable artifacts

Prefer these repo-local artifacts:

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
  references/
schemas/
contracts/
migrations/
tests/
scripts/
```

Adapt paths to the project. Preserve the intent: Codex should be able to
reconstruct the domain, constraints, and current work from files it can read.

## Domain model

Create or update domain docs when business terms matter:

- `docs/domain/glossary.md`: canonical terms, synonyms to avoid, and ambiguous
  terms.
- `docs/domain/workflows.md`: core business flows, actors, state transitions,
  and edge cases.
- `docs/domain/invariants.md`: rules that must not be broken by features,
  migrations, refactors, or UI changes.

Keep these docs operational. Avoid essays. Include examples and references to
tests, schemas, or code owners when they clarify the rule.

## Repo navigation

Make the repo navigable for a fresh agent:

- Keep `AGENTS.md` as a short index, not a full manual.
- Point from `AGENTS.md` to domain docs, architecture docs, plans, and commands.
- Keep architecture boundaries close to the code they govern.
- Store executable plans under `docs/exec-plans/`.
- Put generated artifacts under a clearly named generated directory.
- Prefer structured schemas and contracts over prose when structure matters.

## External knowledge intake

When a durable decision appears outside the repo:

1. Identify the decision, not the whole conversation.
2. Record the decision in the smallest correct repo artifact.
3. Link to the external source only as supporting context.
4. Add or update a test, schema, script, or quality gate when the decision is
   enforceable.

Do not paste long external transcripts into docs. Summarize the rule future
agents need.

## Readability review

During planning, review, or maintenance, ask:

- Could a fresh Codex session understand the business goal from repo files?
- Are domain terms defined where agents can find them?
- Are non-goals and invariants explicit?
- Are schemas, API contracts, migrations, and tests aligned with the docs?
- Is any required knowledge only in chat or external documents?
- Would a failed CI check tell the agent where to look and how to fix it?

If the answer is no, improve the smallest repo artifact that restores
readability.
