# map.add.point()

## Syntax:
`function long map.add.point( long mid, double lat, double lon, string icontype )`

## Description
Add a new point to the map at the given position. The order in which points are added to the map determines the route order.

## Arguments

##

##

##

##
| | | |
|---|---|---|
| `long` | `mid` |  The map object id returned by function [map.create()](map.create.md).  |
| `double` | `lat` |  The point GPS Latitude.  |
| `double` | `lon` |  The point GPS Longitude.  |
| `string` | `icontype` |  The icon type which must be shown for this point. Must be one of: TRIANGLE Point shown as a triangle shape. CIRCLE Point shown as a circle shape. PENTAGON Point shown as a pentagon shape. SQUARE Point shown as a square shape.  |

## Return values
| | |
|---|---|
| <> 0 | A new point object id. |
| 0 | When this function fails. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Related topics
- [Maps Workbench overview](overview.md)
- [Maps Workbench synopsis](synopsis.md)
