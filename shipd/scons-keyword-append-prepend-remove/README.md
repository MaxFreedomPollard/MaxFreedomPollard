# Append, prepend and remove through keyword values

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-10-16** after Auto Review approval. Category: feature. Language: Python.

- Target repository: https://github.com/scons/scons pinned to commit `80c749ed90adc3cf623b5dfa206917067f3b5677`
- Hidden test suite: 2 test files, 1239 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 5 files, 302 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Solver A pass rate | 0/8 = 0% |
| Solver B pass rate | 0/4 = 0% |
| Solver C pass rate | 1/4 = 25% |
| Platform difficulty band | hard |
| Median successful run | 868 LOC changed, 88 agent messages |
| Final review | approved (Shipd Bot Auto Review), bands description/solution/tests = 3/3/2 (3 is top) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> `Append`, `Prepend`, `AppendUnique`, `PrependUnique` and `Remove` become `SCons.Script` globals; as keyword values (wrappers) they work in `Environment()`, `Clone()` and builder calls. A wrapper calls the environment's same-named method with its unexpanded value and option (`delete_existing` or `missing_ok`, default `False`).
>
> Order: `variables=`, `parse_flags=` and plain keywords first, then wrappers in keyword order; surviving builder-default wrappers run before call-provided ones, and a call value replaces the same variable's default.
>
> `env.Remove(missing_ok=False, **kwargs)` removes every occurrence equal to each keyword's value from that variable while survivors keep order. A missing value raises `ValueError`, an unset variable `KeyError`; `missing_ok` true skips both, and every removal is checked before anything changes.
>
> `str` and `CLVar` targets and requests both go through `Split()`, with `str` targets rejoining with single spaces. For a list, deque, tuple or dict target, a `str` request is one element or key, such containers or `CLVar` supply elements or keys, and any other request is one item; target type is kept (tuples becoming plain tuples), and other targets raise `TypeError`.

## What is in this folder

- `task.md`: the problem description the agent sees
- `REDACTED.md`: what was removed from this copy and why
- `Dockerfile`: builds the grading image from the pinned repo checkout
- `Makefile`: clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json`: challenge record (id, status, repo, pinned commit)
- `results/aggregate-stats.json`: solver pass/total and medians
- `results/criteria.json`: the platform's submission criteria record
- `results/solver-rollouts.csv`: one row per counted solver run (verdict, files, LOC, execution time, blocker flag)
- `results/review-outcomes.json`: sanitized review outcomes, per-field bands, and scores

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
