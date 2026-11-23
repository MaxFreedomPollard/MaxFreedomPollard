# Add structured template diagnostics to Nunjucks errors

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and submitted for human review (`2026-08-31`, reviewed `2026-09-01`, `0/10` Luna) and revised through `2026-09-23`. Category: feature. Language: JavaScript.

- Target repository: https://github.com/mozilla/nunjucks pinned to commit `2025c933fba374482ef97122514bb36de6bf9de4`
- Hidden test suite: 4 test files, 2849 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 10 files, 502 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Submission history | Submitted 2026-08-31, reviewed 2026-09-01 (qualityScore = 4); revised through 2026-09-23 |
| Solver runs (Luna) | 0/10 passes |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Make rendering errors report where they happened.
>
> When a template renders synchronously, returning the result or passing it to a callback, an error raised by a function call, filter, property or name lookup, test, membership check written with in, or one of the engine's own checks should carry the position of the construct that raised it. Positions are the parser's lines and columns counted from one, with columns in UTF-16 code units, and an error reports the innermost construct that raised it: the tag name when a tag raises the error itself, and otherwise the lookup, call, filter, test or membership check that failed. When an output expression cannot be converted to text, or throwOnUndefined rejects an undefined value, the error reports where that output expression's opening braces stand.
>
> The error names the template whose source holds the failing construct: the entry template, an included template, the template defining an imported macro, or a parent or child in an inheritance chain, where a block's content belongs to the template that wrote it, including content reached through super, and a parent's own body belongs to the parent. A template that cannot be found or loaded, or a name that cannot be imported from it, is reported at the asking tag. A template that cannot be compiled when it is included, imported or extended reports its own path and the position the parser or compiler records for the failure, raised during the same call when rendering is synchronous. Text that cannot even be split into tags, such as a comment that never closes, is reported where the offending text begins, never borrowing another template's position.
>
> The thrown error exposes that template's path as templatePath, left undefined for a template without a path (null or undefined), the position as lineno and colno, and sourceExcerpt: the failing line preceded and followed by its immediate neighbours where the template has them, all exactly as written. The fields are the same in development and production modes and for templates compiled from strings, served by loaders that disable caching, or produced by precompileString. Include the original failure message when readable.
>
> An error that already carries Nunjucks attribution keeps its coordinates only when both are positive integers stored as primitive numbers. It also keeps its path and excerpt, and if Nunjucks has not reported it yet and it has no path, the template whose construct raised it supplies the path and any missing excerpt. Otherwise all four fields are assigned from the failing construct. Ignore diagnostic fields on other Errors without reading them, and report Error instances with frozen, sealed, non-extensible, read-only or accessor-protected properties without modifying them. Errors from other constructs, asynchronous filters, custom tags and Jinja compatibility mode are outside this change.
>
> Explain the fields in docs/api.md as defined above and describe the change in CHANGELOG.md, naming at least one field.

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
