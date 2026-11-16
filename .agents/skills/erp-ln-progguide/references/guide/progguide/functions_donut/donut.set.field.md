# donut.set.field()

## Syntax:
`function long donut.set.field( const string i.fieldname, long i.width, long i.height )`

## Description
This function changes the type of the field to Donut. The field will be displayed as chart of type donut.
If the field is displayed a callback function donut.’fieldname’.display is called. In this callback function the donut needs to be defined.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.fieldname` |  The name of the field on the form.  |
| `long` | `i.width` |  The width the Donut can use. The width is in the same unit as on the form editor.  |
| `long` | `i.height` |  The height the Donut can use. The height is in the same unit as on the form editor.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | error, i.fieldname was not found on the form. |
| -2 | error, i.fieldname is not of type long. |
| -3 | error, function should be called from after.form.read section. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Related topics
- [Donut overview and synopsis](overview_and_synopsis.md)
