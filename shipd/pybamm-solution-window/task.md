When a model is solved, the solution is returned as a `Solution` object, and a list of times can be provided to initialize a solution with `sub_solutions`. New `Solution.window(start=None, stop=None)` slices closed `[start, stop]` (`None` uses `t[0]`/`t[-1]`, finite `Python`/`NumPy` real scalars not `bool`, bad or `start > stop` raises `SolverError`, no overlap returns `EmptySolution`).

Nonempty `all_ts` segments in `[start, stop]` clip `all_ts` (endpoints + interior) with `all_models`/`all_inputs`:
  `all_ys` -> cubic Hermite with `all_yps` (plus `yp`), else linear, with single-point `sol[var](t)`
  `ProcessedVariableComputed` -> linear (`cumtrapz_ic` offsets kept), with linear available time-major `sensitivities` across `all_ts`

`Solution` event metadata stays only if final `t` is in `[start, stop]`, and partial `time_indep` integrals raise `SolverError`:
  `first_state` / `last_state` -> work with `sensitivities` where stored, else `SolverError`
  `sub_solutions` / `cycles` / `steps` -> recursive `window()`, non-overlap and stale `summary_variables` dropped, independent copies of arrays/`all_inputs`
