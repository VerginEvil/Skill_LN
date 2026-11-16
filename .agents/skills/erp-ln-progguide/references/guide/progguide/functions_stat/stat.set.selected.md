# stat.set.selected()

## Syntax:
`function void stat.set.selected( boolean i.selected )`

## Description
This function tells whether the Stat should be displayed as being selected or not.

## Arguments
| | | |
|---|---|---|
| `boolean` | `i.selected` |  If i.selected is true the Stat will be displayed with a selected style. Initial default will be false, not selected. If not given the selected state will not change.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.display" section of the field defined as a Stat.

## Related topics
- [Stat overview and synopsis](overview_and_synopsis.md)
