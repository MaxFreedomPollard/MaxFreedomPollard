# Extract windows from composite solution histories

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and cleared **100% of Criteria V4 Step 0-3 + Scope Gate + Harbor (`19/19`) checks**, then stopped after `Solver B 0/2` (`133K-134K` tokens) fell below V4's 256K-token floor. Category: feature. Language: Python.

- Target repository: https://github.com/pybamm-team/PyBaMM pinned to commit `8c6816d27acb7c4b28b6222094da452f75202ac8`
- Hidden test suite: 88 test cases across 3 files, 1609 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 3 files, 459 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Criteria V4 automated checks | 100% Step 0-3 + Scope Gate + Harbor 19/19 PASS |
| Solver B rollouts | 0/2 (72/88 and 73/88 tests passed at 134.2K and 133.4K tokens, below V4's 256,000-token floor) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> When a model is solved, the solution is returned as a `Solution` object, and a list of times can be provided to initialize a solution with `sub_solutions`. New `Solution.window(start=None, stop=None)` slices closed `[start, stop]` (`None` uses `t[0]`/`t[-1]`, finite `Python`/`NumPy` real scalars not `bool`, bad or `start > stop` raises `SolverError`, no overlap returns `EmptySolution`).
>
> Nonempty `all_ts` segments in `[start, stop]` clip `all_ts` (endpoints + interior) with `all_models`/`all_inputs`:
>   `all_ys` -> cubic Hermite with `all_yps` (plus `yp`), else linear, with single-point `sol[var](t)`
>   `ProcessedVariableComputed` -> linear (`cumtrapz_ic` offsets kept), with linear available time-major `sensitivities` across `all_ts`
>
> `Solution` event metadata stays only if final `t` is in `[start, stop]`, and partial `time_indep` integrals raise `SolverError`:
>   `first_state` / `last_state` -> work with `sensitivities` where stored, else `SolverError`
>   `sub_solutions` / `cycles` / `steps` -> recursive `window()`, non-overlap and stale `summary_variables` dropped, independent copies of arrays/`all_inputs`

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
