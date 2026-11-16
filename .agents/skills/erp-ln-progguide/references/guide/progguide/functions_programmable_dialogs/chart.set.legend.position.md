# chart.set.legend.position()

## Syntax:
`#include <bic_dialog>`
`function long chart.set.legend.position( long chart, string legendpos )`

## Description
Sets the position of the legend.

## Arguments
| | | |
|---|---|---|
| `long` | `chart` |  The id returned by the function chart.new  |
| `string` | `legendpos` |  Position the legend of the chart will be displayed. Options: CHART.LEGENDPOS.STANDARD CHART.LEGENDPOS.RIGHT CHART.LEGENDPOS.BOTTOM Default: CHART.LEGENDPOS.STANDARD.  |

## Return values
Return values 0 Success. -1 Failure, probably chart identification is not correct.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2521.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
