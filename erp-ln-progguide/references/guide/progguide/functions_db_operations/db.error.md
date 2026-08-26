# db.error()

## Syntax:
`function long db.error( [ long table_id ] )`

## Description
Use this to retrieve the error code returned by the most recent database action. If you specify a table ID, the function retrieves the most recent error code returned by an action on that table.

## Arguments
| | | |
|---|---|---|
| `[ long` | `table_id ]` |  The table ID, as returned by [db.bind()](db.bind.md).  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
