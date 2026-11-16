# field.update()

## Syntax:
`function [void|long] field.update( [ long mode, long element ] )`

## Description
Use this hook to (re) determine the value of the field based on the current record values. Think of determining defaults and calculating derived values. When using this hook you don't have to use the *when.field.changes* section in the UI script to update fields.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  optional mode flag, one of { 0, DAL_NEW, DAL_UPDATE }  |
| `[ long` | `element ]` |    |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
- This hook is called in case a field on which this field depends (by means of a HOOK_UPDATE or HOOK_IS_APPLICABLE dependency) has changed. Just before the [4GL engine](../glossary/glossary.md#fourgl_engine) calls the the *when.field.changes* section, it will call this hook for each field that depends on the field that was changed. The 4GL engine will take care that the hooks are called in the right order.

- In case of *Subdals* you have to use [dal.save.object()](../functions_db_operations/dal.save.object.md) in order to let dependent fields update themselves. This function triggers dependent fields to update themselves. It will take care that the update hooks are called in the right order.

Note  Normally this hook should have a `void` return type. Only if it is possible that this hook finds a data setup error (as opposed to a programming error), and if that error could not have been detected earlier or elsewhere, then return type `long` is allowed. In that case an error is indicated by `return(DALHOOKERROR)` or something equivalent.
When there is also a [fieldname.make.valid()](fieldname.make.valid.md) hook for the same field, the return of field.make.valid will overwrite the return of the field.update. To prevent the overwrite of the return value, to always give an error when the field.update fails, the function [dal.field.update.error.cannot.be.made.valid()](dal.field.update.error.cannot.be.made.valid.md) can be used.
Note  This hook will only be called in case a HOOK_UPDATE or HOOK_IS_APPLICABLE dependency relationship has been defined in the [before.open.object.set()](before.open.object.set.md) hook. See also [DAL2 Field dependencies](dal2_field_dependencies.md).
Note  In this hook you can use [dal.is.copy.active()](../functions_db_operations/dal.is.copy.active.md) to determine the record is being copied.

## Examples
E.g. if you currently have the following programmed in your UI script:
```

field.a:
when.field.changes:
    if a <= 10 then
        b = 5
        c = 6
    else
        b = 0
        c = 0
    endif
```
Then this will become the following in your DAL:
```

function extern void b.update()
{
    if a <= 10 then
        b = 5
    else
        b = 0
    endif
}

function extern void c.update()
{
    if a <= 10 then
        c = 6
    else
        c = 0
    endif
}
```

## Example
```

function extern void whinh200.sfty.update()
{
    on case whinh200.ittp
    case whinh.ittp.receipt:
        if whinh200.order.origin.is(whinh200.oorg,
                        whinh.oorg.maint.work,
                        whinh.oorg.maint.work.man,
                        whinh.oorg.production,
                        whinh.oorg.production.man,
                        whinh.oorg.product.asc,
                        whinh.oorg.product.asc.man) then
            whinh200.sfty = tctyps.work.center
        else
            whinh200.sfty = tctyps.partner
        endif
        break
    case whinh.ittp.issue:
    case whinh.ittp.transfer:
    case whinh.ittp.item.transfer:
        whinh200.sfty = tctyps.warehouse
        break
    endcase
}
```

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 Field dependencies](dal2_field_dependencies.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
