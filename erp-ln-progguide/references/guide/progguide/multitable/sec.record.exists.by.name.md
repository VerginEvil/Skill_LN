# sec.record.exists.by.name()

## Syntax:
`function boolean sec.record.exists.by.name( const string tablename(), long occ )`

## Description
Check whether a secondary table record exists. When the record is saved but not yet committed, the function returns `true`.

## Arguments
| | | |
|---|---|---|
| `const string` | `tablename()` |  The name of the secondary table. This must be the name of a table for which [sec.add.table()](sec.add.table.md) has been called and a valid id has been returned.  |
| `long` | `occ` |  The occurence number that must be checked. (Like `actual.occ`). For single occurrence sessions this number will always be 1. For multi occurrence sessions it is a number between 1 and the number of rows.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2210.

## Return value
A boolean telling whether or not a record exists.
Note  Multi Table functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 2210](../tiv/tiv_2210.md).

## Related topics
- [Multi Table Overview](overview.md)
- [Multi Table synopsis](synopsis.md)
