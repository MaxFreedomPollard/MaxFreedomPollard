# Keep list numbering when Word lists are interrupted or restarted

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and complete implementation clearing Scope Gate and image verification before auto-archiving under Criteria V4's compact-repo Solver B horizon limit. Category: feature. Language: Python.

- Target repository: https://github.com/mwilliamson/python-mammoth pinned to commit `f3b7b9fc73fdbffe6ebac77e6b3ac6c418ee33d9`
- Hidden test suite: 2 test files, 1137 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 6 files, 115 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Platform checks completed | Scope Gate PASS, Image verification PASS |
| Platform status | Auto-archived on 2026-11-12; retired under Criteria V4's compact-repo Solver B horizon limit |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Mammoth should track counters per abstract numbering definition and level, with separate counters for the body, footnotes, endnotes and comments. Each level starts at w:start or 0 if omitted, the first paragraph using a w:num with w:startOverride on that level starts at the override value, and any list paragraph resets deeper levels of its definition.
>
> In HTML, the ol directly wrapping a numbered paragraph's li should get a start attribute when its first item isn't 1, and an item should merge into the preceding ol only when its number is one past the last item in that ol. Numbered paragraphs omitted from the output still consume their number, and Markdown output should count from the same start.

## What is in this folder

- `task.md`: the problem description the agent sees
- `REDACTED.md`: what was removed from this copy and why
- `Dockerfile`: builds the grading image from the pinned repo checkout
- `Makefile`: clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json`: challenge record (id, status, repo, pinned commit)
- `results/summary.json`: sanitized summary of platform checks, rollouts, review status, and patch hashes

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
