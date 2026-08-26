# plcm.set.activity.name

## Syntax:
`function long plcm.set.activity.name( string activity.id, string name )`

## Description
Change the name of an activity.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `string` | `name` |  New name for the activity  |

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
