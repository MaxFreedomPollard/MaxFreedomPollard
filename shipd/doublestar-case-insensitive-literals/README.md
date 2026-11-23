# Fix case-insensitive literal path resolution

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and submitted for human review on `2026-09-03` (`0/9` Luna) and revised through `2026-09-26` with VCA verification. Category: bug fix. Language: Go.

- Target repository: https://github.com/bmatcuk/doublestar pinned to commit `a9ad9e0ef4d6b7e4443090e9a7201d847a881711`
- Hidden test suite: 2 test files, 2764 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 6 files, 479 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Submission history | Submitted and reviewed 2026-09-03 (qualityScore = 4); revised through 2026-09-26 |
| Solver runs (Luna) | 0/9 passes |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Fix `WithCaseInsensitive` to resolve whole literals and literal components around wildcards and braces to every matching filesystem spelling. Literal equality uses `unicode.ToLower`; raw bracket ranges also match folded starts.
>
> Report distinct pathnames in directory-listing order. `GlobWalk` callback `SkipDir` returns leave independent spellings and brace alternatives eligible. Enabled filesystem errors precede every callback.
>
> After listing failure, the literal child's exact lookup determines success, absence or error. Within literal prefixes, deeper exact outcomes override ancestor refusals, even through symlinks. Resume folding below accessible directories, including after wildcards and braces.
>
> Each complete brace expansion has its own pre-wildcard literal prefix. `FailOnPatternNotExist` requires every folded spelling of that entire prefix to be absent; ignored I/O refusals are not absence. An unfinished prefix ending at a file is absent. File spellings cannot mask directories. Apply I/O options independently to every spelling's listings and exact lookups.
>
> Past the original first wildcard, `NoFollow` permits exact recovery only when symlink traversal is ruled out; unknown link status is unsafe. Otherwise apply the listing error and continue independent spellings. Braces and recovery never reset this boundary.
>
> `FilepathGlob` folds escaped, rooted and relative literal bases, including leading `..`. `Glob` and `GlobWalk` preserve requested trailing `/` on whole-literal directories.

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
