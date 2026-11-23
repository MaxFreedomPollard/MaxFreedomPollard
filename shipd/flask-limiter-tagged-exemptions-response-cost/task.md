`Limit`, `RouteLimit`, `ApplicationLimit`, `MetaLimit`, `RequestLimit`, `Limiter.limit`, and `Limiter.shared_limit` accept a new optional `tag` parameter (`None` when blank), propagated to `RequestLimit` during evaluation and breach. `Limiter.exempt` accepts a new `tags` parameter (`str` or `Iterable[str]`) that merges `ExemptionScope` flags per non-blank matching `tag`, adding no exemption if none remain, and Unicode whitespace is stripped across `tag`, `tags`, and CLI `--tag`. Nonzero route flags also exempt matching decorated limits, and tagged route flags beyond `DEFAULT | APPLICATION` exempt matching blueprint limits.

Across non-meta limits and default or application `cost` settings, `cost` also accepts a new `Callable[[Response], int]`:
  pre-request -> `cost <= 0` skips only the storage check, while `Callable[[Response], int]` gates without deducting
  post-response -> for unbreached limits when `deduct_when` is `None` or truthy, deducts evaluated `cost > 0` and refreshes `current_limit` and `current_limits` window stats

CLI `limits` and `clear` commands:
  new `--tag` option -> filters matching limits when non-blank, omitting empty sections and unmatched routes unless `--endpoint` or `--path` is passed to `limits`
  `limits` -> appends `tag: <tag>` to tagged limit options
