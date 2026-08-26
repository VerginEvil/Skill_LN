# map.add.circle()

## Syntax:
`function void map.add.circle( long rpid, double radius, string color, double opacity )`

## Description
Display a semi-transparent circle around a point.

## Arguments
| | | |
|---|---|---|
| `long` | `rpid` |  A route point object id returned by function [map.add.point()](map.add.point.md).  |
| `double` | `radius` |  The circle radius.  |
| `string` | `color` |  The circle color, this can be a decimal or hexadecimal color. In case of a hexadecimal color a # needs to be added to the color for example #FF0000 for red.  |
| `double` | `opacity` |  The opacity of the circle.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2420.

## Related topics
- [Maps Workbench overview](overview.md)
- [Maps Workbench synopsis](synopsis.md)
