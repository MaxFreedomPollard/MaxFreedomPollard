# ShipD portfolio: accepted coding-agent benchmark challenges

Ten of the benchmark challenges authored for shipd.ai (Datacurve's Quest Olympus platform), included here as examples, each accepted after automated checks, ten-plus solver runs, and human review. A challenge is five artifacts: a public repo pinned to one commit, a problem description written as a maintainer's issue, a hidden test patch with a runner, a reference solution that passes it, and a Dockerfile that builds the grading image. The platform's solver, Nova, attempts each task from the description alone; a challenge is accepted only when it is fair (no false positives, no environment blockers), solvable, long-horizon, and hard enough that the solver passes at most half the time.

| # | Challenge | Repo @ commit | Kind | Accepted | Nova pass rate | Difficulty | Review bands |
|---|---|---|---|---|---|---|---|
| 1 | Decode sorted and navigable collections | netflix/archaius @ f40de16d1c74 | feature | 2026-09-22 | 2/19 = 11% | hard | 3/3/3 |
| 2 | Stream distinct yielded resolutions with complete, transparent unsafe-cache outcomes | webpack/enhanced-resolve @ aefeac310a82 | feature | 2026-09-08 | 1/10 = 10% | hard | 3/3/2 |
| 3 | Correct suppression decisions and explain hidden violations | pycqa/flake8 @ efe6750405be | feature | 2026-09-17 | 1/10 = 10% | hard | 3/3/3 |
| 4 | Add typed repository status snapshots from Git porcelain v2 | gitpython-developers/gitpython @ db47516dac75 | feature | 2026-09-25 | 4/10 = 40% | medium | 3/3/3 |
| 5 | Bind match capture patterns and comprehension walrus targets in scope metadata | instagram/libcst @ d9a255843b5c | bug fix | 2026-08-18 | 3/10 = 30% | hard | 3/3/3 |
| 6 | Add ROLLUP, FETCH FIRST and TABLESAMPLE support to the query builder | coleifer/peewee @ 349997736ba2 | feature | 2026-08-20 | 1/12 = 8% | hard | 3/2/2 |
| 7 | Support the eBPF CPU v4 instructions | qmonnet/rbpf @ e3128159a7df | feature | 2026-09-28 | 1/20 = 5% | hard | 3/3/2 |
| 8 | Add the RISC-V B bit-manipulation extension | mortbopet/ripes @ 5b8a616edcb6 | feature | 2026-10-07 | 0/10 = 0% | hard | 3/3/3 |
| 9 | Support postgres session statements and the @ and ^@ operators | tobymao/sqlglot @ 896032a7aeec | feature | 2026-08-15 | 1/10 = 10% | hard | 3/3/3 |
| 10 | Recognise default arms in the inside, matches and generate case forms, and require begin and end after do, repeat and final | chipsalliance/verible @ 6cce8f192b55 | feature | 2026-09-23 | 1/10 = 10% | hard | 2/3/3 |

Review bands are the human reviewer's per-field grades for description / solution / tests; 3 is the top band. Every challenge also carries the platform's own criteria record, the solver run log, and the full review history under `results/`.

## Layout

One folder per challenge:

- [`archaius-sorted-navigable-collections/`](archaius-sorted-navigable-collections/)
- [`enhanced-resolve-yielded-resolutions/`](enhanced-resolve-yielded-resolutions/)
- [`flake8-suppression-decisions/`](flake8-suppression-decisions/)
- [`gitpython-porcelain-v2-status/`](gitpython-porcelain-v2-status/)
- [`libcst-scope-metadata/`](libcst-scope-metadata/)
- [`peewee-rollup-fetchfirst-tablesample/`](peewee-rollup-fetchfirst-tablesample/)
- [`rbpf-ebpf-cpu-v4/`](rbpf-ebpf-cpu-v4/)
- [`ripes-riscv-b-extension/`](ripes-riscv-b-extension/)
- [`sqlglot-postgres-session-statements/`](sqlglot-postgres-session-statements/)
- [`verible-case-default-forms/`](verible-case-default-forms/)

Each holds the task statement, the grading environment, a README with the task and results, and `results/` with the platform's records. **The hidden tests and reference solutions are redacted**: they were delivered to and paid for by Datacurve (shipd.ai) as private benchmark data, and publishing them would expose the grader and breach the platform's contributor terms. Each folder's `REDACTED.md` states exactly what was removed, with hashes of the originals. The redacted material can be shown privately, under the platform's terms, on request.
