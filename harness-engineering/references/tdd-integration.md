# TDD integration

Use this reference when harness planning reaches feature or bugfix
implementation.

## Built-in TDD gate

Use this gate after planning and before implementation for feature work and
bugfixes, unless the user explicitly opts out. This reference is self-contained;
do not require a separate TDD skill before applying the loop.

Core principle: tests verify behavior through public interfaces, not
implementation details. A good test describes what the system does for a user,
API client, domain workflow, or CLI caller. It should survive internal
refactors.

Do not use horizontal slicing. Do not write all tests first and then all
implementation. Work vertically: one behavior test, one minimal implementation,
then the next behavior.

## Gate before implementation

Before writing implementation code, confirm:

- The public interface or user-visible behavior.
- The behavior that matters most.
- The first tracer-bullet test.
- How to run that test.
- What failure proves the RED step is real.
- The user-approved priority if there are several important behaviors.

Do not implement before the first failing test exists.

## Test shape

Prefer behavior tests through public interfaces:

- UI behavior through user-visible flows.
- API behavior through public endpoints or clients.
- Domain behavior through exported services or use cases.
- CLI behavior through commands and outputs.

Avoid tests that depend on private methods, internal collaborator calls, or
database state that bypasses the public behavior.

## Vertical TDD loop

Use this loop:

```text
RED: write one behavior test -> confirm it fails
GREEN: write minimal code -> confirm it passes
REFACTOR: improve design only while green -> rerun tests
```

Then repeat for the next behavior. Do not write all tests first and then all
implementation.

Per cycle, check:

- The test describes behavior, not private implementation.
- The test uses the public interface or closest stable boundary.
- The test would still pass after an internal refactor.
- The implementation is only enough to pass the current test.
- No speculative feature was added for a future test.

Refactor only while green. If a refactor breaks tests, stop refactoring and
restore green before continuing.

## Red flags

Stop and reset the loop when you catch one of these:

- Implementation code exists before the first failing test.
- The test asserts private methods, internal calls, or incidental database
  state instead of observable behavior.
- Several tests are written before the first implementation slice.
- Code is added for behavior that no current test or acceptance criterion needs.
- A RED state is described as complete without an explicit user-approved
  checkpoint.

## Git checkpoints

Do not push a RED state unless the user explicitly asks for a remote checkpoint
and the failure is documented. Prefer this sequence:

```text
RED: local only, record expected failure in the plan or handoff
GREEN: commit after the behavior passes
REFACTOR: commit after tests pass again
PUSH: only when the branch is shareable and handoff is updated
```

## Harness outputs

Record these in the feature plan or handoff:

- First behavior selected for TDD.
- Test command used.
- RED evidence.
- GREEN evidence.
- Remaining behaviors.
- Any testability or interface design issue discovered.
- Git checkpoint created or intentionally skipped.

If testability is poor, treat that as a harness finding: improve the public
interface, module boundary, fixture, seed data, or validation command.
