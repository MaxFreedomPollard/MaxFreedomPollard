# Make od follow GNU od for address radixes, skips, types, widths and repeated rows

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and full GNU `od` specification compliance implementation with `Solver A 0/8` (`516K` avg tokens), `Solver C` pass (`266K`), and `Solver B 2/2` (`134K-139K`), later archived under Criteria V4's 256K-token Solver B floor. Category: feature. Language: TypeScript.

- Target repository: https://github.com/vercel-labs/just-bash pinned to commit `7537a260e38648e8998db7a95504102ad80b0194`
- Hidden test suite: 33 test files, 4689 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 5 files, 607 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Solver A rollouts | 0/8 passes (516K avg tokens) |
| Solver C / Solver B rollouts | Solver C passed (266K tokens); Solver B 2/2 passed (134K-139K tokens, below V4's 256,000-token floor) |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Make od match GNU od in the C locale for -A/--address-radix, -j/--skip-bytes, -N/--read-bytes, -t/--format, -w/--width and -v/--output-duplicates.
>
> I only need types a and c, plus d, o, u and x in sizes 1, 2 and 4 per -t, and for -j and -N just the b, k, K, kB and KB suffixes, with counts and their sum up to 2^64 - 1 and widths up to 4096. Abbreviated long options and combined short options are outside this scope.
>
> Preserve -c as an ordered shorthand for -t c.
>   -A/-j/-N/-t -> short attached or separate values, long = or separate values; -- ends option parsing
>   -A -> d/o/x radices, or n to suppress addresses; - operand -> stdin, consumed once
>   unsized d/o/u/x -> 4 bytes; counts -> decimal, leading-0 octal or 0x/0X hex
>   `-w` / `--width` -> bare `-w` or `--width` sets `32` bytes per row; explicit decimal width `N` (leading zeros allowed) must be attached (`-wN` or `--width=N`)
>   invalid width `N` (`N == 0` or `N % max_elem_size != 0`) -> falls back to `M = max_elem_size` and writes `"od: warning: invalid width N; using M instead"` to stderr when the dump starts
>   `-j` skip past end -> writes `"od: cannot skip past end of combined input"` to stderr
>   no format option -> 2-byte octal (`o2`)
>
> Process operands in order. Unreadable ones produce `od: NAME: No such file or directory` on stderr and a nonzero exit status while later readable operands still contribute.

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
