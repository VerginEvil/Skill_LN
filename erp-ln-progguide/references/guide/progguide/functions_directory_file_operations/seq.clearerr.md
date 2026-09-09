# seq.clearerr()

## Syntax:
`function long seq.clearerr( long fp )`

## Description
This resets the error and end-of-file indicators for the specified file. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the file was opened.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the file was opened..  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Errror. Probably *fp* not connected |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
