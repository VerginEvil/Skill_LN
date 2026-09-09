# map.show()

## Syntax:
`function void map.show( long mid, string title, [ boolean sync.only ] )`

## Description
Show or update the map. When no map is currently visible a new map session window will be started. When this map is already visible, its content will be updated. The map session window will be brought into view.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  The map object id returned by function [map.create()](map.create.md).  |
| `string` | `title` |  The title of the map which will be shown in the LNUI session tab.  |
| `[ boolean` | `sync.only ]` |  Only synchronize the map session window if it is (still) running. The map session window will not be started if it is not running yet.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.
Notes  Optional argument sync.only is available from TIVLevel 2590.

## Related topics
- [Maps Workbench overview](overview.md)

- [Maps Workbench synopsis](synopsis.md)
