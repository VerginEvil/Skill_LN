# plcm.set.activity.completion.percentage

## Syntax:
`function long plcm.set.activity.completion.percentage( string activity.id, long completion.percentage )`

## Description
Change the completion.percentage of an activity.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `long` | `completion.percentage` |  The completion percentage for the activity (0-100)  |

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
