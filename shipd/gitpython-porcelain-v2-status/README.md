# Add typed repository status snapshots from Git porcelain v2

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-09-25** after human review. Category: feature. Language: Python.

- Target repository: https://github.com/gitpython-developers/gitpython pinned to commit `db47516dac750c5968b8f6d388b18712c355df50`
- Hidden test suite: 51 test functions (421 graded test cases), 927 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 4 files, 276 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 4/10 = 40% |
| Platform difficulty band | medium |
| Median successful run | 413.5 LOC changed, 55 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/3 (3 is the top band), after 1 review round |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (4/10 solved)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **pass** (No false positives detected)

The platform replaced its difficulty and long-horizon rows with new agent-pool rows on 2026-10-09, after this challenge was accepted, so `results/criteria.json` (read on 2026-10-12) lists those new rows as pending.

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add Repo.status_snapshot() from Git porcelain v2 NUL output, enumerating nested untracked files individually while reporting an ignored directory as one directory path. Return StatusSnapshot with branch_oid, branch_head and upstream (None if absent), ahead, behind and stash_count (zero if absent), and entries (a tuple in Git's order); empty output yields that all-default snapshot. Map (initial) branch OID and (detached) head to None; ignore unknown # headers.
> 
> StatusEntry has kind ('1', '2', 'u', '?', or '!'), path, original_path, xy, submodule, modes, object_ids, and score. Paths and branch names must round-trip through os.fsencode. Tracked modes and object_ids keep Git field order as tuples (three modes/two OIDs for 1/2; four modes/three OIDs for u). Type 2 stores its raw R.../C... score and reads original_path from the next NUL field. Other kinds set original_path and score to None; ?/! also set xy and submodule to None and both tuples to empty.
> 
> Validate: XY is two chars from .MADRCUT; submodule is N... or S[C.][M.][U.]; modes are six octal digits; OIDs are 40/64 hex digits; type-2 score is R/C plus ASCII decimal 0-100. Header counts require ASCII decimal digits and +ahead -behind. Counts and scores may have leading zeros and any number of digits. Headers start with # and one ASCII space; a known key is then followed by one ASCII space and a value that does not start with a space, and branch.head and branch.upstream values run to the end of the record. Repeated well-formed known headers are accepted. Record fixed fields use exactly one ASCII space between tokens. Raise ValueError on malformed known headers or records, unknown kinds, empty paths, stray empty NUL fields, and truncated output (a single trailing line feed is ignored); a failing git status raises GitCommandError whatever it printed. Export both types from git.repo and git, including __all__; both imports must resolve from the working tree when `python -m pytest` runs at the repository root.

## What is in this folder

- `task.md`: the problem description the agent sees
- `REDACTED.md`: what was removed from this copy and why
- `Dockerfile`: builds the grading image from the pinned repo checkout
- `Makefile`: clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json`: platform record (id, version, repo, commit)
- `results/criteria.json`: the platform's submission criteria record
- `results/aggregate-stats.json`: solver pass/total and medians
- `results/nova-rollouts.csv`: one row per solver run counted at acceptance (verdict, files, LOC, messages, time, blocker flag)
- `results/review-outcomes.json`: every human review round: outcome, per-field bands, scores

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
