# SQL and delayed locks
The purpose of delayed locking is to postpone the physical lock of a record as long as possible. The program places the physical lock immediately before updating. During updating, the value of the record at the moment of selection must be known, as this is compared to the value at the moment of updating. During comparison, the relationships between fields are taken into account.
For a record to be delayed-locked when selected, the keyword FOR UPDATE must be included in the [SELECT clause](select.md) statement. In SQL, 'normal' record locking is not possible.
When placing a delayed lock on a record, the program fills the field <table>._dlock with an identification number linked to the record. This field identifies the original record. This guarantees a fast search procedure. This field will be overwritten when changing the record buffer.
Updates in combination with SELECT FOR UPDATE are executed with the following functions:
```

db.insert(table, DB.RETRY [, eflag])
db.update(table, DB.RETRY [, eflag])
db.delete(table, DB.RETRY [, eflag])
```
The DB.RETRY flag indicates that we are dealing here with updates with SELECT FOR UPDATE and retry points. This flag ensures that the actual update action is postponed until the commit. The [db.update()](../functions_db_operations/db.update.md) and [db.delete()](../functions_db_operations/db.delete.md) functions with the DB.RETRY flag can be invoked only in combination with SELECT FOR UPDATE. The use of [db.insert()](../functions_db_operations/db.insert.md) with the DB.RETRY flag, on the other hand, is not linked to the use of SELECT FOR UPDATE.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
