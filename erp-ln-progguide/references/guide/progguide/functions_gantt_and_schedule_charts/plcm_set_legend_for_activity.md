# plcm.set.legend.for.activity

## Syntax:
`function long plcm.set.legend.for.activity( string activity.id, string legend.id )`

## Description
Lets the complete activity refer to a legend entry. The activity will get the color of the legend.
Note that plcm.create.legend.entry() must be called for this legend.id before the plcm.start() has been called.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `string` | `legend.id` |  ID of the legend.  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
