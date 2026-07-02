# Audit

Use this reference when the repository needs an entropy report before cleanup.

## Audit goal

Produce a ranked map of drift signals. Do not fix everything during audit. The
output should make the next cleanup slice obvious and small.

## Mechanical scan

Run the bundled scanner when available:

```text
python .agents/skills/entropy-gc/scripts/entropy_scan.py <repo>
```

If the skill is installed outside the target repo, pass the absolute path to the
repo. Use `--json` only when another script will consume the output.

The scanner looks for conservative signals:

- Large source or doc files.
- TODO, FIXME, HACK, TEMP, WORKAROUND, and similar markers.
- Type or lint escape hatches such as `as any`, `@ts-ignore`, or
  `eslint-disable`.
- Repeated utility, helper, adapter, parser, formatter, or client filenames.
- Missing common harness artifacts.
- Documentation placeholders.

Treat every finding as a prompt for inspection. A scan result is not permission
to refactor.

## Manual passes

After the mechanical scan, inspect the repo for:

- Repeated review comments.
- Multiple helpers that solve the same problem differently.
- Domain terms with several names.
- Architecture docs that no longer match imports or runtime boundaries.
- Active plans that are completed, stale, or missing current state.
- Generated artifacts mixed with authored docs.
- Tests that pass while key user journeys are untested.
- Logs, metrics, or traces that do not help diagnose likely failures.
- Code that guesses external data shapes instead of validating boundaries.

## Ranking

Rank findings by this order:

1. User-visible correctness or data risk.
2. Security, privacy, reliability, or migration risk.
3. Agent confusion: patterns likely to be copied incorrectly.
4. Review cost: findings that repeatedly consume human attention.
5. Local cleanup cost and blast radius.

Prefer the smallest finding that reduces future confusion.

## Report format

Use this structure:

```markdown
# Entropy report

## Summary
- High-risk findings:
- Medium-risk findings:
- Low-risk findings:

## Top findings
1. Finding:
   Evidence:
   Risk:
   Suggested slice:
   Guardrail:

## False positives
- Finding:
  Reason:

## Recommended next slice
- Goal:
- Files likely touched:
- Validation:
- Rollback:
```

If the audit will feed scheduled automation, save it under the repo's existing
quality or maintenance location.
