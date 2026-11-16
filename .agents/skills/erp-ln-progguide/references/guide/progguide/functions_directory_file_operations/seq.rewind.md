# seq.rewind()

## Syntax:
`function long seq.rewind( long fp )`

## Description
This sets the current file position to the beginning of the file. It is equivalent to: [seq.seek()](seq.seek.md) except that the return value is always -1 on error.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the particular file was opened.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error; probably *fp* not connected. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
