# plcm.add.root.activity

## Syntax:
`function long plcm.add.root.activity( string root.activity.id, string root.activity.name )`

## Description
Call this function only once. The root activity will serve as highest level parent for all other activities. Therefore it will be displayed as summary bar in the Gantt view.

## Arguments
| | | |
|---|---|---|
| `string` | `root.activity.id` |  Unique ID for the activity.  |
| `string` | `root.activity.name` |  Name for the root activity.  |

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
