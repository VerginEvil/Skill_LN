# sql.break()

## Syntax:
`function long sql.break( long sql_id )`

## Description
This stops the specified query and clears any interim results. The *sql_id* argument indicates the query ID, as returned by [sql.parse()](sql.parse.md). The function does not remove the query itself. So the query can be reused after binding to another variable, for example.

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
