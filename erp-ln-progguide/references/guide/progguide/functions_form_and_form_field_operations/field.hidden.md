# field.hidden()

## Syntax:
`function void field.hidden( const string i.field.name, ... )`

## Description
This function hides the specified fields from the form, including associated label, and button. To hide a particular element of an array field, append the element number (in parenthesis) to the field name. The fields will be marked as being initially hidden.
The fields can be made visible again by a user by Personalizing the Form.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.field.name, ...` |  A list of the field names that should be made initially hidden.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
