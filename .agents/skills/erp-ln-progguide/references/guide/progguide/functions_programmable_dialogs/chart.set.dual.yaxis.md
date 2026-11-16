# chart.set.dual.yaxis()

## Syntax:
`#include <bic_dialog>`
`function long chart.set.dual.yaxis( long chart, long type, [ string title ] )`

## Description
Tells the chart to show a second Y-axis on the right side of the chart for the line series.
Only to be used if the chart is of type CHART_TYPE_BAR or CHART_TYPE_STACKEDBAR and line series are added to the chart by function chart.add.line.series.

## Arguments
| | | |
|---|---|---|
| `long` | `chart` |  The identifier of the chart. The identifier must be returned by the function chart.new().  |
| `long` | `type` |  Data type for the second Y-axis. Possible values: DB.LONG, DB.DOUBLE.  |
| `[ string` | `title ]` |  The title for the second Y-axis.  |

## Return values
0 in case of success.
-1 in case of an error, probably chart identification is not correct.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2521.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [chart.new()](chart.new.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
