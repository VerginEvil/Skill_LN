# dal.change.object()

## Syntax:
`#include <bic_dam>`
`function long dal.change.object( string dal_name )`

## Description
Use this to indicate the DAL that the current record is about to be changed. After this call, fields can be changed with [dal.set.field()](dal.set.field.md). And after that, the record can be saved with [dal.save.object()](dal.save.object.md).

## Arguments
| | | |
|---|---|---|
| `string` | `dal_name` |  A string containing the name of the DAL.  |

## Return values
| | |
|---|---|
| 0 | OK |
| DALHOOKERROR | The DAL could not be opened |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Hooks called
- [before.open.object.set()](../functions_dal/before.open.object.set.md) if this is the first call to the DAL

- [before.change.object()](../functions_dal/before.change.object.md)

Note  This function does not lock the record!

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
