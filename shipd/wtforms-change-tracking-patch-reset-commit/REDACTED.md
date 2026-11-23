# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (64 tests across 2 files (later expanded locally to 69 tests with 68/68 mutants killed), 4373 added lines; sha256 `05e11b0259052766a0967720f9175fb618ddb3570ac50ff988ac9c5b39572a2f`)
- `solution.patch`: the reference solution that passes those tests (5 files, 386 added lines; sha256 `6b32ac9587f7494967bd78398d4e4f4332758aef54454aaf04612cc7f7e134e8`)

**Why.** This challenge was authored for Datacurve's ShipD (Quest Olympus) benchmark platform. To keep the portfolio uniform with the accepted challenges and avoid leaking private evaluation suites or platform artifacts into public model training data, the hidden tests and reference solution are withheld from this public copy. They remain in the author's private archive; the hashes above let anyone with the originals confirm they match.

**Also trimmed, for the same reason.** The reviewer's free-text feedback in `results/review-outcomes.json` quoted specific hidden tests and solution internals, and the per-run summary column in `results/nova-rollouts.csv` described which hidden tests each solver run failed. Outcomes, per-field bands, quality scores, pass/fail flags, and run metrics are kept.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The withheld tests and reference solution can be shown privately on request.
