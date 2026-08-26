# remove.field.from.view()

## Syntax:
`function void remove.field.from.view( const string fname )`

## Description
The view fields for a dynamic session are determined by the view-property of a field in the DFE or, in case of dynamic index switching, by the view column in the Available Indices by Session session. You can use this function to conditionally remove a field from the view-area. e.g. Based on the current index (the predefined variable *session.current.index*).

## Arguments
| | | |
|---|---|---|
| `const string` | `fname` |  The name of the form field to be removed from the view. To specify a particular element of an array field, append the element number (in parentheses) to the field name. For example: "ttadv301.labl(2)".  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Use this function only in the before.program or after.form.read section.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
