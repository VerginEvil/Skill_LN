# db.lock.table()

## Syntax:
`function long db.lock.table( long table_id )`

## Description
This locks a specified table. Other users cannot then write to or delete the table or any parts of the table. Nor can they lock the table or any parts of the table. The lock is released by [commit.transaction()](commit.transaction.md) or [abort.transaction()](abort.transaction.md)
Note that this function cannot be used within a transaction; see [Transaction handling](../functions_database_handling/transaction_handling.md).

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |

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
