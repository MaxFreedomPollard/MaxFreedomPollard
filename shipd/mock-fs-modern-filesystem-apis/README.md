# Mock modern filesystem APIs

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and submitted for human review (`2026-09-17`, reviewed `2026-09-18`, `0/10` Luna) and revised across `fs.cp`, `fs.opendir`, `fs.statfs`, and recursive `fs.readdir`. Category: feature. Language: JavaScript.

- Target repository: https://github.com/tschaub/mock-fs pinned to commit `bbcea1835921cadc7edeeccbfa922cce5688ac0c`
- Hidden test suite: 2 test files, 956 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 6 files, 559 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Submission history | Submitted 2026-09-17, reviewed 2026-09-18 (qualityScore = 3); later dropped by Scope Gate cross-language overlap rule |
| Solver runs (Luna) | 0/10 passes |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add fs.cp, fs.opendir, fs.statfs and recursive fs.readdir to mock-fs.
>
> Directory copies require recursive. Reject self-copies and copies into the source tree. An existing destination directory is merged into; force and errorOnExist apply only to colliding files and symlinks. These are replaced unless force is false, which skips them or fails when errorOnExist is true. A directory and a non-directory never replace each other. Filters see every entry, the source included, and prune rejected entries with their subtrees. Copy symlinks as links: a relative target becomes an absolute path, resolved from the directory that holds the link, unless verbatimSymlinks preserves its text. preserveTimestamps retains modification times of files, directories and symlinks, merged directories included. Failures use Node's own fs.cp and fs.Dir error codes, and a colliding symlink fails like a file.
>
> Directory handles expose their opening path and support asynchronous iteration, which closes the handle after the last entry.
>
> statfs describes the whole mock file system: type zero, 4096-byte blocks, 1,000,000 blocks and 1,000,000 inodes, with bigint figures when requested. Every file, directory and symlink consumes one inode. Hard links share their inode and content blocks. Only file content occupies blocks, rounded up per file; all unused blocks are available.
>
> Recursive listings include all descendants, even beneath symlinked directories. With throwIfNoEntry false, statSync and lstatSync return undefined for a missing path, and statSync also for a path through a file.

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
