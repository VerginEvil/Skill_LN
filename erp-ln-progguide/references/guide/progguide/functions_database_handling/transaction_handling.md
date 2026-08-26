# Transaction handling
With respect to database actions, a transaction is a sequence of related actions that are treated as a unit. The actions that make up a transaction are processed in their entirety, or not at all.
A transaction ends with the function [commit.transaction()](../functions_db_operations/commit.transaction.md) (all changes made during the transaction are stored in the database) or with the function [abort.transaction()](../functions_db_operations/abort.transaction.md) (no changes are stored in the database). A transaction starts with the first database call after the beginning of a process, or with the first database call after the preceding transaction has ended.
A transaction is automatically rolled back (that is, it is undone) when a process is canceled and if a program ends without a *commit.transaction()* or *abort.transaction()* after the last database call.
Certain database actions cannot be placed within a transaction, because they cannot be rolled back. These actions are: [db.create.table()](../functions_db_operations/db.create.table.md), [db.drop.table()](../functions_db_operations/db.drop.table.md), [db.clear.table()](../functions_db_operations/db.clear.table.md) with the NO.ROLLBACK option, [db.lock.table()](../functions_db_operations/db.lock.table.md), and [set.transaction.readonly()](../functions_db_operations/set.transaction.readonly.md). These functions can be called only at the start of a program or after the end of the preceding transaction. These functions will not start a new transaction.
You can set a [retry point](retry_points.md) immediately before a transaction. In case of an error, the system returns to this point and re-executes the transaction from there.
A read-only transaction is a transaction in which you are permitted only to read records (without lock) from the database. A read-only transaction starts with the function *set.transaction.readonly()* (this must be called after ending the preceding transaction or at the beginning of the program) and ends with a *commit.transaction()* or *abort.transaction()*.

## Related topics
- [Database handling overview](overview.md)
- [Locking](locking.md)
- [Retry points](retry_points.md)
- [Error handling](error_handling.md)
- [Hints for using SQL](hints_for_using_sql.md)
- [Hints for using db.retry.point](hints_for_using_db.retry.point.md)
- [Infor Enterprise Server SQL](baan_sql.md)
