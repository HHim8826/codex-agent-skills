# Schedule

Use this reference when deciding how entropy GC should run over time.

## Rule

The skill is not the scheduler. The repository should own the schedule through
CI, cron, a task runner, or a documented manual cadence.

## Cadence

Choose the lightest cadence that catches drift before it spreads:

| Repo state | Cadence | Action |
| --- | --- | --- |
| Small or early repo | Monthly or manual | Run audit and update debt tracker |
| Active product repo | Weekly | Run scan, update quality score, choose one slice |
| Agent-heavy repo | Daily scan, weekly collect | Open targeted cleanup only above threshold |
| Release window | Before release | Focus on docs, reliability, and migration risk |

Do not open cleanup PRs automatically until the repo has stable checks and low
false-positive noise.

## CI pattern

A scheduled CI job can:

1. Run `scripts/scan-entropy`.
2. Upload or comment the report.
3. Fail only on agreed hard gates.
4. Open an issue or PR when findings exceed a threshold.

Most findings should be advisory at first. Promote only stable, high-value
checks into blocking gates.

## Human review budget

Keep scheduled output reviewable:

- Summaries should fit in a short PR or issue.
- Suggested cleanup should be one slice.
- Automated PRs should be small enough to review quickly.
- Repeated false positives should tune the scanner, not train humans to ignore
  alerts.

## Schedule artifact

Record the schedule in the repo:

```markdown
# Entropy GC schedule

## Cadence
[daily, weekly, monthly, manual]

## Command
[script or CI job]

## Thresholds
[what opens an issue, PR, or fails CI]

## Owner or review path
[who or what reviews output]

## Last tuning
[date and change]
```
