# after.abort.transaction()

## Syntax:
`function void after.abort.transaction( )`

## Description
This hook is called after the application did an [abort.io()](../functions_db_operations/abort.io.md) in the UI script from the *after.choice* of the *choice.update.db* section
If there is a DAL for an object set, this hook is called to perform the required actions.
This hook is called only by the STP and CDAS. It is *not* called by Data Access Methods or [abort.transaction()](../functions_db_operations/abort.transaction.md)

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [Object hooks](object_hooks.md)
