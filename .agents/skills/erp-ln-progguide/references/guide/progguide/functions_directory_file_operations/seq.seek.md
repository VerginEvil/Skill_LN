# seq.seek()

## Syntax:
`function long seq.seek( long offset, long opt, long fp )`

## Description
This changes the current file position.

## Arguments
| | | |
|---|---|---|
| `long` | `offset` |  The new file position, as a number of bytes.  |
| `long` | `opt` |  This determines whether the specified offset is from the beginning of the file, the end of the file, or the current file position: 0 new position is offset from the beginning of the file 1 new position is offset from the current file position 2 new position is offset from the end of the file  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.  |

## Return values
| | |
|---|---|
| >= 0 | Success. Returns new position in bytes from the beginning of the file. |
| < 0 | Error; probably *fp* not connected. Current file position is not changed. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  It is undefined whether or not seq.seek() past end-of-file succeeds or fails.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
