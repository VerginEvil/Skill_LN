# stat.add.tooltipline()

## Syntax:
`function void stat.add.tooltipline( const string i.tooltip )`

## Description
This function adds a tooltip line to the Stat. LN UI will display each line as a separate line below each other.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.tooltip` |  A tooltip description. Multiple added lines are displayed as separate lines by LN UI.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section of the field defined as a Stat.

## Related topics
- [Stat overview and synopsis](overview_and_synopsis.md)
