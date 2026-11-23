# Tagged limit exemptions, response-aware deduction costs, and CLI tag filtering

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and submitted to **Auto Review twice** (`r19`, `r20`: `agents` Band 3, `description` Band 3), then rebuilt to `R32` (`79/79` mutants killed) and cleared **100% of Criteria V4 Step 0-3 + Scope Gate checks** before stopping at V4's 256K-token Orion floor. Category: feature. Language: Python.

- Target repository: https://github.com/alisaifee/flask-limiter pinned to commit `0e715b6fbb4655756f747c78d95d61deaa69dd1c`
- Hidden test suite: 57 tests across 2 files (79/79 mutants killed), 5780 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 6 files, 449 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Auto Review (r19, r20) | agents Band 3, description Band 3 (rebuilt to R32 to resolve sibling-breach response-cost edge) |
| Criteria V4 quality checks (R32) | Prechecks 14/14 PASS, Scope Gate PASS, Verify Tests 114/57 PASS, Harbor PASS, Reward Hacking PASS, Solution Quality PASS, Test Quality PASS (0 blocking) |
| Sequential V4 rollouts (R32) | Nova 0/4, Orion 0/4 (105K-142K tokens across 20 runs, below V4's 256,000-token floor) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> `Limit`, `RouteLimit`, `ApplicationLimit`, `MetaLimit`, `RequestLimit`, `Limiter.limit`, and `Limiter.shared_limit` accept a new optional `tag` parameter (`None` when blank), propagated to `RequestLimit` during evaluation and breach. `Limiter.exempt` accepts a new `tags` parameter (`str` or `Iterable[str]`) that merges `ExemptionScope` flags per non-blank matching `tag`, adding no exemption if none remain, and Unicode whitespace is stripped across `tag`, `tags`, and CLI `--tag`. Nonzero route flags also exempt matching decorated limits, and tagged route flags beyond `DEFAULT | APPLICATION` exempt matching blueprint limits.
>
> Across non-meta limits and default or application `cost` settings, `cost` also accepts a new `Callable[[Response], int]`:
>   pre-request -> `cost <= 0` skips only the storage check, while `Callable[[Response], int]` gates without deducting
>   post-response -> for unbreached limits when `deduct_when` is `None` or truthy, deducts evaluated `cost > 0` and refreshes `current_limit` and `current_limits` window stats
>
> CLI `limits` and `clear` commands:
>   new `--tag` option -> filters matching limits when non-blank, omitting empty sections and unmatched routes unless `--endpoint` or `--path` is passed to `limits`
>   `limits` -> appends `tag: <tag>` to tagged limit options

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
