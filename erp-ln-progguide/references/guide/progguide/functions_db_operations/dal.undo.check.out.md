# dal.undo.check.out()

## Syntax:
`#include <bic_dam>`
`function long dal.undo.check.out( const string tbl.name )`

## Description
Undoes a check-out of the business object to which the active record belongs. The undo check-out fails in case the business object is not checked-out, or if the state of the object is other than `DBCM_STATUS_DRAFT`, `DBCM_STATUS_DRAFT_REV`, or `DBCM_STATUS_REJECTED`.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name` |  A table code.  |

## Return values
| | |
|---|---|
| 0 | In case of success. |
| <> 0 |  An error occurred.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and Value of argument tbl.name starts with "tx"

## Related topics
- [Database operations overview](overview.md)
- [Database Change Management (DBCM) overview](../functions_dbcm/overview.md)
- [Database operations synopsis](synopsis.md)
