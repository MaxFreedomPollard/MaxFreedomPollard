# Redacted material

Two files that belong to this challenge are deliberately absent from this shareable copy:

- `test.patch`: the hidden test suite and its `test.sh` runner (64 test functions, 910 added lines; sha256 `ff431787fbdb6253b17f17d8ae4771caabb771191a821d1f854fa49651e103fe`)
- `solution.patch`: the reference solution that passes those tests (4 files, 146 added lines; sha256 `8f1a68006af567638a1720edd5ad72c98f09b098cd398f198e649d4816769f61`)

**Why.** This challenge was delivered to, and paid for by, Datacurve (shipd.ai) as private benchmark data. The hidden tests and the reference solution are the grader. Publishing them would expose the benchmark, let it leak into model training data, and breach the platform's contributor terms. They remain with the platform and in the author's private archive; the hashes above let anyone with the originals confirm they match.

**Also trimmed, for the same reason.** The reviewer's free-text feedback in `results/review-outcomes.json` quoted specific hidden tests and solution internals, and the per-run summary column in `results/nova-rollouts.csv` described which hidden tests each solver run failed. Outcomes, per-field bands, quality scores, pass/fail flags, and run metrics are kept.

**What remains is enough to judge the work.** The task statement the agent received (`task.md`, also quoted in the README), the grading environment (`Dockerfile`, `Makefile`), the platform's acceptance record (`results/criteria.json`, `results/aggregate-stats.json`), the solver run log, and every human-review outcome. The hidden tests and reference solution can be shown privately, under the platform's terms, on request.
