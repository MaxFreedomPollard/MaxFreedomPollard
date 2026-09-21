My code contributions are live on many agentic evolution repositories, such as [NVIDIA's SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator), [NVIDIA's Molt](https://github.com/NVIDIA-NeMo/labs-molt), [Hermes Agent Self-Evolution](https://github.com/NousResearch/hermes-agent-self-evolution), [autocontext](https://github.com/greyhaven-ai/autocontext) and [headlong](https://github.com/laude-institute/headlong).

I am a long-time contributor to [Hermes Agent](https://github.com/NousResearch/hermes-agent), as well as to many other projects, including [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins), which makes any agent harness multimodal-native, and [86Box](https://github.com/86Box/86Box), an emulator of x86-based machines.

Creator of [Compartment](https://github.com/MaxFreedomPollard/Compartment), an encrypted, fully offline memory for AI agents, and other projects such as [nuclear compute](https://github.com/MaxFreedomPollard/nuclear-computing) and the [Artificial Knowledge Collection](https://github.com/MaxFreedomPollard/artificial-knowledge-collection-6.0). My [Compartment](https://github.com/MaxFreedomPollard/Compartment) agentic memory now ships as a default memory option in [Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/plugin-catalog/compartment.yaml).

## Accepted benchmark challenges

Challenges authored for Datacurve's ShipD platform, each accepted after automated checks, solver runs and human review; [three are included here](shipd/) as examples, with the hidden tests and reference solutions withheld to protect Datacurve's proprietary benchmark material, and each folder records exactly what was removed:

- **[instagram/libcst](https://github.com/instagram/libcst)**: [Bind match capture patterns and comprehension walrus targets in scope metadata](shipd/libcst-scope-metadata/)
- **[coleifer/peewee](https://github.com/coleifer/peewee)**: [Add ROLLUP, FETCH FIRST and TABLESAMPLE support to the query builder](shipd/peewee-rollup-fetchfirst-tablesample/)
- **[tobymao/sqlglot](https://github.com/tobymao/sqlglot)**: [Support postgres session statements and the @ and ^@ operators](shipd/sqlglot-postgres-session-statements/)

## Merged contributions

### [NousResearch](https://github.com/NousResearch)

- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)**: credited as a contributor in the [v2026.6.19](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.19), [v2026.7.1](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.1), [v2026.8.3](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3) and [v2026.9.11](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.11) release notes
  - [feat(plugin-catalog): add compartment (encrypted offline memory provider)](https://github.com/NousResearch/hermes-agent/pull/114494)
  - [fix(skills): make bundled-update backup handling crash-safe and idempotent](https://github.com/NousResearch/hermes-agent/commit/3581131e7de1560633c921b4782ea87dcbac3a9e)
  - [test(skills): add regression tests for bundled-update backup recovery](https://github.com/NousResearch/hermes-agent/commit/9a2b976326340f0fec7eb9a88cfeb953ffdd1e56)
  - [fix(curator): stop the rollback safety snapshot from pruning its target](https://github.com/NousResearch/hermes-agent/commit/fc1119ca66e321989a61564aa526b33cb6146d41)
  - [fix(curator): stop restore from matching unrelated skills by name prefix](https://github.com/NousResearch/hermes-agent/commit/992b9223893453b3b1527b2ba728996ec81e83f2)
  - [fix(tools): stop read_file rendering a phantom empty line for newline-terminated files](https://github.com/NousResearch/hermes-agent/commit/10c34dd7e2441c14f19abea3656fba718999b589)
  - [Merge consecutive same-role contents for native Gemini](https://github.com/NousResearch/hermes-agent/commit/936af2f4f549f5ff22ef00b082748d115080780e)
  - [fix(config): merge duplicate kanban block so auto_subscribe_on_create default survives](https://github.com/NousResearch/hermes-agent/commit/aa636c6fca0d7d9af7c574c524c43cb2035a6242)
  - [fix(curator): restore the real skills tree when a rollback extract dies part-way](https://github.com/NousResearch/hermes-agent/commit/65e9ece964988b03c777ea6a563f438cad42f2e1)
  - [fix(yuanbao): await the forwarded-records loading heartbeat](https://github.com/NousResearch/hermes-agent/commit/87f5c5351a2c56e27dc271d7a865a874c18b0bfd)
  - [fix(auth): a transient read failure is not corruption](https://github.com/NousResearch/hermes-agent/commit/31032b4f51a0b254b751a838f927f34baee1bd03)
  - [fix(gateway): do not claim a destructive-slash opt-out that was not saved](https://github.com/NousResearch/hermes-agent/commit/eeaba3a88db906dc1bc7e86946644adbce4bbe75)
  - [fix(sessions): briefly wait out a live compression lock instead of killing the turn](https://github.com/NousResearch/hermes-agent/commit/221be76e36de4f2c0c9395126a71552abe7b4a9f)
  - [fix(cli): dispatch /background inline instead of queuing it behind the turn](https://github.com/NousResearch/hermes-agent/commit/3dee0634c1436635fbcf51c87a7f32b4101a41b9)
  - [test: restore four silently shadowed definitions and guard against more](https://github.com/NousResearch/hermes-agent/commit/7729c183b4a2f70c3b583eee6f93e7149a4081f8)
  - [fix(gemini): collapse array-typed tool schemas instead of crashing translation](https://github.com/NousResearch/hermes-agent/commit/6a04ea67c0e75ef1218bf4ceaac071c2f16a0701)
- **[NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)**
  - [fix(config): honor explicit --hermes-repo and make config construction non-fatal](https://github.com/NousResearch/hermes-agent-self-evolution/pull/122)
- **[NousResearch/wandb-rs](https://github.com/NousResearch/wandb-rs)**
  - [Add Run::finish() to flush pending logs before exit](https://github.com/NousResearch/wandb-rs/pull/2)

### [86Box/86Box](https://github.com/86Box/86Box)

- [softpower: Fix the power-off delay spinner range overflowing int16_t](https://github.com/86Box/86Box/pull/7888)
- [Voodoo: Fix nccTable0 Q2 writes landing in the I2 coefficient](https://github.com/86Box/86Box/pull/7926)
- [XTA: Restore the missing break in the WDXT-150 case](https://github.com/86Box/86Box/pull/7925)
- [Config: Fix crash loading a config without a mouse_type key](https://github.com/86Box/86Box/pull/7924)
- [net_plip: Fix misplaced parenthesis disabling the transmit bounds check](https://github.com/86Box/86Box/pull/7923)
- [Fix machines and BIOS entries missing on case-sensitive filesystems](https://github.com/86Box/86Box/pull/7922)
- [GUS: Fix the ADC sample rate divisor missing the +2 bias](https://github.com/86Box/86Box/pull/7941)
- [MIDI: Fix input queue overflow hang and broken real-time bytes](https://github.com/86Box/86Box/pull/7940)

### [laude-institute/headlong](https://github.com/laude-institute/headlong)

- [traj: recursive tail and cat return the whole tree, in order](https://github.com/laude-institute/headlong/pull/110)
- [ci: point the smoke container's apt at the Azure mirror](https://github.com/laude-institute/headlong/pull/114)
- [traj: formatted tail and cat return the steps --filter matches](https://github.com/laude-institute/headlong/pull/112)

### [NVIDIA](https://github.com/NVIDIA)

- **[NVIDIA/OWL](https://github.com/NVIDIA/OWL)**
  - [Add OWL_DOUBLE types to typeToString](https://github.com/NVIDIA/OWL/pull/28)
- **[NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)**
  - [feat(reporting): record the evaluated source identity on benchmark cards](https://github.com/NVIDIA/SkillEvaluator/pull/131)
- **[NVIDIA/TileGym](https://github.com/NVIDIA/TileGym)**
  - [fix(ops): export tilecpp only when its backend is available](https://github.com/NVIDIA/TileGym/pull/200)
- **[NVIDIA-NeMo/labs-molt](https://github.com/NVIDIA-NeMo/labs-molt)**
  - [fix(recipe): resubmit the renamed GLM-5.2 Slurm script](https://github.com/NVIDIA-NeMo/labs-molt/pull/135)
- **[NVIDIA-RTX/NRI](https://github.com/NVIDIA-RTX/NRI)**
  - [Fix: include NRIRayTracing.h in NRIWrapperVK.h](https://github.com/NVIDIA-RTX/NRI/pull/260)

### [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins)

- [fix(shared): read input_audio.format from a URL's path, not its query string](https://github.com/QwenLM/Qwen-MM-Plugins/pull/54)
- [fix(shared): normalize box corner order before drawing](https://github.com/QwenLM/Qwen-MM-Plugins/pull/52)
- [fix(core): apply EXIF orientation in read_image, crop and draw_bbox](https://github.com/QwenLM/Qwen-MM-Plugins/pull/51)

### [abema/go-mp4](https://github.com/abema/go-mp4)

- [Fix numTemporalLayers and temporalIdNested bit widths in hvcC](https://github.com/abema/go-mp4/pull/185)
- [Fix discarded errors in marshalSlice and marshalUint](https://github.com/abema/go-mp4/pull/187)

### [apache](https://github.com/apache)

- **[apache/answer](https://github.com/apache/answer)**
  - [fix: comment url swaps title and answer id](https://github.com/apache/answer/pull/1603)
- **[apache/datasketches-java](https://github.com/apache/datasketches-java)**
  - [Fix Util.numDigits returning 0 for 0 and 1, and 18 for 1E18](https://github.com/apache/datasketches-java/pull/762)

### [boyter/scc](https://github.com/boyter/scc)

- [fix(asp.net): correct the server side comment terminator](https://github.com/boyter/scc/pull/772)
- [fix(dart): count single quoted string literals](https://github.com/boyter/scc/pull/773)

### [caronc/apprise](https://github.com/caronc/apprise)

- [Honor language= in onesignal:// and preserve it through url()](https://github.com/caronc/apprise/pull/1720)
- [Preserve query parameters in signl4:// url()](https://github.com/caronc/apprise/pull/1732)

### [celery/kombu](https://github.com/celery/kombu)

- [fix(utils): don't evict a key when overwriting an existing LRUCache entry](https://github.com/celery/kombu/pull/2621)
- [fix(utils): advance the token bucket timestamp even when the bucket is full](https://github.com/celery/kombu/pull/2652)

### [ClickHouse/clickhouse-go](https://github.com/ClickHouse/clickhouse-go)

- [fix(chcol): return true from HasType when the Variant carries a type](https://github.com/ClickHouse/clickhouse-go/pull/2006)
- [fix(churl): validate each host of a comma separated DSN authority](https://github.com/ClickHouse/clickhouse-go/pull/2005)

### [deschler/django-modeltranslation](https://github.com/deschler/django-modeltranslation)

- [fix: Rewrite F() expressions inside Q objects](https://github.com/deschler/django-modeltranslation/pull/822)
- [fix: Rewrite translated field names in all annotate() expressions](https://github.com/deschler/django-modeltranslation/pull/825)

### [ekzhang/jax-js](https://github.com/ekzhang/jax-js)

- [Fix copysign() dropping the magnitude when y is zero](https://github.com/ekzhang/jax-js/pull/214)
- [Fix sign() returning 1 for NaN](https://github.com/ekzhang/jax-js/pull/215)

### [fastify/fast-json-stringify](https://github.com/fastify/fast-json-stringify)

- [fix: drop unmatched properties when additionalProperties is false](https://github.com/fastify/fast-json-stringify/pull/879)
- [fix: apply the else branch when a schema has if and else but no then](https://github.com/fastify/fast-json-stringify/pull/884)

### [foliojs/pdfkit](https://github.com/foliojs/pdfkit)

- [Fix annotation rectangle under a rotated transformation matrix](https://github.com/foliojs/pdfkit/pull/1794)
- [Fix doc.list() throwing on a numbered or lettered list with align center or right](https://github.com/foliojs/pdfkit/pull/1800)

### [greyhaven-ai/autocontext](https://github.com/greyhaven-ai/autocontext)

- [fix: default dataclass metadata to a dict, not a pydantic FieldInfo](https://github.com/greyhaven-ai/autocontext/pull/1324)
- [fix: mirror every compaction ledger append, not only large chunks](https://github.com/greyhaven-ai/autocontext/pull/1345)

### [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)

- [[fix] Write the sparsity CSV columns once in three sparse evaluators](https://github.com/huggingface/sentence-transformers/pull/3985)
- [[docs] Describe the MarginMSE target as the signed margin](https://github.com/huggingface/sentence-transformers/pull/4009)

### [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)

- [fix(video-subtitles): keep the space between merged subtitle clauses](https://github.com/hugohe3/ppt-master/pull/283)
- [fix(quick): read the deck language and theme fonts from the roster's first page](https://github.com/hugohe3/ppt-master/pull/292)

### [hyparam/hyparquet](https://github.com/hyparam/hyparquet)

- [Fix $not filters on dot-notation paths](https://github.com/hyparam/hyparquet/pull/177)
- [Keep default parsers when only some are overridden](https://github.com/hyparam/hyparquet/pull/178)

### [jhd3197/ServerKit](https://github.com/jhd3197/ServerKit)

- [fix(bitbucket): send redirect_uri on the authorize hop](https://github.com/jhd3197/ServerKit/pull/139)
- [fix(logs): compare whole segments in path guard](https://github.com/jhd3197/ServerKit/pull/145)

### [jundot/omlx](https://github.com/jundot/omlx)

- [fix(eval): stop a comma from swallowing the GSM8K answer](https://github.com/jundot/omlx/pull/3484)
- [fix(eval): honor a stated "answer is X" in multiple choice](https://github.com/jundot/omlx/pull/3668)

### [kenn-io/agentsview](https://github.com/kenn-io/agentsview)

- [fix(search): derive snippet spans from the matched bytes](https://github.com/kenn-io/agentsview/pull/1643)
- [fix(quality): keep signal excerpts on rune boundaries](https://github.com/kenn-io/agentsview/pull/1788)

### [meriyah/meriyah](https://github.com/meriyah/meriyah)

- [fix(parser): restrict continue targets to iteration statement labels](https://github.com/meriyah/meriyah/pull/646)
- [fix(parser): parse `/` after an `await` identifier as division](https://github.com/meriyah/meriyah/pull/659)

### [nominal-io/instro](https://github.com/nominal-io/instro)

- [fix(eload): cache mode only after the driver confirms set_mode](https://github.com/nominal-io/instro/pull/485)
- [fix(dmm): release the driver and reset apply state when close() fails](https://github.com/nominal-io/instro/pull/534)

### [open-circle/valibot](https://github.com/open-circle/valibot)

- [fix(cache): clone cached issues to stop issue paths from accumulating](https://github.com/open-circle/valibot/pull/1620)
- [fix(i18n): add missing async action translations](https://github.com/open-circle/valibot/pull/1645)

### [psd-tools/psd-tools](https://github.com/psd-tools/psd-tools)

- [fix: keep the bytes after a Hue/Saturation block's range records (#645)](https://github.com/psd-tools/psd-tools/pull/794)
- [fix: replace the layer at an index instead of inserting before it](https://github.com/psd-tools/psd-tools/pull/811)

### [python-attrs/cattrs](https://github.com/python-attrs/cattrs)

- [Sort extra keys when formatting ForbiddenExtraKeysError](https://github.com/python-attrs/cattrs/pull/776)
- [Escape the index note when structuring heterogeneous tuples](https://github.com/python-attrs/cattrs/pull/777)

### [quinn-rs/quinn](https://github.com/quinn-rs/quinn)

- [[0.11.x] proto: reject transport parameters with a mismatched length](https://github.com/quinn-rs/quinn/pull/2866)
- [proto: reject transport parameters with a mismatched length](https://github.com/quinn-rs/quinn/pull/2832)

### [raysan5/raylib](https://github.com/raysan5/raylib)

- [[rtext] Fix TextToPascal()/TextToCamel() truncating text after a separator](https://github.com/raysan5/raylib/pull/6132)
- [[rtext] Fix TextSplit() reading past its buffer on text of 1024 bytes or more](https://github.com/raysan5/raylib/pull/6136)

### [Tencent](https://github.com/Tencent)

- **[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)**
  - [fix(record): record a page reload instead of dropping it as a same-URL navigation](https://github.com/Tencent/BrowserSkill/pull/184)
- **[Tencent/WeKnora](https://github.com/Tencent/WeKnora)**
  - [fix(knowledge): keep long non-ASCII folder names valid UTF-8](https://github.com/Tencent/WeKnora/pull/3056)

### [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent)

- [fix(diff): compare bad file extensions case-insensitively](https://github.com/The-PR-Agent/pr-agent/pull/3103)
- [fix(bitbucket): send inline comment ranges with start_to](https://github.com/The-PR-Agent/pr-agent/pull/3384)

### [TimothyYe/godns](https://github.com/TimothyYe/godns)

- [fix: match ip_type case-insensitively in IONOS and Hetzner providers](https://github.com/TimothyYe/godns/pull/316)
- [fix: discard wrong-family IP instead of returning it from getIPOnline](https://github.com/TimothyYe/godns/pull/319)

### [vadimdemedes/ink](https://github.com/vadimdemedes/ink)

- [Fix `wrapText` cache key collision between different texts and widths](https://github.com/vadimdemedes/ink/pull/998)
- [Fix multi-line `<Text>` vanishing when it starts above the top of the output](https://github.com/vadimdemedes/ink/pull/1001)

### [wemake-services/django-modern-rest](https://github.com/wemake-services/django-modern-rest)

- [Fix `q` weights in `Accept` header parsing](https://github.com/wemake-services/django-modern-rest/pull/1407)
- [Strip optional whitespace when splitting headers on `,`](https://github.com/wemake-services/django-modern-rest/pull/1526)

### [agavra/tuicr](https://github.com/agavra/tuicr)

- [fix(input): type AltGr characters in the command, search and filter prompts](https://github.com/agavra/tuicr/pull/694)

### [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)

- [fix(rag): escape Excel Markdown table cells](https://github.com/agentscope-ai/agentscope/pull/2528)

### [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

- [fix(wiki): drop a leading BOM on a page with no frontmatter](https://github.com/akitaonrails/ai-memory/pull/663)

### [amicalhq/amical](https://github.com/amicalhq/amical)

- [fix(shortcuts): accept bare Return as a macOS shortcut key](https://github.com/amicalhq/amical/pull/183)

### [bitshifter/glam-rs](https://github.com/bitshifter/glam-rs)

- [fix(vec): round half-way cases away from zero in the SIMD backends](https://github.com/bitshifter/glam-rs/pull/831)

### [boa-dev/boa](https://github.com/boa-dev/boa)

- [fix(string): reject signed Infinity and non-decimal literals in StringToNumber](https://github.com/boa-dev/boa/pull/5509)

### [castorini/rank_llm](https://github.com/castorini/rank_llm)

- [Fix trec_eval dropping the first evaluation option](https://github.com/castorini/rank_llm/pull/437)

### [chakra-ui/chakra-ui](https://github.com/chakra-ui/chakra-ui)

- [fix(react): read the important marker only at the end of a value](https://github.com/chakra-ui/chakra-ui/pull/10970)

### [charmbracelet/catwalk](https://github.com/charmbracelet/catwalk)

- [fix: add missing providers to KnownProviders](https://github.com/charmbracelet/catwalk/pull/578)

### [crmne/spotifast](https://github.com/crmne/spotifast)

- [Clear a queued song's row without taking the playlist's own](https://github.com/crmne/spotifast/pull/344)

### [crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam)

- [channel: Implement Display and Error for TryReadyError and ReadyTimeoutError](https://github.com/crossbeam-rs/crossbeam/pull/1327)

### [dalathegreat/Battery-Emulator](https://github.com/dalathegreat/Battery-Emulator)

- [Fix SOL-ARK-LV-CAN 0x359 over-current sign bug](https://github.com/dalathegreat/Battery-Emulator/pull/2929)

### [devitocodes/devito](https://github.com/devitocodes/devito)

- [misc: Snapshot the environment when a switchenv is entered](https://github.com/devitocodes/devito/pull/3019)

### [Effect-TS/effect](https://github.com/Effect-TS/effect)

- [fix(cli): split key=value pairs at the first separator](https://github.com/Effect-TS/effect/pull/8086)

### [elastio/bon](https://github.com/elastio/bon)

- [Strip the `r#` prefix from raw identifiers in `derive(Debug)`](https://github.com/elastio/bon/pull/402)

### [embassy-rs/embassy](https://github.com/embassy-rs/embassy)

- [embassy-sync: wake the next waiter when a FairSemaphore acquire is canceled](https://github.com/embassy-rs/embassy/pull/6964)

### [evcxr/evcxr](https://github.com/evcxr/evcxr)

- [Fix comment handling when looking for commands](https://github.com/evcxr/evcxr/pull/507)

### [expressjs/multer](https://github.com/expressjs/multer)

- [fix: report the decoded filename on LIMIT_FILE_SIZE](https://github.com/expressjs/multer/pull/1478)

### [floci-io/floci](https://github.com/floci-io/floci)

- [fix(eventbridge,scheduler): read cron day-of-week as AWS 1-7 SUN-SAT](https://github.com/floci-io/floci/pull/3147)

### [gbdev/rgbds](https://github.com/gbdev/rgbds)

- [Avoid signed overflow in RGBLINK's `+`, `-`, and `*`](https://github.com/gbdev/rgbds/pull/2060)

### [gdsfactory/gdsfactory](https://github.com/gdsfactory/gdsfactory)

- [fix: keep grid_with_text labels on their anchors](https://github.com/gdsfactory/gdsfactory/pull/4821)

### [georust/rstar](https://github.com/georust/rstar)

- [Fix overflow panic draining an empty tree with integer coordinates](https://github.com/georust/rstar/pull/246)

### [go-goyave/goyave](https://github.com/go-goyave/goyave)

- [httputil: fix quality value parsing in ParseMultiValuesHeader](https://github.com/go-goyave/goyave/pull/295)

### [gotenberg/gotenberg](https://github.com/gotenberg/gotenberg)

- [fix(libreoffice): report an encrypted .xlsb as password-protected](https://github.com/gotenberg/gotenberg/pull/1655)

### [inducer/loopy](https://github.com/inducer/loopy)

- [Fix CudaCallable type inference never being called](https://github.com/inducer/loopy/pull/1048)

### [ishepard/pydriller](https://github.com/ishepard/pydriller)

- [Fix added_lines and deleted_lines dropping "++" and "--" content](https://github.com/ishepard/pydriller/pull/324)

### [joncampbell123/dosbox-x](https://github.com/joncampbell123/dosbox-x)

- [drive_virtual: fix CHDIR succeeding on a file on drive Z:](https://github.com/joncampbell123/dosbox-x/pull/6533)

### [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale)

- [fix(core): parse MiMo Code and fx on the local report path](https://github.com/junhoyeo/tokscale/pull/1300)

### [kgateway-dev/kgateway](https://github.com/kgateway-dev/kgateway)

- [fix(deployer): merge gmsaCredentialSpecName from its own field](https://github.com/kgateway-dev/kgateway/pull/14660)

### [kubescape/kubescape](https://github.com/kubescape/kubescape)

- [fix(rbacgraph): order escalation results instead of reading map order](https://github.com/kubescape/kubescape/pull/3739)

### [leookun/cursor-byok](https://github.com/leookun/cursor-byok)

- [fix(search): stop a repeated URL from faking cross-engine agreement](https://github.com/leookun/cursor-byok/pull/431)

### [libarchive/libarchive](https://github.com/libarchive/libarchive)

- [man: fix option names that archive_write_set_options rejects](https://github.com/libarchive/libarchive/pull/3495)

### [magefree/mage](https://github.com/magefree/mage)

- [Fix Wickersmith's Tools creating untapped Scarecrow tokens](https://github.com/magefree/mage/pull/16115)

### [maplibre/maplibre-tile-spec](https://github.com/maplibre/maplibre-tile-spec)

- [fix(ts): keep byte RLE within the lengths its headers can express](https://github.com/maplibre/maplibre-tile-spec/pull/1653)

### [marin-community/marin](https://github.com/marin-community/marin)

- [[markdown] Omit the link and image title when the HTML has none](https://github.com/marin-community/marin/pull/8938)

### [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk)

- [auth: strip a terminating slash from the issuer before building metadata URLs](https://github.com/modelcontextprotocol/go-sdk/pull/1245)

### [modelscope/ms-swift](https://github.com/modelscope/ms-swift)

- [fix(metrics): mask ignored labels in padding-free seq_acc](https://github.com/modelscope/ms-swift/pull/10049)

### [mozilla/pontoon](https://github.com/mozilla/pontoon)

- [Update data-theme when the user picks a theme](https://github.com/mozilla/pontoon/pull/4501)

### [noahbald/oxvg](https://github.com/noahbald/oxvg)

- [fix(oxvg_optimiser): keep ellipses selected by a stylesheet in convertShapeToPath](https://github.com/noahbald/oxvg/pull/277)

### [odygrd/quill](https://github.com/odygrd/quill)

- [Flush sinks and run periodic tasks when manual backend polling drains the queues](https://github.com/odygrd/quill/pull/989)

### [onnx/onnx](https://github.com/onnx/onnx)

- [fix(reference): reorder Unique outputs correctly when sorted=0](https://github.com/onnx/onnx/pull/8424)

### [openhab/openhab-addons](https://github.com/openhab/openhab-addons)

- [[nobohub] Fix ignored keepaliveInterval setting](https://github.com/openhab/openhab-addons/pull/21613)

### [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)

- [fix(server): relay client websocket closes with a legal code](https://github.com/opensandbox-group/OpenSandbox/pull/1731)

### [oras-project/oras](https://github.com/oras-project/oras)

- [fix: attribute recursive copy tag failures to the destination](https://github.com/oras-project/oras/pull/2157)

### [pacifio/atlas](https://github.com/pacifio/atlas)

- [fix(redact): route JSONL payloads through the structure-aware pass](https://github.com/pacifio/atlas/pull/244)

### [pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)

- [fix(types): hash 0.0 and -0.0 to the same value](https://github.com/pgdogdev/pgdog/pull/1507)

### [pixijs/pixijs](https://github.com/pixijs/pixijs)

- [fix: handle strokes wider than the shape in Ellipse.strokeContains](https://github.com/pixijs/pixijs/pull/12185)

### [pmndrs/koota](https://github.com/pmndrs/koota)

- [🐛 core: fix query hash collisions from the shared sort buffer](https://github.com/pmndrs/koota/pull/281)

### [probe-rs/probe-rs](https://github.com/probe-rs/probe-rs)

- [Fix the semihosting file open modes for update and append](https://github.com/probe-rs/probe-rs/pull/4312)

### [PyLabRobot/pylabrobot](https://github.com/PyLabRobot/pylabrobot)

- [fix(resources): center a plate on the adapter hole's y size, not its x size](https://github.com/PyLabRobot/pylabrobot/pull/1244)

### [quarkusio/quarkus](https://github.com/quarkusio/quarkus)

- [Qute: require the index parameter for list get/take/takeLast](https://github.com/quarkusio/quarkus/pull/56460)

### [rust-diplomat/diplomat](https://github.com/rust-diplomat/diplomat)

- [hir: resolve callback optional-opaque returns in the enclosing module](https://github.com/rust-diplomat/diplomat/pull/1271)

### [sql-formatter-org/sql-formatter](https://github.com/sql-formatter-org/sql-formatter)

- [fix(singlestoredb): support % as the modulo operator](https://github.com/sql-formatter-org/sql-formatter/pull/971)

### [srl-labs/containerlab](https://github.com/srl-labs/containerlab)

- [fix: canonical image name for registries addressed by host and port](https://github.com/srl-labs/containerlab/pull/3391)

### [tconbeer/harlequin](https://github.com/tconbeer/harlequin)

- [fix: write the Feather file version the Data Exporter asked for](https://github.com/tconbeer/harlequin/pull/1158)

### [testem/testem](https://github.com/testem/testem)

- [fix(report-file): surface write stream errors instead of a TypeError](https://github.com/testem/testem/pull/2058)

### [tombi-toml/tombi](https://github.com/tombi-toml/tombi)

- [fix(lexer): close multi-line string after escaped backslash](https://github.com/tombi-toml/tombi/pull/2167)

### [uutils/coreutils](https://github.com/uutils/coreutils)

- [fmt: honor -x and -X instead of always matching prefixes exactly](https://github.com/uutils/coreutils/pull/14417)

### [velero-io/velero](https://github.com/velero-io/velero)

- [Scope schedule and repo CLI list calls to the Velero namespace](https://github.com/velero-io/velero/pull/10482)

### [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni)

- [[Doc] Fix markdownlint findings in the serving API reference](https://github.com/vllm-project/vllm-omni/pull/7111)

### [vuejs/test-utils](https://github.com/vuejs/test-utils)

- [fix: keep the namespace prefix in attributes()](https://github.com/vuejs/test-utils/pull/2941)

### [wshobson/agents](https://github.com/wshobson/agents)

- [fix(adapters): quote YAML scalars in OpenCode and Copilot frontmatter](https://github.com/wshobson/agents/pull/700)

### [xintaofei/codeg](https://github.com/xintaofei/codeg)

- [fix(cline): close a stripped block at its own closing tag](https://github.com/xintaofei/codeg/pull/670)

### [yoanbernabeu/grepai](https://github.com/yoanbernabeu/grepai)

- [fix(search): break score ties deterministically so ranking is reproducible](https://github.com/yoanbernabeu/grepai/pull/303)

### [zenstackhq/zenstack](https://github.com/zenstackhq/zenstack)

- [fix(zod): treat `@uuid` without a version as any UUID version](https://github.com/zenstackhq/zenstack/pull/2832)

Earlier hermes-agent commits are also carried by 216 downstream copies and derivatives of that project ([list](contributions.md#downstream-copies-carrying-these-commits)).

## Projects

- [Compartment](https://github.com/MaxFreedomPollard/Compartment): Encrypted, fully offline agentic memory. One click install, GUI w/ memory map, all OS and agents. Superior memory creation, storage and retrieval. Python, Apache-2.0, with a [docs site](https://maxfreedompollard.github.io/Compartment/). Listed in [Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/pull/127), [Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents/pull/402), [Awesome-Agent-Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory/pull/70), [awesome-mcp-servers](https://github.com/TensorBlock/awesome-mcp-servers/pull/1510), [awesome-mcp](https://github.com/abordage/awesome-mcp/pull/91), [toolsdk-mcp-registry](https://github.com/toolsdk-ai/toolsdk-mcp-registry/pull/418).
- [nuclear-computing](https://github.com/MaxFreedomPollard/nuclear-computing): Nuclear compute (radiative compute) as an alternative computing substrate to electronic and quantum machines: one radioactive medium supplies power, logic, memory, and interconnect, enabling sealed portable computers that compute without external power.
- [artificial-knowledge-collection-6.0](https://github.com/MaxFreedomPollard/artificial-knowledge-collection-6.0): Knowledge of special interest to AI: nine datasets of concepts, relationships, constants and measurements, each one clean file, aligned into a single 544,279-node map, plus a reasoning benchmark. Artificial knowledge for artificial intelligence.

## Certifications and education

- MBA, University of Adelaide (now Adelaide University), 2024
- Google IT Support Professional Certificate
- IBM Cybersecurity Analyst Professional Certificate
- Google Project Management Professional Certificate
- Library & Information Services, University of Adelaide and the Australian Library and Information Association (ALIA)
- Foundations of Finance, University of Cambridge
- Member, Association for the Advancement of Artificial Intelligence (AAAI)
- Board Approved Member, Council on the Ageing (COTA) NSW, since 2026
- National Member, National Seniors Australia, since 2025

## Contact

[linkedin.com/in/maxfreedom](https://www.linkedin.com/in/maxfreedom/)
