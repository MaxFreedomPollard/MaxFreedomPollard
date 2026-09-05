# Bind match capture patterns and comprehension walrus targets in scope metadata

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-08-18** after human review. Category: bug fix. Language: Python.

- Target repository: https://github.com/instagram/libcst pinned to commit `d9a255843b5cdbecc6834684d233bce1f2987f9d`
- Hidden test suite: 64 test functions, 910 added lines, plus a `test.sh` runner — **redacted from this copy, see `REDACTED.md`**
- Reference solution: 4 files, 146 added lines — **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 3/10 = 30% |
| Platform difficulty band | hard |
| Median successful run | 268 LOC changed, 60 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/3 (3 is the top band), after 1 review round |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (3/10 solved)
- Difficulty: **pass** (30% — Hard)
- Long-horizon: **pass** (Median files: 4, messages: 60, LOC: 268)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **warn** (Passed with caveats)

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Bind the names that match statement patterns capture in the metadata layer, and put assignment expression targets inside comprehensions in the scope PEP 572 assigns them. Today structural pattern matching is invisible to scope analysis, and a walrus target inside a comprehension is recorded in the comprehension's own scope. Fix both ScopeProvider and ExpressionContextProvider.
> 
> A match pattern binds exactly the names Python's own semantics say it binds, in the scope containing the match statement, with store context on the bound names, and nothing else. For example, `case [first, *rest]:` binds `first` and `rest`. Whatever the pattern evaluates as a value keeps its existing access behavior and context.
> 
> An assignment expression inside a comprehension or generator expression binds its target in the nearest enclosing non-comprehension scope, as PEP 572 specifies, so in `def f(data): return [y := g(x) for x in data]` the name `y` lands in the scope of `f`. For both constructs, every syntactic binding site records its own assignment, reads resolve to the assignments that precede them, and the results stay consistent with everything the scope model already does: its scope declarations, its visibility rules, its accesses and references, and its qualified names. Code that uses neither construct is analyzed exactly as before.

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
