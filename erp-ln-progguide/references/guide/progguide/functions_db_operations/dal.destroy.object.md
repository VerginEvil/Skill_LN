# dal.destroy.object()

## Syntax:
`#include <bic_dam>`
`function long dal.destroy.object( string tbl.name, [ long error.flag ] )`

## Description
Deletes a record of the given table. The record must have been locked for update. This function does the same as [dal.destroy()](dal.destroy.md), however it does more detailed permission checking. Further, the [method.is.allowed()](../functions_dal/method.is.allowed.md) hook is always called ( [dal.destroy()](dal.destroy.md) allows you to skip this hook by passing FALSE to the prop_check parameter).
Except for more detailed permission checking, this function is equivalent to:
`dal.destroy(tbl.name, tbl.cursor, retval, true, db.retry)`
The sequence of the actions is as follows:
1. Table level permission is checked
1. Record level permission is checked
1. The method.is.allowed(DAL_DESTROY) hook is called
1. The before.destroy.object hook is called
1. The delete is performed
1. The after.destroy.object hook is called

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  The table name of the DAL.  |
| `[ long` | `error.flag ]` |  For some errors, it is possible to indicate the action the system must perform when the error occurs. You use this argument to specify the required action(s). See [Error handling](../functions_database_handling/error_handling.md).  |

## Return values
| | |
|---|---|
| 0 | Record is deleted |
| DALHOOKERROR | One of the hooks blocked the delete action |
| DALNOSETPERM | No table level permission |
| DALNOOBJPERM | No record level permission |
| > 0 | The error code of the db.delete() action |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Error Handling
In case a database error occurs (a return value greater than 0), then this function will set an error message. E.g. in case a record cannot be deleted because it is used in another table then an error message is set.

## Hooks called
- [before.open.object.set()](../functions_dal/before.open.object.set.md) if this is the first call to the DAL
- [method.is.allowed()](../functions_dal/method.is.allowed.md)
- [before.destroy.object()](../functions_dal/before.destroy.object.md)
- [after.destroy.object()](../functions_dal/after.destroy.object.md)    Notes  This function can be be used for Update Sessions as well as Integrations via OpenWorld. Because it performs more detailed permission checking it is a bit slower than [dal.destroy()](dal.destroy.md). Therefore it is advised to use [dal.destroy()](dal.destroy.md) in case performance is at stake.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
