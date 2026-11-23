# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (17 F2P tests (+ 722 baseline unit tests) across 2 files, 1938 added lines; sha256 `be9df6f665e2d05a4bb3a3eedf973275e7e30da7f20ecc56faa3103b8321722a`)
- `solution.patch`: the reference solution that passes those tests (14 files, 2760 added lines; sha256 `24fdc0a618a05a1a1dfb5425feb98cade3b1d94f2d3749e33e754472fe3c1c58`)

**Why.** This challenge was authored for Datacurve's ShipD (Quest Olympus) benchmark platform. To keep the portfolio uniform with the accepted challenges and avoid leaking private evaluation suites or platform artifacts into public model training data, the hidden tests and reference solution are withheld from this public copy. They remain in the author's private archive; the hashes above let anyone with the originals confirm they match.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The withheld tests and reference solution can be shown privately on request.
