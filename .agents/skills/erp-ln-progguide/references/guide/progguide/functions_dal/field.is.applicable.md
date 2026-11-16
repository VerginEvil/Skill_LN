# field.is.applicable()

## Syntax:
`function boolean field.is.applicable( [ long mode, long element ] )`

## Description
Use this hook to indicate whether the field is applicable. If a field is not applicable then the 4GL Engine disables the field and the field will be cleared. Depending on the data type of the field the field's value then becomes:
| | |
|---|---|
| string | "" |
| double | 0.0 |
| long | 0 |
| enum | The default value as defined in the Data Dictionary |

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  optional mode flag, one of { 0, DAL_NEW, DAL_UPDATE }  |
| `[ long` | `element ]` |  optional element number in case the field is an element of an array (for non array fields this value is 1)  |

## Return values
The hook should return False in case the field is not applicable. In that case the [4GL engine](../glossary/glossary.md#fourgl_engine) will disable the field in the UI and the field will be cleared. In any other case the hook should return True (i.e. the field is applicable).

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- At the time the [4GL engine](../glossary/glossary.md#fourgl_engine) determines whether fields need to be disabled cq. enabled: this is done just before calling the *before.display.object* and the *when.field.changes* sections

- At the time of checking the field's value, in case the field is not empty and the field is not never applicable.

- In case the field is defined as a [DAL2 Field dependencies](dal2_field_dependencies.md) of another field and that other field changes. See also the [field.update()](field.update.md) hook.

Note  In this hook you should test on fields belonging to table of the DAL (current record values).
If this hook does not exist, it is assumed that the field is applicable. Note that the field can still be never applicable!
The [4GL engine](../glossary/glossary.md#fourgl_engine) will show the following message to the end-user in case the field has a value and it appears to be not applicable: The %1$s field must be empty.
It is advised to set an error message with [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the field is not applicable.

## Example
```

function extern boolean whinh200.sfit.is.applicable()
{
    if whinh200.ittp <> whinh.ittp.item.transfer then
        dal.set.error.message("whinhs0239")
        |* The Ship-from Item is not applicable in case the
        |* Inventory transaction type is not set to Item Transfer.
        return(false)
    endif
    ...
    return(true)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [field.update()](field.update.md)

- [DAL2 Field dependencies](dal2_field_dependencies.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
