# dal.get.object()

## Syntax:
`#include <bic_dam>`
`function long dal.get.object( string tbl.name, long lock, [ string key_field1, string key_value1 ], ... )`

## Description
Reads a record of the given table. In case the lock parameter is set to true, the record is locked for update. This function accepts a list of primary key field/value pairs.
The sequence of the actions is as follows:
1. The key fields are set according to the passed list of fields
1. The before.get.object hook is called with the DAL_FIND option
1. The record is read or locked
1. Record level permission is checked
1. The after.get.object hook is called with the DAL_FIND option   In case this function is called in the context of a 4GL-Session for a table which is either defined as the maintable or a secondary table for this session, this function will check whether the requested record is already present in the 4GL-Engine buffers. If so, the 4GL-Engine record buffer is fetched and will not be read from the database. This is especially useful when in a DAL script of a secondary table the corresponding maintable record is needed.
Note  The dal.get.object() function will return the table fields which are updated through the UI script or by the UI. However, in case these table fields are changed in a DAL script before the dal.get.object() function is called, the dal.get.object() will overwrite these changes.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  the table name of the DAL.  |
| `long` | `lock` |  if true the record is locked for update  |
| `[ string` | `key_field1 ]` |  |
| `[ string` | `key_value1 ]` |  |
| `` | `...` |  List of primary key field / value pairs in the format "ppmmm999.ffff", value. In case of array elements, specify the field as "ppmmm999.ffff(element)"  |

## Return values
| | |
|---|---|
| 0 | Record is read or locked for update |
| DALHOOKERROR | One of the hooks blocked the read action |
| DALNOOBJPERM | No record level permission |
| > 0 | The error code of the read action in case this failed (e.g. ENOREC). For a list of possible errormessages see the list of [db-errormessages](../errors/database_errors.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Hooks called
- [before.open.object.set()](../functions_dal/before.open.object.set.md) if this is the first call to the DAL
- [before.get.object()](../functions_dal/before.get.object.md)
- [after.get.object()](../functions_dal/after.get.object.md)

## Error Handling
In case a database error occurs (a return value greater than 0), then this function will set an error message. E.g. in case a record is not found then an error message is set. So if you want to ignore such an error, make sure that you reset the dal error message stack by calling [dal.reset.error.messages()](../functions_message_handling/dal.reset.error.messages.md) or [dal.clear.error.messages()](../functions_message_handling/dal.clear.error.messages.md).

## Example
```

Identical constructions:

tisfc001.pdno = i.prod.order
ret.val = dal.get.object("tisfc001", false)

ret.val = dal.get.object("tisfc001", false, “tisfc001.pdno”, i.prod.order)
```
Note  This function is can be used in Update Sessions as well as Integrations via OpenWorld. However, be aware that since this function calls the [before.get.object()](../functions_dal/before.get.object.md) and [after.get.object()](../functions_dal/after.get.object.md) hooks it cannot match the performance of a BaanSQL query. So in most cases, it is advised to write your own query.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
