# enable.db.dll()

## Syntax:
`function void enable.db.dll( )`

## Description
This enables the call of the db hooks in the db dll. (db.before.insert, db.before.update, db.before.delete, db.after.insert, db.after.update, db.after.delete)

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [DB DLL Overview](overview.md)

- [Data Access Layer](../functions_dal/overview.md)

- [Object hooks](../functions_dal/object_hooks.md)

- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
