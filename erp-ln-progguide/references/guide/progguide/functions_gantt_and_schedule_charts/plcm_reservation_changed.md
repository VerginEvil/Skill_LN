# plcm.reservation.changed

## Syntax:
`function boolean plcm.reservation.changed( const string activity.id., const string old.resource.id, const string new.resource.id )`

## Description
Callback-function for when a reservation is about to change in the UI.

## Arguments
| | | |
|---|---|---|
| `const string` | `activity.id.` |  ID of the from activity.  |
| `const string` | `old.resource.id` |  ID of the old assigned resource.  |
| `const string` | `new.resource.id` |  ID of the new assigned resource  |

## Return values
True, when the delete is allowed.
False, when the delete is not allowed.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)

- [Example](example.md)
