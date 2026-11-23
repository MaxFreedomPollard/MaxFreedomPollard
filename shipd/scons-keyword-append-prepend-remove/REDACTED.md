# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (2 test files, 1239 added lines; sha256 `8156643287d657a77933750a84ca06942ca62d216dab0b3484b7e28f44bc880c`)
- `solution.patch`: the reference solution that passes those tests (5 files, 302 added lines; sha256 `aeec35470933ff3165025a14f340d849300706d4fb7b07a9c253714e09b18f66`)

**Why.** This challenge was delivered to, and paid for by, Datacurve (shipd.ai) as private benchmark data. The hidden tests and the reference solution are the grader. Publishing them would expose the benchmark, let it leak into model training data, and breach the platform's contributor terms. They remain with the platform and in the author's private archive; the hashes above let anyone with the originals confirm they match.

**Also trimmed, for the same reason.** The reviewer's free-text feedback in `results/review-outcomes.json` quoted specific hidden tests and solution internals, and the per-run summary column in `results/solver-rollouts.csv` described which hidden tests each solver run failed. Outcomes, per-field bands, quality scores, pass/fail flags, and run metrics are kept.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The hidden tests and reference solution can be shown privately, under the platform's terms, on request.
