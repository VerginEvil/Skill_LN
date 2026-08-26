# db.insert()

## Syntax:
`function long db.insert( long table_id, [ long mode, long eflag ] )`

## Description
This adds a new record to a specified table. The record pointer does not change.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `[ long` | `mode ]` |  This has two possible values:  |
| `[ long` | `eflag ]` |  For some errors, it is possible to indicate the action the system must perform when the error occurs. You use this argument to specify the required action(s). See [Error handling](../functions_database_handling/error_handling.md).  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
