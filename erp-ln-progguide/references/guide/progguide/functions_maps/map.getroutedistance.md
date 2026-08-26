# map.getroutedistance()

## Syntax:
`function double map.getroutedistance( long mid )`

## Description
Get the distance in kilometers of the current route. Add a new point to the map at the given position. The order of points added to the map is equal to the route order.
Note: This function should not be called directly after the map.show function is called. If the map is displayed modeless (the default mode), the route distance will be 0 (unknown) if this function is called directly after the call of function map.show.
Instead the function set.alarm(1000) can be called. In the on.choice of the interrupt choice section the map.getroutedistance function can be called. And the distance displayed in a field or status message.
Of course this function can also be called from another option. A different Show and Get distance option. The set.alarm is only needed if the Display of the map and the determination of the distance is done by one menu or field option.
See [Maps Workbench examples](examples.md).

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  The map object id returned by function [map.create()](map.create.md).  |

## Return values
| | |
|---|---|
| > 0 | The distance in kilometers of the last route shown in the map. |
| 0 | When no route is shown, or the distance is unknown. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2420.

## Related topics
- [Maps Workbench overview](overview.md)
- [Maps Workbench synopsis](synopsis.md)
