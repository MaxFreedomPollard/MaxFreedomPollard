# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (2 test files, 876 added lines; sha256 `e9cc5609da43248b2f66623dc1122893b3dca239f4b5e6fdc90669076a180fae`)
- `solution.patch`: the reference solution that passes those tests (4 files, 276 added lines; sha256 `879c6c6e14741d8141d0349feab89c998fc74b0e4df98f4cf4f6cd25dcc60f3e`)

**Why.** This challenge was delivered to, and paid for by, Datacurve (shipd.ai) as private benchmark data. The hidden tests and the reference solution are the grader. Publishing them would expose the benchmark, let it leak into model training data, and breach the platform's contributor terms. They remain with the platform and in the author's private archive; the hashes above let anyone with the originals confirm they match.

**Also trimmed, for the same reason.** The reviewer's free-text feedback in `results/review-outcomes.json` quoted specific hidden tests and solution internals, and the per-run summary column in `results/solver-rollouts.csv` described which hidden tests each solver run failed. Outcomes, per-field bands, quality scores, pass/fail flags, and run metrics are kept.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The hidden tests and reference solution can be shown privately, under the platform's terms, on request.
