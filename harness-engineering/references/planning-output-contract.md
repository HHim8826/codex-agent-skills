# Planning output contract

Use this reference when planning could otherwise end as a chat-only summary.

## Core rule

Do not treat a chat plan as complete unless the user explicitly asks for
discussion only. Planning must leave the next agent with a durable artifact or a
short handoff.

Use the smallest artifact that preserves recoverability:

| Situation | Output |
| --- | --- |
| Tiny task, no durable decision | Update session handoff only |
| Feature or bugfix with behavior change | Feature brief in `docs/product-specs/` |
| Multi-step implementation | Plan in `docs/exec-plans/active/` |
| Architecture boundary or dependency changed | Update `ARCHITECTURE.md` |
| Quality, reliability, or validation gap found | Update `docs/QUALITY_SCORE.md` or equivalent |
| User explicitly requested discussion only | No file write; say no artifact was written |

## After a planning interview

For a zero-start project, follow the built-in interview in
`zero-to-harness.md`. If the user also invokes `$grill-me`, use the same
one-question-at-a-time contract rather than running a second interview. After
the questions are resolved, return to this contract and persist the appropriate
artifact.

Do not stop after the final interview answer with only a chat summary.

## Planning artifact checklist

Before planning is complete, record:

- Goal and non-goals.
- Public interface or user-visible behavior.
- Acceptance criteria.
- Architecture impact.
- Test strategy and first TDD behavior, if feature or bugfix work.
- Validation commands.
- Runtime or browser evidence needed.
- Risks, rollback notes, or open questions.

## Durable docs threshold

Do not put every task detail into long-lived docs. Promote only durable
knowledge:

- Product behavior or requirement changes.
- Architecture, dependency, or data-flow decisions.
- Validation, CI, observability, or testing strategy changes.
- Known quality gaps and next actions.
- Lessons that future agents must know to avoid repeating a mistake.
