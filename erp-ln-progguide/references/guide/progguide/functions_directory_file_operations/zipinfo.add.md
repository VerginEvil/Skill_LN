# zipinfo.add()

## Syntax:
`function [long] zipinfo.add( long handle, const string entry, [ long type ] )`

## Description
Adds an entry to a zipinfo object. The entry may either be a directory or a file. Optionally, the entry type (directory or file) may be specified.

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  a handle to a zipinfo object. Retrieved by zipinfo.new() or zipfile.info().  |
| `const string` | `entry` |  the name of a file or a directory  |
| `[ long` | `type ]` |  specify TDIR for directories, or TFILE for files; if not specified an attempt is made to determine the type using the entry name  |

## Return values
| | |
|---|---|
| 0 | OK, success. |
| <> 0 | When an error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function is available from [TIV](../tiv/tiv_overview.md) [1900](../tiv/tiv_1900.md).

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
