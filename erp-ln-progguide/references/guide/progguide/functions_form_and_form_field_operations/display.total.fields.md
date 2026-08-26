# display.total.fields()

## Syntax:
`function void display.total.fields( string fieldname1, void value1, string fieldname2,..., void value2,... )`

## Description
When a total line is included in a form, this function displays total values for specified fields in the grid. The function takes one or more pairs of arguments. In each pair, the first argument is the field name; the second argument is the total value for that field.
The fields must be defined on the form as multioccurrence form fields. They must also be declared in the UI script. Alternately, the fields can be table fields.
To add a total line to a grid, add the following code to the UI script:
```

before.program:
    fattr.total.line = true
```
Preferably call this function from the program section [on.display.total.line](../4gl_features/4gl_program_sections.md). Alternatively for every update that effects the total fields, call *display.total.fields()* to display the new totals.
The total line can display an enum value. To do this, the description of the enum must be passed using [enum.descr$()](../functions_enumerates/enum.descr.md). For example:
```

display.total.fields( "tffbs.dbcr",
                      enum.descr$( "tfgld.dbcr", tfgld.dbcr.debit ) )
```

## Arguments
| | | |
|---|---|---|
| `string` | `fieldname1` |   |
| `void` | `value1` |   |
| `string` | `fieldname2,...` |   |
| `void` | `value2,...` |   |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  Total fields are always read-only. They cannot be disabled or enabled.
Total fields have the same display properties as the fields above them.
If a field specified by the function is an array field, the total value is displayed in the first field of the array. Subsequent fields in the array cannot be addressed by the function.
Conditional total line (LN UI)  In case the session should display the total line conditionally, for example depending on specific fields in the view, then `fattr.total.line` *must* always be set to `true` in the `before.program` section.
The total line will not be shown if `display.total.fields` is not called. Alternatively, `fattr.total.line` can be set to `false` in a later section (such as `init.group` of `group.1`). In that case, the on.display.total.fields section will not be called and display.total.fields will not do anything.

## Example
```

before.program:
    fattr.total.line = true

on.display.total.line:
    display.total.fields( "whwmd000.amnt1", tot_1,
                          "whwmd000.amnt2", tot_2 )
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
