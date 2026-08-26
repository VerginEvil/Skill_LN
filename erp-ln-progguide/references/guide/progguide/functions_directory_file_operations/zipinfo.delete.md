# zipinfo.delete()

## Syntax:
`function [long] zipinfo.delete( long handle )`

## Description
Deletes a zipinfo object.

## Arguments
| | | |
|---|---|---|
| `long` | `handle` |  a handle to a zipinfo object. Retrieved by zipinfo.new() or zipfile.info().  |

## Return values
| | |
|---|---|
| 0 | OK, success. |
| < 0 | When an error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function is available from [TIV](../tiv/tiv_overview.md) [1900](../tiv/tiv_1900.md).

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
