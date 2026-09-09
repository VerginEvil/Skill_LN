# commit.transaction()

## Syntax:
`function long commit.transaction( )`

## Description
This ends the current transaction. All changes made during the transaction are stored in the database.
To cancel a transaction, use [abort.transaction()](abort.transaction.md) instead.

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
