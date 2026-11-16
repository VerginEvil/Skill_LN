# plcm.set.resource.property.value

## Syntax:
`function long plcm.set.resource.property.value( string resource.id, string property.id, string property.value )`

## Description
Sets a resource property. The property will be visualized in the table part of the Schedule view.

## Arguments
| | | |
|---|---|---|
| `string` | `resource.id` |  ID of the resource.  |
| `string` | `property.id` |  ID of the property. The following property.id's are predefined, and must not be used in this function. NAME|ID|QUANTITY  |
| `string` | `property.value` |  Value of the property  |

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
