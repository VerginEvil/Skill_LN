# map.add.point()

## Syntax:
`function long map.add.point( long mid, double lat, double lon, string icontype, [ boolean is.clickable, const string pointid ] )`

## Description
Add a new point to the map at the given position.
The order in which points are added to the map determines the route order.
If a point is clickable a prcm notification will be sent to the session if the user clicks on the point on the map.
Notify subject: "maps:" + str$(process id of the session that starts the map workbench)
Notify aspect: pointid. Because the string aspect of the notify function is limited to 32 string characters, the pointid has to be limited to 32 string characters.
The pointid and arrowid should all have a unique id, so the session knows on which object the user clicked.

## Arguments

## TRIANGLE

## CIRCLE

## PENTAGON

## SQUARE
| | | |
|---|---|---|
| `long` | `mid` |  The map object id returned by function [map.create()](map.create.md).  |
| `double` | `lat` |  The point GPS Latitude.  |
| `double` | `lon` |  The point GPS Longitude.  |
| `string` | `icontype` |  The icon type which must be shown for this point. Must be one of: Point shown as a triangle shape. Point shown as a circle shape. Point shown as a pentagon shape. Point shown as a square shape.  |
| `[ boolean` | `is.clickable ]` |  Sets the point to be clickable or not. If a point is clickable a unique pointid should also be given. Default: false pointid is mandatory if is.clickable is true. If pointid is not given is.clickable will be set to false.  |
| `[ const string` | `pointid ]` |  Identification of the point by the application. This identification is used when adding an Arrow between two points and is the way to know which point is clicked if click events are supported by this map. Mandatory if is.clickable is true  |

## Return values
| | |
|---|---|
| <> 0 | A new point object id. |
| 0 | When this function fails. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Note: The arguments is.clickable and pointid are supported from TIV level 2531.

## Related topics
- [Maps Workbench overview](overview.md)

- [Maps Workbench synopsis](synopsis.md)
