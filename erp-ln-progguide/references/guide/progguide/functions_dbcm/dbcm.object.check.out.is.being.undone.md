# dbcm.object.check.out.is.being.undone()

## Syntax:
`function boolean dbcm.object.check.out.is.being.undone( const string toid$ )`

## Description
Checks if the check-out of the specified object is being undone. That is, if the dbcm.undo.check.out.object() function is in progress.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id. A Typed Object Id is a string of 34 characters identifying a checked-out business object.  |

## Return values
| | |
|---|---|
| true | The check-out is being undone. |
| false | In any other case. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2201.
Note  This function is available in ES10.4.2 from TIV level 2041.
This function is available in ES10.5.x from TIV level 2151.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
