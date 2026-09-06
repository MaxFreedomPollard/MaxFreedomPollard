# ShipD portfolio: accepted coding-agent benchmark challenges

Three benchmark challenges authored for shipd.ai (Datacurve's Quest Olympus platform), each accepted after automated checks, ten-plus solver runs, and human review. A challenge is five artifacts: a public repo pinned to one commit, a problem description written as a maintainer's issue, a hidden test patch with a runner, a reference solution that passes it, and a Dockerfile that builds the grading image. The platform's solver, Nova, attempts each task from the description alone; a challenge is accepted only when it is fair (no false positives, no environment blockers), solvable, long-horizon, and hard enough that the solver passes at most half the time.

| # | Challenge | Repo @ commit | Kind | Accepted | Nova pass rate | Difficulty | Review bands |
|---|---|---|---|---|---|---|---|
| 1 | Bind match capture patterns and comprehension walrus targets in scope metadata | instagram/libcst @ d9a255843b5c | bug fix | 2026-08-18 | 3/10 = 30% | hard | 3/3/3 |
| 2 | Add ROLLUP, FETCH FIRST and TABLESAMPLE support to the query builder | coleifer/peewee @ 349997736ba2 | feature | 2026-08-20 | 1/12 = 8% | hard | 3/2/2 |
| 3 | Support postgres session statements and the @ and ^@ operators | tobymao/sqlglot @ 896032a7aeec | feature | 2026-08-15 | 1/10 = 10% | hard | 3/3/3 |

Review bands are the human reviewer's per-field grades for description / solution / tests; 3 is the top band. Every challenge also carries the platform's own criteria record, the solver run log, and the full review history under `results/`.

## Layout

One folder per challenge:

- [`libcst-scope-metadata/`](libcst-scope-metadata/)
- [`peewee-rollup-fetchfirst-tablesample/`](peewee-rollup-fetchfirst-tablesample/)
- [`sqlglot-postgres-session-statements/`](sqlglot-postgres-session-statements/)

Each holds the task statement, the grading environment, a README with the task and results, and `results/` with the platform's records. **The hidden tests and reference solutions are redacted**: they were delivered to and paid for by Datacurve (shipd.ai) as private benchmark data, and publishing them would expose the grader and breach the platform's contributor terms. Each folder's `REDACTED.md` states exactly what was removed, with hashes of the originals. The redacted material can be shown privately, under the platform's terms, on request.
