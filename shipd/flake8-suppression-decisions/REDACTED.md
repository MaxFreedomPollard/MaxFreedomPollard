# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (116 test functions (513 graded test cases), 3952 added lines; sha256 `14c181018126ba60f568b47ba89601b2c60ffb6a9c52e18781ec2c630a2734fa`)
- `solution.patch`: the reference solution that passes those tests (13 files, 798 added lines; sha256 `1a5855199af701d364d5647208e41912ba15b2504d64e2176d36814567d97488`)

**Why.** This challenge was delivered to, and paid for by, Datacurve (shipd.ai) as private benchmark data. The hidden tests and the reference solution are the grader. Publishing them would expose the benchmark, let it leak into model training data, and breach the platform's contributor terms. They remain with the platform and in the author's private archive; the hashes above let anyone with the originals confirm they match.

**Also trimmed, for the same reason.** The reviewer's free-text feedback in `results/review-outcomes.json` quoted specific hidden tests and solution internals, and the per-run summary column in `results/nova-rollouts.csv` described which hidden tests each solver run failed. Outcomes, per-field bands, quality scores, pass/fail flags, and run metrics are kept.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), the platform's acceptance record (`results/criteria.json`, `results/aggregate-stats.json`), the solver run log, and every human-review outcome. The hidden tests and reference solution can be shown privately, under the platform's terms, on request.
