# map.add.legendline()

## Syntax:
`function void map.add.legendline( long mid, string label, string icontype, [ string color ] )`

## Description
Add a line to to the legend explaining the meaning of an icontype.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  The map object id returned by function [map.create()](map.create.md).  |
| `string` | `label` |  A textual explanation of the meaning of this icontype.  |
| `string` | `icontype` |  The icon type for which the explanation is given. See function [map.add.point()](map.add.point.md) for the supported icon type values.  |
| `[ string` | `color ]` |  The color of the icon, this can be a decimal or hexadecimal color. In case of a hexadecimal color a # needs to be added to the color for example #FF0000 for red. This argument is available from TIV level 2420.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Related topics
- [Maps Workbench overview](overview.md)

- [Maps Workbench synopsis](synopsis.md)
