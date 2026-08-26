# ue.get.origin()

## Syntax:
`function extern long ue.get.origin( )`

## Description
This function returns the origin of the execution of the User Exit hook.

## Return values
This hooks returns: UE_FROM_4GLE in case the hook was executed from the 4GL Engine. UE_FROM_DAL in case the hook was executed from a dal action. UE_FROM_DB in case the hook was executed from a db action.

## Context
This function is implemented in the 4GL Engine and can be used in UEDLL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [User Exit DLL Overview](overview.md)
- [Data Access Layer](../functions_dal/overview.md)
- [Object hooks](../functions_dal/object_hooks.md)
- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
