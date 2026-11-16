# field.enum.is.applicable()

## Syntax:
`function boolean field.enum.is.applicable( [ long mode, long element ] )`

## Description
Use this hook to indicate whether a certain enum constant is applicable. In case the enum constant is not applicable the [4GL engine](../glossary/glossary.md#fourgl_engine) will not show it in the field's list box, so the end-user cannot select it.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  optional mode flag, one of { 0, DAL_NEW, DAL_UPDATE }  |
| `[ long` | `element ]` |  optional element number in case the field is an element of an array (for non array fields this value is 1)  |

## Return values
The hook should return True in case the enum constant is applicable. In case the enum constant is not applicable it should return False.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- At the time the [4GL engine](../glossary/glossary.md#fourgl_engine) determines the enum masks of enum fields: this is done just before calling the *before.display.object* and the *when.field.changes* sections

- At the time of checking the field's value

Note  This hook only applies to enum fields.
If this hook does not exist, it is assumed that the enum constant is applicable.
The [4GL engine](../glossary/glossary.md#fourgl_engine) will show the following message to the end-user in case the field value is the enum value being checked and this is not allowed: Change the value of the %1$s field.
It is advised to set an error message with [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the enum constant is not applicable.

## Example
```

function extern boolean whinh200.oorg.sales.is.applicable(long mode)
{
    if mode = 0 then
        return(true)
    endif

    if not TD.IMPLEMENTED then
        dal.set.error.message("whinhs8532")
        |* The Sales Order Origin cannot be selected in
        |* case Order Management is not implemented.
        return(false)
    endif

    if show.only.manual.orders then
        dal.set.error.message("whinhs8533")
        |* Only Manual Sales Orders can be selected.
        return(false)
    endif

    return(true)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
