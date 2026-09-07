# Max Freedom Pollard

This repository is my portfolio. Everything below links to work you can open: the projects, the merged code, the benchmark challenges in this repo's own folders, and the credentials behind them.

## Accepted benchmark challenges

Challenges authored for Datacurve's ShipD platform, each accepted after automated checks, solver runs and human review; [three are included here](shipd/) as examples, with the hidden tests and reference solutions withheld to protect Datacurve's proprietary benchmark material, and each folder records exactly what was removed:

- **[instagram/libcst](https://github.com/instagram/libcst)**: [Bind match capture patterns and comprehension walrus targets in scope metadata](shipd/libcst-scope-metadata/)
- **[coleifer/peewee](https://github.com/coleifer/peewee)**: [Add ROLLUP, FETCH FIRST and TABLESAMPLE support to the query builder](shipd/peewee-rollup-fetchfirst-tablesample/)
- **[tobymao/sqlglot](https://github.com/tobymao/sqlglot)**: [Support postgres session statements and the @ and ^@ operators](shipd/sqlglot-postgres-session-statements/)

## Merged contributions

Code merged into other projects:

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)**: 12 merged commits; credited as a contributor in many release notes since June
  - [fix(skills): make bundled-update backup handling crash-safe and idempotent](https://github.com/NousResearch/hermes-agent/commit/3581131e7de1560633c921b4782ea87dcbac3a9e)
  - [test(skills): add regression tests for bundled-update backup recovery](https://github.com/NousResearch/hermes-agent/commit/9a2b976326340f0fec7eb9a88cfeb953ffdd1e56)
  - [fix(curator): stop the rollback safety snapshot from pruning its target](https://github.com/NousResearch/hermes-agent/commit/fc1119ca66e321989a61564aa526b33cb6146d41)
  - [fix(curator): stop restore from matching unrelated skills by name prefix](https://github.com/NousResearch/hermes-agent/commit/992b9223893453b3b1527b2ba728996ec81e83f2)
  - [Merge consecutive same-role contents for native Gemini](https://github.com/NousResearch/hermes-agent/commit/936af2f4f549f5ff22ef00b082748d115080780e)
  - [fix(curator): restore the real skills tree when a rollback extract dies part-way](https://github.com/NousResearch/hermes-agent/commit/65e9ece964988b03c777ea6a563f438cad42f2e1)
  - [fix(yuanbao): await the forwarded-records loading heartbeat](https://github.com/NousResearch/hermes-agent/commit/87f5c5351a2c56e27dc271d7a865a874c18b0bfd)
  - [fix(auth): a transient read failure is not corruption](https://github.com/NousResearch/hermes-agent/commit/31032b4f51a0b254b751a838f927f34baee1bd03)
  - [fix(gateway): do not claim a destructive-slash opt-out that was not saved](https://github.com/NousResearch/hermes-agent/commit/eeaba3a88db906dc1bc7e86946644adbce4bbe75)
  - [fix(sessions): briefly wait out a live compression lock instead of killing the turn](https://github.com/NousResearch/hermes-agent/commit/221be76e36de4f2c0c9395126a71552abe7b4a9f)
  - [fix(cli): dispatch /background inline instead of queuing it behind the turn](https://github.com/NousResearch/hermes-agent/commit/3dee0634c1436635fbcf51c87a7f32b4101a41b9)
  - [test: restore four silently shadowed definitions and guard against more](https://github.com/NousResearch/hermes-agent/commit/7729c183b4a2f70c3b583eee6f93e7149a4081f8)
- **[NousResearch/wandb-rs](https://github.com/NousResearch/wandb-rs)**: [Add Run::finish() to flush pending logs before exit](https://github.com/NousResearch/wandb-rs/commit/c5f552464f13d56a5abd73c2dfb88b193e991d4e)
- **[NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)**: [fix(config): honor explicit --hermes-repo and make config construction non-fatal (#122)](https://github.com/NousResearch/hermes-agent-self-evolution/commit/0a929e3aa20e15cf04dc7c28492a7d41a5139125)
- **[laude-institute/headlong](https://github.com/laude-institute/headlong)**: [traj: recursive tail and cat return the whole tree, in order](https://github.com/laude-institute/headlong/commit/e4ca135a5ab11a19d3dc363d4241885c83b4c3f8)
- **[vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni)**: [Fix markdownlint findings in the serving API reference](https://github.com/vllm-project/vllm-omni/commit/946b843e6142033d61df473dcfd2e2e213ef6c34)
- **[probe-rs/probe-rs](https://github.com/probe-rs/probe-rs)**: [Fix the semihosting file open modes for update and append](https://github.com/probe-rs/probe-rs/commit/615bf5e042224b36235a6f01aebd45e94ab82dda)
- **[gotenberg/gotenberg](https://github.com/gotenberg/gotenberg)**: [fix(libreoffice): report an encrypted .xlsb as password-protected](https://github.com/gotenberg/gotenberg/commit/c21ceacd4b1027a68d06931625916ddcb15c79bd)
- **[maplibre/maplibre-tile-spec](https://github.com/maplibre/maplibre-tile-spec)**: [fix(ts): keep byte RLE within the lengths its headers can express](https://github.com/maplibre/maplibre-tile-spec/commit/049b170f9037e6948da193139e554edadaf50a15)
- **[zenstackhq/zenstack](https://github.com/zenstackhq/zenstack)**: [fix(zod): treat `@uuid` without a version as any UUID version](https://github.com/zenstackhq/zenstack/commit/3f1ed72510af67ed758dd9ed6f17bc744dc7dd2a)
- **[oras-project/oras](https://github.com/oras-project/oras)**: [fix: attribute recursive copy tag failures to the destination](https://github.com/oras-project/oras/commit/f54f368af1fb3d45c2ac33287c23c9b100a13385)
- **[ekzhang/jax-js](https://github.com/ekzhang/jax-js)**: [Fix copysign() dropping the magnitude when y is zero](https://github.com/ekzhang/jax-js/commit/970fa22d934ce2e617cd3a993c6ecc8b736496f2)
- **[celery/kombu](https://github.com/celery/kombu)**: [fix(utils): don't evict a key when overwriting an existing LRUCache entry](https://github.com/celery/kombu/commit/a6cdf538f86192fa1cb58fb827cad344d06de510)
- **[PyLabRobot/pylabrobot](https://github.com/PyLabRobot/pylabrobot)**: [fix(resources): center a plate on the adapter hole's y size, not its x size](https://github.com/PyLabRobot/pylabrobot/commit/2c05867f0c779469505f539a9f89017849d52a7b)
- **[openhab/openhab-addons](https://github.com/openhab/openhab-addons)**: [[nobohub] Fix ignored keepaliveInterval setting](https://github.com/openhab/openhab-addons/commit/ca013260596cafd90afab18878a9e9a906379a5c)
- **[magefree/mage](https://github.com/magefree/mage)**: [Fix Wickersmith's Tools creating untapped Scarecrow tokens](https://github.com/magefree/mage/commit/c6221e0c95a575c4f4a1707468df12fab234cae7)
- **[raysan5/raylib](https://github.com/raysan5/raylib)**: [[rtext] Fix TextToPascal()/TextToCamel() truncating text after a separator](https://github.com/raysan5/raylib/commit/2b991b0243c3dccf48ed926bcb754c60846f96c1)
- **[junhoyeo/tokscale](https://github.com/junhoyeo/tokscale)**: [fix(core): parse MiMo Code and fx on the local report path](https://github.com/junhoyeo/tokscale/commit/dff9949244eb5463b96671706595752a3f4ff2cb)
- **[floci-io/floci](https://github.com/floci-io/floci)**: [fix(eventbridge,scheduler): read cron day-of-week as AWS 1-7 SUN-SAT](https://github.com/floci-io/floci/commit/60a8a9d25262ab9a35033ed5c9778600a89a1e94)
- **[boyter/scc](https://github.com/boyter/scc)**: [fix(asp.net): correct the server side comment terminator](https://github.com/boyter/scc/commit/eb6ac4cb889beabbfb2cb40841c1c07ff6adc25c)
- **[86Box/86Box](https://github.com/86Box/86Box)**: [softpower: Fix the power-off delay spinner range overflowing int16_t](https://github.com/86Box/86Box/commit/14d6e1defd368d78a2655b1cd294f6d45e9d9795)
- **[agavra/tuicr](https://github.com/agavra/tuicr)**: [fix(input): type AltGr characters in the command, search and filter prompts](https://github.com/agavra/tuicr/commit/58eb8e163342ef49313cc9f508db9751980bd773)
- **[Tencent/WeKnora](https://github.com/Tencent/WeKnora)**: [fix(knowledge): keep long non-ASCII folder names valid UTF-8](https://github.com/Tencent/WeKnora/commit/801005f736b5e76c514588f3ac9abe5212ebb219)
- **[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)**: [fix(server): relay client websocket closes with a legal code](https://github.com/opensandbox-group/OpenSandbox/commit/242b20926ab64a8366e5d4fa6b79d92a294027c3)
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)**: [fix(rag): escape Excel Markdown table cells](https://github.com/agentscope-ai/agentscope/commit/d8629a987133adba33a4bdd2b6c8c721cfef12eb)
- **[Effect-TS/effect](https://github.com/Effect-TS/effect)**: [fix(cli): split key=value pairs at the first separator](https://github.com/Effect-TS/effect/commit/291d616282b666bbba3664143fa1d19e839a6a5d)
- **[pacifio/atlas](https://github.com/pacifio/atlas)**: [fix(redact): route JSONL payloads through the structure-aware pass](https://github.com/pacifio/atlas/commit/d9ee007aa1427999d9495a925c8eacc127a6d86d)
- **[kubescape/kubescape](https://github.com/kubescape/kubescape)**: [fix(rbacgraph): order escalation results instead of reading map order](https://github.com/kubescape/kubescape/commit/023d1285ef37c7ffbf9eba16ad3a861bc86680fd)
- **[The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent)**: [fix(diff): compare bad file extensions case-insensitively](https://github.com/The-PR-Agent/pr-agent/commit/d6c8b9a502216b32eab9c5f89675b66a59002150)
- **[bitshifter/glam-rs](https://github.com/bitshifter/glam-rs)**: [fix(vec): round half-way cases away from zero in the SIMD backends](https://github.com/bitshifter/glam-rs/commit/40535a3a2d6b652c7558a984ddabbdbb7ba34084)
- **[huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)**: [[fix] Write the sparsity CSV columns once in three sparse evaluators](https://github.com/huggingface/sentence-transformers/commit/729f28e551e723a9bac6052e597f379d181bbad7)
- **[modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk)**: [auth: strip a terminating slash from the issuer before building metadata URLs](https://github.com/modelcontextprotocol/go-sdk/commit/5bc078a7959a745d1311fefa280b36c5cde19929)
- **[dalathegreat/Battery-Emulator](https://github.com/dalathegreat/Battery-Emulator)**: [Fix SOL-ARK-LV-CAN 0x359 over-current sign bug](https://github.com/dalathegreat/Battery-Emulator/commit/47e9aecec3471c448a3f826e2b6476d72908cdb7)
- **[deschler/django-modeltranslation](https://github.com/deschler/django-modeltranslation)**: [fix: Rewrite F() expressions inside Q objects](https://github.com/deschler/django-modeltranslation/commit/3a67e47eb0ac20f6464f062986f19a2ccc5c309e)
- **[python-attrs/cattrs](https://github.com/python-attrs/cattrs)**: [Sort extra keys when formatting ForbiddenExtraKeysError](https://github.com/python-attrs/cattrs/commit/bc34a466a878d3259d01d0169b3fb95420d7d50d)
- **[xintaofei/codeg](https://github.com/xintaofei/codeg)**: [fix(cline): close a stripped block at its own closing tag](https://github.com/xintaofei/codeg/commit/145ef0782fb79a54c0db562b199074ad8221c4d5)
- **[mozilla/pontoon](https://github.com/mozilla/pontoon)**: [Update data-theme when the user picks a theme](https://github.com/mozilla/pontoon/commit/e852341fb6a7ed0b7c369a1daa029e14e3b94376)
- **[uutils/coreutils](https://github.com/uutils/coreutils)**: [fmt: honor -x and -X instead of always matching prefixes exactly](https://github.com/uutils/coreutils/commit/8da0fa6bb5147ae76ca3936f354d8ccbe25a7db4)
- **[chakra-ui/chakra-ui](https://github.com/chakra-ui/chakra-ui)**: [fix(react): read the important marker only at the end of a value](https://github.com/chakra-ui/chakra-ui/commit/d88c3e9424e5c9d7afacc09899d81cebfd223d09)
- **[castorini/rank_llm](https://github.com/castorini/rank_llm)**: [Fix trec_eval dropping the first evaluation option](https://github.com/castorini/rank_llm/commit/22d55d090a03643417cdb710391b073d1578410c)
- **[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)**: [fix(video-subtitles): keep the space between merged subtitle clauses](https://github.com/hugohe3/ppt-master/commit/2bb95544bd7c39ca16bdb1d04e1f0176cbfef68b)
- **[crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam)**: [channel: Implement Display and Error for TryReadyError and ReadyTimeoutError](https://github.com/crossbeam-rs/crossbeam/commit/38dacb462261fcd64edcb308aed9cbf95c8c82c3)
- **[elastio/bon](https://github.com/elastio/bon)**: [Strip the `r#` prefix from raw identifiers in `derive(Debug)`](https://github.com/elastio/bon/commit/300abd62ff2bf08e9f6c699e665db4e0258acb64)

The hermes-agent commits are also carried by 216 downstream copies and derivatives of that project ([list](contributions.md#downstream-copies-carrying-these-commits)).

## Projects

- [Compartment](https://github.com/MaxFreedomPollard/Compartment): Encrypted, fully offline agentic memory. One click install, GUI w/ memory map, all OS and agents. Superior memory creation, storage and retrieval. Python, Apache-2.0, with a [docs site](https://maxfreedompollard.github.io/Compartment/). Listed in [Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/pull/127), [Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents/pull/402), [Awesome-Agent-Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory/pull/70), [awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers/pull/1510), [awesome-mcp](https://github.com/abordage/awesome-mcp/pull/91), [toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry/pull/418).
- [nuclear-computing](https://github.com/MaxFreedomPollard/nuclear-computing): Nuclear compute (radiative compute) as an alternative computing substrate to electronic and quantum machines: one radioactive medium supplies power, logic, memory, and interconnect, enabling sealed portable computers that compute without external power.
- [artificial-knowledge-collection-6.0](https://github.com/MaxFreedomPollard/artificial-knowledge-collection-6.0): Knowledge of special interest to AI: nine datasets of concepts, relationships, constants and measurements, each one clean file, aligned into a single 544,279-node map, plus a reasoning benchmark. Artificial knowledge for artificial intelligence.

## Certifications and education

- MBA, University of Adelaide (now Adelaide University), 2024
- Google IT Support Professional Certificate
- IBM Cybersecurity Analyst Professional Certificate
- Google Project Management Professional Certificate
- NSW Security Equipment Specialist Licence; Master Security Licence
- Member, Association for the Advancement of Artificial Intelligence (AAAI)

## Contact

[linkedin.com/in/maxfreedom](https://www.linkedin.com/in/maxfreedom/)
