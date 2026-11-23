# Add lexical defer statements to Luau

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and full 37-file lexer, parser, AST, typechecker, bytecode compiler, and VM implementation (`11/11` ASan-clean new tests, `1,216/1,216` baseline tests); stopped at Scope Gate because another platform author had also drafted a Luau `defer` task. Category: feature. Language: C++.

- Target repository: https://github.com/luau-lang/luau pinned to commit `c87565b8b0db5d5d5bfd2b8b00ad6573e5d06d9f`
- Hidden test suite: 11 ASan-clean F2P tests (+ 1,216 baseline tests) across 2 files, 889 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 37 files, 710 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Local verification | 11/11 ASan-clean F2P tests passing, 1,216/1,216 baseline tests passing |
| Platform status | Stopped at Scope Gate due to duplicate topic overlap with another author's draft |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add lexical `defer do ... end` scope-exit statements across Luau's parser, pretty printer, compiler, VM interpreter, type checker, and linter.
>
> `defer` is context-sensitive: only `defer do ... end` at statement start parses as defer, leaving `defer` usable as a variable, parameter, field, or function name. Defer bodies reject direct `return`, outer `break`, outer `continue`, and `...`, while nested loops or functions may use theirs. Pretty-printing (with/without CST) round-trips `defer do ... end`.
>
> Evaluating `defer` registers its body for enclosing block, loop iteration, or function exit; unreached defers never run. Defers execute LIFO, inner scopes first. Captured outer locals stay live by reference across mutations and escaping closures. Return expressions evaluate before defers run, preserving single and multiple returns if defers mutate returned locals.
>
> In `while`, numeric `for`, and generic `for` loops, `break` and `continue` run iteration defers before jumping. In `repeat ... until`, body defers run after `until`; `break` runs them immediately and `continue` unwinds inner blocks before `until`. Behavior holds across `-O0` through `-O2`.
>
> On errors, `xpcall` handlers run before unwinding; pending defers run LIFO up to `pcall`/`xpcall` or coroutine exit, propagating the latest unhandled error while remaining defers run. Yielding inside defer errors; yielding around defers preserves them until exit, uncaught error, or `coroutine.close` (returning `false` and the error on failure). Garbage-collected coroutines run no defers.
>
> Strict and nonstrict type checking (both solvers) and linting analyze defer bodies without leaking refinements. Native codegen (`--codegen`) and experimental coroutine finalizers are out of scope.

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
