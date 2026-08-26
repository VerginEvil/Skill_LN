# dir.open.tree()

## Syntax:
`function long dir.open.tree( const string path, [ long nlevels, long read_type ] )`

## Description
This is similar to [dir.open()](dir.open.md) in that it reads a specified directory into memory. However, *dir.open.tree()* can retrieve up to 256 directory levels.
The function returns a pointer ( *dfd*) to the directory data. [dir.entry()](dir.entry.md), [dir.rewind()](dir.rewind.md), and [dir.close()](dir.close.md) use this pointer to access the directory.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  The path to the required directory. This can have a maximum length of 512 characters (it might be further restricted by OS/file system limitations).  |
| `[ long` | `nlevels ]` |  Use this optional argument to indicate the number of directory levels that must be read. The default is one.  |
| `[ long` | `read_type ]` |  Use this argument to filter on types. It is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2150](../tiv/tiv_2150.md). If this argument is not provided, then TDIR + TFILE value is used as default. Allowed values, that can be combined with bit.or, are:  |

## Return values
| | |
|---|---|
| > 0 | Success; A pointer to the directory data. |
| <= 0 | Error; The negative error value may be system dependent. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  When a large directory tree is requested, this function can consume a large amount of memory and CPU time. This may block other processes in the same bshell for several minutes or longer, depending on the overall system load.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
