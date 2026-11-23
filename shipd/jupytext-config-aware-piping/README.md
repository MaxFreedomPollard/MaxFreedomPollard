# Support config-aware notebook piping and cell filtering

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and built and rolled out (`0/7` Solver B across `89K-114K` tokens) before being reverted/archived at the Criteria V4 cutover due to the new 256K-token Solver B floor. Category: feature. Language: Python.

- Target repository: https://github.com/jupytext/jupytext pinned to commit `932bcdb243842598acb00f6ab861b645bfc98b6a`
- Hidden test suite: 2 test files (100% statement and branch coverage on modified lines), 1498 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 5 files, 234 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Solver B rollouts | 0/7 passes (89,186 to 114,275 tokens) |
| Platform status change | Reverted and archived at Criteria V4 cutover (< 256,000-token Solver B floor) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> New `JupytextConfiguration` traits (`pipe_fmt=""` and `pipe_cell_filter=""`), CLI option `--pipe-cell-filter`, and new `pipe_notebook` parameters (`cell_filter` and `config`) default `pipe_fmt` to `"auto:percent"` in CLI `--pipe` and `--check` (or `"py:percent"` in `pipe_notebook`, skipping execution when no cells match).
>
> `combine_inputs_with_outputs` combines the text and metadata from the first notebook, with the outputs and metadata of the second notebook, using `cell_filter`, `parse_cell_filter` and `cell_matches_filter` on comma-separated `code`, `markdown`, `raw` and `tag:<name>` rules:
>   unset, "" or whitespace-only filter -> None; invalid or empty token or empty tag -> ValueError; no "-" match and a "+" or unprefixed match in each present group -> cell matches
>   selected output slot -> updated with matched piped cell or dropped if unmatched; unselected cell -> kept in place; unmatched source cell -> placed before next matched slot or at end
>   root_level_metadata_as_raw_cell -> explicit fmt > config > jupytext metadata; jupytext.root_level_metadata from piped output or source notebook -> preserved

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
