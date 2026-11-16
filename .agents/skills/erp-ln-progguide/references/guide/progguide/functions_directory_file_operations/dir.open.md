# dir.open()

## Syntax:
`function long dir.open( const string path, [ long read_type ] )`

## Description
This reads the specified directory into memory. The *path* argument can have a maximum length of 512 characters.
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

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
