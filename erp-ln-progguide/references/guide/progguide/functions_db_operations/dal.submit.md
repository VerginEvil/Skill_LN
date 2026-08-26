# dal.submit()

## Syntax:
`#include <bic_dam>`
`function long dal.submit( const string tbl.name )`

## Description
Assigns the *Pending* status to the checked-out Business Object that is identified by the current record.
Only *Draft*, *Draft (Revision)*, and *Rejected* business objects can be submitted.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name` |  A table code.  |

## Return values
| | |
|---|---|
| 0 | The submit was successful. |
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
