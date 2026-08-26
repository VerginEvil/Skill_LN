# plcm.add.reservation

## Syntax:
`function long plcm.add.reservation( string activity.id, string resource.id )`

## Description
Assigns an activity to a resource.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity to assign.  |
| `string` | `resource.id` |  ID of the resource to assign the activity to.  |

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
