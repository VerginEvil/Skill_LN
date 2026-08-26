# dal.set.property()

## Syntax:
`#include <bic_dam>`
`function long dal.set.property( string tbl.name, long object_set, string prop_name, void value, long mode )`

## Description
In order to notify the DAL about a change to the value of a property, you must use this function to change the value. Using this function ensures that the relevant property hooks are executed when the value is changed. If you use an assignment or the db.* functions to change a property value, the DAL is not notified of the change. Consequently, the property checks in the DAL are not executed.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  A string containing the name of the DAL.  |
| `long` | `object_set` |  The ID of an open object set (if this ID is not known, use the table ID).  |
| `string` | `prop_name` |  The name of the property whose value must be changed.  |
| `void` | `value` |  |
| `long` | `mode` |  Use this to indicate the value for the *has_changed* flag of the property. The possible values are DAL_NEW or DAL_UPDATE.  |

## Return values
Always 0

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## DEPRECATED
This function has been deprecated. Please use [dal.set.field()](dal.set.field.md) instead.

## Remark
The property check is not executed by calling this function, only the has_changed flag is set. The return value of this function is therefore not the return value of the property check, but 0.
There is another function: [dal.set.property.with.check()](dal.set.property.with.check.md) which does the same as dal.set.property, but also calls the property check immediately.
You can call this function from both UI and DAL scripts.

## Example
This is an example of using the function in a DAL script to update an object in another object set.
```

| This function is in the DAL of tdsls401

function extern long after.save.object(long mode)
{
    long ret

    if mode = DAL_NEW then
        old.amnt = 0
    endif
    select  tdsls400.*
    from    tdsls400 for update
    where   tdsls400.orno =:tdsls401.orno
    selectdo
        dal.set.property("tdsls400", ttdsls400, "tdsls400.amnt",
            tdsls400.amnt - old.amnt + tdsls401.amnt, DAL_UPDATE)
        dal.update("tdsls400", ttdsls400, ret, true, db.retry)
    endselect
    return(ret)
}
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
