# Detect resolution order, async, property mutability and abstract method API breakages

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and submitted for human review (`2026-08-25`..`28`), scored **perfect 3/3/3 (`overallQuality: 3`)**, and reached `finalizing_review` before an administrative platform revert (`managerVerdict: revert`). Category: feature. Language: Python.

- Target repository: https://github.com/mkdocstrings/griffe pinned to commit `a345344b40f50f8556ee5d08665880ff9251485f`
- Hidden test suite: 2 test files, 2427 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 11 files, 802 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Submission history | Submitted 2026-08-25 and 2026-08-28; reviewed 2026-08-30 |
| Review quality score | overallQuality = 3, qualityScore = 7 (top 3/3/3 bands) |
| Platform status change | Reached finalizing_review; administratively reverted to draft (managerVerdict = revert) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Extend API breakage checks with four kinds of change, for both source loading and runtime inspection. Both modes recognize properties built by calling property or abc's abstractproperty, and abc's abstractclassmethod and abstractstaticmethod. Member comparisons follow inheritance: compare overrides with the inherited members they replace, and dropped overrides with those then exposed. Each CLI comparison against a git reference inspecting both versions at runtime must read each from its own checkout without cached modules from the other.
>
> Report CLASS_CHANGED_MRO once per class when its old and new lists of resolved base paths in Class.mro() order differ at any depth. Omit unresolvable bases separately for each version. Complete comparisons and report all other breakages despite inconsistent MROs, import cycles or modeled unresolvable objects on either side; inconsistent MROs are not breakages.
>
> Report FUNCTION_CHANGED_ASYNC with boolean old and new states when functions change between synchronous and asynchronous, including generators and the underlying functions of plain, static or class methods.
>
> Report ATTRIBUTE_CHANGED_MUTABILITY when a property loses its writable (setter) or deletable (deleter) capability, even if it retains the other; gains are not breaking. Only name-binding statements replace properties, never bare annotations. Replacement by a non-property loses both. Removal still reports mutability loss beside OBJECT_REMOVED, with an empty new capability set.
>
> On each class, report CLASS_ADDED_ABSTRACT_METHOD once for each newly abstract method defined by its body, in name order; report the method's name. Inherited methods, property accessors, imported functions and already abstract methods do not count. Replacing an old imported abstract function with a body-defined abstract method counts. Unresolvable old members count as not abstract. Later deletion or rebinding in the module namespace does not change whether the class body defined the method.
>
> Export ClassChangedMroBreakage, ClassAddedAbstractMethodBreakage, FunctionChangedAsyncBreakage and AttributeChangedMutabilityBreakage from the package root and include them in __all__. Encode every breakage's as_dict as deterministic JSON with sorted capability lists. Add a json explanation style returning this encoding; griffe check in this style writes only one JSON array of all reported breakages to stdout (empty if none) and nothing to stderr.
>
> Extend every breakage dictionary with filepath and lineno for its object's file and line. For git comparisons, map temporary worktree paths to surviving files relative to the actual invocation directory. Removed objects have lineno 0. json_decoder reconstructs the class matching its kind, whose as_dict equals the input dictionary, restoring capability sets.
>
> Give griffe check repeatable --only and --ignore filters naming breakage kinds; --ignore wins overlaps. Filter reports, not detection. An empty filtered result exits 0. Reject invalid kind names with the name on stderr and exit code 2.

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
