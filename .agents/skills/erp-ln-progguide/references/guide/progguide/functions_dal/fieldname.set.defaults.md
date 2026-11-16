# fieldname.set.defaults()

## Syntax:
`function long field.set.defaults( long has_changed )`

## Description
Use this hook to set defaults based on a specified field. The function name is ppmmmvss.bbbb.check(), where pp is the package code, mmm is the module code, vss is the table number, and bbbb is the field name.
If this hook exists, it is executed only by B3 through a BOI in case of DAL_NEW or DAL_UPDATE.
A record will be created or modified in a specific order. This order should be defined in the table definition in the section default sequence.
| | |
|---|---|
| default mandatory | Possible values are: *Always* this field should be passed by the BOI (insert) *Conditionally* this field can be set by defaults; otherwise mandatory *Not* this field is not really required; but can be passed |
| sequence | This indicates the number in the sequence. The lowest number will be executed first (0 does not count). First the sequence for default mandatory *Always* will be executed, followed by *Conditionally* and *Not*. |

## Arguments
| | | |
|---|---|---|
| `long` | `has_changed` |    |

## Return values
This hook returns 0 if the value of the field is accepted. It returns a negative value (DALHOOKERROR) if the value is not accepted.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Points of Attention
- The field order is very important and is hierarchically structured. The first element of the *default mandatory* *Always* is the most important. After all elements of that category have been checked the first element of the *default mandatory* *Conditionally* is most important. After all elements of that category have been checked the first element of the *default mandatory* *Not* is most important. If an element (table field) in one of the categories have been managed this field should not be updated (by defaults generated from other fields lower in the hierarchy).

- Mandatory fields cannot always automatically be derived from the table definitions. Check for instance tisfc001.pdno (Production Order). One should check both UI and DAL script in order to see which fields belong to what category ( *Always / Conditionally / Not*).

- Hint: Use ttaad4100 with DAL for checking the quality of the DAL.

- *Default mandatory* *Always* fields should be controlled via domain or table field check.

- *Default mandatory* *Conditionally* fields should be checked via the DAL.

## See also
[Property methods](property_methods.md)
Note  This hook is not executed in case of [Extended DAL (DAL2)](dal2_overview.md). It is therefore advised to replace this property hook by the new [DAL2 Field hooks](dal2_field_hooks.md).

## Example
```

function extern long tisfc001.pdno.set.defaults(long has_changed)
{
    domain tclngt length.of.group   |* Length of Order Series Group
    domain tcbool defaults.found    |* Defaults by Order Series Found

    if has_changed = DAL_NEW then
        tisfc001.rswc = tisfc000.rswc
        get.and.fill.defaults.of.order.serie(tisfc000.ngpd,
            get.sfc.serie.out.of.pdno(tisfc001.pdno,
            length.of.group), defaults.found)
    endif

    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [DAL hooks](dal_hooks.md)
