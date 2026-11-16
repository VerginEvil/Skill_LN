# db.clear.table()

## Syntax:
`function long db.clear.table( long table_id, [ long flag, long comp_nr ] )`

## Description
This deletes all data from a specified table. Reference counters are automatically updated.
By default (WITH.ROLLBACK), all deleted records are saved in rollback segments. Consequently, using this function to clear a large table can result in reduced performance and, in some cases, can cause overflow of the internal rollback segments.
Note that this function cannot be used within a transaction if the option NO.ROLLBACK is given; see [Transaction handling](../functions_database_handling/transaction_handling.md).

## Arguments
| | |
|---|---|
| WITH.ROLLBACK | The table is cleared in a single transaction. All records are saved in rollback segments. This is the default option. |
| NO.ROLLBACK | The table is cleared in one or more transactions, depending on the number of records in the table. Each transaction is automatically committed after 20 records have been deleted. The number of records deleted in the final transaction can be 20 or less; this depends on how many records remain to be deleted. When you use this option, transactions are small and records are not saved in rollback segments. When you use this option, you must place *db.clear.table()* at the start of the transaction. |

## Return values
0: success
<> 0: error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
