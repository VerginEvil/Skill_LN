# db.retry.point()

## Syntax:
`function void db.retry.point( )`

## Description
This sets a retry point for the current transaction. The program returns to this point if an error occurs during the transaction; the transaction is then retried. When you include a retry point for a transaction, you must set it before the start of the transaction.
When a retry occurs, all messages that were set with dal.set.error.message are also reset. Messages that were set before the retry point will be retained.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Database handling overview](../functions_database_handling/overview.md)
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
