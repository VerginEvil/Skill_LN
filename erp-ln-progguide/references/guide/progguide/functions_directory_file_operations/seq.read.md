# seq.read()

## Syntax:
`function long seq.read( ref string buffer, long nrbytes, long fp )`

## Description
This reads a specified number of bytes from a specified file into *buffer*. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.

## Arguments
| | | |
|---|---|---|
| `ref string` | `buffer` |  Buffer  |
| `long` | `nrbytes` |  Number of bytes to read.  |
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the particular file was opened.  |

## Return values
| | |
|---|---|
| > 0 | Number of bytes read. |
| 0 | Either end of file encountered or the number of bytes to read was 0. |
| -1 | Error; probably *fp* not connected.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
