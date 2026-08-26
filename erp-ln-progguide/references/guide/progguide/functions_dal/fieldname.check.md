# fieldname.check()

## Syntax:
`function long field.check( long has_changed, [ long element ] )`

## Description
Use this hook to program logical integrity rules for a specified field. The function name is *ppmmmvss.bbbb*.check(), where *pp* is the package code, *mmm* is the module code, *vss* is the table number, and *bbbb* is the field name.
| | |
|---|---|
| Insert a new object | Update an existing object |
|  Does the property check for all fields. The has_changed flag is *always* set to DAL_NEW. Also for fields that are not changed!  |  Does the property check for all fields. The has_changed flag is *only* set to DAL_UPDATE for changed fields. For unchanged fields, the flag is cleared.  |

## Arguments
| | | |
|---|---|---|
| `long` | `has_changed` |  |
| `[ long` | `element ]` |  This is set for array fields only. It indicates the index of the array element that must be checked.  |

## Return values
This hook returns 0 if the value of the field is accepted. It returns a negative value (DALHOOKERROR) if the value is not accepted.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## See also
[Property methods](property_methods.md)
Note  With regards to [Extended DAL (DAL2)](dal2_overview.md) it is advised to replace this property hook by the new [DAL2 Field hooks](dal2_field_hooks.md).
This hook is still supported for backward compatiblity reasons, but the consequence is that the field is not regarded as a DAL2 field.

## Example
```

A property hook programmed in DLL tdsls040:
function extern long tdsls040.oqua.check(long has_changed)
{
    if has_changed <> 0 and tdsls040.stat = tdsls.stat.invoiced then
        dal.set.error.message("tdsls44041")
        | Order is already invoiced, cannot change
        | quantity
        return(DALHOOKERROR)
    endif
    ...
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [DAL hooks](dal_hooks.md)
