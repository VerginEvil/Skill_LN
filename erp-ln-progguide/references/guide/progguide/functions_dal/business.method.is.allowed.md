# business.method.is.allowed()

## Syntax:
`function boolean business.method.is.allowed( )`

## Description
Use this hook to check whether the business method may be executed. If the business method may not be executed, then the 4GL engine will *disable* the corresponding form command on the UI.

## Return values
The hook should return False if the business method may not be executed. It should return True in case it is allowed to execute the business method.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
This hook is called by the DAL itself or by the 4GL engine.
This hook is called when the 4GL engine determines whether the form command related to the business method should be disabled. This is just before calling the *before.display.object* and *when.field.changes* sections as well as the *after.choice* subevent of the *choice.mark.occur* event section.
Note  If this hook does not exist, it is assumed that the corresponding form command is allowed. (E.g. it will not be disabled in the UI).
It is advised to set an error message with [dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the business method is not allowed.

## Example
See [business.method.is.never.allowed()](business.method.is.never.allowed.md)

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)
- [DAL2 Business method hooks](dal2_bm_hooks.md)
- [DAL2 and the 4GL Engine](dal2_4gle.md)
