# plcm.command.performed

## Syntax:
`function long plcm.command.performed( string command.id, const long activities.context.count, const string activities.context(), const long resources.context.count, string resources.context() )`

## Description
Callback-function for when a "custom' command has been performed in the UI.

## Arguments
| | | |
|---|---|---|
| `string` | `command.id` |  ID of the command.  |
| `const long` | `activities.context.count` |  Number of items in activities.context() array  |
| `const string` | `activities.context()` |  Array of activity id's that are selected in the UI.  |
| `const long` | `resources.context.count` |  Number of items in resources.context() array  |
| `string` | `resources.context()` |  Array of resource id's that are selected in the UI.  |

## Return values
None.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)

- [Example](example.md)
