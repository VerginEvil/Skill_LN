# plcm.add.activity

## Syntax:
`function long plcm.add.activity( string parent.activity.id, string activity.id, string activity.name, [ long start.date, long end.date, long completion.percentage ] )`

## Description
Adds a child activity to an activity. This will cause the parent activity to be displayed as a summary bar.

## Arguments
| | | |
|---|---|---|
| `string` | `parent.activity.id` |  ID of the parent activity.  |
| `string` | `activity.id` |  Unique ID of the activity.  |
| `string` | `activity.name` |  Name for the activity.  |
| `[ long` | `start.date ]` |  Date the activity starts (utc) If a start.date is passed, end.date is mandatory.  |
| `[ long` | `end.date ]` |  Date the activity ends (utc)  |
| `[ long` | `completion.percentage ]` |  The completion percentage for the activity (0-100)  |

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
