# dbcm.object.is.checked.out()

## Syntax:
`function boolean dbcm.object.is.checked.out( const string toid$ )`

## Description
Tests whether the business object identified by the specified Typed Object Id is checked-out.

## Arguments
| | | |
|---|---|---|
| `const string` | `toid$` |  A Typed Object Id. A Typed Object Id is a string of 34 characters identifying a checked-out business object.  |

## Return values
| | |
|---|---|
| true | The business object is checked-out. |
| false | In any other case. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.

## Related topics
- [Database Change Management (DBCM) overview](overview.md)
- [Database Change Management operations synopsis](synopsis.md)
