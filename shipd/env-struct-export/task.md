Only field-owned keys consumed by Parse may be exported, and each value must satisfy both keyed and keyless prefix readers of its key. Export may refuse expand/file fields, slices of structs, parser-owned structs and pointers to those structs. Otherwise it succeeds exactly when a permitted map round-trips the source's non-ignored fields through ParseWithOptions under the same options. Empty successful exports return non-nil maps; failures return nil maps and errors naming all responsible fields. OnSet is ignored during export and readback. Nil slices and maps remain distinct from empty ones.

Nonempty scalar spellings are fixed by underlying kind, including for named types with text methods: unchanged strings, true/false booleans, decimal integers, Go's default %g spelling of the underlying float32/float64 value, and time.Duration.String output. Collections use Parse's separator tags, with complete encoded map entries sorted before joining.

Neither the source nor Options.Environment nor the process environment is modified; results are invariant under environment changes that preserve decoding semantics.

Provide `Export(v interface{}) (map[string]string, error)` and `ExportWithOptions(v interface{}, opts Options) (map[string]string, error)`. The source is a non-nil struct pointer; other inputs and duplicate field-owned keys fail.
