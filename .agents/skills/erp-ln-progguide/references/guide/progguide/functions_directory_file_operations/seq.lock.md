# seq.lock()

## Syntax:
`function long seq.lock( long mode, long offset, long size, long fp )`

## Description
This sets read and write locks on a specified file or segment of a file.

## Arguments
| | |
|---|---|
| SEQ_R_LCK | read lock |
| SEQ_W_LCK | write lock |
| SEQ_F_R_LCK | file lock (read) |
| SEQ_F_W_LCK | file lock (write) |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| -1 | Error; probably *fp* not connected. |
| < -1 | Operating system error code. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  A read lock prevents any process from setting a write lock on the protected file or file segment. Multiple read locks can be set for the same file or file segment. The file with which the lock is associated must have been opened with read access (see [seq.open()](seq.open.md)).
A write lock prevents any process from setting a read lock or a write lock on the protected file or file segment. Only one write lock can exist for a particular file or file segment. The file with which the lock is associated must have been opened with write access.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
