# seq.write()

## Syntax:
`function long seq.write( const string buffer, long nrbytes, long fp )`

## Description
This function appends the specified number of bytes from the specified buffer to the specified file, beginning at the current file position.

## Arguments
| | | |
|---|---|---|
| `const string` | `buffer` |  Input string, providing the bytes to be written to the file.  |
| `long` | `nrbytes` |  The number of bytes to be written to the file. A negative number triggers the complete buffer to be written.  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.  |

## Return values
| | |
|---|---|
| > 0 | Number of bytes actually written. |
| 0 | End-of-file. |
| < -1 | Error; Probably *fp* not connected. (the last system error is available in the *e* variable – for example, for file system full, *e* will be ENOSPC (that is, 28) – for a list of error codes, see [Infor ES errors and messages](../errors/overview.md)) |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  Seq.write() doesn't write at the current file position if the file was opened with "a" or "a+", but it always appends at the end of the file, even after the file pointer was moved to another location using seq.seek(). This allows multiple processes appending to the same file.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
