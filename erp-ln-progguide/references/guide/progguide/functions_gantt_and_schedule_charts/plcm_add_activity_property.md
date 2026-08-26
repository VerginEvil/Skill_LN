# plcm.add.activity.property

## Syntax:
`function long plcm.add.activity.property( string property.id, string property.label )`

## Description
Adds a property to an activity. The property will be visualized as a column in the table part of the Gantt view.

## Arguments
| | | |
|---|---|---|
| `string` | `property.id` |  ID of the property. The following property.id's are predefined. You can change the label for these predefined properties. NAME|ID|START|END|RESOURCE Adding a property with id equal to "TOOLTIP" will also add a tooltip on the activity.  |
| `string` | `property.label` |  Label (column header) of the property.  |

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
