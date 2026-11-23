# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (57 tests across 2 files (79/79 mutants killed), 5780 added lines; sha256 `751add607da53f91149c596b7a1221f43c39b2c7d8560018f0e7802ca67c0bbc`)
- `solution.patch`: the reference solution that passes those tests (6 files, 449 added lines; sha256 `a02eee8a8fbc6c72bf62e7139afe86ee99159a867d44f72c1515a88ed400662e`)

**Why.** This challenge was authored for Datacurve's ShipD (Quest Olympus) benchmark platform. To keep the portfolio uniform with the accepted challenges and avoid leaking private evaluation suites or platform artifacts into public model training data, the hidden tests and reference solution are withheld from this public copy. They remain in the author's private archive; the hashes above let anyone with the originals confirm they match.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The withheld tests and reference solution can be shown privately on request.
