# Support multi-root module concatenation for shared chunks

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and cleared Criteria V4 quality checks, Scope Gate, and long-horizon rollouts (`Orion 339K-714K` tokens, `Vega 442K-561K` tokens on `v1`), with `v2g` verified across all 5 webpack `tsc` configs and `npm pack` before platform enrollment closed. Category: feature. Language: JavaScript.

- Target repository: https://github.com/webpack/webpack pinned to commit `a393e82c485374a74fc85c7894f0e4d9520d772e`
- Hidden test suite: 17 F2P tests (+ 722 baseline unit tests) across 2 files, 1938 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 14 files, 2760 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Criteria V4 quality checks | v1 cleared 7/7 checks + Scope Gate (0% overlap); v2 cleared Harbor Build Image, Verify Tests, Verify Solution, Flakiness 6x/6x, Description Quality, Reward Hacking, and local 5-config tsc + npm pack verification |
| V4 rollouts (v1) | Orion 0/4 (339K-714K compacted tokens, 10-14/17 tests), Vega 0/4 (442K-561K tokens, 2-13/17 tests); Fair task, No cheating, No env blockers, Long Orion runs all PASS |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> `optimization.concatenateModules` can concatenate modules when possible to generate less modules, more efficient code and enable more optimizations by the minimizer (an options object implies 'true'), yet when `optimization.splitChunks` splits chunks by shared modules and cache group (or behind a non-concatenated importer), independent ESM roots stay separate. Adding `multiRoot?: boolean` (`false` default, `webpack.validate()`) on `ConcatenateModulesOptions` hoists same-runtime roots in the same chunks like the referencing module into a `ConcatenatedModule`, and can also concatenate CommonJS modules with statically analyzable exports (`commonjs: false` disables). Stats add information about modules nested in other modules (like with module concatenation) (`nestedModules`) and show reasons why optimization bailed out for modules (`optimizationBailout`). External `require()`, `import()`, and `import defer` stay unexposed; subsets merge only when eager external deps are accessible in all chunks and each root's side-effect and cycle evaluation order holds.
>
> A concatenated CommonJS module relies on the root's ESM export rendering, so it can only be an inner module. With `{ multiRoot: true }`, every exposed root preserves standalone ESM export, re-export, and module namespace semantics across chunks and concatenated consumers. Builds still handle the this context correctly according to the spec for namespace objects (`strictThisContextOnImports`), inline ESM exports that bind to small primitive constants (`optimization.inlineExports`), rename exports when possible to generate shorter code (`optimization.mangleExports`), output javascript files as module source type (`output.module`), and cache generated modules and chunks to improve performance for multiple incremental builds (`cache`).

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
