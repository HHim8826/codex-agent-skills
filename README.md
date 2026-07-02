# Codex agent skills

This repository contains reusable skills for keeping agent-driven software
projects understandable, verifiable, and maintainable. Each skill follows the
Agent Skills directory format and includes a `SKILL.md` entry point.

## Included skills

The repository currently provides two complementary skills:

- [`harness-engineering`](./harness-engineering/SKILL.md) helps you establish
  repository guardrails, validation, agent readability, runtime inspection,
  Git checkpoints, and durable handoffs.
- [`entropy-gc`](./entropy-gc/SKILL.md) helps you detect repository drift,
  prioritize cleanup work, and turn recurring findings into enforceable
  project checks.

## Installation

To install all skills for one project, clone this repository into that
project's `.agents/skills` directory:

```shell
git clone https://github.com/HHim8826/codex-agent-skills.git .agents/skills
```

If `.agents/skills` already exists, clone the repository elsewhere and copy
only the skill directories you need. Keep each `SKILL.md` at
`.agents/skills/<skill-name>/SKILL.md`.

## Usage

Codex loads a skill when your request matches the trigger in its `description`
frontmatter. You can also name a skill directly in your request, such as:

```text
Use $harness-engineering to plan this repository migration.
```

Open a skill's `SKILL.md` to review its workflow, then load only the referenced
files that match your current task.

## Validation

Run these checks from the repository root before publishing changes:

```shell
python harness-engineering/scripts/check_workflow_contract.py
python -m py_compile harness-engineering/scripts/check_workflow_contract.py
python -m py_compile entropy-gc/scripts/entropy_scan.py
python entropy-gc/scripts/entropy_scan.py --help
```

## License

This repository is available under the [MIT License](./LICENSE).
