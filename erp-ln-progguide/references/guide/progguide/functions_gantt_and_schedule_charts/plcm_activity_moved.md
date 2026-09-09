# plcm.activity.moved

## Syntax:
`function boolean plcm.activity.moved( string activity.id, long start.date, long end.date )`

## Description
Callback-function for when the activity end-date and/or start-date have been changed in the UI.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `long` | `start.date` |  New start date.  |
| `long` | `end.date` |  New end date.  |

## Return values
True, when the move is allowed.
False, when the move is not allowed.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)

- [Example](example.md)
