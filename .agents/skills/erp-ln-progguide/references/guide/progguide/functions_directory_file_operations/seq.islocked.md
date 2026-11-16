# seq.islocked()

## Syntax:
`function long seq.islocked( long mode, long offset, long size, long fp )`

## Description
This checks whether a specified file or segment of a file has been locked by [seq.lock()](seq.lock.md).

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
| 0 | File or file segment not locked. |
| <> 0 | File or file segment locked |

## Context
This function is implemented in the porting set and can be used in all script types.
Remark  On Windows this function does not work and always returns a value < 0.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
