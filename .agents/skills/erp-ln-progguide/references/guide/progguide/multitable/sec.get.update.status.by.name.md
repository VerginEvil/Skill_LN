# sec.get.update.status.by.name()

## Syntax:
`function long sec.get.update.status.by.name( const string tablename(), long occ )`

## Description
Retrieve the update status of occurrence `occ` of a secondary table `id`.

## Arguments
| | | |
|---|---|---|
| `const string` | `tablename()` |  The name of the secondary table. This must be the name of a table for which [sec.add.table()](sec.add.table.md) has been called and a valid id has been returned.  |
| `long` | `occ` |  The occurence number that must be checked. (Like `actual.occ`). For single occurrence sessions this number will always be 1. For multi occurrence sessions it is a number between 1 and the number of rows.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2210.

## Return value
The result uses the same defines as the value of the [update.status](../misc/predefined_variables.md) variable for the main table.
| | |
|---|---|
| 0 | No update |
| ADD.SET | during add |
| MODIFY.SET | during modify |
| MARK.DELETE | during delete |

## Related topics
- [Multi Table Overview](overview.md)

- [Multi Table synopsis](synopsis.md)
