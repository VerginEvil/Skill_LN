# is.field.invisible()

## Syntax:
`function boolean is.field.invisible( string field_name(18) )`

## Description
This checks whether a specified field is currently visible or invisible. To specify a particular element of an array field, append the element number (in parentheses) to the field name. For example: "ttadv301.labl(2)".
For multicurrency fields specify -1 for the element number, for example: `"tfacr200.fcmh(-1)"`.

## Arguments
| | | |
|---|---|---|
| `string` | `field_name(18)` |   |

## Return values
FALSE field is visible
TRUE field is invisible

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Use [inputfield.invisible()](inputfield.invisible.md) to hide a field. Use [inputfield.visible()](inputfield.visible.md) to redisplay it again. For dynamic forms, you can use this function only in the *before.program* section.

## Example
```

    if not is.field.invisible("ttadv200.cpac") then
        display("ttadv200.cpac")
    endif
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
