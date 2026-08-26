# to.field()

## Syntax:
`function void to.field( field field, [ long occ ] )`

## Description
This transfers control of the 4GL engine to the specified field after input to or display of the current field. This overrides the TAB sequence of the form. You can specify the field by using the field number or a string containing the field name.
After handling the specified field, control passes to the next field in the TAB sequence.

## Arguments
| | | |
|---|---|---|
| `field` | `field` |   |
| `[ long` | `occ ]` |  The occurrence number. (optional) This parameter is available from [TIV](../tiv/tiv_overview.md) [TIV 1900](../tiv/tiv_1900.md).  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## See also
[to.form()](to.form.md)
Note  In a well-designed GUI, users (and not the application) select and initiate the actions to be performed. Using *to.field()* removes control from the user. Therefore it does not conform to good GUI design principles.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
