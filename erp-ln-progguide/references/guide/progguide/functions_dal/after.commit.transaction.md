# after.commit.transaction()

## Syntax:
`function void after.commit.transaction( )`

## Description
Use this to update other database tables after an update of the current table has been committed to the database.
This object hook is called just after the *after.update.db.commit* event section in a UI script. If there is a DAL for an object set, this hook is called to perform the required actions.
This hook is called only by the STP and CDAS. It is *not* called by Data Access Methods or [commit.transaction()](../functions_db_operations/commit.transaction.md)

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [Object hooks](object_hooks.md)
