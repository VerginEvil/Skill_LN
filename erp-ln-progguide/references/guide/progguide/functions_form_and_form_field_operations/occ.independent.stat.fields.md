# occ.independent.stat.fields()

## Syntax:
`function long occ.independent.stat.fields( ... )`

## Description
Occurrence independent means that the values are not based on one or more selected rows in the grid.
All Stat fields will be occurrence independent.
Used by Conditional Formatting functionality.

## Arguments
| | | |
|---|---|---|
| `` | `...` |  Reserved for future.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Wrong parameter. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2520.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
- [Stat overview and synopsis](../functions_stat/overview_and_synopsis.md)
