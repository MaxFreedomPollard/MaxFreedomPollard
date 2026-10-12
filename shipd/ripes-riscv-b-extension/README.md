# Add the RISC-V B bit-manipulation extension

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **accepted on 2026-10-07** after human review. Category: feature. Language: C++.

- Target repository: https://github.com/mortbopet/ripes pinned to commit `5b8a616edcb6f0a2ddb07e78951348b72497f1e1`
- Hidden test suite: 29 tests, 3731 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 18 files, 1141 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest`

## Results at acceptance

| Measure | Value |
|---|---|
| Nova (platform solver, codex_cli / openai/gpt-5.6-luna) pass rate | 0/10 = 0% |
| Vega (platform strong solver, codex_cli / openai/gpt-5.6-sol) pass rate | 1/1 = 100% |
| Platform difficulty band | hard |
| Median successful run | 1073 LOC changed, 105 agent messages |
| Human review | approved, bands description/solution/tests = 3/3/3 (3 is the top band), after 2 review rounds |

Submission criteria checked by the platform:

- Fair task: **pass** (No fairness issues)
- Solvable: **pass** (1/11 solved)
- No cheating: **pass** (No cheating detected)
- No environment blockers: **pass** (No environment blockers detected)
- No false positives: **warn** (Passed with caveats)

The platform replaced its difficulty and long-horizon rows with new agent-pool rows on 2026-10-09, after this challenge was accepted, so `results/criteria.json` (read on 2026-10-12) lists those new rows as pending.

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Every processor must offer B for selection, with its own description. Adding B must not reinterpret existing I, M or C instructions or decode other encodings as B. With B selected, the Zba, Zbb and Zbs instructions below must assemble and execute, and their disassembly must reassemble identically. Shift amounts and bit indices accept exactly what the corresponding existing shifts accept. The ISA name and -march put B after M and C; -march spells it b or _zba_zbb_zbs.
> 
> Encodings use opcode[6:0] OP(0x33), OI(0x13), OP32(0x3b) or OI32(0x1b), with rd[11:7] and rs1[19:15]. R=(opcode,[31:25],[14:12]) has rs2[24:20]; U=(opcode,[31:20],[14:12]); I5=(opcode,[31:25],[14:12]) has a five-bit shift or index in [24:20]; I6=(opcode,[31:26],[14:12]) has a six-bit one in [25:20]. Slashed lists pair by position; unmarked encodings cover both widths.
> 
> Zba has sh1add/sh2add/sh3add R(OP,0x10,2/4/6). RV64 also has add.uw R(OP32,0x04,0); sh1add.uw/sh2add.uw/sh3add.uw R(OP32,0x10,2/4/6); and slli.uw I6(OI32,0x02,1). shNadd computes (rs1 << N) + rs2 modulo XLEN for N=1,2,3. The .uw forms first zero-extend rs1's low 32 bits; add.uw adds rs2, shNadd.uw shifts before adding rs2, and slli.uw shifts by its immediate.
> 
> Zbb has andn/orn/xnor R(OP,0x20,7/6/4); max/maxu/min/minu R(OP,0x05,6/7/4/5); rol/ror R(OP,0x30,1/5); clz/ctz/cpop U(OI,0x600/0x601/0x602,1); sext.b/sext.h U(OI,0x604/0x605,1); orc.b U(OI,0x287,5); zext.h U(OP,0x080,4) on RV32 or U(OP32,0x080,4) on RV64; rev8 U(OI,0x698,5) on RV32 or U(OI,0x6b8,5) on RV64; and rori I5(OI,0x30,5) on RV32 or I6(OI,0x18,5) on RV64. RV64 also has clzw/ctzw/cpopw U(OI32,0x600/0x601/0x602,1); rolw/rorw R(OP32,0x30,1/5); and roriw I5(OI32,0x30,5).
> 
> Andn, orn and xnor compute rs1 & ~rs2, rs1 | ~rs2 and ~(rs1 ^ rs2). Min and max compare signed XLEN values, minu and maxu unsigned. Clz and ctz count leading and trailing zeros, giving the operand width for zero; cpop counts set bits; the w counts use the low 32 bits. Sext.b and sext.h sign-extend the low byte and halfword; zext.h zero-extends the low halfword. Rol rotates left, ror and rori right, by the low log2(XLEN) shift bits, wrapping through XLEN; the w rotations use five shift bits, wrap through 32, then sign-extend. Orc.b maps nonzero bytes to 0xff and zero bytes to zero; rev8 reverses byte order across XLEN.
> 
> Zbs has bclr/bext R(OP,0x24,1/5); binv R(OP,0x34,1); bset R(OP,0x14,1); and bclri/bexti/binvi/bseti I5(OI,0x24/0x24/0x34/0x14,1/5/1/1) on RV32 or I6(OI,0x12/0x12/0x1a/0x0a,1/5/1/1) on RV64. They clear, extract, invert or set the rs1 bit indexed by the low log2(XLEN) bits of rs2 or the immediate; bext returns it as 0 or 1. Without B, B instructions neither assemble nor execute and never appear in disassembly.

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
