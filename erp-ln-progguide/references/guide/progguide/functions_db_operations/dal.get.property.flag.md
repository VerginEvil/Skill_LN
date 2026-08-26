# dal.get.property.flag()

## Syntax:
`#include <bic_dam>`
`function long dal.get.property.flag( string tbl.name, long object_set, string prop_name )`

## Description
Use this to retrieve the value of the *has_changed* flag (see [Property hooks](../functions_dal/property_hooks.md)) for any database property dat.get.property.flag. The property must have been changed by the [dal.set.property()](dal.set.property.md) function.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  A string containing the name of the DAL.  |
| `long` | `object_set` |  The ID of an open object set (if this ID is not known, use the table ID).  |
| `string` | `prop_name` |  A string containing the name of the field for which the *has_changed* value must be returned.  |

## Return values
The function returns the value of the *has_changed* flag of the specified property. The possible values are:
| | |
|---|---|
| 0 | Property not changed. |
| DAL_NEW | Change caused by inserting a new object. |
| DAL_UPDATE | Change caused by updating an existing object. |
Properties with no check function in the DAL always return 0.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function should not be used after the the actual insert/update has been done. E.g. it should not be used in any 'after' hook in the DAL, Table Extension DLL or DB DLL.

## Example
This function is programmed in DAL tdsls401.
```

function extern long tdsls401.oqua.check(long has_changed)
{
    if tdsls400.stat = tdsls.stat.invoiced then
        if has_changed or
            dal.get.property.flag("tdsls401", ttdsls401,
                "tdsls401.pric") then
            dal.set.error.message("tdsls44042")
            | You cannot change quantity or price, because
            | the order is already invoiced
            return(DALHOOKERROR)
        endif
    else
        if tdsls401.oqua > tdsls401.comq then
            dal.set.error.message("tdsls44043")
            | Order quantity may not exceed committed
            | quantity
            return(DALHOOKERROR)
        endif
    endif
    …
    return(0)
}
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
