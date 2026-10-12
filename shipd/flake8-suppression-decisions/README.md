# Correct suppression decisions and explain hidden violations

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-09-17** after human review. Category: feature. Language: Python.

- Target repository: https://github.com/pycqa/flake8 pinned to commit `efe6750405be77b661f64e60002c4ef8e922daf5`
- Hidden test suite: 116 test functions (513 graded test cases), 3952 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 13 files, 798 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 1/10 = 10% |
| Platform difficulty band | hard |
| Median successful run | 560 LOC changed, 113 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/3 (3 is the top band), after 2 review rounds |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (1/10 solved)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **pass** (No false positives detected)

The platform replaced its difficulty and long-horizon rows with new agent-pool rows on 2026-10-09, after this challenge was accepted, so `results/criteria.json` (read on 2026-10-12) lists those new rows as pending.

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add `--suppression-report PATH`, also configurable as `suppression-report`, to audit hidden Flake8 violations. A relative PATH is resolved against the working directory in both forms.
> 
> Recognize a file directive only at the start of an own-line comment token. Use `\s*# flake8[:=]\s*noqa` without a word boundary after `noqa`. Both this expression and the file code-list prefix below use Unicode case-insensitive matching. A codeless directive anywhere suppresses the file. A coded directive suppresses nothing and generates E903 once at its line only if the file has no codeless directive; otherwise no E903 is generated. The file code-list prefix is `:[ \t]?[A-Z]+[0-9]+`, immediately after `noqa`; other suffixes make the directive codeless. If tokenization fails, every matching raw-line directive suppresses the file regardless of trailing codes. `--disable-noqa` disables file/inline suppression and E903, but leaves per-file ignores active.
> 
> Collect suppressed candidates from every analyzed input, including stdin and E902 read failures. When a report is requested, also run plugins in blanket-suppressed files that ordinary linting skips. Exclude only the additional plugin work from ordinary diagnostics, counts, statistics, benchmark totals and exit-status calculation. Audit only candidates (including E903) selected by shared configuration before per-file ignores. Record every independently sufficient reason: each blanket directive and the first inline noqa match in Flake8's physical-line span. For inline suppression, use only that first match; do not consider later matches, even if one lists the candidate's code. In a disk file that fails to tokenize, an inline noqa on the reported line still suppresses E999, as Flake8 does today, and the report records that inline reason. Choose the per-file mapping with the longest matching normalized pattern, breaking ties by configured order. For that candidate, record its original pattern only when the mapping ignores its code under Flake8's select/ignore precedence. Deduplicate reasons and order them as file directives by line, inline, then per-file.
> 
> The report is a JSON object with integer `version` equal to `1` and a `files` array. Each file object contains string `path` and a `suppressed` array of candidate objects. Candidates contain string `code` and `message`, integer `line >= 0` and `column >= 1`, and a nonempty `reasons` array. The minimum fields of each reason object are `kind: "file" | "inline"` and integer `line >= 1`, or `kind: "per-file"` and string `pattern`.
> 
> For each display name, emit the result from its last analysis, including an empty result. Always sort the `files` array by path. Sort fresh candidates by line, column, code, then message. Each requested report atomically replaces prior contents with the current invocation's complete output. With no analyzed files, write an empty `files` array. Any report write or replacement failure must produce a diagnostic and nonzero exit status, preserve existing report bytes and leave no temporary files.

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
