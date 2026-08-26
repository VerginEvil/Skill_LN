# plcm.delete.reservation

## Syntax:
`function long plcm.delete.reservation( string activity.id, string resource.id )`

## Description
Deletes a reservation.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity the resource is assigned to.  |
| `string` | `resource.id` |  ID of the assigned resource.  |

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
