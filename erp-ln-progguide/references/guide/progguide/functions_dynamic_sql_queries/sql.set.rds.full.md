# sql.set.rds.full()

## Syntax:
`function long sql.set.rds.full( long sql_id, long size )`

## Description
This sets the size of the RDBMS buffer. The buffer is used to send the result rows of a query from the database back to the client (that is, the bshell). For example, if a query fetches 20 rows and you have set the size of the buffer to 5, then the database sends the rows back to the client five at a time.
You call the function immediately after calling [sql.parse()](sql.parse.md).

## Arguments
| | | |
|---|---|---|
| `long` | `sql_id` |  The query ID, as returned by [sql.parse()](sql.parse.md).  |
| `long` | `size` |  The size of the buffer, in rows.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Dynamic SQL queries overview](overview.md)
- [Dynamic SQL queries synopsis](synopsis.md)
