# file.stat()

## Syntax:
`function long file.stat( string file_name, ref long file_size, [ ref long ctime, ref long mtime, ref long atime ] )`

## Description
This returns information about a specified file. It is a short version of the [stat.info()](stat.info.md) function.

## Arguments
| | | |
|---|---|---|
| `string` | `file_name` |  The name of the file for which information is required.  |
| `ref long` | `file_size` |  The file size in bytes.  |
| `[ ref long` | `ctime ]` |  The time when the file status was last changed, as a number of seconds since 00:00:00 GMT, January 1, 1970.  |
| `[ ref long` | `mtime ]` |  The time when the file was last modified, as a number of seconds since 00:00:00 GMT, January 1, 1970.  |
| `[ ref long` | `atime ]` |  The time when the file data was last accessed, as a number of seconds since 00:00:00 GMT, January 1, 1970.  |

## Return values
| | |
|---|---|
| 0 | File exists. |
| <> 0 | Operating system error code. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
