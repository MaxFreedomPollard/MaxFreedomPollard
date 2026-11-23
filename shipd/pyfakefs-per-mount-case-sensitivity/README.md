# Case sensitivity per mount point and Unicode name matching on macOS

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and cleared **100% of Criteria V4 pre-rollout gates** (`97` F2P tests, `0` warnings) on `R30`, then stopped after `Solver B #1` passed legitimately in `116.2K` tokens (below V4's 256K floor). Category: feature. Language: Python.

- Target repository: https://github.com/pytest-dev/pyfakefs pinned to commit `f43fce450a7b53fe27a5b99ca5ef5494c22eee72`
- Hidden test suite: 97 F2P tests, 2536 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 3 files, 198 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Criteria V4 automated checks (R30) | 100% pre-rollout gates PASS (0 warnings) |
| Solver B #1 rollout | 1/1 PASS_LEGITIMATE (116,214 tokens, below V4's 256,000-token floor) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Under Linux and macOS, the root path (`/`) is the only mount point created in the fake file system. If you need support for more mount points, you can add them using `FakeFilesystem.add_mount_point(path, total_size=None, can_exist=False, case_sensitive=None)` with a new last parameter `case_sensitive=None`:
>   case_sensitive=None -> follows is_case_sensitive (including later changes)
>   case_sensitive=True / False -> overrides is_case_sensitive for that mount point
>
> Each path component in path APIs and public `FakeDirectory` methods (`add_entry`, `get_entry`, `remove_entry`) is checked by the mount point holding its directory:
>   case-insensitive -> str.lower() comparison
>   OSType.MACOS -> equal NFD forms match under either case policy (OSType.LINUX and OSType.WINDOWS do not normalize)
>
> For matching spellings in the same directory, directory listings keep the stored name and new-entry creation raises `FileExistsError`. Renaming when old and new paths differ only by a matching final name:
>   case-insensitive mount -> stores the new spelling in place
>   case-sensitive mount -> leaves the entry unchanged

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
