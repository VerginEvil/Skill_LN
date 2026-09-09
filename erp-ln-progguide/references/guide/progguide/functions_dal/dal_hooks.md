# DAL hooks
A hook is a function, with a predefined name, that the DAL programmer programs in a DAL script. The function is used to program logic integrity rules for database access. The DAL script is compiled into a DLL.
When a user issues a command to access the database, the [4GL engine](../glossary/glossary.md#fourgl_engine) loads the DAL DLL for the object being accessed and calls the hooks to perform the integrity checks. Provided that a DAL script exists for an object set being accessed, the [4GL engine](../glossary/glossary.md#fourgl_engine) always ensures that the hooks in the DAL are called at the appropriate times.
A DAL script can contain two types of hooks:

- [Property hooks](property_hooks.md)

- [Object hooks](object_hooks.md)

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)
