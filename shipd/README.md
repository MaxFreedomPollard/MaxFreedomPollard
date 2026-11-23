# ShipD portfolio: coding-agent benchmark challenges

Thirty-five benchmark challenges authored for shipd.ai (Datacurve's Quest Olympus platform) across Python, Go, C++, TypeScript, JavaScript, Java, and Rust. A challenge consists of five artifacts: a public repository pinned to one commit, a problem description written as a maintainer's issue, a hidden test patch with a runner, a reference solution that passes it, and a Dockerfile that builds the grading image. Platform solvers (Nova, Orion, and Vega) attempt each task from the description alone under automated fairness, solution-quality, reward-hacking, flakiness, and solver-horizon checks.

Thirteen challenges below were officially accepted and paid. Another ten passed Auto Review, entered `finalizing_review`, or completed human review before retroactive platform policy changes (including the November 2026 Criteria V4 cutover introducing a 256,000-token Orion sequence-length floor). The remaining twelve are full post-October Criteria V4 builds (including compiler, bundler, and runtime tasks across Binaryen, Webpack, Svelte, esbuild, and Luau) that cleared automated quality checks or full local verification before hitting Criteria V4's token floor, topic crowding, or platform enrollment closure.

## Accepted challenges (13)

| # | Challenge | Repo @ commit | Lang | Kind | Accepted | Passers | Review bands |
|---|---|---|---|---|---|---|---|
| 1 | [Decode sorted and navigable collections](archaius-sorted-navigable-collections/) | netflix/archaius @ f40de16d1c74 | Java | feature | 2026-09-22 | 2/19 Nova | 3/3/3 |
| 2 | [Stream distinct yielded resolutions with complete, transparent unsafe-cache outcomes](enhanced-resolve-yielded-resolutions/) | webpack/enhanced-resolve @ aefeac310a82 | JS | feature | 2026-09-08 | 1/10 Nova | 3/3/2 |
| 3 | [Correct suppression decisions and explain hidden violations](flake8-suppression-decisions/) | pycqa/flake8 @ efe6750405be | Python | feature | 2026-09-17 | 1/10 Nova | 3/3/3 |
| 4 | [Add typed repository status snapshots from Git porcelain v2](gitpython-porcelain-v2-status/) | gitpython-developers/gitpython @ db47516dac75 | Python | feature | 2026-09-25 | 4/10 Nova | 3/3/3 |
| 5 | [Bind match capture patterns and comprehension walrus targets in scope metadata](libcst-scope-metadata/) | instagram/libcst @ d9a255843b5c | Python | bug fix | 2026-08-18 | 3/10 Nova | 3/3/3 |
| 6 | [Add ROLLUP, FETCH FIRST and TABLESAMPLE support to the query builder](peewee-rollup-fetchfirst-tablesample/) | coleifer/peewee @ 349997736ba2 | Python | feature | 2026-08-20 | 1/12 Nova | 3/2/2 |
| 7 | [Add sentence and paragraph movement to the Vi and Emacs key bindings](python-prompt-toolkit-sentence-paragraph-motion/) | prompt-toolkit/python-prompt-toolkit @ 583b3412c792 | Python | feature | 2026-09-26 | 4/10 Nova | 3/3/3 |
| 8 | [Support the eBPF CPU v4 instructions](rbpf-ebpf-cpu-v4/) | qmonnet/rbpf @ e3128159a7df | Rust | feature | 2026-09-28 | 1/20 Nova | 3/3/2 |
| 9 | [Add the RISC-V B bit-manipulation extension](ripes-riscv-b-extension/) | mortbopet/ripes @ 5b8a616edcb6 | C++ | feature | 2026-10-07 | 0/10 Nova, 1/1 Vega | 3/3/3 |
| 10 | [Append, prepend and remove through keyword values](scons-keyword-append-prepend-remove/) | scons/scons @ 80c749ed90ad | Python | feature | 2026-10-16 | 0/8 Nova, 0/4 Orion, 1/4 Vega | 3/3/2 |
| 11 | [Support postgres session statements and the @ and ^@ operators](sqlglot-postgres-session-statements/) | tobymao/sqlglot @ 896032a7aeec | Python | feature | 2026-08-15 | 1/10 Nova | 3/3/3 |
| 12 | [Lossless write-back of parsed SMBIOS structures](u-root-smbios-writeback/) | u-root/u-root @ 34ab30280534 | Go | bug fix | 2026-10-17 | 0/8 Nova, 1/4 Vega | 3/2/3 |
| 13 | [Recognise default arms in the inside, matches and generate case forms, and require begin and end after do, repeat and final](verible-case-default-forms/) | chipsalliance/verible @ 6cce8f192b55 | C++ | feature | 2026-09-23 | 1/10 Nova | 2/3/3 |

## Auto Review approved & submitted since Oct 2026 (4)

| # | Challenge | Repo @ commit | Lang | Date | Review & platform outcome |
|---|---|---|---|---|---|
| 14 | [Export under Parse key ownership](env-struct-export/) | caarlos0/env @ 505764460181 | Go | 2026-11-02 | Auto Review approved (3/2/2, `meets_bar`); archived under V4 256K Orion floor |
| 15 | [Tagged limit exemptions, response-aware deduction costs, and CLI tag filtering](flask-limiter-tagged-exemptions-response-cost/) | alisaifee/flask-limiter @ 0e715b6fbb46 | Python | 2026-11-18 | Auto Review ran twice (agents/description Band 3); R32 cleared 100% V4 checks + Nova 0/4 + Orion 0/4 (< 256K floor) |
| 16 | [Index deals up to suit isomorphism](pokerkit-suit-isomorphism-indexing/) | uoftcprg/pokerkit @ b2fcc75c05ac | Python | 2026-10-19 | Auto Review approved (3/3/2) & human-reviewed; upgraded locally before V4 256K Orion floor |
| 17 | [Add form and field change tracking, partial patching, reset, and commit](wtforms-change-tracking-patch-reset-commit/) | pallets-eco/wtforms @ 46f626e5cd1f | Python | 2026-10-28 | Auto Review approved (3/2/2) -> `finalizing_review`; reverted at Nov 17 V4 cutover (< 256K floor) |

## Human-review submitted & policy-reverted (6)

| # | Challenge | Repo @ commit | Lang | Date | Review & platform outcome |
|---|---|---|---|---|---|
| 18 | [Add Micro QR Code encoding](barcode-micro-qr-encoding/) | boombuler/barcode @ 8485d4afd9da | Go | 2026-10-10 | Reached `finalizing_review` (reverted); revised v4 cleared all four quality checks |
| 19 | [Fix case-insensitive literal path resolution](doublestar-case-insensitive-literals/) | bmatcuk/doublestar @ a9ad9e0ef4d6 | Go | 2026-09-03 | Human-reviewed (0/9 Luna); revised with VCA verification |
| 20 | [Detect resolution order, async, property mutability and abstract method API breakages](griffe-api-breakage-checks/) | mkdocstrings/griffe @ a345344b40f5 | Python | 2026-08-30 | Scored 3/3/3 (`overallQuality: 3`) -> `finalizing_review` (reverted by platform) |
| 21 | [Mock modern filesystem APIs](mock-fs-modern-filesystem-apis/) | tschaub/mock-fs @ bbcea1835921 | JS | 2026-09-18 | Human-reviewed (0/10 Luna); later dropped by Scope Gate cross-language overlap rule |
| 22 | [Add structured template diagnostics to Nunjucks errors](nunjucks-structured-template-diagnostics/) | mozilla/nunjucks @ 2025c933fba3 | JS | 2026-09-01 | Human-reviewed (0/10 Luna); revised through v5 |
| 23 | [Add Kostka-Foulkes polynomials](sympy-kostka-foulkes-polynomials/) | sympy/sympy @ 3f58eb0ce808 | Python | 2026-10-04 | Reached `finalizing_review` (reverted after V2 strong-model pass-rate change) |

## Criteria V4 audited & complete post-Oct 2026 builds (12)

| # | Challenge | Repo @ commit | Lang | Date | Verification & status |
|---|---|---|---|---|---|
| 24 | [Support type visibility annotations in open and closed world](binaryen-type-visibility/) | WebAssembly/binaryen @ 4408fed200e9 | C++ | 2026-11-21 | 10/10 V4 checks PASS (23 files), Orion 1/3 solved (228.6K tokens) |
| 25 | [Preserve ESM module evaluation order with code splitting](esbuild-splitting-import-order/) | evanw/esbuild @ f6058f8364fe | Go | 2026-11-21 | Prechecks 15/15, Scope Gate, Verify Tests/Solution/Flakiness PASS (+1,747 LOC) |
| 26 | [Conditional ETag and Cache-Control lifecycle](flask-smorest-etag-cache-control/) | marshmallow-code/flask-smorest @ 2a0dc534586c | Python | 2026-10-19 | Complete build (103 F2P tests, 100% stmt/branch coverage) |
| 27 | [Support config-aware notebook piping and cell filtering](jupytext-config-aware-piping/) | jupytext/jupytext @ 932bcdb24384 | Python | 2026-11-19 | Orion 0/7 (89K-114K); reverted/archived at V4 cutover |
| 28 | [Make od follow GNU od for address radixes, skips, types, widths and repeated rows](just-bash-gnu-od/) | vercel-labs/just-bash @ 7537a260e386 | TS | 2026-11-02 | Nova 0/8, Vega pass (266K), Orion 2/2 (134K-139K) |
| 29 | [Producer partition pause flow control and selective unsent buffer abort](kafka-python-producer-pause-abort/) | dpkp/kafka-python @ 89df9871b848 | Python | 2026-11-20 | 100% V4 Step 0-3 + Scope Gate PASS, Nova 0/4 (< 256K Orion floor) |
| 30 | [Add lexical defer statements to Luau](luau-lexical-defer/) | luau-lang/luau @ c87565b8b0db | C++ | 2026-11-20 | Full 37-file compiler/VM build (11/11 ASan-clean, 1,216/1,216 base); Scope Gate topic overlap |
| 31 | [Extract windows from composite solution histories](pybamm-solution-window/) | pybamm-team/PyBaMM @ 8c6816d27acb | Python | 2026-11-20 | 100% V4 Step 0-3 + Scope Gate + Harbor 19/19 PASS, Orion 0/2 (< 256K floor) |
| 32 | [Case sensitivity per mount point and Unicode name matching on macOS](pyfakefs-per-mount-case-sensitivity/) | pytest-dev/pyfakefs @ f43fce450a7b | Python | 2026-11-20 | 100% V4 pre-rollout gates PASS (97 F2P tests, 0 warnings), Orion #1 pass (116K) |
| 33 | [Keep list numbering when Word lists are interrupted or restarted](python-mammoth-word-list-numbering/) | mwilliamson/python-mammoth @ f3b7b9fc73fd | Python | 2026-10-29 | Scope Gate PASS, image verification PASS |
| 34 | [Add $state.from custom accessor rune](svelte-state-from-rune/) | sveltejs/svelte @ 8720544ff764 | TS | 2026-11-21 | 100% V4 gates PASS (45 files, 0 Test Quality warnings), Orion #1 21/22 (163K) |
| 35 | [Support multi-root module concatenation for shared chunks](webpack-multi-root-concatenation/) | webpack/webpack @ a393e82c4853 | JS | 2026-11-22 | v1 cleared 7/7 checks + Scope Gate + Orion 0/4 (339K-714K) + Vega 0/4 (442K-561K); v2g (+2,760 LOC) verified across all 5 tsc configs + npm pack |

Review bands are the reviewer's per-field grades for description / solution / tests; 3 is the top band. Accepted entries include the platform's criteria record, solver run log, and sanitized review history under `results/`; additional reviewed and audited builds include a sanitized `results/summary.json` alongside their full task spec and grading environment.

## Layout

One folder per challenge (35 total):

- [`archaius-sorted-navigable-collections/`](archaius-sorted-navigable-collections/)
- [`barcode-micro-qr-encoding/`](barcode-micro-qr-encoding/)
- [`binaryen-type-visibility/`](binaryen-type-visibility/)
- [`doublestar-case-insensitive-literals/`](doublestar-case-insensitive-literals/)
- [`enhanced-resolve-yielded-resolutions/`](enhanced-resolve-yielded-resolutions/)
- [`env-struct-export/`](env-struct-export/)
- [`esbuild-splitting-import-order/`](esbuild-splitting-import-order/)
- [`flake8-suppression-decisions/`](flake8-suppression-decisions/)
- [`flask-limiter-tagged-exemptions-response-cost/`](flask-limiter-tagged-exemptions-response-cost/)
- [`flask-smorest-etag-cache-control/`](flask-smorest-etag-cache-control/)
- [`gitpython-porcelain-v2-status/`](gitpython-porcelain-v2-status/)
- [`griffe-api-breakage-checks/`](griffe-api-breakage-checks/)
- [`jupytext-config-aware-piping/`](jupytext-config-aware-piping/)
- [`just-bash-gnu-od/`](just-bash-gnu-od/)
- [`kafka-python-producer-pause-abort/`](kafka-python-producer-pause-abort/)
- [`libcst-scope-metadata/`](libcst-scope-metadata/)
- [`luau-lexical-defer/`](luau-lexical-defer/)
- [`mock-fs-modern-filesystem-apis/`](mock-fs-modern-filesystem-apis/)
- [`nunjucks-structured-template-diagnostics/`](nunjucks-structured-template-diagnostics/)
- [`peewee-rollup-fetchfirst-tablesample/`](peewee-rollup-fetchfirst-tablesample/)
- [`pokerkit-suit-isomorphism-indexing/`](pokerkit-suit-isomorphism-indexing/)
- [`pybamm-solution-window/`](pybamm-solution-window/)
- [`pyfakefs-per-mount-case-sensitivity/`](pyfakefs-per-mount-case-sensitivity/)
- [`python-mammoth-word-list-numbering/`](python-mammoth-word-list-numbering/)
- [`python-prompt-toolkit-sentence-paragraph-motion/`](python-prompt-toolkit-sentence-paragraph-motion/)
- [`rbpf-ebpf-cpu-v4/`](rbpf-ebpf-cpu-v4/)
- [`ripes-riscv-b-extension/`](ripes-riscv-b-extension/)
- [`scons-keyword-append-prepend-remove/`](scons-keyword-append-prepend-remove/)
- [`sqlglot-postgres-session-statements/`](sqlglot-postgres-session-statements/)
- [`svelte-state-from-rune/`](svelte-state-from-rune/)
- [`sympy-kostka-foulkes-polynomials/`](sympy-kostka-foulkes-polynomials/)
- [`u-root-smbios-writeback/`](u-root-smbios-writeback/)
- [`verible-case-default-forms/`](verible-case-default-forms/)
- [`webpack-multi-root-concatenation/`](webpack-multi-root-concatenation/)
- [`wtforms-change-tracking-patch-reset-commit/`](wtforms-change-tracking-patch-reset-commit/)

Each folder holds the verbatim task statement, the grading `Dockerfile` and `Makefile`, a README with the task and verification results, and `results/` with sanitized platform records. **The hidden tests and reference solutions are redacted**: for accepted challenges they were delivered to and paid for by Datacurve (shipd.ai) as private benchmark data, and for all entries withholding them keeps the portfolio consistent and prevents evaluation suites from leaking into public training data. Each folder's `REDACTED.md` states exactly what was removed, with SHA-256 hashes of the originals.
