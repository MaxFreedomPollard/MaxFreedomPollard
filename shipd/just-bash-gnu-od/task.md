Make od match GNU od in the C locale for -A/--address-radix, -j/--skip-bytes, -N/--read-bytes, -t/--format, -w/--width and -v/--output-duplicates.

I only need types a and c, plus d, o, u and x in sizes 1, 2 and 4 per -t, and for -j and -N just the b, k, K, kB and KB suffixes, with counts and their sum up to 2^64 - 1 and widths up to 4096. Abbreviated long options and combined short options are outside this scope.

Preserve -c as an ordered shorthand for -t c.
  -A/-j/-N/-t -> short attached or separate values, long = or separate values; -- ends option parsing
  -A -> d/o/x radices, or n to suppress addresses; - operand -> stdin, consumed once
  unsized d/o/u/x -> 4 bytes; counts -> decimal, leading-0 octal or 0x/0X hex
  `-w` / `--width` -> bare `-w` or `--width` sets `32` bytes per row; explicit decimal width `N` (leading zeros allowed) must be attached (`-wN` or `--width=N`)
  invalid width `N` (`N == 0` or `N % max_elem_size != 0`) -> falls back to `M = max_elem_size` and writes `"od: warning: invalid width N; using M instead"` to stderr when the dump starts
  `-j` skip past end -> writes `"od: cannot skip past end of combined input"` to stderr
  no format option -> 2-byte octal (`o2`)

Process operands in order. Unreadable ones produce `od: NAME: No such file or directory` on stderr and a nonzero exit status while later readable operands still contribute.
