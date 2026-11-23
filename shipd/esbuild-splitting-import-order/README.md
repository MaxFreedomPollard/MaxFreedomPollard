# Preserve ESM module evaluation order with code splitting

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and cleared `15/15` Prechecks, Scope Gate, `Verify Tests`, `Verify Solution`, and `Verify Flakiness` across esbuild's linker and code-splitting chunk graph. Category: bug fix. Language: Go.

- Target repository: https://github.com/evanw/esbuild pinned to commit `f6058f8364fe7ab91ca57a83e02577ed74c9cae4`
- Hidden test suite: 24 F2P tests across 2 files, 1543 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 5 files, 1747 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Criteria V4 checks completed | Prechecks 15/15 PASS, Scope Gate PASS, Verify Tests PASS, Verify Solution PASS, Verify Flakiness PASS |
| Scope | 5 production files, +1,747 LOC in linker/chunking graph |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Consider this code bundled with `esbuild --bundle --outdir=build --format=esm --splitting --platform=node --out-extension:.js=.mjs ./entry1.js ./entry2.js` (or `api.Build` with `Bundle: true`, `Splitting: true`, `Format: api.FormatESModule`):
>
> ```js
> // entry1.js
> import "./init-dep-1.js";
> import "./run-dep.js";
>
> // entry2.js
> import "./init-dep-2.js";
> import "./run-dep.js";
>
> // init-dep-1.js
> globalThis.foo = { log: () => console.log("entry 1") };
>
> // init-dep-2.js
> globalThis.foo = { log: () => console.log("entry 2") };
>
> // run-dep.js
> globalThis.foo.log();
> ```
>
> `esbuild` moves `run-dep.js` into a shared chunk and imports it above `init-dep-1.js` and `init-dep-2.js`, crashing at runtime with `TypeError: Cannot read properties of undefined`.
>
> Please fix code-split ESM bundling so every entry runs its live modules in ECMA-262 `InnerModuleEvaluation` depth-first post-order. That covers entry-local setup, agreeing or conflicting shared chunks, diamonds (shared leaves run once), synchronous cycles, live `export let` bindings, top-level functions and classes, `export { ... } from`, `export * from`, top-level `await`, dynamic `import()` sharing modules with static entries, CommonJS imports, and static `External` imports ordered relative to both bundled modules and other externals.
>
> Keep shared modules in non-entry shared chunks instead of copying them into each entry, and keep existing splitting output when chunks only export pure literals or functions or already match ECMA-262 order. Unused modules and unused `/* @__PURE__ */` calls (including selective `sideEffects: false` barrels) must stay tree-shakeable, while live `/* @__PURE__ */` calls must not get reordered ahead of earlier modules. Default `.js`/`.mjs` extensions, `MinifyWhitespace`/`MinifyIdentifiers`/`MinifySyntax`, linked `Sourcemap` (`.map` files), and deduplicated `Metafile` external `imports` should all keep working.

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
