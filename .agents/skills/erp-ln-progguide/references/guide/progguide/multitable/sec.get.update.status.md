# sec.get.update.status()

## Syntax:
`function long sec.get.update.status( long id, long occ )`

## Description
Retrieve the update status of occurrence `occ` of secondary table `id`.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  The ID of the secondary table. This ID was obtained via a call to [sec.add.table()](sec.add.table.md).  |
| `long` | `occ` |  The occurence number that must be checked. (Like `actual.occ`). For single occurrence sessions this number will always be 1. For multi occurrence sessions it is a number between 1 and the number of rows.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

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
