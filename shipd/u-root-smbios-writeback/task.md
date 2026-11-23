Fix MarshalBinary for typed SMBIOS values parsed from a table (types 0 to 4, 7, 9, 14, 17, 38 and 43).

MarshalBinary(v) = source bytes with v's edits written, if ParseTable then the type's parse function returns v on those bytes; otherwise an error:
  written: field read at offset o -> written at o; header Length never written
  skipped: field past the end of a short table -> not written, not compared, no lengthening
  text unchanged -> number kept
  text changed, the number names a string no other field of the parsed structure uses -> same number, replaced in place
  text changed, number 0, a number naming no string, or a number shared in the parsed structure -> appended after the existing strings, in field order
  text empty -> number 0, read back as Not Specified
  string with no referrer left -> removed; each higher number -1, including a number that names no string
  list gains or loses items -> Length += size difference; bytes after the list move with it
  Info.Marshal -> entry point NumberOfStructs = structures written
  struct literal, no parsed source -> toTable encoding for types 1, 2 and 14; empty embedded Table for the others
  ReplaceSystemInfo, ReplaceBaseboardInfoMotherboard, RemoveBaseboardInfo, RemoveSystemSlotInfo -> rebuild only the structures they change, each under the same rule as MarshalBinary
  RemoveBaseboardInfo -> also drops removed handles from every structure that lists them
