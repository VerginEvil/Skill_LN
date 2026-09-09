# seq.skip()

## Syntax:
`function long seq.skip( long nrbytes, long fp )`

## Description
This skips *nrbytes* bytes, relative to the current file position, in a file represented by *fp*. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the particular file was opened. It is equivalent to: [seq.seek()](seq.seek.md).

## Arguments
| | | |
|---|---|---|
| `long` | `nrbytes` |  This skips nrbytes bytes, relative to the current file position, in a file represented by fp. fp is the file pointer returned by seq.open() when the particular file was opened. It is equivalent to: seq.seek( nrbytes, 1, fp ).  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.  |

## Return values
| | |
|---|---|
| >= 0 | Success. Returns new position in bytes from the beginning of the file. |
| < 0 | Error; probably *fp* not connected. Current file position is not changed. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  It is undefined whether or not seq.skip() past end-of-file succeeds or fails.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
