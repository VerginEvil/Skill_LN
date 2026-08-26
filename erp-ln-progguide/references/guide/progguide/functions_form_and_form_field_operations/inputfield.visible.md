# inputfield.visible()

## Syntax:
`function void inputfield.visible( string field_name(18) )`

## Description
Use this to redisplay one or more fields made invisible by [inputfield.invisible()](inputfield.invisible.md). To redisplay a particular element of an array field, append the element number (in parentheses) to the field name. For example: `"ttadv301.labl(2)"`.
For multicurrency fields specify -1 for the element number, for example: `"tfacr200.fcmh(-1)"`.

## Arguments
| | | |
|---|---|---|
| `string` | `field_name(18)` |   |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Use [is.field.invisible()](is.field.invisible.md) to check whether a specified field is currently visible or invisible.

## Example
```

before.field:
        inputfield.visible( "ttadv200.cpac" )
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
