# 520 EBUFUPD - Buffered update failed
| |
|---|
| *Description:* |
| This error occurs when flushing of buffered updates fails. The flushing can fail due to a lock or referential integrity constraint.  |
| *Solution:* |
| When error.bypass has been set to 1, unsetting it may lead to falling back to a retry point. |
