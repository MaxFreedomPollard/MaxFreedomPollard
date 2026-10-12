Support SortedSet, NavigableSet, SortedMap and NavigableMap decoding. Unset configuration proxy methods returning these interfaces must yield empty collections. Fix the null default for methods declared to return Collection. Add forSortedSetOf, forNavigableSetOf, forSortedMapOf and forNavigableMapOf to ArchaiusType with Class and Type overloads. The new helpers reject a null type argument with a NullPointerException.

Add sparse descendant decoding for nested maps and collections, including containers whose intermediate properties are unset. For parameterized map or collection values, a map entry name is the nonempty segment up to the first dot or bracket. Scalar-valued map keys retain the entire suffix. Malformed paths contribute no children. Collection indices use canonical nonnegative decimal notation, contiguous from [0].

Explicit properties override descendants, including explicit empty strings. Treat containers with no decodable children as absent while retaining explicitly empty children.

Decode map keys through the configured Decoder's Type overload.
