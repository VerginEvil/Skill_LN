# field.is.valid()

## Syntax:
`function boolean field.is.valid( [ long mode, long element ] )`

## Description
Use this hook to perform any checks not already defined in one of the other field hooks. Some examples:
Examples: whether a reference exists or whether the reference is valid. Whether a start date is less than an end date, etc.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  optional mode flag, one of { 0, DAL_NEW, DAL_UPDATE }  |
| `[ long` | `element ]` |    |

## Return values
The hook should return True in case the field is valid. In case the field is not valid it should return False.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- At the time of checking the fields value, but ONLY for non-enum fields and ONLY in case the field is not empty, otherwise the [field.is.mandatory()](field.is.mandatory.md) hook is called

Note  This hook is *NOT* called for *enum* fields. See [field.enum.is.applicable()](field.enum.is.applicable.md) for checking enum values.
If this hook does not exist, it is assumed that the field is valid.
The [4GL engine](../glossary/glossary.md#fourgl_engine) will show the following message to the end-user in case the field is not valid: Change the value of the %1$s field.
It is advised to set an error message with [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the field is not valid.

## Example
```

function extern boolean whinh200.otyp.is.valid(long mode)
{
    if mode = 0 then
        |* Not changed
        return(true)
    endif

    if order.type.ok(whinh200.otyp, whinh200.ittp) <> 0 then
        |* Error message is set in order.type.ok
        return(false)
    endif

    return(true)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
