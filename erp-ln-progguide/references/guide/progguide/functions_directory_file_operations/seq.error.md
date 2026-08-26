# seq.error()

## Syntax:
`function long seq.error( long fp )`

## Description
This checks the error indicator of a specified file. The error indicator is set when an error occurs while reading from or writing to the file. It lasts until it is cleared by [seq.clearerr()](seq.clearerr.md) or until the file is closed. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the file was opened.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the file was opened. .  |

## Return values
| | |
|---|---|
| 0 | Error indicator not set. |
| > 0 | Error indicator set |
| -1 | Error; probably *fp* not connected  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
