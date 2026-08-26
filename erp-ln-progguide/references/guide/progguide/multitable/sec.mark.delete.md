# sec.mark.delete()

## Syntax:
`function void sec.mark.delete( long id )`

## Description
Perform an `MARK.DELETE` on a secondary table. The record will be deleted on the next save ( `update.db`).

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  The ID of the secondary table. This ID was obtained via a call to [sec.add.table()](sec.add.table.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  Multi Table functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Related topics
- [Multi Table Overview](overview.md)
- [Multi Table synopsis](synopsis.md)
