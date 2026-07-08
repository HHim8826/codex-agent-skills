# Review loop

Use this reference when a task needs self-review, second-agent review, PR
feedback handling, or confidence beyond local validation.

## Core rule

Review is a loop, not a checkbox. The work is not ready until important review
findings are fixed, converted into harness improvements, or recorded as explicit
blockers.

For non-trivial work, independent review is part of the completion gate, not a
best-effort extra. If independent review cannot be used, the limitation must be
explicit and the main agent must compensate with focused self-review.

Independent review improves signal, but it does not replace evidence. Accuracy
comes from a clear rubric, raw artifacts, validation commands, and a documented
decision for each finding.

## When to run it

Use the review loop for:

- Feature or bugfix work that changes user-visible behavior.
- Architecture, data, security, reliability, or migration changes.
- UI changes where runtime inspection matters.
- PRs with human or agent feedback.
- Harness changes that alter how future agents work.

Skip it only for tiny, mechanical edits where validation and diff inspection
fully prove the change. Record the skip reason before finalization.

## Independent review requirement

Use a sub-agent or review tool when policy and permissions allow. Require
independent review for non-trivial changes and high-risk changes. Skip it only
when the change is trivial, policy forbids spawning a reviewer, or no
independent reviewer is available.

Use sub-agent or independent reviewer review for:

- User-visible feature or bugfix behavior.
- Security, privacy, permissions, data integrity, reliability, or migration
  changes.
- Broad refactors, dependency boundary changes, or architecture changes.
- UI changes where runtime evidence or visual behavior matters.
- Harness, skill, agent workflow, CI, or validation changes that future agents
  will copy.
- Work where the main agent made tradeoffs and confirmation bias is likely.

Sub-agent review is optional for:

- Typos and wording-only edits.
- Pure formatting changes.
- Tiny doc edits with no workflow or behavior impact.
- Mechanical changes fully covered by deterministic validation.

If sub-agent review is required but unavailable, record that as a review
limitation and compensate with narrower scope, stronger validation, or an
explicit blocker.

The record must include:

- Whether independent review was required.
- Whether a sub-agent or review tool was used.
- The exact reason independent review was skipped or unavailable.
- Which self-review passes were run instead.

## Local review passes

Run focused passes instead of one vague review:

1. Spec review: check acceptance criteria, non-goals, docs, and tests.
2. Harness review: check validation commands, observability, runtime evidence,
   and repeated manual checks that should become scripts or tests.
3. Architecture review: check boundaries, dependency direction, ownership,
   duplicated patterns, and hidden coupling.

Use a separate sub-agent or review tool for the focused passes when the policy
above calls for independent review. If not available, run the same passes
yourself and say that no independent reviewer was available.

## Evaluator calibration

An independent reviewer is not automatically skeptical. Reviewers can approve
shallow testing, praise generic output, or talk themselves out of real bugs.
When that happens, tune the review rubric before trusting future passes.

Calibrate the evaluator by:

- Reading review logs or comments for missed bugs, weak approvals, or vague
  praise.
- Turning subjective standards into concrete criteria and hard thresholds.
- Requiring the reviewer to exercise the running app, API, data state, or logs
  when runtime behavior matters.
- Adding edge cases that the reviewer skipped.
- Feeding corrected examples back into the review prompt, checklist, docs, or
  validation script.

For UI and product-quality work, grade functionality and craft, but also grade
whether the output has product depth and avoids generic default patterns. For
software correctness work, prefer criteria that can fail the change: missing
core interactions, stub-only behavior, untested data mutations, broken API
routes, hidden state mismatch, or shallow happy-path testing.

If a reviewer repeatedly approves work that later fails validation or human
review, treat that as a harness bug. Fix the rubric, prompt, test, script, or
runtime evidence requirement before relying on the same reviewer again.

## Prompt hygiene

Do not contaminate the independent review with the main agent's conclusion.
Pass raw artifacts and constraints, not the intended answer.

Provide:

- User request or feature brief.
- Relevant spec, plan, acceptance criteria, or issue.
- Diff or changed files.
- Validation commands and results.
- Runtime evidence, logs, screenshots, or traces when relevant.
- The exact review pass requested.

Avoid:

- Telling the reviewer what you think is wrong.
- Providing your preferred fix.
- Asking for agreement with your conclusion.
- Bundling several review goals into one vague prompt.
- Hiding known failures or unverified assumptions.

After review returns, the main agent must triage findings instead of accepting
them blindly.

## Sub-agent prompts

Use focused prompts like these:

```text
Review this change for spec compliance. Use only the provided request, spec,
diff, and validation output. Report missing acceptance criteria, undocumented
behavior changes, and tests that do not prove the user journey.
```

```text
Review this change for harness quality. Use only the provided diff, commands,
and runtime evidence. Identify repeated manual checks that should become tests,
scripts, docs, architecture checks, observability, or CI gates.
```

```text
Review this change for architecture drift. Use only the provided architecture
rules, diff, and validation output. Identify boundary violations, hidden
coupling, duplicated patterns, and unclear ownership.
```

## Prompt templates

Use these prompts for self-review when independent review is not required or
not available:

```text
Review this change for spec compliance. Focus on missing acceptance criteria,
undocumented behavior changes, and tests that do not prove the user journey.
```

```text
Review this change for harness quality. Identify repeated manual checks that
should become tests, scripts, docs, architecture checks, or observability.
```

```text
Review this change for architecture drift. Identify boundary violations,
hidden coupling, duplicated patterns, and unclear ownership.
```

## Feedback handling

For each finding:

- Fix it when it is correct and in scope.
- Add or update a test, script, doc, lint rule, or quality gate when the finding
  points to a recurring problem.
- Record it as an explicit blocker when it cannot be resolved in the current
  task.
- Ignore it only when the reason is concrete and documented.

Do not collapse all feedback into a vague "addressed review" note. Record the
important result: fixed, converted into harness, deferred with blocker, or
rejected with reason.

## Completion evidence

Before handoff, PR update, or final response, record:

- Review passes performed.
- Reviewer or tool used, if any.
- Whether sub-agent review was required, used, skipped, or unavailable.
- Findings fixed.
- Harness improvements added.
- Findings deferred or rejected, with reasons.
- Validation command and runtime evidence after review fixes.

If review changes behavior, rerun the relevant validation and update docs or
handoff before calling the task complete.
