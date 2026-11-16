# seq.puts()

## Syntax:
`function long seq.puts( const string line, long fp )`

## Description
This writes the specified characters to a specified file, and appends a new line character. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.

## Arguments
| | | |
|---|---|---|
| `const string` | `line` |  Specified characters  |
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the particular file was opened.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error; probably *fp* not connected (the last system error is available in the *e* variable – for example, for file system full, *e* will be ENOSPC (that is, 28) – for a list of error codes, see [Infor ES errors and messages](../errors/overview.md)) |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
