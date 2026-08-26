# abort.transaction()

## Syntax:
`function long abort.transaction( )`

## Description
This cancels the current database transaction. No changes are stored in the database.
To commit a transaction and store changes made in the database, use [commit.transaction()](commit.transaction.md) instead.

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
