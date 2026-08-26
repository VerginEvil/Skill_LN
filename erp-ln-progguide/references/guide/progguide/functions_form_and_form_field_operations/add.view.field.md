# add.view.field()

## Syntax:
`function void add.view.field( long index.nr, const string fname )`

## Description
*Deprecated.* This function is supported for compatibility reasons, do not use this function anymore but use for conditional view-fields [remove.field.from.view()](remove.field.from.view.md).
Standard use the field-property "View" instead. In case of dynamic index switching, use the View column in the Available Indices by Session session. For conditional view-fields it is possible to add viewfields with this function from *before.program* or *after.form.read* section.

## Arguments
| | | |
|---|---|---|
| `long` | `index.nr` |  The index identifier. If this is 0, the field is not associated with any index. It is always a view field.  |
| `const string` | `fname` |  The name of the form field to be added. To specify a particular element of an array field, append the element number (in parentheses) to the field name. For example: "ttadv301.labl(2)".  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
