# Support the eBPF CPU v4 instructions

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-09-28** after human review. Category: feature. Language: Rust.

- Target repository: https://github.com/qmonnet/rbpf pinned to commit `e3128159a7df1207104723b25ebe4ea6b172a677`
- Hidden test suite: 25 tests, 1861 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 6 files, 370 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-rust:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 1/20 = 5% |
| Platform difficulty band | hard |
| Median successful run | 733 LOC changed, 115 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/2 (3 is the top band), after 1 review round |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (1/19 solved)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **pass** (No false positives detected)

The platform replaced its difficulty and long-horizon rows with new agent-pool rows on 2026-10-09, after this challenge was accepted, so `results/criteria.json` (read on 2026-10-12) lists those new rows as pending.

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add the instructions that version 4 of the eBPF instruction set introduces to the verifier and to all three execution engines.
> 
> DIV and MOD with offset 1 are signed division and modulo. The quotient is truncated toward zero, the minimum value divided by -1 gives itself with a remainder of 0, division by zero gives 0 and modulo by zero keeps the dividend. For the signed forms in the 32-bit class, the kept dividend is its low 32 bits and the minimum value is 0x80000000. MOV from a register with offset 8 or 16, or 32 in the 64-bit class, copies the low 8, 16 or 32 bits of the source sign-extended to the width of the operation.
> 
> Loads with mode 0x80 exist only in the LDX class, in byte, half word and word sizes, and are the mode 0x60 loads of the same size except that they sign-extend the value to 64 bits. The END operation in the 64-bit class exists only with the K source, and swaps the bytes of the low 16, 32 or 64 bits named by the immediate and zeroes the bits above. JA in the JMP32 class jumps by its 32-bit immediate, and its offset field must be 0. The ebpf module exports the new mode as BPF_MEMSX (0x80) and the new opcodes as LD_B_SX_REG (0x91), LD_H_SX_REG (0x89), LD_W_SX_REG (0x81), BSWAP (0xd7) and JA32 (0x06).
> 
> The verifier rejects DIV and MOD offsets other than 0 and 1, a non-zero offset on MOV from an immediate, register MOV offsets other than 0 and those above, and any other byte-swap width. Any other field that a new instruction leaves unused, register numbers aside, may hold any value.

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
