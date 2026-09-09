# db.create.table()

## Syntax:
`function long db.create.table( long table_id, long compnr )`

## Description
This creates a new database table.
Note that this function cannot be used within a transaction; see [Transaction handling](../functions_database_handling/transaction_handling.md).

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table identifier `(tppmmm999)` for the new table.  |
| `long` | `compnr` |  This optional argument specifies a company number for the table. The default company is the company of the user.  |

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
