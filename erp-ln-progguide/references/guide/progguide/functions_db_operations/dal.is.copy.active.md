# dal.is.copy.active()

## Syntax:
`#include <bic_dal>`
`function boolean dal.is.copy.active( )`

## Description
You can use this in the [before.save.object()](../functions_dal/before.save.object.md) and [after.save.object()](../functions_dal/after.save.object.md) hooks in `DAL_NEW` mode, to test whether the current record is being inserted, or being copied.
You can use this in the [field.update()](../functions_dal/field.update.md) to test whether the current record is being copied.
It returns `true` when a [dal.copy.object()](dal.copy.object.md) has been done, or when the [4GL engine](../glossary/glossary.md#fourgl_engine) is handling a `DUPL.OCCUR`, or `GLOBAL.COPY` choice.

## Return values
`true` when the current record is being copied, `false` in any other case.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1801.

## Example
```

function extern long before.save.object(long mode)
{
        on case mode
        case DAL_NEW:
                if dal.is.copy.active() then
                        | Record is being copied, also copy children
                        if copy.children() <> 0 then
                                return(DALHOOKERROR)
                        endif
                else
                        | Record is new ...
                endif
                break
        case DAL_UPDATE:
                break
        endcase

        return(0)
}
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
