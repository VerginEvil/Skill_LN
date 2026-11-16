# set.enum.array.for.field()

## Syntax:
`function void set.enum.array.for.field( const string field.name, const long size, const long values )`

## Description
In case the field is a *listbox*, this fills the list with a specified set of enumerate values.
In case the field is an *optionset*, only the options that are specified will be *enabled*; all other options will be *disabled*.
This function should be used in the *before.display.object* section and/or in the *when.field.changes* section of each field on which the change depends.

## Arguments
| | | |
|---|---|---|
| `const string` | `field.name` |  The name of the enumerated field. For example, "ttadv996.type". For an array field, include the array element. For example, "tttadv996.type(5)".  |
| `const long` | `size` |  the size of the *values* array.  |
| `const long` | `values` |  The values to be displayed in the field.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Notes  You can set enumerate values only for the current occurrence.
If the existing value of an enumerated field in not included in the new set, the nearest valid enum value is selected by the 4GL Engine.
If you want to *hide* any options in case of an optionset, use the function [set.initial.enum.array.for.field()](set.initial.enum.array.for.field.md) in the *after.form.read* section.
To set enum values for the *ask.enum()* function, use *set.ask.enum.values()*.

## Example
```

field ttadv996.fld1:
when.field.changes:
    long values(1)  based
    long size

    size = 0
    alloc.mem(values, depth2)
    for i = 1 to depth2
        if ( tdpst000.turn(i) = tcyesno.no and
           tdpst094.stto = tcyesno.yes) or
           ( tdpst000.ordi(i) = tcyesno.no and
           tdpst094.stoi = tcyesno.yes ) or
           ( tdpst000.canc(i) = tcyesno.no and
           tdpst094.stdl = tcyesno.yes ) then
            | not allowed
        else
            size = size + 1
            values(size) = enum.value(i)
        endif
    endfor
    set.enum.array.for.field("ttadv996.type", size, values)
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)

- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
