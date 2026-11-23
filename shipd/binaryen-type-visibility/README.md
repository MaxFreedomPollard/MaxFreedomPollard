# Support type visibility annotations in open and closed world

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and cleared **10/10 Criteria V4 automated checks** (`15/15` Prechecks, Scope Gate, `467/23` tests, Harbor, Flakiness `6x/6x`, Description Quality, Solution Quality, Reward Hacking, Test Quality `0/0`) and solved `1/3` on Orion (`228.6K` tokens). Category: feature. Language: C++.

- Target repository: https://github.com/WebAssembly/binaryen pinned to commit `4408fed200e9a5fd1f5ea520a3b2707ad6500fb4`
- Hidden test suite: 23 F2P tests (+ 467 baseline tests) across 2 files, 2500 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 23 files, 645 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Criteria V4 automated checks | 10/10 PASS (Prechecks 15/15, Scope Gate, Verify Tests 467/23, Harbor Verify Solution, Flakiness 6x/6x, Description Quality, Solution Quality, Reward Hacking, Test Quality 0/0) |
| Orion rollouts | 1/3 solved (passing run: 228.6K tokens; stopped short of V4's 256,000-token floor due to C++ rebuild wall-clock budget) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> The `--closed-world` flag lets us assume that we can make arbitrary changes to types as long as those types are not part of the module's contract with the outside world. Otherwise a single `anyref` or `funcref` export blocks modifying struct, array, or referenced function types. New payload-free, non-conflicting WAT annotations `(@private)`, `(@protected)`, and `(@public)` attach before `(type ...)`:
>   `WAT` / `binary` -> explicit annotations round-trip via WAT printing, `ModuleUtils::copyModule`, `GlobalTypeRewriter`, and a consumed binary custom section
>   `WasmValidator` -> invalid if `(@private)` marks a type exposed or structurally reachable from exposed, `(@protected)`, or `(@public)` types
>
> In an open world, the outside environment may cast a publicized type down to any of its subtypes. Type visibility splits into `private` (definition and values internal), `protected` (definition fixed, values internal), and `public` (both external), where identity-only open-world dependencies and `--closed-world` boundary-reachable types default to `protected`:
>   `visibility` -> dependencies of `(@protected)`/`(@public)` stay at least `protected`, open-world `(@protected)` halts exposure, open-world `(@private)` keeps itself and unannotated dependents `private`, `(@public)` propagates exposure only in open world
>   `passes` -> `--gto`, `--signature-pruning`, `--cfp`, `--type-refining`, `--abstract-type-refining`, and `--type-merging` run in open world, while `--gufa` (with `--traps-never-happen` `call_ref`), `--gsi`, `--generate-global-effects`, and `--remove-unused-module-elements` gate external value, call, and field-read assumptions on `public` (including `public` supertypes/subtypes) rather than `WorldMode`

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
