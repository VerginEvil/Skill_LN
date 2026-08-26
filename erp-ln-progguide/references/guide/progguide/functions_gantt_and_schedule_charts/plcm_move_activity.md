# plcm.move.activity

## Syntax:
`function long plcm.move.activity( string activity.id, long start.date, long end.date )`

## Description
Sets a new start/end date for an activity

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity to move.  |
| `long` | `start.date` |  New start.date (utc)  |
| `long` | `end.date` |  New end date (utc)  |

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
