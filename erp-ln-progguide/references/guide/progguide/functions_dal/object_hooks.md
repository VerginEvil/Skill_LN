# Object hooks
Object hooks are used for checking the logic integrity of objects (that is, records in a table).
Object hooks replace the *before.read*, *after.read*, *before.write*, *after.write*, *before.rewrite*, *after.rewrite*, *before.delete*, and *after.delete* subsections in the *main.table.io* section of the UI script.
If there is a DAL for an object set, the [4GL engine](../glossary/glossary.md#fourgl_engine) calls the object hooks in the DAL every time that a [Data Access Methods (DAM)](dam.md) is executed for that object set. The object hooks perform the necessary checks to ensure the logical integrity of the objects being accessed. Any of the above mentioned sections in the UI script are ignored. So, if a UI script contains any of these sections, you must replace these by object hooks in the DAL.

## Available object hooks
- Open object set hook - [before.open.object.set()](before.open.object.set.md)

- Get object hooks - [before.get.object()](before.get.object.md), [after.get.object()](after.get.object.md)

- New object hooks - [before.new.object()](before.new.object.md), [after.new.object()](after.new.object.md) (DAL2 only)

- Change object hooks - [before.change.object()](before.change.object.md), [after.change.object()](after.change.object.md) (DAL2 only)

- Destroy object hooks - [before.destroy.object()](before.destroy.object.md), [after.destroy.object()](after.destroy.object.md)

- Save object hooks - [before.save.object()](before.save.object.md), [after.save.object()](after.save.object.md)

- After commit transaction hook - [after.commit.transaction()](after.commit.transaction.md)

- After abort transaction hook - [after.abort.transaction()](after.abort.transaction.md)

- Method is allowed hook - [method.is.allowed()](method.is.allowed.md)

- Default object set hook - [set.object.defaults()](set.object.defaults.md)

## Return values and errors
Only the before hooks can prevent a database action. The *after.get.object()* hook can prevent a record from being sent to the UI. Both these types of hooks block continuation of the calling method if the return value is set to DALHOOKERROR (a negative constant). If the return value is zero, the method continues.
The following table indicates how return values and error messages are handled. The STP column indicates how the [4GL engine](../glossary/glossary.md#fourgl_engine) reacts if a hook returns a DALHOOKERROR. The Messages column indicates what happens to messages when an error occurs. The DAM column indicates how Data Access Methods react when an error occurs.
| | | | |
|---|---|---|---|
| Hook | STP | Messages | DAM |
| before.open.object.set() | exit | display | return |
| before.get.object() | ignore | ignore | return |
| after.get.object() | skip | ignore | return |
| before.new.object() | ignore | display | return |
| after.new.object() | skip | display | return |
| before.change.object() | ignore | display | return |
| after.change.object() | skip | display | return |
| before.destroy.object() | return | display | return |
| after.destroy.object() | skip | display | return |
| before.save.object() | return | display | return |
| after.save.object() | skip | display | return |

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [DAL hooks](dal_hooks.md)
