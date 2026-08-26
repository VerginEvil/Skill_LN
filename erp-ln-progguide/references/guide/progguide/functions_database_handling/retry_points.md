# Retry points
A retry point is a position in a program script to which the program returns if an error occurs within a transaction. The transaction is then retried. There are a number of situations where retry points are useful:
- During the time that a delayed lock is applied to a record, an error can occur that causes the system to execute an [abort.transaction()](../functions_db_operations/abort.transaction.md). In such cases, all that Infor Enterprise Server can do is inform the program that the transaction has been aborted. However, if retry points are used, the system can automatically retry the transaction without the user being aware of this.
- Some database systems generate an *abort.transaction()* when a dirty record is read (that is, a record that has been changed but not yet committed). An *abort.transaction()* may also be generated when two or more processes simultaneously attempt to change, delete, or add the same record. In all these situations, Infor Enterprise Server can conceal the problem from the user by using retry points. It simply retries the transaction. If there is no retry point, the transaction is aborted and the session is terminated.
- In Infor Enterprise Server, updates are buffered, so the success or failure of an update is not known until [commit.transaction()](../functions_db_operations/commit.transaction.md) is called. If an update fails, the commit of the transaction also fails, and the entire transaction must be repeated. If retry points are used, the system automatically retries the transaction.
- Retry points can also resolve potential deadlock problems. If, for example, the system is unable to lock a record, it rolls the transaction back and tries again.   It is vital that retry points are included in all update programs.

## Coding retry points
The retry point for a transaction must be placed at the start of a transaction. The following example illustrates how you program retry points:
```

db.retry.point()                    | set retry point
if db.retry.hit() > 0 then
                ......              | code to execute when the system
                                    | goes back to retry point
else
                ......              | initialization of retry point
endif
```
The function [db.retry.hit()](../functions_db_operations/db.retry.hit.md) returns 0 when the retry point is generated - that is, the first time the code is executed. It returns a value unequal to 0 when the system returns to the retry point through the database layer.
When the system goes back to a retry point, it clears the internal stack of functions, local variables, and so on that were called during the transaction. The program continues from where the retry point was generated. The value of global variables is NOT reset.
When a commit fails, the database automatically returns to its state at the start of the transaction; the program is set back to the last retry point. It is vital, therefore, that the retry point is situated at the start of the transaction. The *db.retry.hit()* call must follow the [db.retry.point()](../functions_db_operations/db.retry.point.md) call. Do not place it in the SQL loop itself as this makes the code very nontransparent. When a retry point is placed within a transaction, the system produces a message and terminates the session.

## Testing retry points
The following bshell resources and environment variables enable you to test the operation of retry points:
| | |
|---|---|
| [TEST_RETRY](../misc/bshell_environment_variables.md) | This bshell environment variable indicates how often the system must go back to a retry point at the moment of committing. This cannot be used when testing different sessions with retry points parallel.  |
| [max_retry](../misc/bshell_resources.md) | This bshell resource indicates how often the system may return to a retry point as a result of an abort in an update action. Default: 10  |

## Related topics
- [Database handling overview](overview.md)
- [Transaction handling](transaction_handling.md)
- [Locking](locking.md)
- [Error handling](error_handling.md)
- [Hints for using SQL](hints_for_using_sql.md)
- [Hints for using db.retry.point](hints_for_using_db.retry.point.md)
- [Bshell environment variable "TEST_RETRY"](../misc/bshell_environment_variables.md)
- [Bshell resource "max_retry"](../misc/bshell_resources.md)
- [Infor Enterprise Server SQL](baan_sql.md)
