# sql.close()

## Syntax:
`function long sql.close( long sql_id )`

## Description
This deletes all internal information relating to the specified query. The *sql_id* argument indicates the query ID, as returned by [sql.parse()](sql.parse.md).

## Arguments
| | | |
|---|---|---|
| `long` | `sql_id` |   |

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
