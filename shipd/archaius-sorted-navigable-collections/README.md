# Decode sorted and navigable collections

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-09-22** after human review. Category: feature. Language: Java.

- Target repository: https://github.com/netflix/archaius pinned to commit `f40de16d1c74ffd0efbd12b14342e78969a3d5bf`
- Hidden test suite: 31 tests, 997 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 4 files, 210 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-jvm:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 2/19 = 11% |
| Orion (platform strong solver, codex_cli / openai/gpt-5.6-luna) pass rate | 0/1 = 0% |
| Platform difficulty band | hard |
| Median successful run | 428 LOC changed, 165 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/3 (3 is the top band), after 1 review round |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (2/20 solved)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **pass** (No false positives detected)

The platform replaced its difficulty and long-horizon rows with new agent-pool rows on 2026-10-09, after this challenge was accepted, so `results/criteria.json` (read on 2026-10-12) lists those new rows as pending.

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Support SortedSet, NavigableSet, SortedMap and NavigableMap decoding. Unset configuration proxy methods returning these interfaces must yield empty collections. Fix the null default for methods declared to return Collection. Add forSortedSetOf, forNavigableSetOf, forSortedMapOf and forNavigableMapOf to ArchaiusType with Class and Type overloads. The new helpers reject a null type argument with a NullPointerException.
> 
> Add sparse descendant decoding for nested maps and collections, including containers whose intermediate properties are unset. For parameterized map or collection values, a map entry name is the nonempty segment up to the first dot or bracket. Scalar-valued map keys retain the entire suffix. Malformed paths contribute no children. Collection indices use canonical nonnegative decimal notation, contiguous from [0].
> 
> Explicit properties override descendants, including explicit empty strings. Treat containers with no decodable children as absent while retaining explicitly empty children.
> 
> Decode map keys through the configured Decoder's Type overload.

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
