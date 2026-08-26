# db.clear.table()

## Syntax:
`function long db.clear.table( long table_id, [ long flag, long comp_nr ] )`

## Description
This deletes all data from a specified table. Reference counters are automatically updated.
By default (WITH.ROLLBACK) , all deleted records are saved in rollback segments. Consequently, using this function to clear a large table can result in reduced performance and, in some cases, can cause overflow of the internal rollback segments.
Note that this function cannot be used within a transaction if the option NO.ROLLBACK is given; see [Transaction handling](../functions_database_handling/transaction_handling.md).

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `[ long` | `flag ]` |  Use this optional argument to indicate whether the delete operation must be performed as a single transaction or as multiple transactions. The possible values are:  |
| `[ long` | `comp_nr ]` |  This optional argument specifies a company number for the table. The default company is the company of the user.  |

## Return values
0: success
<> 0: error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
