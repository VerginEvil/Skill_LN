# plcm.set.legend.for.activity.division

## Syntax:
`function long plcm.set.legend.for.activity.division( string activity.id, string legend.id, long Start.percentage, long End.percentage, [ long Num.decimals ] )`

## Description
Lets a division of an activity refer to a legend entry. Thedivision will get the color of the legend.
Note that plcm.create.legend.entry() must be called for this legend.id before the plcm.start() has been called.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `string` | `legend.id` |  ID of the legend.  |
| `long` | `Start.percentage` |  0-99. Start of the division within the activity  |
| `long` | `End.percentage` |  1-100. End of the division within the activity  |
| `[ long` | `Num.decimals ]` |  0-6. Number of decimals (default 2) to be used in the percentage values (optional)  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
