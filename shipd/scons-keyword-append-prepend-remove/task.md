`Append`, `Prepend`, `AppendUnique`, `PrependUnique` and `Remove` become `SCons.Script` globals; as keyword values (wrappers) they work in `Environment()`, `Clone()` and builder calls. A wrapper calls the environment's same-named method with its unexpanded value and option (`delete_existing` or `missing_ok`, default `False`).

Order: `variables=`, `parse_flags=` and plain keywords first, then wrappers in keyword order; surviving builder-default wrappers run before call-provided ones, and a call value replaces the same variable's default.

`env.Remove(missing_ok=False, **kwargs)` removes every occurrence equal to each keyword's value from that variable while survivors keep order. A missing value raises `ValueError`, an unset variable `KeyError`; `missing_ok` true skips both, and every removal is checked before anything changes.

`str` and `CLVar` targets and requests both go through `Split()`, with `str` targets rejoining with single spaces. For a list, deque, tuple or dict target, a `str` request is one element or key, such containers or `CLVar` supply elements or keys, and any other request is one item; target type is kept (tuples becoming plain tuples), and other targets raise `TypeError`.
