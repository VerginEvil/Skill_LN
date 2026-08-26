# fieldname.make.valid()

## Syntax:
`function long field.make.valid( long mode, [ long element ] )`

## Description
This hook is meant to adjust the field's value before it is checked. You can use it for example to round a field's value.

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |  |
| `[ long` | `element ]` |  This is set for array fields only. It indicates the index of the array element that must be checked.  |

## Return values
This hook returns 0 if no errors occurred. It returns DALHOOKERROR if the field cannot be made valid.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- when the user changes the value and tabs out the field in the User Interface, just after the *before.checks* sub-event section of the field.
- in case the field depends on another field (a HOOK_UPDATE dependency exists) and that other field has changed, then this hook is called just after the field's update hook (if present). This applies only to DAL2.
- at the time [dal.save.object()](../functions_db_operations/dal.save.object.md) is called, and the field previously was assigned a value with [dal.set.field()](../functions_db_operations/dal.set.field.md).

## Example
```

function extern long tfgld102.amth.make.valid(long mode)
{
        tccom.dll0001.round.amount(tfgld102.amth, no.hcur,
                domainof(tfgld102.amth), home.curr, home.crnd)
        return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [DAL hooks](dal_hooks.md)
- [DAL2 Flow of field hooks](dal2_flow.md)
