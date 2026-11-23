# Producer partition pause flow control and selective unsent buffer abort

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and cleared **100% of Criteria V4 Step 0-3 + Scope Gate checks** (`574` baseline + `32` F2P tests) and `Nova 0/4` (`639.5K` avg tokens), before stopping at V4's 256K-token Orion floor. Category: feature. Language: Python.

- Target repository: https://github.com/dpkp/kafka-python pinned to commit `89df9871b84843ad8b9dbd48d5b8d11d06227acf`
- Hidden test suite: 32 F2P tests (+ 574 baseline tests) across 2 files, 2216 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 8 files, 513 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Criteria V4 automated checks | Prechecks 14/14 PASS, Scope Gate PASS, Verify Tests 574/32 PASS, Harbor PASS, Reward Hacking PASS, Solution Quality PASS, Test Fairness PASS (0 blocking) |
| V4 rollouts | Nova 0/4 (639.5K avg tokens); Orion avg 121.1K tokens (stopped below V4's 256,000-token floor) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> `KafkaProducer` and `RecordAccumulator` gain new `pause(*partitions)`, `resume(*partitions)`, `paused()`, and `abort_buffered(*partitions, error=None)` methods. All four raise `IllegalStateError` on closed `KafkaProducer`; non-`TopicPartition` partitions or non-`Exception` `error` instances raise `TypeError` before mutation, defaulting `None` to `Cancelled()`.
>
> `paused()` returns a `set` copy; paused partitions still buffer appends and expire at `delivery_timeout_ms`, while `ready()`, draining, and `AddPartitionsToTxn` skip them unless closed, completing a transaction, or `include_paused` is active, and `resume` wakes `Sender` on unpause. `KafkaProducer.flush` and `RecordAccumulator.begin_flush`/`await_flush_completion` gain a new `include_paused=False` flag draining and awaiting paused partitions when truthy without unpausing, as do `commit_transaction` and `close` for `timeout=None` or `> 0`. `DefaultPartitioner.partition` and `StickyPartitioner.partition`/`on_new_batch` gain a new `paused_partitions=None` `TopicPartition` iterable, forwarded by keyword while any partition is paused when accepted, excluding paused partitions for unkeyed records unless the whole pool is paused and rotating sticky state off them.
>
> `ProducerBatch` adds a new `is_unsent` property, `True` while incomplete and never drained, retried, or split from non-unsent batches; `RecordAccumulator.append` starts a new batch rather than coalescing into a non-unsent tail. `abort_buffered` aborts, closes, and deallocates only `is_unsent` batches on target or all partitions, dropping emptied unadded transaction partitions and returning the aborted record count.

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
