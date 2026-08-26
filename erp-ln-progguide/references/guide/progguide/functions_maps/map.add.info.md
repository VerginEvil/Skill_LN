# map.add.info()

## Syntax:
`function long map.add.info( long rpid, string title )`

## Description
Add an info object to a route point. An info object will be shown as a tooltip when the user hovers the mouse pointer over a route point icon.

## Arguments
| | | |
|---|---|---|
| `long` | `rpid` |  A route point object id returned by function [map.add.point()](map.add.point.md).  |
| `string` | `title` |  The title of the tooltip. This title can be empty.  |

## Return values
| | |
|---|---|
| <> 0 | A new info object id. |
| 0 | When this function fails. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Related topics
- [Maps Workbench overview](overview.md)
- [Maps Workbench synopsis](synopsis.md)
