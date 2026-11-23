# Add form and field change tracking, partial patching, reset, and commit

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **Auto Review approved on 2026-10-28** (entered `finalizing_review`; later reverted to draft at the 2026-11-17 Criteria V4 cutover due to the new 256K-token Solver B sequence floor). Category: feature. Language: Python.

- Target repository: https://github.com/pallets-eco/wtforms pinned to commit `46f626e5cd1faa841927d2dd14f8752d183f5077`
- Hidden test suite: 64 tests across 2 files (later expanded locally to 69 tests with 68/68 mutants killed), 4373 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 5 files, 386 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Solver A pass rate | 0/27 = 0% |
| Solver B pass rate | 1/4 = 25% (passing run: 1,232 LOC, 47 messages, 105K tokens) |
| Solver C pass rate | 0/4 = 0% |
| Auto Review | approved (Shipd Bot), bands description/solution/tests = 3/2/2 (3 is top) |
| Platform status change | Entered finalizing_review on 2026-10-28; reverted at the 2026-11-17 Criteria V4 cutover (+250t compensation) because Solver B solved below V4's new 256,000-token floor |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> On `BaseForm` and `FormField`, `initial_data` maps each field name to its `initial_data`, `changed` is `True` when any field has `changed`, `changed_fields` lists changed field names in field order, and `changed_data` and `changes` map each changed field name to its `changed_data` (for a `FormField`, or `data` otherwise) and `changes`. In `Field.process`, `initial_data` stores an independent copy of the `process_data` and filter result on initial data or default before `formdata`, while `FieldList.process` sets `initial_data` to the baseline entry values from initial data or default padded to `min_entries`. On `Field` and `FieldList`, comparing `data` with `initial_data` treats `float` and `Decimal` `NaN` values as equal (recursively in `list`, `tuple`, and `dict` values); `changed` is `True` when `data` differs from `initial_data` (or on `FieldList` when any entry has `changed`), and `changes` returns `(initial_data, data)` when `changed` or `None` otherwise.
>
> `BaseForm.patch(formdata=None, obj=None, data=None, extra_filters=None, **kwargs)` and `patch(formdata=None, data=unset_value, extra_filters=None)` on `Field`, `FormField`, and `FieldList` apply partial updates without altering `initial_data`, running filters in `process()` order and `post_process(formdata)` when updated (or on `BaseForm.patch` even when no field matches). With non-`None` `formdata`, `patch` updates only matched fields or sorted indexed `FieldList` entries matching `separator`-prefixed keys in `formdata` and appends `FieldList` entries past `len(entries)` up to `max_entries`. Without `formdata`, `patch` updates only fields matched from `obj`, `kwargs`, or `data` in order, where an iterable `FieldList` sequence updates and resizes entries between `min_entries` and `max_entries` (raising `TypeError` if non-iterable).
>
> On `BaseForm`, `FormField`, `FieldList`, and `Field`, `reset()` restores `data` and `FieldList` entries from `initial_data`, sets `raw_data` to `None`, clears `errors`, `process_errors`, and `form_errors`, and runs `post_process(None)` once per field, while `commit()` advances `initial_data` to an independent copy of `data` across the target and nested fields or entries without clearing `raw_data` or errors.

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
