# dal.destroy()

## Syntax:
`#include <bic_dam>`
`function void dal.destroy( string dal.name, long object_set, ref long retval, long prop_check, [ long mode, long eflag ] )`

## Description
Use this to delete a database record. The function encapsulates the [db.delete()](db.delete.md) function with the DAL hooks of the object set. If the [before.destroy.object()](../functions_dal/before.destroy.object.md) hook fails, the database operation is cancelled.

## Arguments
| | | |
|---|---|---|
| `string` | `dal.name` |  A string containing the name of the DAL.  |
| `long` | `object_set` |  The ID of an open object set (if this ID is not known, use the table ID).  |
| `ref long` | `retval` |  The return value of the object hooks (< 0), of the [db.delete()](db.delete.md) function (> 0), or 0 if the function is successful.  |
| `long` | `prop_check` |  A boolean value that indicates whether or not the [method.is.allowed()](../functions_dal/method.is.allowed.md) hook must be executed. If set to TRUE, the method.is.allowed() hook is executed immediately before the [before.destroy.object()](../functions_dal/before.destroy.object.md) hook. If set to FALSE, the method.is.allowed() hook is not executed.  |
| `[ long` | `mode ]` |  Set this to DB.RETRY if retry points and the SELECT FOR UPDATE statement are being used. The actual database action is postponed until the transaction is committed.  |
| `[ long` | `eflag ]` |  For some errors, it is possible to indicate the action the system must perform when the error occurs. You use this argument to specify the required action(s). See [Error handling](../functions_database_handling/error_handling.md)  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
