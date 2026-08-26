# 512 EDDCORRUPT - Incorrect table definition
| |
|---|
| *Description:* |
| This error can indicate: That the data dictionary is corrupt. The table definition does not match the table.  |
| *Solution:* |
| Probably a table is copied from one environment to another, without taking care of the table definitions. Use LN's *bdbpre* and *bdbpost* tools to copy tables.  |
-
-
