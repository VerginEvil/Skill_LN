# sql.fetch()

## Syntax:
`function long sql.fetch( long sql_id )`

## Description
This reads a single query result and stores the values retrieved in the variables specified in the SELECT list. The *sql_id* argument indicates the query ID, as returned by [sql.parse()](sql.parse.md). You must call the function for each individual record in the result set.

## Arguments
| | | |
|---|---|---|
| `long` | `sql_id` |    |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |
The function returns eendfile when it reaches the end of the result set. It returns enorec if the set is empty.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Dynamic SQL queries overview](overview.md)

- [Dynamic SQL queries synopsis](synopsis.md)
