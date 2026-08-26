# sec.mark.delete.by.name

## Syntax:
`function void sec.mark.delete.by.name( const string tablename() )`

## Description
Perform an `MARK.DELETE` on a secondary table. The record will be deleted on the next save ( `update.db`).

## Arguments
| | | |
|---|---|---|
| `const string` | `tablename()` |  The name of the secondary table. This must be the name of a table for which [sec.add.table()](sec.add.table.md) has been called and a valid id has been returned.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2210.
Note  Multi Table functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 2210](../tiv/tiv_2210.md).

## Related topics
- [Multi Table Overview](overview.md)
- [Multi Table synopsis](synopsis.md)
