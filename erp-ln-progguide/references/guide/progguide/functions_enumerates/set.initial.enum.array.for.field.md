# set.initial.enum.array.for.field()

## Syntax:
`function void set.initial.enum.array.for.field( const string field.name, long size, const long values )`

## Description
This function applies to enumerated fields that are displayed as listbox or option set. It limits the number of options to the specified set of enum constants. Any options not specified will be *hidden*.

## Arguments
| | | |
|---|---|---|
| `const string` | `field.name` |  The name of the optionset field. For example, "ttadv996.type". For an array field, include the array element. For example, "tttadv996.type(5)".  |
| `long` | `size` |  The size of the *values* array.  |
| `const long` | `values` |  The values to be displayed in the field.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.
Notes  This function can only be called in the *after.form.read* section. Use the function ` [set.enum.array.for.field()](set.enum.array.for.field.md)` in other sections.
You can set enumerate values for the current occurrence only.
If the existing value of an enumerated field in not included in the new set, the 4GL Engine selects the nearest valid option.

## Example
```

long enum.values(1) based
long enum.count
after.form.read:
        enum.count = determine.applicable.types(enum.values)
        set.initial.enum.array.for.field("ttadv996.type", enum.count, enum.values)
        | Session only works with specified values.
```

## Related topics
- [Enumerates overview and synopsis](overview_and_synopsis.md)
- [Enumerate and set constants](../3gl_features/enumerate_and_set_constants.md)
