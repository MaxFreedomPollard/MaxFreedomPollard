# Lossless write-back of parsed SMBIOS structures

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-10-17** after Auto Review approval. Category: bug fix. Language: Go.

- Target repository: https://github.com/u-root/u-root pinned to commit `34ab3028053499999c2d8a00a02240fc6e6dbee7`
- Hidden test suite: 6 test files, 1501 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 14 files, 453 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Solver A pass rate | 0/8 = 0% |
| Solver C pass rate | 1/4 = 25% |
| Platform difficulty band | hard |
| Median successful run | 1004 LOC changed |
| Final review | approved (Shipd Bot Auto Review), bands description/solution/tests = 3/2/3 (3 is top) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Fix MarshalBinary for typed SMBIOS values parsed from a table (types 0 to 4, 7, 9, 14, 17, 38 and 43).
>
> MarshalBinary(v) = source bytes with v's edits written, if ParseTable then the type's parse function returns v on those bytes; otherwise an error:
>   written: field read at offset o -> written at o; header Length never written
>   skipped: field past the end of a short table -> not written, not compared, no lengthening
>   text unchanged -> number kept
>   text changed, the number names a string no other field of the parsed structure uses -> same number, replaced in place
>   text changed, number 0, a number naming no string, or a number shared in the parsed structure -> appended after the existing strings, in field order
>   text empty -> number 0, read back as Not Specified
>   string with no referrer left -> removed; each higher number -1, including a number that names no string
>   list gains or loses items -> Length += size difference; bytes after the list move with it
>   Info.Marshal -> entry point NumberOfStructs = structures written
>   struct literal, no parsed source -> toTable encoding for types 1, 2 and 14; empty embedded Table for the others
>   ReplaceSystemInfo, ReplaceBaseboardInfoMotherboard, RemoveBaseboardInfo, RemoveSystemSlotInfo -> rebuild only the structures they change, each under the same rule as MarshalBinary
>   RemoveBaseboardInfo -> also drops removed handles from every structure that lists them

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
