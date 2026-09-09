# Locking
Database inconsistencies can arise when two or more processes attempt to update or delete the same record or table. Read inconsistencies can arise when changes made during a transaction are visible to other processes before the transaction has been completed – for example, the transaction might subsequently be abandoned. To avoid such inconsistencies, Infor Enterprise Server supports the following locking mechanisms:

- Record locking

- Table locking

- Application locking

## Record locking
To ensure that only one process at a time can modify a record, the database driver locks the record when the first process attempts to modify it. Other processes cannot then update or delete the record until the lock has been released. However, they can still read the record.
While one process is updating a table, it is important that other processes retain read consistency on the table. Read consistency means that a process does not see uncommitted changes. Updates become visible to other processes only when the transaction has been commited. Some database systems do not support read consistency, and so a dirty read is possible. A dirty read occurs when one process updates a record and another process views the record before the modifications have been committed. If the modifications are rolled back, the information read by the second process becomes invalid.

## Supported features
The supported databases can be found in the platform support matrix. Unless mentioned differently all supported databases use record locking, consistent read and transactions.

## Delayed locks
Locking a record for longer than required can result in unnecessarily long waiting times. The use of delayed locks solves this problem to a great extent.
A delayed lock is applied to a record immediately before changes are committed to the database and not earlier. When the record is initially read, it is temporarily stored. Immediately before updating the database, the system reads the value of the record again, this time placing a lock on it. If the record is already locked, the system goes back to the [Retry points](retry_points.md) and retries the transaction. If the record is not locked, the system compares the content of the record from the first read with the content from the second read. If changes have been made to the record by another process since the first read, the error EROWCHANGED is returned and the transaction is undone. If no changes have occurred, the update is committed to the database.
You place a delayed lock by adding the keyword FOR UPDATE to the SELECT statement (see [Infor Enterprise Server SQL](baan_sql.md)). For example:
```

table   tpctst999
db.retry.point()
SELECT pctst999.*
FROM pctst999 FOR UPDATE
SELECTDO
                pctst999.dsca = "...."
                ....
                db.update(tpctst999, DB.RETRY)
ENDSELECT
```

## Table locks
Infor Enterprise Server provides a table locking mechanism, which enables you to lock all the records in a specified table. A table lock prevents other processes from modifying or locking records in the table but not from reading them. This is useful when a particular transaction would otherwise require a large number of record locks. You use the db.lock.table() function to apply a table lock.

## Application locks
An [Application locks: overview](../functions_appl/application_locks_overview.md) prevents other applications and users from reading and/or modifying an application's data during critical operations. It is not part of a transaction and so is not automatically removed when a transaction is committed. Instead, an application lock is removed when the application ends or when [appl.delete()](../functions_appl/appl.delete.md) is called.

## Related topics
- [Database handling overview](overview.md)

- [Transaction handling](transaction_handling.md)

- [Retry points](retry_points.md)

- [Error handling](error_handling.md)

- [Hints for using SQL](hints_for_using_sql.md)

- [Hints for using db.retry.point](hints_for_using_db.retry.point.md)

- [Infor Enterprise Server SQL](baan_sql.md)
