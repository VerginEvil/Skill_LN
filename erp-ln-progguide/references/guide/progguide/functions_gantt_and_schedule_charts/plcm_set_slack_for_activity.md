# plcm.set.slack.for.activity()

## Syntax:
`function long plcm.set.slack.for.activity( string activity.id, long start.date, long end.date, string legend.id )`

## Description
Sets the slack attributes of an activity. The slack will get the color of the legend.
Note that plcm.create.legend.entry() must be called for this legend.id before the plcm.start() has been called.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `long` | `start.date` |  Start date for the activity slack (utc).  |
| `long` | `end.date` |  End date for the activity slack (utc).  |
| `string` | `legend.id` |  ID of the legend for the slack.  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function can be implemented with [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 2130](../tiv/tiv_2130.md) and requires LN UI 12.0.3 or higher.
This function supports one slack per activity for LN UI 12.0.3 and two slacks per activity for LN UI 12.0.4 or higher.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
