New `JupytextConfiguration` traits (`pipe_fmt=""` and `pipe_cell_filter=""`), CLI option `--pipe-cell-filter`, and new `pipe_notebook` parameters (`cell_filter` and `config`) default `pipe_fmt` to `"auto:percent"` in CLI `--pipe` and `--check` (or `"py:percent"` in `pipe_notebook`, skipping execution when no cells match).

`combine_inputs_with_outputs` combines the text and metadata from the first notebook, with the outputs and metadata of the second notebook, using `cell_filter`, `parse_cell_filter` and `cell_matches_filter` on comma-separated `code`, `markdown`, `raw` and `tag:<name>` rules:
  unset, "" or whitespace-only filter -> None; invalid or empty token or empty tag -> ValueError; no "-" match and a "+" or unprefixed match in each present group -> cell matches
  selected output slot -> updated with matched piped cell or dropped if unmatched; unselected cell -> kept in place; unmatched source cell -> placed before next matched slot or at end
  root_level_metadata_as_raw_cell -> explicit fmt > config > jupytext metadata; jupytext.root_level_metadata from piped output or source notebook -> preserved
