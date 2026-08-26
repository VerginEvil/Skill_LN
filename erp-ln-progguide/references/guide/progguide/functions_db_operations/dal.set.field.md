# dal.set.field()

## Syntax:
`#include <bic_dam>`
`function void dal.set.field( string fld.name, void value, [ long element ] )`

## Description
Sets the value of the given field and informs the DAL that the field is changed.
This function does the same as:
`ret.val = dal.set.property(tbl.name, tbl.cursor, fld.name, value, mode)`
where *tbl.name* and *tbl.cursor* are provided automatically, and *mode* is DAL_NEW after [dal.new.object()](dal.new.object.md) or [dal.copy.object()](dal.copy.object.md), and otherwise DAL_UPDATE.

## Arguments
| | | |
|---|---|---|
| `string` | `fld.name` |  the name of the field  |
| `void` | `value` |  the new value of the field  |
| `[ long` | `element ]` |  optional element of the field in case of array fields (default is 1)  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Preconditions
When used in a DAL hook, it is only possible to set fields of other DALs. So the following is not allowed:
```

function extern void tdsls400.pono.update()
{
        | Not allowed
        dal.set.field("tdsls400.pono", value)
        | Correct
        tdsls400.pono = value
}
```
The only exception is the [set.object.defaults()](../functions_dal/set.object.defaults.md) hook. In that hook it is allowed to use dal.set.field() for a field of the current DAL. In this way any field dependencies are taken into account when a save is done.
Note  This function does not update any dependent fields itself, nor does it check the field's value! These actions are done during a save.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
