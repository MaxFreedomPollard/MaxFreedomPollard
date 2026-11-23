# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (23 F2P tests (+ 467 baseline tests) across 2 files, 2500 added lines; sha256 `31ada7c28df431018945a47277bf153cc0e0bcb0853b0a229ba768b6949d5a18`)
- `solution.patch`: the reference solution that passes those tests (23 files, 645 added lines; sha256 `ea87f067fdcb7810aa08583726ef10e1eb69969477ae49e4c8c4a108648f1238`)

**Why.** This challenge was authored for Datacurve's ShipD (Quest Olympus) benchmark platform. To keep the portfolio uniform with the accepted challenges and avoid leaking private evaluation suites or platform artifacts into public model training data, the hidden tests and reference solution are withheld from this public copy. They remain in the author's private archive; the hashes above let anyone with the originals confirm they match.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The withheld tests and reference solution can be shown privately on request.
