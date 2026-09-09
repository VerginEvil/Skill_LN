# dal.recall()

## Syntax:
`#include <bic_dam>`
`function long dal.recall( const string tbl.name )`

## Description
Makes a request to recall the checked-out business object that is identified by the current record.
This is only possible for *Pending* objects.

## Arguments
| | | |
|---|---|---|
| `const string` | `tbl.name` |  A table code.  |

## Return values
| | |
|---|---|
| 0 | The request for recall was successfully made. |
| <> 0 | An error occurred. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1800.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2120 and Value of argument tbl.name starts with "tx"

## Hooks called
- [on.recall()](../functions_dal/on.recall.md)

## Related topics
- [Database operations overview](overview.md)

- [Database Change Management (DBCM) overview](../functions_dbcm/overview.md)

- [Database operations synopsis](synopsis.md)
