# set.enum.values.for.field()

## Syntax:
`function void set.enum.values.for.field( const string field.name, [ long ALL_ENUMS_EXCEPT, enum enum_value,... ] )`

## Description
In case the field is a *listbox*, this fills the list with a specified set of enumerate values.
In case the field is an *optionset*, only the options that are specified will be *enabled*; all other options will be *disabled*.
This function should used in the *before.display.object* section and/or in the *when.field.changes* section of each field on which the change depends.

## Arguments
| | | |
|---|---|---|
| `const string` | `field.name` |  The name of the enumerated field. For example, "ttadv996.type". For an array field, include the array element. For example, "tttadv996.type(5)".  |
| `[ long` | `ALL_ENUMS_EXCEPT ]` |  This optional macro specifies that the succeeding list of enumerate values represents those values that are to be *excluded* from the enumerate set. Otherwise, the list of enumerate values represents the values that are to be *included*.  |
| `[ enum` | `enum_value,... ]` |  The values to be displayed in the field, separated by commas [,]. This is an optional argument. If not included, all enumerate values defined for the field are available.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Notes  You can set enumerate values only for the current occurrence.
If the existing value of an enumerated field in not included in the new set, the nearest valid enum value is selected by the 4GL Engine.
If you want to *hide* any options in case of an optionset, use the function [set.initial.enum.values.for.field()](set.initial.enum.values.for.field.md) in the *after.form.read* section.
To set enum values for the *ask.enum()* function, use *set.ask.enum.values()*.

## Example
```

field ttadv996.fld1:
when.field.changes:
        if ttadv996.fld1 < SOME_VALUE then
                set.enum.values.for.field("ttadv996.type",
			ttadv.ktex.session, ttadv.ktex.form, ttadv.ktex.domain)
                | if the current value of ttadv996.type is not in the new set,
                | the 4GL engine will pick the nearest valid one.
        else
                set.enum.values.for.field("ttadv996.type")
                | all enum items are available
        endif
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)

- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
