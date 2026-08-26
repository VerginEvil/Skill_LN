# dal.new.object()

## Syntax:
`#include <bic_dam>`
`function long dal.new.object( string tbl.name )`

## Description
Use this to indicate the DAL that a new record is about to be inserted. This function set record defaults, by calling [db.set.to.default()](db.set.to.default.md) and the [set.object.defaults()](../functions_dal/set.object.defaults.md) hook.
After this call, fields can be set with [dal.set.field()](dal.set.field.md). And after that, the record can be saved with [dal.save.object()](dal.save.object.md).

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  A string containing the name of the DAL.  |

## Return values
| | |
|---|---|
| 0 | OK |
| DALHOOKERROR | The DAL could not be opened |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Hooks called
- [before.open.object.set()](../functions_dal/before.open.object.set.md) if this is the first call to the DAL
- [before.new.object()](../functions_dal/before.new.object.md)
- [set.object.defaults()](../functions_dal/set.object.defaults.md)

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
