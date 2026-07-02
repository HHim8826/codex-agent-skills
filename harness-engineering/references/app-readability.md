# App readability

Use this reference when Codex must inspect, drive, debug, or verify a running
application.

## Core rule

Make the running app readable to agents, not only to humans. UI state, logs,
metrics, traces, seed data, and app instance details should be inspectable from
the local environment and recordable as evidence.

## Worktree-local app instances

When the project supports git worktrees, each worktree should be able to start
an isolated app instance.

Record or provide:

- Start command.
- Local URL.
- Port selection strategy.
- Environment file or variable strategy.
- Database, cache, queue, and storage isolation.
- Seed data command.
- Reset command.
- Log path or log query.
- Known limitations.

Prefer stable commands:

```text
scripts/run-local
scripts/run-worktree
scripts/inspect-runtime
scripts/validate-feature
```

If the project cannot support isolated worktree instances yet, document the
gap and the next smallest fix.

## Browser-readable UI

For UI changes, prefer direct runtime inspection over static code reading.

Use browser tooling when available:

- Navigate to the target route.
- Capture DOM snapshot, accessibility tree, or relevant element state.
- Capture screenshots when visual layout matters.
- Exercise the user interaction path.
- Compare before and after behavior when fixing regressions.

Record the route, data setup, actions, and evidence in the feature plan,
handoff, or PR notes.

## Logs

Logs should be structured enough for an agent to search and reason about:

- Timestamp.
- Level.
- Event name.
- Request or correlation ID.
- User, tenant, session, or actor ID when safe.
- Route, command, job, or workflow name.
- Error code and sanitized error details.

Do not rely on human-readable paragraphs when a stable event field would make
debugging deterministic.

## Metrics and traces

Metrics and traces should support diagnosis, not only dashboards.

Make these discoverable:

- Metric names and labels.
- Trace/span names.
- How to query recent errors, latency, retries, and failed jobs.
- How to correlate UI action -> request -> service -> data operation.
- Which dashboards or local endpoints are authoritative.

When a feature introduces a new failure mode, add a log, metric, trace, or
diagnostic note that makes the failure inspectable.

## Runtime evidence

For important UI or service behavior, done means evidence exists:

- Command used to start the app.
- URL or endpoint inspected.
- Seed data or fixture used.
- Browser action path or API request.
- Screenshot, DOM assertion, accessibility evidence, log query, metric query,
  or trace ID.
- Result and remaining uncertainty.

Do not require heavy runtime evidence for trivial changes. Require it when
tests cannot prove the user experience or operational behavior.

## Handoff data

When work continues later, include runtime state in the handoff if relevant:

- App instance URL.
- Worktree path.
- Start command.
- Seed/reset status.
- Evidence captured.
- Logs, metrics, or traces inspected.
- Known runtime blockers.
