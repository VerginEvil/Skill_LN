# plcm.set.resource.quantity

## Syntax:
`function long plcm.set.resource.quantity( string resource.id, long quantity )`

## Description
Change the quantity of a resource.

## Arguments
| | | |
|---|---|---|
| `string` | `resource.id` |  ID of the resource  |
| `long` | `quantity` |  New quantity for the resource  |

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
