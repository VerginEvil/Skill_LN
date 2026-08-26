# field.is.readonly()

## Syntax:
`function boolean field.is.readonly( [ long mode, long element ] )`

## Description
Use this hook to indicate whether the field is readonly. If a field is readonly then the 4GL Engine makes the field readonly in the UI. The field however, still can have a value.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  optional mode flag, one of { 0, DAL_UPDATE }  |
| `[ long` | `element ]` |  |

## Return values
The hook should return True in case the field is readonly. In that case the 4GL engine will make the field appear readonly on the UI. In any other case the hook should return False (i.e. the field is not readonly).

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- At the time the 4GL engine determines whether fields need to be disabled cq. enabled: this is done just before calling the *before.display.object* and the *when.field.changes* sections
- At the time of checking the fields value, in case the record is being modified (DAL_UPDATE)
- In case the field is defined as a [DAL2 Field dependencies](dal2_field_dependencies.md) of another field and that other field changes. See also the [field.update()](field.update.md) hook.     Note  Readonly is defined as: the field's value cannot be modified, even not by the application.
If this hook does not exist, it is assumed that the field not readonly.
Note that this hook is NEVER called in *mode* DAL_NEW!
The 4GL engine will show the following message to the end-user in case the field is changed and it appears to be readonly: *It is not allowed to change the %1$s field.*
It is advised to set an error message with [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the field is readonly.

## Example
```

function extern boolean whinh200.otyp.is.readonly()
{
    if not MANUAL.WHINH200 then
        dal.set.error.message("whinhs2359")
        |* The Order Type can only be changed for Manual Orders.
        return(true)
    endif
    ...
    return(false)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)
- [field.update()](field.update.md) hook
- [DAL2 Field dependencies](dal2_field_dependencies.md)
- [DAL2 and the 4GL Engine](dal2_4gle.md)
- [DAL2 Flow of field hooks](dal2_flow.md)
