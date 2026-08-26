# seq.unlock()

## Syntax:
`function long seq.unlock( long mode, long offset, long size, long fp )`

## Description
This removes a lock set by [seq.lock()](seq.lock.md).

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |  The type of lock to remove:  |
| `long` | `offset` |  To remove a lock on a segment of the file, use this argument and the *size* argument to specify the offset of the segment from the beginning of the file and the length of the segment. The value of this argument must be >= 0 for mode SEQ_R_LCK and mode SEQ_W_LCK. It will be ignored for mode SEQ_F_R_LCK and for mode SEQ_F_W_LCK;  |
| `long` | `size` |  For an explanation see the *offset* argument. The value of this argument must be >= 1 for mode SEQ_R_LCK and mode SEQ_W_LCK. It will be ignored for mode SEQ_F_R_LCK and for mode SEQ_F_W_LCK;  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the file was opened.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| -1 | Error; probably *fp* not connected.  |
| < -1 | Error; Negative error value. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  All locks set on a file by a particular process are removed automatically when the file descriptor for the file is closed by the process (see [seq.close()](seq.close.md)) or when the process itself terminates.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
