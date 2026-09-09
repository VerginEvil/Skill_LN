# Data Access Methods (DAM)
You use Data Access Methods (DAM) to update the database via the DAL. In a UI script, you can use the methods to update any object set. In a DAL script, you can use the methods to update objects in an object set other than the one with which the script itself is associated.
There are three Data Access Methods:

- [dal.update()](../functions_db_operations/dal.update.md)

- [dal.new()](../functions_db_operations/dal.new.md)

- [dal.destroy()](../functions_db_operations/dal.destroy.md)

These functions encapsulate the [db.update()](../functions_db_operations/db.update.md). [db.insert()](../functions_db_operations/db.insert.md), and [db.delete()](../functions_db_operations/db.delete.md) functions respectively, together with the DAL hooks of the object set.

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Transition issues (BAAN IV to Infor Enterprise Server)](transition_issues_baan_iv_to_baanerp.md)
