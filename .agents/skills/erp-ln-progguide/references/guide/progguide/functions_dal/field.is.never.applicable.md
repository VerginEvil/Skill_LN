# field.is.never.applicable()

## Syntax:
`function boolean field.is.never.applicable( )`

## Description
Use this hook to indicate if the field is never applicable. If a field is never applicable then the [4GL engine](../glossary/glossary.md#fourgl_engine) will not display the field in the UI (it is made invisible at start up of a session). A field can become never applicable based on a static constraint, like a parameter setting.

## Return values
The hook should return true in case the field is never applicable. In that case the [4GL engine](../glossary/glossary.md#fourgl_engine) will remove the field from the UI. In any other case the hook should return False.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- Just before the [4GL engine](../glossary/glossary.md#fourgl_engine) calls the *after.form.read* section of the UI script

- At the time of checking the fields value, but only in case the field is not empty

Note  In this hook you should test on fields that have a *static* nature. In practice this means that you will test fields that do not belong to the business object you're dealing with. So you should not use this hook to test a field of an order header in the DAL of the order lines. Instead, think of parameter settings, user profiles. meta data etc.
If this hook does not exist, it is assumed that the field is not never applicable. Note that this does not mean that the field is applicable. See the [field.is.applicable()](field.is.applicable.md) hook.
By default, the [4GL engine](../glossary/glossary.md#fourgl_engine) will check fields that are defined as never applicable to see if they are empty. You can skip these checks by calling function [dal.skip.never.applicable.checks()](../functions_db_operations/dal.skip.never.applicable.checks.md) in the [before.open.object.set()](before.open.object.set.md) hook of the DAL.
In case checks have to be performed and the field has a value and is never applicable then the [4GL engine](../glossary/glossary.md#fourgl_engine) shows the following message to the end-user: The %1$s field must be empty.
It is advised to set an error message with [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the field is never applicable.

## Example
```

function extern domain tcbool whinh200.sfrv.is.never.applicable()
{
    if whwmd000.lfcs = tcyesno.no then
        dal.set.error.message("whinhs0395")
        |* The Engineering Revision field is not applicable
        |* according to the Warehousing Parameters.
        return(true)
    endif

    return(false)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
