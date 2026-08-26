# plcm.set.activity.property

## Syntax:
`function long plcm.set.activity.property( string activity.id, string property.id, string property.value )`

## Description
Sets an activity property. The property will be visualized in the table part of the Gantt view.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `string` | `property.id` |  D of the property. The following property.id's are predefined, and must not be used in this function. NAME|ID|START|END|RESOURCE When using property.id equals "TOOLTIP", the tooltip on the activity will also change. When using property.id equals "SLACK_TOOLTIP", the tooltip of the slack for the activity will also change.  |
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
