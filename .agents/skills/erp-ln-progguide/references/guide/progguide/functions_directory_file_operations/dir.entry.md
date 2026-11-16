# dir.entry()

## Syntax:
`function string dir.entry( long dfd, long read_type, [ ref long return_type, ref long filesize, ref long mode ] )`

## Description
This retrieves entries from a previously opened directory. It retrieves the entries sequentially.

## Arguments
| | |
|---|---|
| TDIR | directories |
| TFILE | files |
| TLINK | symbolic link. |
| | |
|---|---|
| TDIR | directory |
| TFILE | file |
| TLINK | symbolic link |
| | |
|---|---|
| STAT_READABLE | read |
| STAT_WRITEABLE | read, write, and delete |
| STAT_EXECUTABLE | run program |

## Return values
The directory entry. Or an empty string if the end of the entry list has been reached.

## Context
This function is implemented in the porting set and can be used in all script types.
Symbolic links  The TLINK macro is allowed to be used on all platforms, but its functionality (support for symbolic links) is limited to UNIX/Linux only. This macro has no effect on Windows. This macro is available as of [TIV](../tiv/tiv_overview.md) [level 2150](../tiv/tiv_2150.md).

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
