# db.check.row.changed()

## Syntax:
`function long db.check.row.changed( long table_id )`

## Description
This function checks whether a record that has been delayed locked and changed by the current process has been changed by another process ("user"). It does not check whether the row has been modified in the current process. In a way it answers the question: "If I would update the current record now, would I get the infamous EROWCHANGED error?"

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |

## Return values
| | |
|---|---|
| 0 | Record has not been changed by another process. |
| <> 0 | Error. |
| EROWCHANGED | Record has been changed by another process. |
| ENOCURR | No current record set. The db-call interface (e.g. db.eq(..., db.delayed)) must be used to set a current record, before calling the db.check.row.changed() function. |
| ENOTLOCKED | Record has not been (delayed) locked. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
