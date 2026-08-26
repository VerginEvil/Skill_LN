# seq.eof()

## Syntax:
`function long seq.eof( long fp )`

## Description
This checks the end-of-file indicator of a specified file. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the file was opened.
An end-of-file indication lasts until it is cleared by [seq.clearerr()](seq.clearerr.md) or until the file is closed.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the file was opened. .  |

## Return values
| | |
|---|---|
| 0 | End-of-file indicator not set. |
| > 0 | End-of-file indicator set |
| -1 | Error; probably *fp* not connected  |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  The end-of-file indication is only set when really trying to *read* past end-of-file, and not when moving past end-of-file using [seq.seek()](seq.seek.md) or [seq.skip()](seq.skip.md).

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
