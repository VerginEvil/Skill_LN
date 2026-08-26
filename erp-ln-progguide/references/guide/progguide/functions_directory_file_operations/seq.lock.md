# seq.lock()

## Syntax:
`function long seq.lock( long mode, long offset, long size, long fp )`

## Description
This sets read and write locks on a specified file or segment of a file.

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |  The type of lock to set:  |
| `long` | `offset` |  To set a lock on a segment of the file, use this argument and the *size* argument to specify the offset of the segment from the beginning of the file and the length of the segment. The value of this argument must be >= 0 for mode SEQ_R_LCK and mode SEQ_W_LCK. It will be ignored for mode SEQ_F_R_LCK and for mode SEQ_F_W_LCK;  |
| `long` | `size` |  For an explanation see the *offset* argument. The value of this argument must be >= 1 for mode SEQ_R_LCK and mode SEQ_W_LCK. It will be ignored for mode SEQ_F_R_LCK and for mode SEQ_F_W_LCK;  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the file was opened.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| -1 | Error; probably *fp* not connected.  |
| < -1 | Operating system error code. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  A read lock prevents any process from setting a write lock on the protected file or file segment. Multiple read locks can be set for the same file or file segment. The file with which the lock is associated must have been opened with read access (see [seq.open()](seq.open.md)).
A write lock prevents any process from setting a read lock or a write lock on the protected file or file segment. Only one write lock can exist for a particular file or file segment. The file with which the lock is associated must have been opened with write access.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
