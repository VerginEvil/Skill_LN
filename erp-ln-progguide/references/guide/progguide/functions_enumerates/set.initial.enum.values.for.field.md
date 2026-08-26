# set.initial.enum.values.for.field()

## Syntax:
`function void set.initial.enum.values.for.field( const string field.name, long ALL_ENUMS_EXCEPT, enum enum_value, ... )`

## Description
This function applies to enumerated fields that are displayed as listbox or optionset. It limits the number of options to the specified set of enum constants. Any options not specified will be *hidden*.

## Arguments
| | | |
|---|---|---|
| `const string` | `field.name` |  The name of the optionset field. For example, "ttadv996.type". For an array field, include the array element. For example, "tttadv996.type(5)".  |
| `long` | `ALL_ENUMS_EXCEPT` |  This optional macro specifies that the succeeding list of enumerate values represents those values that are to be *excluded* from the enumerate set. Otherwise, the list of enumerate values represents the values that are to be *included*.  |
| `enum` | `enum_value, ...` |  The options to be displayed on the form, separated by commas [,]. This is an optional argument. If not included, all enumerate values (= all options) defined for the field are available.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Notes  This function can only be called in the *after.form.read* section. Use the function ` [set.enum.values.for.field()](set.enum.values.for.field.md)` in other sections.
You can set enumerate values for the current occurrence only.
If the existing value of an enumerated field in not included in the new set, the 4GL Engine selects the nearest valid option.
This function restricts the set of enum constants for the Find dialog and filter as well.

## Example
```

after.form.read:
        if SOME_CONDITION then
                set.initial.enum.values.for.field("ttadv996.type",
                    ttadv.ktex.session, ttadv.ktex.form, ttadv.ktex.domain)
                | Session only works with specified values.
        endif
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)
- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
