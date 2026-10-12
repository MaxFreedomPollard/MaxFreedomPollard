# Recognise default arms in the inside, matches and generate case forms, and require begin and end after do, repeat and final

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-09-23** after human review. Category: feature. Language: C++.

- Target repository: https://github.com/chipsalliance/verible pinned to commit `6cce8f192b55640ddd5221b926cc952d979aa2b7`
- Hidden test suite: 59 tests, 3690 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 4 files, 386 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 1/10 = 10% |
| Platform difficulty band | hard |
| Median successful run | 987 LOC changed, 215 agent messages |
| Human review | approved, bands description/solution/tests = 2/3/3 (3 is the top band), after 1 review round |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (1/10 solved)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **warn** (Passed with caveats)

The platform replaced its difficulty and long-horizon rows with new agent-pool rows on 2026-10-09, after this challenge was accepted, so `results/criteria.json` (read on 2026-10-12) lists those new rows as pending.

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Extend case-missing-default to cover inside, matches and generate cases, retaining qualifier exemptions and excluding randcase.
> 
> Require direct begin/end bodies for do, repeat and final in explicit-begin, with independent, enabled-by-default do_enable, repeat_enable and final_enable switches. Direct means begin follows the keyword, or repeat's condition, with only comments between. Exclude assignment/nonblocking-trigger repeat controls, production repeats of any randsequence, however nested, and deferred-assertion final. These exclusions do not cover procedural statements inside randsequence code blocks or standalone repeat loops with event-controlled bodies.
> 
> Only a do-loop's terminating while is exempt from while diagnostics, and no switch changes which while that is. A do-loop's body is one statement of any kind; a label, attribute or qualifier before it is part of that statement. It ends at the end, join, join_any, join_none, endcase or endsequence that closes it, including any end label, after the last branch of an if or assertion, after a nested loop, or otherwise at its semicolon. A complete preprocessor conditional is one body. A standalone macro call or directive needs no semicolon, but a macro call that ends a line inside a longer statement does not end it.
> 
> In explicit-begin, a macro call ending at a line break must not hide diagnostics for its containing statement or subsequent statements. Recognize optional with-variable lists, nested/assignment-pattern braces and semicolon-ended constraint prototypes, so statements after a constraint stay checkable; constraint if/else clauses are not procedural statements.

## What is in this folder

- `task.md`: the problem description the agent sees
- `REDACTED.md`: what was removed from this copy and why
- `Dockerfile`: builds the grading image from the pinned repo checkout
- `Makefile`: clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json`: platform record (id, version, repo, commit)
- `results/criteria.json`: the platform's submission criteria record
- `results/aggregate-stats.json`: solver pass/total and medians
- `results/nova-rollouts.csv`: one row per solver run counted at acceptance (verdict, files, LOC, messages, time, blocker flag)
- `results/review-outcomes.json`: every human review round: outcome, per-field bands, scores

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
