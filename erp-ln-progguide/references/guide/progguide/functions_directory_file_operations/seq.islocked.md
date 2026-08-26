# seq.islocked()

## Syntax:
`function long seq.islocked( long mode, long offset, long size, long fp )`

## Description
This checks whether a specified file or segment of a file has been locked by [seq.lock()](seq.lock.md).

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |  The type of lock you want to check for:  |
| `long` | `offset` |  To check whether a particular segment of the file has been locked, use this argument and the *size* argument to specify the offset of the segment from the beginning of the file and the length of the segment. The value of this argument must be >= 0 for mode SEQ_R_LCK and mode SEQ_W_LCK. It will be ignored for mode SEQ_F_R_LCK and for mode SEQ_F_W_LCK;  |
| `long` | `size` |  For an explanation see the *offset* argument. The value of this argument must be >= 1 for mode SEQ_R_LCK and mode SEQ_W_LCK. It will be ignored for mode SEQ_F_R_LCK and for mode SEQ_F_W_LCK;  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the file was opened.  |

## Return values
| | |
|---|---|
| 0 | File or file segment not locked. |
| <> 0 | File or file segment locked |

## Context
This function is implemented in the porting set and can be used in all script types.
Remark  On Windows this function does not work and always returns a value < 0.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
