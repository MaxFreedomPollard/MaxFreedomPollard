# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (32 F2P tests (+ 574 baseline tests) across 2 files, 2216 added lines; sha256 `986345034691486715b44e3fcb70b536051ab1cda700f233c70925327198f61b`)
- `solution.patch`: the reference solution that passes those tests (8 files, 513 added lines; sha256 `5154e0b02b054df9b25439641dfbb2bbf1b67ac6bcd55efa7ddfcbb56fefbf9c`)

**Why.** This challenge was authored for Datacurve's ShipD (Quest Olympus) benchmark platform. To keep the portfolio uniform with the accepted challenges and avoid leaking private evaluation suites or platform artifacts into public model training data, the hidden tests and reference solution are withheld from this public copy. They remain in the author's private archive; the hashes above let anyone with the originals confirm they match.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The withheld tests and reference solution can be shown privately on request.
