# Add Kostka-Foulkes polynomials

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and submitted on `2026-10-04` and reached `finalizing_review` before being reverted (`managerVerdict: revert`) after a strong-model pass-rate policy change. Category: feature. Language: Python.

- Target repository: https://github.com/sympy/sympy pinned to commit `3f58eb0ce808f8c4917ab0b8ae67d133fc794c3f`
- Hidden test suite: 78 tests across 2 files, 2351 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 5 files, 482 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Submission history | Submitted 2026-10-04; reached finalizing_review |
| Strong-model rollout check | 4/4 Solver B passes (median 495 LOC, 34.5 messages) |
| Platform status change | Reverted to draft (managerVerdict = revert) after the V2 strong-model pass-rate cutoff |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> kostka_foulkes(shape, content, t=Symbol('t'))
>     sum(t**charge(reading_word(T)) for T in SSYT(shape, content)) as a SymPy expression, S.Zero if there is no such T
>
>     float, complex or Decimal t is sympified first
>
>     must handle every content when: sum(shape) <= 16; or shape == (n,) or (1,) * n with n <= 2000; or sum(shape) <= 30 and content[6:] is all 1s
>
> charge(word)
>     Lascoux-Schutzenberger charge of word (up to 2000 letters), a tuple of positive integers with content(word) a partition
>
>     charge(word) == sum of index over each standard subword (right-to-left), index(1) == 0, index(r + 1) == index(r) + (pos(r + 1) > pos(r))
>
> IntegerPartition.kostka_foulkes(content, t) == kostka_foulkes(self, content, t)
>
> Parts: () or a weakly decreasing tuple of positive integers (shape and content); an IntegerPartition works wherever Parts does
>
> SSYT(shape, content) denotes the fillings T of the cells (i, j) with j < shape[i] by integers >= 1, T[i][j] <= T[i][j + 1], T[i][j] < T[i + 1][j] where both cells exist, and content[i] == number of entries equal to i + 1
> reading_word(T) denotes tuple(x for row in reversed(T) for x in row)
>
> module sympy.combinatorics.tableaux (new); kostka_foulkes and charge are exported from sympy.combinatorics

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
