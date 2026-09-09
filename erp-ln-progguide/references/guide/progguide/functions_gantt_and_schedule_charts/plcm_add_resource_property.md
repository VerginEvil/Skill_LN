# plcm.add.resource.property

## Syntax:
`function long plcm.add.resource.property( string property.id, string property.label )`

## Description
Adds a property to a resource. The property will be visualized as a column in the table part of the Schedule view.

## Arguments
| | | |
|---|---|---|
| `string` | `property.id` |  ID of the property. The following property.id's are predefined. You can change the label for these predefined properties. NAME|ID|QUANTITY  |
| `string` | `property.label` |  Label (column header) of the property  |

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
