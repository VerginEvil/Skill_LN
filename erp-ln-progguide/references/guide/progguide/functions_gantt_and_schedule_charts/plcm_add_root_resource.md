# plcm.add.root.resource

## Syntax:
`function long plcm.add.root.resource( string root.resource.id, string root.resource.name )`

## Description
Call this function only once. The root resource will serve as highest level parent for all other resources

## Arguments
| | | |
|---|---|---|
| `string` | `root.resource.id` |  Unique ID for the resource.  |
| `string` | `root.resource.name` |  Name for the root resource.  |

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
