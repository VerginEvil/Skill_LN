# db.drop.table()

## Syntax:
`function long db.drop.table( long table_id, [ long flag, long comp_nr ] )`

## Description
This deletes a specified table. Data and indices associated with the table are also deleted. Reference counters are automatically updated.
Note that this function cannot be used within a transaction; see [Transaction handling](../functions_database_handling/transaction_handling.md).

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `[ long` | `flag ]` |  If you set this optional argument to DB.IGNORE.ALL.REFS, the data is deleted regardless of whether it is referenced by other tables. WARNING: if you don't need this behavior, please leave out the argument completely. Never supply another value than DB.IGNORE.ALL.REFS to this argument.  |
| `[ long` | `comp_nr ]` |  This optional argument specifies a company number for the table. The default company is the company of the user.  |

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
