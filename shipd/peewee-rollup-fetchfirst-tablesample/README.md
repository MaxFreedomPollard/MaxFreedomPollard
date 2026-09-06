# Add ROLLUP, FETCH FIRST and TABLESAMPLE support to the query builder

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-08-20** after human review. Category: feature. Language: Python.

- Target repository: https://github.com/coleifer/peewee pinned to commit `349997736ba294bba7624589c7b17deab141d9e0`
- Hidden test suite: 73 test functions, 1133 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 4 files, 454 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 1/12 = 8% |
| Platform difficulty band | hard |
| Median successful run | 323 LOC changed, 90 agent messages |
| Human review | approved, bands description/solution/tests = 3/2/2 (3 is the top band), after 4 review rounds |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (1/12 solved)
- Difficulty: **pass** (8%, Hard)
- Long-horizon: **pass** (Median files: 2, messages: 90, LOC: 323)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **pass** (No false positives detected)

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add support for five SELECT constructs whose grammar differs by backend.
> 
> Rollup accepts expressions or nested tuples and renders inside GROUP BY, composing with plain grouping expressions and with each other. On PostgreSQL, group_by(Rollup(region, product)) generates GROUP BY ROLLUP(region, product). On MySQL a rollup generates the postfix form GROUP BY region, product WITH ROLLUP; there it must be the only grouping expression, and combining it with ORDER BY raises ValueError at SQL generation. Each form has its own toggle, and either alone means rollup is supported; a backend with neither raises ValueError.
> 
> fetch_first(n, with_ties=False) generates OFFSET m FETCH FIRST n ROWS ONLY, or ROWS WITH TIES, on PostgreSQL, and plain fetch_first generates LIMIT n elsewhere; like limit(), passing no value clears it. WITH TIES requires ORDER BY and raises ValueError where unsupported, and combining limit() with fetch_first() raises ValueError at SQL generation on every backend. fetch_first applies to compound selects too, rendering after the whole compound. The conflict rule is judged per query: an operand's own limit() coexists with the compound's fetch_first, while both on the compound itself conflict. An operand's own fetch_first stays scoped to that operand, grouped wherever an operand-level limit would be. first() and exists() replace the clause with a LIMIT of their own row count, count() preserves the ordering WITH TIES depends on, count(clear_limit=True) clears the clause as it clears a limit, and prefetch wraps a parent carrying the clause in a derived table as it does one carrying a limit.
> 
> TableSample(source, method, *arguments, seed=None) renders on PostgreSQL after its source as TABLESAMPLE method(arguments) with an optional REPEATABLE (seed), keeping the method name as written; arguments and seed that are expressions render as SQL, and other values become bind parameters. The source must be a physical table, which may be aliased, or a join whose right-hand side is one, the clause rendering immediately after that table's alias, ahead of any join predicate, the join unchanged. A subquery, values list, CTE or other non-table source raises ValueError at SQL generation, as does TableSample elsewhere.
> 
> Function.within_group(*ordering) renders an ordered-set aggregate's ordering outside the argument list, as percentile_cont(0.5) WITHIN GROUP (ORDER BY qty), on PostgreSQL only, and precedes any FILTER clause. The existing order_by() places its ordering inside the argument list, so the two are mutually exclusive and setting both raises ValueError, as does rendering on a backend without support.
> 
> is_distinct_from(rhs) and is_not_distinct_from(rhs) are added, matching a NULL operand where = and != drop it. Each backend's accepted spelling is generated: the standard a IS DISTINCT FROM b, MySQL's a <=> b, which carries the NOT DISTINCT sense so the plain form renders NOT (a <=> b), and SQLite's a IS NOT b. A backend with none raises ValueError.
> 
> Backend support is expressed as Database feature toggles groupby_rollup, groupby_rollup_postfix, fetch_first_clause, tablesample, ordered_set_aggregates and distinct_from_syntax, the last carrying DF_STANDARD, DF_NULL_SAFE_EQ or DF_IS_NOT rather than a boolean. Rollup and TableSample are exported from the module root.

## What is in this folder

- `task.md`: the problem description the agent sees
- `REDACTED.md`: what was removed from this copy and why
- `Dockerfile`: builds the grading image from the pinned repo checkout
- `Makefile`: clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json`: platform record (id, version, repo, commit)
- `results/criteria.json`: the platform's submission criteria at acceptance
- `results/aggregate-stats.json`: solver pass/total and medians
- `results/nova-rollouts.csv`: one row per solver run counted at acceptance (verdict, files, LOC, messages, time, blocker flag)
- `results/review-outcomes.json`: every human review round: outcome, per-field bands, scores

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
