# map.add.arrow()

## Syntax:
`function long map.add.arrow( long mid, const string start.pointid, const string end.pointid, long arrow.direction, [ long i.arrow.weight, long i.arrow.colort, boolean is.clickable, const string arrowid ] )`

## Description
Add an arrow on the map between the given start- and endpoint.
If an arrow is clickable a prcm notification will be sent to the session if the user clicks on the arrow on the map.
Notify subject: maps:” + str$(process id of the session that starts the map workbench)
Notify aspect: arrowid. Because the string aspect of the notify function is limited to 32 string characters, the arrowid has to be limited to 32 string characters.
The pointid and arrowid should all have a unique id, so the session knows on which object the user has clicked.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  The map object id returned by function [map.create()](map.create.md).  |
| `const string` | `start.pointid` |  Identification of the Start Point specified by function map.add.point.  |
| `const string` | `end.pointid` |  Identification of the End Point specified by function map.add.point.  |
| `long` | `arrow.direction` |  Direction of the arrow. Must be one of: ARROW.DIRECTION.START Arrow points to the start point. ARROW.DIRECTION.END Arrow points to the end point. ARROW.DIRECTION.BOTH Arrow will point to the start and to the end point.  |
| `[ long` | `i.arrow.weight ]` |  Weight of the arrow, value between 1 and 10. Default: 4.  |
| `[ long` | `i.arrow.colort ]` |  Color of the arrow, possible values: ARROW.COLOR.BLACK ARROW.COLOR.GREEN ARROW.COLOR.RED ARROW.COLOR.BLUE ARROW.COLOR.YELLOW Default: ARROW.COLOR.BLACK.  |
| `[ boolean` | `is.clickable ]` |  Sets the arrow to be clickable or not. If an arrow is clickable a unique arrowid should also be given. Default: false arrowid is mandatory if is.clickable is true. If arrowid is not given is.clickable will be set to false.  |
| `[ const string` | `arrowid ]` |  Identification of the arrow by the application. This identification is the way to know which arrow has been clicked on the prcm "maps" notification. Mandatory if is.clickable is true  |

## Return values
| | |
|---|---|
| <> 0 | Success, Arrow object id. |
| 0 | Failure, Possible reason: Map object id is not correct. The start.pointid is not found in the Map object. The end.pointid is not found in the Map object. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2531.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Maps Workbench overview](overview.md)

- [Maps Workbench synopsis](synopsis.md)
