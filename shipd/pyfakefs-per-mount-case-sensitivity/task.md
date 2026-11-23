Under Linux and macOS, the root path (`/`) is the only mount point created in the fake file system. If you need support for more mount points, you can add them using `FakeFilesystem.add_mount_point(path, total_size=None, can_exist=False, case_sensitive=None)` with a new last parameter `case_sensitive=None`:
  case_sensitive=None -> follows is_case_sensitive (including later changes)
  case_sensitive=True / False -> overrides is_case_sensitive for that mount point

Each path component in path APIs and public `FakeDirectory` methods (`add_entry`, `get_entry`, `remove_entry`) is checked by the mount point holding its directory:
  case-insensitive -> str.lower() comparison
  OSType.MACOS -> equal NFD forms match under either case policy (OSType.LINUX and OSType.WINDOWS do not normalize)

For matching spellings in the same directory, directory listings keep the stored name and new-entry creation raises `FileExistsError`. Renaming when old and new paths differ only by a matching final name:
  case-insensitive mount -> stores the new spelling in place
  case-sensitive mount -> leaves the entry unchanged
