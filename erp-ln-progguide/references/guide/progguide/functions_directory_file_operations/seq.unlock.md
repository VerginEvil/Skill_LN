# seq.unlock()

## Syntax:
`function long seq.unlock( long mode, long offset, long size, long fp )`

## Description
This removes a lock set by [seq.lock()](seq.lock.md).

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
| < -1 | Error; Negative error value. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  All locks set on a file by a particular process are removed automatically when the file descriptor for the file is closed by the process (see [seq.close()](seq.close.md)) or when the process itself terminates.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
