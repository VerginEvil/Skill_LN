# 206 ENOTLOCKED - Record not locked
| |
|---|
| *Description:* |
| This error indicates that the record is not locked. This error can occur: When a commit is done in the middle of a selectdo -endselect and the same record is updated. When the update is forgotten. After error 100 occurred, caused by an old fashioned command like `db.eq`. Baan sets e=100 and proceeds, after this error 206 can occur. |
| *Solution:* |
| Ensure none of the above mentioned situations applies anymore. |
