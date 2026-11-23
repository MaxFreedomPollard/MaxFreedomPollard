# Add $state.from custom accessor rune

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and cleared **100% of Criteria V4 pre-rollout gates** (`15/15` Prechecks, Scope Gate, `7/7` dynamic checks with `0` Test Quality warnings) across 45 compiler, parser, and runtime files before stopping at V4's 256K-token Solver B floor. Category: feature. Language: TypeScript.

- Target repository: https://github.com/sveltejs/svelte pinned to commit `8720544ff76456198c8b434d09e8b4a8b59d3b8c`
- Hidden test suite: 22 F2P tests across 2 files, 3011 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 45 files, 793 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Criteria V4 automated checks | 100% PASS (Prechecks 15/15, Scope Gate, 7/7 dynamic checks, 0 Test Quality warnings) |
| Solver B #1 rollout | 21/22 tests passed (605 LOC across 66 files, 163K tokens, stopped below V4's 256,000-token floor) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> The `$state` rune allows you to create reactive state, which means that your UI reacts when it changes. New `$state.from(accessor)` (`declare namespace $state`, `{ get(): T; set?: (value: NoInfer<T>) => void }`) does not proxy or mutate the original object (client and SSR). When calling methods in JavaScript, the value of `this` matters (`this === accessor`):
>   `accessor.get()` -> uncached dynamic lookup, init throws `TypeError` unless non-`null` object with `function` `get`
>   `accessor.set(v)` -> dynamic lookup returning `v` (`TypeError` if not `function`), client writes in `untrack` under `$state` `state_unsafe_mutation` rules
>
> Class instances are not proxied. Instead, you can use `$state.from` in class fields (whether public or private), or as the first assignment to a property immediately inside the `constructor`. You can declare `$state.from` in `.svelte.js` and `.svelte.ts` files or other `$state` scopes (hoisted `var` reads `undefined` before init), and you can update it like you would update any other variable:
>   `++` / `bind:` -> JS assignments/updates (short-circuit ops, `number`/`bigint` `++`/`--`), `$state` bindings/runes, and component exports (`get` always, `set` if non-`const`)
>   `state_invalid_*` -> reuse `$state` diagnostics, except 1 arg (`rune_invalid_arguments_length`), no destructuring (`state_invalid_placement`), no module exports even `const` (`state_invalid_export`), `state_referenced_locally` like `$state.raw`

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
