# Add Micro QR Code encoding

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and submitted on `2026-09-28`..`29`, reached `finalizing_review` (`managerVerdict: revert`), then revised on `2026-10-10` to clear all four platform quality gates (`FOUR_CHECKS_CLEAR`). Category: feature. Language: Go.

- Target repository: https://github.com/boombuler/barcode pinned to commit `8485d4afd9da706ac5dfecd60c5616eb640ca4cd`
- Hidden test suite: 5 test files, 3024 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 3 files, 333 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Submission history | Submitted 2026-09-28 and 2026-09-29; reviewed 2026-10-10 |
| Post-review revision (v4) | Cleared Prechecks, Verify Solution, Verifier Completeness Audit, and Solution Quality |
| Platform status change | Reached finalizing_review before managerVerdict = revert |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add qr.EncodeMicro(content string, level ErrorCorrectionLevel, mode Encoding) (barcode.Barcode, error) for the smallest ISO/IEC 18004 Micro QR symbol M1-M4 at the requested level, without a quiet zone. Return errors for empty content, content exceeding that level's capacity, unsupported levels or modes, Numeric content outside ASCII digits, or AlphaNumeric content outside its existing alphabet. Unicode preserves and counts raw bytes, including invalid UTF-8. Auto encodes one segment using the first mode that can encode all content at that level: Numeric, AlphaNumeric, Unicode.
>
> Version n is 2n+9 modules square. M1 supports only Numeric, AlphaNumeric needs M2 or later, and Unicode M3 or later. The mode indicator uses n-1 bits: Numeric=0, AlphaNumeric=1, Unicode=2. Character counts use n+2 bits for Numeric and n+1 for AlphaNumeric/Unicode. Terminate with 2n+1 zero bits, truncated at capacity.
>
> Symbol numbers 0-7 are M1-L, M2-L, M2-M, M3-L, M3-M, M4-L, M4-M, M4-Q, with respectively 2, 5, 6, 6, 8, 8, 10, 14 error-correction codewords in one block. M1/M3's last data codeword contains four bits. Pad codewords never fill it; unused bits are zero. Error correction takes these as a byte's high half, with a zero low half.
>
> Use one top-left finder, light right/bottom separators and top/left timing patterns alternating from dark beside the separator. The 15 format bits concatenate the 3-bit symbol number, 2-bit mask number and ten BCH check bits (generator 10100110111), then XOR with 100010001000101.
>
> Apply Micro masks 0-3, respectively QR masks 1, 4, 6, 7, only to data/error-correction modules. For rightmost-column and bottom-row dark counts a,b, maximize 16*min(a,b)+max(a,b), breaking ties toward the lower mask number.
>
> Define barcode.TypeMicroQR = "Micro QR Code" and return it in Metadata. ColorModel conversion must keep dark and light modules distinct.

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
