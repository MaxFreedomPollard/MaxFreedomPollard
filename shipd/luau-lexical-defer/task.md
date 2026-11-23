Add lexical `defer do ... end` scope-exit statements across Luau's parser, pretty printer, compiler, VM interpreter, type checker, and linter.

`defer` is context-sensitive: only `defer do ... end` at statement start parses as defer, leaving `defer` usable as a variable, parameter, field, or function name. Defer bodies reject direct `return`, outer `break`, outer `continue`, and `...`, while nested loops or functions may use theirs. Pretty-printing (with/without CST) round-trips `defer do ... end`.

Evaluating `defer` registers its body for enclosing block, loop iteration, or function exit; unreached defers never run. Defers execute LIFO, inner scopes first. Captured outer locals stay live by reference across mutations and escaping closures. Return expressions evaluate before defers run, preserving single and multiple returns if defers mutate returned locals.

In `while`, numeric `for`, and generic `for` loops, `break` and `continue` run iteration defers before jumping. In `repeat ... until`, body defers run after `until`; `break` runs them immediately and `continue` unwinds inner blocks before `until`. Behavior holds across `-O0` through `-O2`.

On errors, `xpcall` handlers run before unwinding; pending defers run LIFO up to `pcall`/`xpcall` or coroutine exit, propagating the latest unhandled error while remaining defers run. Yielding inside defer errors; yielding around defers preserves them until exit, uncaught error, or `coroutine.close` (returning `false` and the error on failure). Garbage-collected coroutines run no defers.

Strict and nonstrict type checking (both solvers) and linting analyze defer bodies without leaking refinements. Native codegen (`--codegen`) and experimental coroutine finalizers are out of scope.
