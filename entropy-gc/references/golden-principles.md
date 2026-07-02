# Golden principles

Use this reference when defining the repo rules that entropy GC should protect.

## Purpose

Golden principles are opinionated, repo-local rules that keep future agent work
consistent. They capture human taste once, then make it enforceable.

## Good principles

A good principle is:

- Specific enough for an agent to apply.
- Connected to a real failure, review comment, or drift pattern.
- Enforceable by a check, test, doc rule, or review checklist.
- Short enough to keep in working memory during implementation.

Avoid principles that only say "write clean code" or "be consistent." They do
not tell an agent what to do.

## Starter principles

Adapt these to the repo:

| Principle | Enforcement path |
| --- | --- |
| Prefer shared utilities over hand-rolled duplicates | duplicate helper scan |
| Validate boundary data instead of probing guessed shapes | schema tests or lint |
| Keep domain terms canonical | glossary and docs check |
| Keep `AGENTS.md` as an index, not a manual | docs review |
| Separate generated docs from authored design docs | docs check |
| Add observability for new failure modes | review checklist or tests |
| Archive completed plans with outcome notes | plan gardening check |

## Template

Use this shape:

```markdown
# Golden principles

## Principle: [short rule]

Reason:
[What drift or failure this prevents.]

Applies to:
[Files, domains, workflows, or review stage.]

Examples:
- Good:
- Bad:

Enforcement:
[test, script, lint, docs check, manual review, or planned check]
```

## Promotion rule

Promote a preference into a golden principle when:

- The same review comment appears more than once.
- A bug came from an unclear pattern.
- Agents copy a local anti-pattern.
- The repo has two valid-looking ways to do the same thing.

If the principle cannot be enforced yet, record the manual check and the next
automation step.
