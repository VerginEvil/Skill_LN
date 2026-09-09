# dal.reject()

## Syntax:
`#include <bic_dam>`
`function long dal.reject( const string tbl.name, const string reason$ )`

## Description
Rejects any changes and/or actions done to the current checked-out Business Object and sets the given reason for rejecting.
This is possible for *Pending* objects, which become Rejected, and for objects for which a Recall has been requested, which will then become Pending again.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name` |  A table code like "tdsls400".  |
| `const string` | `reason$` |  A reason for the rejection.  |

## Return values
| | |
|---|---|
| 0 | The request for reject was successfully made. |
| <> 0 | An error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Hooks called
- [on.reject()](../functions_dal/on.reject.md)

## Related topics
- [Database operations overview](overview.md)

- [Database Change Management (DBCM) overview](../functions_dbcm/overview.md)

- [Database operations synopsis](synopsis.md)
