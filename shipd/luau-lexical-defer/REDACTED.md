# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (11 ASan-clean F2P tests (+ 1,216 baseline tests) across 2 files, 889 added lines; sha256 `13bc8bc8f24091db84770e4c4307099d82d913f772912d4d537b4d95e125e692`)
- `solution.patch`: the reference solution that passes those tests (37 files, 710 added lines; sha256 `92e3d0ff3cf2ce2e8da755ad042cc34686cc8fc9d4801a54d4e3b23381c240b3`)

**Why.** This challenge was authored for Datacurve's ShipD (Quest Olympus) benchmark platform. To keep the portfolio uniform with the accepted challenges and avoid leaking private evaluation suites or platform artifacts into public model training data, the hidden tests and reference solution are withheld from this public copy. They remain in the author's private archive; the hashes above let anyone with the originals confirm they match.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), and the sanitized platform check, rollout, and review summary under `results/`. The withheld tests and reference solution can be shown privately on request.
