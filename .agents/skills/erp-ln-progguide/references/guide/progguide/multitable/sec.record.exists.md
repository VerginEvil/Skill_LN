# sec.record.exists()

## Syntax:
`function boolean sec.record.exists( long id, long occ )`

## Description
Check whether a secondary table record exists. When the record is saved but not yet committed, the function returns `true`.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  The ID of the secondary table. This ID was obtained via a call to [sec.add.table()](sec.add.table.md).  |
| `long` | `occ` |  The occurence number that must be checked. (Like `actual.occ`). For single occurrence sessions this number will always be 1. For multi occurrence sessions it is a number between 1 and the number of rows.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Return value
A boolean telling whether or not a record exists.
Note  Multi Table functionality is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Related topics
- [Multi Table Overview](overview.md)

- [Multi Table synopsis](synopsis.md)
