# field.is.mandatory()

## Syntax:
`function boolean field.is.mandatory( [ long mode, long element ] )`

## Description
Use this hook to indicate whether the field is mandatory. If a field is mandatory then it should have a value other than "", 0.0, 0 or empty.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  optional mode flag, one of { 0, DAL_NEW, DAL_UPDATE }  |
| `[ long` | `element ]` |  optional element number in case the field is an element of an array (for non array fields this value is 1)  |

## Return values
The hook should return True in case the field is mandatory. In any other case the hook should return False (i.e. the field is not mandatory).

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- At the time of checking the fields value, but ONLY in case the field is empty
- Since Enterprise Server 8.3, the 4GL engine now also calls the field.is.mandatory() hook when displaying data, in order to be able to determine if a form field is mandatory (this is used by the UI to display a red asterix in front of the form field or not). In this case, the hook is called when displaying the form field and also when the field is empty. Any dal error messages set in the hook are ignored     Note  If this hook does not exist, the table field definition in the Data Dictionary is checked. So if the field is defined as mandatory in the Data Dictionary, the field must have a value.
Make sure that the hook does not conflict with the Mandatory setting of the field in the Data Dictionary. So do not return False in case the field is defined as Mandatory in the Data Dictionary.
The 4GL engine will show the following message to the end-user in case the field is empty and it appears to be mandatory: Enter a value for the %1$s field.
It is advised to set an error message with [dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()](../functions_message_handling/dal.set.error.message.md) to indicate the reason why the field is mandatory.

## Example
```

function extern boolean whinh200.sfit.is.mandatory()
{
    if whinh200.ittp = whinh.ittp.item.transfer then
        dal.set.error.message("whinhs0181")
        |* Ship-from item must be filled for an item transfer.
        return(true)
    endif

    return(false)
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)
- [DAL2 and the 4GL Engine](dal2_4gle.md)
- [DAL2 Flow of field hooks](dal2_flow.md)
