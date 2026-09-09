# 203 ETRANSACTIONON - Transaction is on
| |
|---|
| *Description:* |
| This error indicates that this action is not allowed within a transaction. |
| *Solution:* |
| Ensure that the transaction is not on. If needed and possible, issue a commit.transaction() or abort.transaction() before this action. |
