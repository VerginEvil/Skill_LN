# plcm.add.resource

## Syntax:
`function long plcm.add.resource( string parent.resource.id, string resource.id, string resource.name, [ long quantity ] )`

## Description
Adds a child resource to a resource.

## Arguments
| | | |
|---|---|---|
| `string` | `parent.resource.id` |  ID of the parent resource.  |
| `string` | `resource.id` |  Unique ID of the resource.  |
| `string` | `resource.name` |  Name for the resource.  |
| `[ long` | `quantity ]` |  Optional. Quantity  |

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
