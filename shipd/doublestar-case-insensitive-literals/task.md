Fix `WithCaseInsensitive` to resolve whole literals and literal components around wildcards and braces to every matching filesystem spelling. Literal equality uses `unicode.ToLower`; raw bracket ranges also match folded starts.

Report distinct pathnames in directory-listing order. `GlobWalk` callback `SkipDir` returns leave independent spellings and brace alternatives eligible. Enabled filesystem errors precede every callback.

After listing failure, the literal child's exact lookup determines success, absence or error. Within literal prefixes, deeper exact outcomes override ancestor refusals, even through symlinks. Resume folding below accessible directories, including after wildcards and braces.

Each complete brace expansion has its own pre-wildcard literal prefix. `FailOnPatternNotExist` requires every folded spelling of that entire prefix to be absent; ignored I/O refusals are not absence. An unfinished prefix ending at a file is absent. File spellings cannot mask directories. Apply I/O options independently to every spelling's listings and exact lookups.

Past the original first wildcard, `NoFollow` permits exact recovery only when symlink traversal is ruled out; unknown link status is unsafe. Otherwise apply the listing error and continue independent spellings. Braces and recovery never reset this boundary.

`FilepathGlob` folds escaped, rooted and relative literal bases, including leading `..`. `Glob` and `GlobWalk` preserve requested trailing `/` on whole-literal directories.
