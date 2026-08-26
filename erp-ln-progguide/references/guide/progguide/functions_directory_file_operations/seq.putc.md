# seq.putc$()

## Syntax:
`function string seq.putc$( string char, long fp )`

## Description
This writes a specified character to a specified file. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.

## Arguments
| | | |
|---|---|---|
| `string` | `char` |  character  |
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the particular file was opened.  |

## Return values
The character written to the file. Or an empty string (a string of length 0) if the end-of-file was reached or an error occurred.
The last system error is available in the *e* variable – for example, for file system full, *e* will be ENOSPC (that is, 28) – for a list of error codes, see [Infor ES errors and messages](../errors/overview.md).

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
