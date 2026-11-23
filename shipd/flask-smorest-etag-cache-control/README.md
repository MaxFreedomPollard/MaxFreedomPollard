# Conditional ETag and Cache-Control lifecycle

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and complete implementation with `103` F2P tests (`100%` statement and branch coverage on modified lines); auto-archived before Criteria V4 because compact ~2.5K-LOC libraries sit below the 256K-token Solver B ceiling. Category: feature. Language: Python.

- Target repository: https://github.com/marshmallow-code/flask-smorest pinned to commit `2a0dc534586cf37742e3a2c59c36b8a5066446f7`
- Hidden test suite: 103 F2P tests across 2 files, 4219 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 4 files, 396 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Local verification | 103 F2P tests passing, 100% statement and branch coverage |
| Platform status | Auto-archived on 2026-11-12; retired under Criteria V4's compact-repo Solver B horizon limit |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> ETag is a web cache validation mechanism. It allows an API client to make conditional requests. The ETag feature is available through the `Blueprint.etag` decorator (`enabled`, `weak`, `include_headers`), `Blueprint.cache_control`, and `Blueprint` (`etag`, `etag_weak`, `etag_include_headers`, `cache_control`), applying outer-to-inner across nested blueprints, `MethodView`, and view functions for any decorator or `register_blueprint` order:
>   check_etag (optional weak=False) -> strong If-Match check
>   set_etag and auto-ETag -> resolve weak (explicit>endpoint>blueprint>False) and case-insensitive include_headers in response.headers order, with weak If-None-Match checks
>
> `Cache-Control` directives (strings, mappings, iterables, or kwargs) with stripped lowercase `"_"`->`"-"` names merge in place across layers (or clear on `False`):
>   formatting -> True/"" formats as name, int>=0 as name=val (ValueError if <0), and str as name="val" (if whitespace/comma) or name=val
>   updating -> False/None removes keys, and public/private are mutually exclusive
>
> When ETag is computed with response data, that data may contain headers. It can be disabled globally with the `ETAG_DISABLED` application parameter across sync/async views and OpenAPI specs:
>   200<=status_code<400 -> sets non-empty Cache-Control on the response when absent before automatic ETag computation
>   304 NotModified(headers=None) -> includes ETag plus active Cache-Control

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
