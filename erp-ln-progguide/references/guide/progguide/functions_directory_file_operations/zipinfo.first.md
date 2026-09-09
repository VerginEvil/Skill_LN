# zipinfo.first()

## Syntax:
`function boolean zipinfo.first( long handle, ref string entry, ref long type )`

## Description
Retrieves the first entry from a zipinfo object.

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  a handle to a zipinfo object. Retrieved by zipinfo.new() or zipfile.info().  |
| `ref string` | `entry` |  the returned name of the entry.  |
| `ref long` | `type` |  the returned entry type: TDIR for directories, TFILE for files  |

## Return values
| | |
|---|---|
| True | the zipinfo object has a first entry. |
| False | the zipinfo object has no first entry. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function is available from [TIV](../tiv/tiv_overview.md) [1900](../tiv/tiv_1900.md).

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
