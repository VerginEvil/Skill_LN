# progressbar.set.field()

## Syntax:
`function long progressbar.set.field( const string i.fieldname, [ const string i.title, const string i.subtitle, boolean i.is.mirrored ] )`

## Description
This function changes the type of the field to Progress bar. The field will be displayed as chart of type Horizontal Stacked Bar.
If the field is displayed, the before.display section of the field will be called. In this section the values of the progress bar need to be set.

## Arguments
| | |
|---|---|
| True | Progress bar is displayed mirrored. |
| False | Progress bar is not displayed mirrored. |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | error, i.fieldname was not found on the form. |
| -2 | error, i.fieldname is not of type long. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2610.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Related topics
- [Progress bar overview and synopsis](overview_and_synopsis.md)
