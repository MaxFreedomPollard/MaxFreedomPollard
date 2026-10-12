# Stream distinct yielded resolutions with complete, transparent unsafe-cache outcomes

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-09-08** after human review. Category: feature. Language: JavaScript.

- Target repository: https://github.com/webpack/enhanced-resolve pinned to commit `aefeac310a824190502425fc89f0b72d0237dd18`
- Hidden test suite: 80 tests, 4137 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 19 files, 1315 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 1/10 = 10% |
| Platform difficulty band | hard |
| Median successful run | 583 LOC changed, 148 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/2 (3 is the top band), after 4 review rounds |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (1/10 solved)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **warn** (Passed with caveats)

The platform replaced its difficulty and long-horizon rows with new agent-pool rows on 2026-10-09, after this challenge was accepted, so `results/criteria.json` (read on 2026-10-12) lists those new rows as pending.

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add lazy streaming iteration for yielding resolutions. Fix yielded exports results, duplicate delivery and unsafe-cache transparency.
> 
> In asynchronous yielding mode across all resolver routes, every result goes to resolveContext.yield; successful completion returns undefined, and failures report their original error after any delivered prefix. Genuine exports misses still fail without deliveries.
> 
> Deliver each distinct path/query/fragment tuple once per resolution. Suppressed duplicates still count as found. Never expose internal restriction bookkeeping.
> 
> An ordinary fallback-only answer must not hide a package created before the next call. Keep ordinary and yielding entries separate.
> 
> For yielding resolutions, capture the complete described-resolve outcome. Include configured fallback even after a package yields, and eligible public after-described-resolve taps. Warm replay must deliver the saved results without invoking these sources again. Preserve the callback outcome separately from yielded values: yield-only completion allows parent routes to continue; a returned terminal request still stops them. Publish new yielding entries only after the whole resolution succeeds, not when an inner route completes. Failures retain their uncached prefix and leave no newly reusable answers.
> 
> Top-level consumer edits must not affect later deliveries or replays.
> 
> Provide Resolver.resolveIterator, package-level iterate and the create.iterate(options) factory. Resolution calls accept (parent, request, iteratorContext?) or (context, parent, request, iteratorContext?), preserving the corresponding promise API's context defaults. A file URL in the first argument is a parent, not a context object.
> 
> These requirements concern JavaScript runtime behavior; TypeScript declarations, synchronous resolution APIs and cache dependency capture or replay are outside this task. The iterator context accepts native AbortController signals. Every call returns a new self-iterating asynchronous iterator of full request objects, including path:false.
> 
> Only the first next starts resolution work; stream values before completion, including on cold cache misses. Match buffered values and outstanding reads FIFO. Success drains the buffer before done/undefined. On any resolver failure, including a synchronous startup throw after deliveries, first drain any buffered prefix. Then reject pending and subsequent reads with the original error.
> 
> return(value) discards buffered results and resolves pending reads as done with undefined; later reads are also done. It resolves its own call as done with value. throw(error) discards buffered results and rejects pending reads with that error; later reads are done. It rejects its own call with the same error. Both work before first next, ignore late producer activity and replace earlier errors with done.
> 
> Pre-abort prevents resolution. In-flight abort discards buffers and persistently rejects reads with an Error named AbortError, independent of signal.reason. Release signal listeners on success, failure, return, throw and abort. Abort after producer completion has no effect, even with buffered results.

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
