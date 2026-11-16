# dir.open.tree()

## Syntax:
`function long dir.open.tree( const string path, [ long nlevels, long read_type ] )`

## Description
This is similar to [dir.open()](dir.open.md) in that it reads a specified directory into memory. However, *dir.open.tree()* can retrieve up to 256 directory levels.
The function returns a pointer ( *dfd*) to the directory data. [dir.entry()](dir.entry.md), [dir.rewind()](dir.rewind.md), and [dir.close()](dir.close.md) use this pointer to access the directory.

## Arguments
| | |
|---|---|
| TDIR | directory |
| TFILE | file |
| TLINK | symbolic link |

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
