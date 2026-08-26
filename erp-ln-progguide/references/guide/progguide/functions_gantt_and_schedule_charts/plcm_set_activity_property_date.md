# plcm.set.activity.property.date

## Syntax:
`function long plcm.set.activity.property.date( string activity.id, string property.id, domain ttutc utc.value )`

## Description
Sets an activity property for a property of the type utc. The property will be visualized in the table part of the Gantt view. The utc (date-time value) will be represented in the format set up in the browser. Same format that is used for the start and end activity date.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `string` | `property.id` |  ID of the property. The following property.id's are predefined, and must not be used in this function. NAME|ID|START|END|RESOURCE  |
| `domain ttutc` | `utc.value` |  Value of the property as a utc  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2390.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
