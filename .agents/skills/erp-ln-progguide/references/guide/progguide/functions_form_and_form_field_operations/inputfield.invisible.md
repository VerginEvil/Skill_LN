# inputfield.invisible()

## Syntax:
`function void inputfield.invisible( string field_name(18),... )`

## Description
This hides the specified field(s) completely. In dynamic sessions, associated label and button are also hidden. To hide a particular element of an array field, append the element number (in parentheses) to the field name. For example: `"ttadv301.labl(2)"`.
For multicurrency fields specify -1 for the element number, for example: `"tfacr200.fcmh(-1)"`.
Note that when the predefined variable *attr.echo* is set to off, the field value is not displayed but the field itself remains visible.
If the invisible command is used after the `"before.program"`, the field, including label etc, is not visible anymore but the space on the form is still reserved. So when the field is made visible again later, the empty reserved space is occupied again with the field.
However, when the field is made invisible in the before program, it may not be made visible later in the code, since no space is available.

## Arguments
| | | |
|---|---|---|
| `string` | `field_name(18),...` |    |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Use [inputfield.visible()](inputfield.visible.md) to redisplay the field again. Use [is.field.invisible()](is.field.invisible.md) to check whether a specified field is currently visible or invisible.

## Example
```

before.program:
     inputfield.invisible( "ttadv200.cpac" )
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
