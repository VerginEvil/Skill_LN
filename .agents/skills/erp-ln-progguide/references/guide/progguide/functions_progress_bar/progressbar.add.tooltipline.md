# progressbar.add.tooltipline()

## Syntax:
`function long progressbar.add.tooltipline( const string i.tooltip )`

## Description
This function adds a tooltip line to Progress bar. LN UI will display each line as a separate line below each other.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.tooltip` |  A tooltip description. Multiple added lines are displayed as separate lines by LN UI.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Failure, Field is not set as being a Progress bar. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2610.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section for the field that is set as a Progress bar by calling the function progressbar.set.field.

## Related topics
- [Progress bar overview and synopsis](overview_and_synopsis.md)
