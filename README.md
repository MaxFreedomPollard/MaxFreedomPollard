# Max Freedom Pollard

This repository is my portfolio. Everything below links to work you can open: the projects, the merged code, the benchmark challenges in this repo's own folders, and the credentials behind them.

## Accepted benchmark challenges

Challenges authored for Datacurve's ShipD platform, each rated at the platform's hardest difficulty band after automated checks, solver runs and human review; [three are included here](shipd/) as examples, with the hidden tests and reference solutions withheld to protect Datacurve's proprietary benchmark material, and each folder records exactly what was removed:

- **[instagram/libcst](https://github.com/instagram/libcst)**: [Bind match capture patterns and comprehension walrus targets in scope metadata](shipd/libcst-scope-metadata/)
- **[coleifer/peewee](https://github.com/coleifer/peewee)**: [Add ROLLUP, FETCH FIRST and TABLESAMPLE support to the query builder](shipd/peewee-rollup-fetchfirst-tablesample/)
- **[tobymao/sqlglot](https://github.com/tobymao/sqlglot)**: [Support postgres session statements and the @ and ^@ operators](shipd/sqlglot-postgres-session-statements/)

## Merged contributions

Code merged into other projects:

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)**: 12 merged commits; credited as a contributor in the [v2026.6.19](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.19), [v2026.7.1](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.1) and [v2026.8.3](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3) release notes
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
