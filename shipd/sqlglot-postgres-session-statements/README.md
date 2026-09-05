# Support postgres session statements and the @ and ^@ operators

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-08-15** after human review. Category: feature. Language: Python.

- Target repository: https://github.com/tobymao/sqlglot pinned to commit `896032a7aeec42dd4249b6c978cf291d71067660`
- Hidden test suite: 23 test functions, 354 added lines, plus a `test.sh` runner — **redacted from this copy, see `REDACTED.md`**
- Reference solution: 6 files, 276 added lines — **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 1/10 = 10% |
| Platform difficulty band | hard |
| Median successful run | 428 LOC changed, 101 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/3 (3 is the top band), after 2 review rounds |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (1/10 solved)
- Difficulty: **pass** (10% — Hard)
- Long-horizon: **pass** (Median files: 7, messages: 101, LOC: 428)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **pass** (No false positives detected)

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add support for these postgres session statements, plus the `@` unary operator and the `^@` binary operator.
> 
> `ABORT` and `ROLLBACK`, each optionally followed by `WORK` or `TRANSACTION`, generate `ROLLBACK`, keeping a trailing `AND CHAIN` or `AND NO CHAIN`. `START TRANSACTION` generates `BEGIN` with its characteristic list, so `start transaction read only` becomes `BEGIN READ ONLY`, and isolation levels, `READ WRITE`, `DEFERRABLE` and `NOT DEFERRABLE` survive a comma separated round trip.
> 
> `DECLARE` takes optional `BINARY`, `INSENSITIVE`, `ASENSITIVE`, `SCROLL` and `NO SCROLL` modifiers, and an optional `WITH HOLD` or `WITHOUT HOLD`, before its `FOR` query. `FETCH` and `MOVE` share one direction grammar: `NEXT`, `PRIOR`, `FIRST`, `LAST` and `ALL` stand alone, `FORWARD` and `BACKWARD` take an optional count or `ALL`, a bare count stands alone, and `ABSOLUTE` and `RELATIVE` each require a possibly negative count. Both verbs then name the cursor after `FROM` or `IN`, keeping whichever introducer was written, as in `fetch forward 5 from c`. `CLOSE` takes a cursor name or `ALL`. A cursor statement missing its introducer or cursor name, a required count after `ABSOLUTE` or `RELATIVE`, or its `CLOSE` argument is a parse error.
> 
> `LOCK TABLE` takes an optional `ONLY`, one or more tables, an optional lock mode from the eight modes `ACCESS SHARE` through `ACCESS EXCLUSIVE`, and an optional `NOWAIT`, so `lock table t nowait` is valid on its own, while `LOCK TABLE` without a table is a parse error. `DISCARD` takes `ALL`, `PLANS`, `SEQUENCES`, `TEMPORARY` or `TEMP`. `@ x` generates `ABS(x)` and takes the whole arithmetic or bitwise expression after it, so `@ a + b` generates `ABS(a + b)`. `x ^@ y` generates `STARTS_WITH(x, y)`, binds looser than arithmetic, bitwise and concatenation, and chains left to right, so `a + b ^@ c || d` generates `STARTS_WITH(a + b, c || d)` and `a ^@ b ^@ c` generates `STARTS_WITH(STARTS_WITH(a, b), c)`.
> 
> All of these generate using the dialect's normal SQL formatting, a semicolon separated script yields one parsed statement per statement, and `move`, `close`, `discard`, `abort` and `declare` remain usable as table, column, alias and function names.

## What is in this folder

- `task.md` — the problem description the agent sees
- `REDACTED.md` — what was removed from this copy and why
- `Dockerfile` — builds the grading image from the pinned repo checkout
- `Makefile` — clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json` — platform record (id, version, repo, commit)
- `results/criteria.json` — the platform's submission criteria at acceptance
- `results/aggregate-stats.json` — solver pass/total and medians
- `results/nova-rollouts.csv` — one row per solver run counted at acceptance (verdict, files, LOC, messages, time, blocker flag)
- `results/review-outcomes.json` — every human review round: outcome, per-field bands, scores

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
