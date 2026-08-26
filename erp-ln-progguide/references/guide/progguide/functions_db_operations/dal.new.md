# dal.new()

## Syntax:
`#include <bic_dam>`
`function void dal.new( string tbl.name, long object_set, ref long retval, long prop_check, [ long mode, long eflag ] )`

## Description
Use this to add a new record to the database. The function encapsulates the [db.insert()](db.insert.md) function with the DAL hooks of the object set. If the [before.save.object()](../functions_dal/before.save.object.md) hook fails, the database operation is cancelled.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  A string containing the name of the DAL.  |
| `long` | `object_set` |  The ID of an open object set (if this ID is not known, use the table ID).  |
| `ref long` | `retval` |  The return value of the object hooks (< 0), of the [db.insert()](db.insert.md) function (> 0), or 0 if the function is successful.  |
| `long` | `prop_check` |  A boolean value that indicates whether or not property checks must be executed. If set to TRUE, the property checks are executed immediately before the [before.save.object()](../functions_dal/before.save.object.md) hook. If set to FALSE, the property checks are not executed.  |
| `[ long` | `mode ]` |  Set this to DB.RETRY if retry points and the SELECT FOR UPDATE statement are being used. The actual database action is postponed until the transaction is committed.  |
| `[ long` | `eflag ]` |  For some errors, it is possible to indicate the action the system must perform when the error occurs. You use this argument to specify the required action(s). See [Error handling](../functions_database_handling/error_handling.md)  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  It is advised to use [dal.new.object()](dal.new.object.md) and [dal.save.object()](dal.save.object.md) when inserting records for an Extended (DAL2) DAL. Only then field dependencies are taken into account. See [DAL2 Field dependencies](../functions_dal/dal2_field_dependencies.md) for more information.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
