# before.open.object.set()

## Syntax:
`function long before.open.object.set( )`

## Description
Use this to program checks that determine whether opening of the object set is permitted.
If this hook exists, it is executed after the *before.program* event section for the main table. It is also called for every first access to a DAL by business methods or Data Access Methods.
You can also use this section to program [Query extensions](query_extensions.md) and to initialize data (like reading parameter tables).

## Return values
The hook returns 0 if opening of the object set is permitted. If the hook returns a negative value (DALHOOKERROR), the session is aborted (if the hook is called by the STP) or the method returns an error (if the hook is called by a DAM or a business method).

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [Object hooks](object_hooks.md)
