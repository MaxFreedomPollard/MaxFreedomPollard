# Add sentence and paragraph movement to the Vi and Emacs key bindings

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-09-26** after Auto Review approval. Category: feature. Language: Python.

- Target repository: https://github.com/prompt-toolkit/python-prompt-toolkit pinned to commit `583b3412c792a5cc9f01adde603679f3824a88f3`
- Hidden test suite: 2 test files, 876 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 4 files, 276 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova pass rate | 4/10 = 40% |
| Platform difficulty band | medium |
| Median successful run | 359.5 LOC changed |
| Final review | approved (Shipd Bot Auto Review), bands description/solution/tests = 3/3/3 (3 is top) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Whitespace means characters for which str.isspace() is true, and a blank line is an empty or whitespace-only line. A sentence ends just after a '.', '!' or '?' and any following run of ')', ']', '"' and "'" characters when whitespace or the end of the text comes next, and just after the last non-whitespace character before each blank line and before the end of the text. Sentences start at the first non-whitespace character of the text and at the first non-whitespace character after each sentence end.
>
> Document gets find_next_sentence_start(count=1), find_previous_sentence_start(count=1) and find_next_sentence_end(count=1), returning the offset from the cursor to the count-th sentence start after the cursor, sentence start before it or sentence end after it, or to the end, start or end of the text when there are fewer, and 0 for a count below 1.
>
> Document also gets find_boundaries_of_current_sentence(count=1, include_whitespace=False), returning the start and end offsets from the cursor of a selection of parts, and (0, 0) for an empty text or a count below 1. The parts are the sentences, each running from a start to the next end, and the runs of whitespace around them; the part under the cursor is the one containing it or the last part.
>
> Without include_whitespace, the selection is count parts starting with that one, or as many as remain. With include_whitespace, on a sentence it is that sentence and the following sentences up to count in all, with the whitespace after the last or, when no whitespace follows it, the whitespace before the first; on whitespace it is the whitespace with the following sentences up to count or, when no sentence follows, with the one sentence before it if there is one.
>
> In Vi mode, the ( and ) motions move to the previous and next sentence start, and the is and as text objects select what find_boundaries_of_current_sentence gives without and with include_whitespace.
>
> Register named commands backward-sentence and forward-sentence, which move as find_previous_sentence_start and find_next_sentence_end give, kill-sentence and backward-kill-sentence, which kill to those positions, and backward-paragraph and forward-paragraph. The paragraph commands move to the count-th blank line above or below the cursor's line, or the farthest such line when there are fewer, keeping the cursor's column or stopping at the end of a shorter line, and to the start or end of the text when there is none. All six take the numeric argument as their count. Repeating a kill command adds the new text to the clipboard in text order, and backward-kill-sentence rings the bell when there is nothing to kill. Emacs mode binds the six commands to Meta-a, Meta-e, Meta-k, Ctrl-x Backspace, Meta-{ and Meta-}.

## What is in this folder

- `task.md`: the problem description the agent sees
- `REDACTED.md`: what was removed from this copy and why
- `Dockerfile`: builds the grading image from the pinned repo checkout
- `Makefile`: clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json`: challenge record (id, status, repo, pinned commit)
- `results/aggregate-stats.json`: solver pass/total and medians
- `results/criteria.json`: the platform's submission criteria record
- `results/nova-rollouts.csv`: one row per counted solver run (verdict, files, LOC, execution time, blocker flag)
- `results/review-outcomes.json`: sanitized review outcomes, per-field bands, and scores

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
