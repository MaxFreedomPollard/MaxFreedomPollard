# Export under Parse key ownership

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **Auto Review approved (3/2/2)** on `2026-11-02` (`effectiveScope: meets_bar`), then held while iterating toward 3/3/3 until Criteria V4's 256K-token Orion floor retired compact Go packages. Category: feature. Language: Go.

- Target repository: https://github.com/caarlos0/env pinned to commit `505764460181dd3bfcd15b26dc7f63b7322737ad`
- Hidden test suite: 3 test files, 4823 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 2 files, 716 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Auto Review | approved, bands description/solution/tests = 3/2/2, effectiveScope = meets_bar |
| Platform quality checks | Verify Solution PASS, Verify Tests PASS, Verify Flakiness PASS, Solution Quality PASS, Test Fairness PASS |
| Platform status change | Archived after Criteria V4 cutover because compact ~2K-LOC Go libraries sit below V4's 256,000-token Orion floor |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Only field-owned keys consumed by Parse may be exported, and each value must satisfy both keyed and keyless prefix readers of its key. Export may refuse expand/file fields, slices of structs, parser-owned structs and pointers to those structs. Otherwise it succeeds exactly when a permitted map round-trips the source's non-ignored fields through ParseWithOptions under the same options. Empty successful exports return non-nil maps; failures return nil maps and errors naming all responsible fields. OnSet is ignored during export and readback. Nil slices and maps remain distinct from empty ones.
>
> Nonempty scalar spellings are fixed by underlying kind, including for named types with text methods: unchanged strings, true/false booleans, decimal integers, Go's default %g spelling of the underlying float32/float64 value, and time.Duration.String output. Collections use Parse's separator tags, with complete encoded map entries sorted before joining.
>
> Neither the source nor Options.Environment nor the process environment is modified; results are invariant under environment changes that preserve decoding semantics.
>
> Provide `Export(v interface{}) (map[string]string, error)` and `ExportWithOptions(v interface{}, opts Options) (map[string]string, error)`. The source is a non-nil struct pointer; other inputs and duplicate field-owned keys fail.

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
