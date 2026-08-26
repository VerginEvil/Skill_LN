# plcm.reservation.deleted

## Syntax:
`function boolean plcm.reservation.deleted( const string activity.id, const string resource.id )`

## Description
Callback-function for when the reservation is about to be deleted in the UI.

## Arguments
| | | |
|---|---|---|
| `const string` | `activity.id` |  ID of the activity.  |
| `const string` | `resource.id` |  ID of the resource.  |

## Return values
True, when the delete is allowed.
False, when the delete is not allowed.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
