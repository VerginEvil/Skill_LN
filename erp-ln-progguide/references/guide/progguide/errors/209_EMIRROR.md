# 209 EMIRROR - Mirroring error
| |
|---|
| *Description:* |
| This error indicates that there is an error in the mirroring of the database. The tables in the mirrored database environment are not consistent anymore. For more information, refer to the log files. |
| *Solution:* |
| Copy the correct tables with Baan's *bdbpre* tool and *bdbpost* tool. If you copy one table from one environment to another, you can have problems with the reference fields. However, the *bdbpre* tool checks these references. |
| < error should not occur > |
