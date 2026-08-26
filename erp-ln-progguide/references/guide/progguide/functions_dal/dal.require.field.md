# dal.require.field()

## Syntax:
`#include <bic_dal>`
`function void dal.require.field( const string fieldname, [ long element, ref boolean field.changed ] )`

## Description
This function can be used to determine a specific order for the calls to the update hooks. The function only works properly if update hooks are triggered by the 4GL engine (amdll), and not called from the application itself.

## Arguments
| | | |
|---|---|---|
| `const string` | `fieldname` |  |
| `[ long` | `element ]` |  |
| `[ ref boolean` | `field.changed ]` |  |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1300.
Note  This function can only be called in the [field.update()](field.update.md) hook.

## Example
As in the example below, the value for "b" depends upon "c" but "c" also depends upon "b". As programmed in the example, when "a" changes (and "a" <= 10) then b.update() is called, and from there the c.update() function is called. In c.update() the value for "c" is determined. Based upon the new "c", "b" can be determined. When "a" changes (and "a" > 10), then b.update() is called. Then c.update() is called, which requires b. The value for "b" is however just calculated, so there is no need to recalculate and c can be determined upon the current value for b. In both cases a dal.require.field("a") is programmed which in fact does not do anything, because the trigger for this all was a change for "a".
```

function extern long before.open.object.set()
{
    ...

    dal.field.depends.on("b",
        HOOK_UPDATE,   "a", "c")
    dal.field.depends.on("c",
        HOOK_UPDATE,   "a", "b")

    ...

    return(0)
}

function extern void b.update()
{
    dal.require.field("a")
    if a <= 10 then
        dal.require.field("c")
        if dal.any.parent.changed() then
            b = c
        endif
    else
        b = 0
    endif
}

function extern void c.update()
{
    dal.require.field("a")
    if a <= 10 then
        c = 6
    else
        dal.require.field("b")
        if dal.any.parent.changed() then
            c = b
        endif
    endif
}
```
