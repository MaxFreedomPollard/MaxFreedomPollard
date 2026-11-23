Add fs.cp, fs.opendir, fs.statfs and recursive fs.readdir to mock-fs.

Directory copies require recursive. Reject self-copies and copies into the source tree. An existing destination directory is merged into; force and errorOnExist apply only to colliding files and symlinks. These are replaced unless force is false, which skips them or fails when errorOnExist is true. A directory and a non-directory never replace each other. Filters see every entry, the source included, and prune rejected entries with their subtrees. Copy symlinks as links: a relative target becomes an absolute path, resolved from the directory that holds the link, unless verbatimSymlinks preserves its text. preserveTimestamps retains modification times of files, directories and symlinks, merged directories included. Failures use Node's own fs.cp and fs.Dir error codes, and a colliding symlink fails like a file.

Directory handles expose their opening path and support asynchronous iteration, which closes the handle after the last entry.

statfs describes the whole mock file system: type zero, 4096-byte blocks, 1,000,000 blocks and 1,000,000 inodes, with bigint figures when requested. Every file, directory and symlink consumes one inode. Hard links share their inode and content blocks. Only file content occupies blocks, rounded up per file; all unused blocks are available.

Recursive listings include all descendants, even beneath symlinked directories. With throwIfNoEntry false, statSync and lstatSync return undefined for a missing path, and statSync also for a path through a file.
