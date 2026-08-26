# business.method.is.never.allowed()

## Syntax:
`function boolean business.method.is.never.allowed( )`

## Description
Use this hook to check whether the business method may never be executed. If the business method may never be executed, then the 4GL engine will remove the corresponding form command from the UI.

## Return values
The hook should return True if the business method may never be executed. It should return False in any other case.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
This hook is called by the DAL itself or by the 4GL engine.
This hook is called when the 4GL engine determines whether the form command related to the business method should be removed. This is just before calling the *after.form.read* section.
Note  If this hook does not exist, it is assumed that the corresponding form command is not never allowed. (E.g. it will not be removed from the UI).
It is advised to set an error message with [dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the business method is never allowed.

## Example
```

|* Business method post.transaction
function extern long post.transaction()
{
    FunctionUsage
    ...
    EndFunctionUsage

    if post.transaction.is.never.allowed() or
       not post.transaction.is.allowed() then
        dal.set.error.message("tfglds0021")
        |* Post transactions is not allowed.
        return(DALHOOKERROR)
    endif

    return(0)
}

function extern boolean post.transaction.is.never.allowed()
{
    if ... then
        dal.set.error.message("tfglds0022")
        |* Finance not implemented.
        return(true)
    endif

    return(false)
}

function extern boolean post.transaction.is.allowed()
{
    if ... then
        dal.set.error.message("tfglds0023")
        |* Transaction is already posted.
        return(false)
    endif

    return(true)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)
- [DAL2 Business method hooks](dal2_bm_hooks.md)
- [DAL2 and the 4GL Engine](dal2_4gle.md)
