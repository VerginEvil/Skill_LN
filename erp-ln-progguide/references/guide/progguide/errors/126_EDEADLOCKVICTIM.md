# 126 EDEADLOCKVICTIM - Transaction is aborted due to deadlock
| |
|---|
| *Description:* |
| This error indicates that the current transaction is aborted due to a deadlock error. This error code results in either a jump to the db.retry.point or in termination of the process (if no db.retry.point is specified). It cannot be handled using error.bypass.  |
| *Solution:* |
| Solve the deadlock condition, or retry the transaction. |
