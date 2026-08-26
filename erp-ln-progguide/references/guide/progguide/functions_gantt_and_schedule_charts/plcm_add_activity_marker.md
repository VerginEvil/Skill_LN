# plcm.add.activity.marker()

## Syntax:
`function long plcm.add.activity.marker( string activity.id, long icon.id, long date_time, string tooltip, string legend.id )`

## Description
Adds a marker to an activity. The marker will be visualized by an icon.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id` |  ID of the activity.  |
| `long` | `icon.id` |  Identification of a marker icon. There are 7 icons predefined. Use one of these predefined icons by specifying: PLCM_ICON_TACK PLCM_ICON_TAG PLCM_ICON_UP PLCM_ICON_BOOKMARK PLCM_ICON_PIN PLCM_ICON_STAR PLCM_ICON_CLOCK  |
| `long` | `date_time` |  The date and time of the marker (utc).  |
| `string` | `tooltip` |  Tooltip of the marker.  |
| `string` | `legend.id` |  ID of the legend of the marker.  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2130.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
