# chart.set.axis.type()

## Syntax:
`#include <bic_dialog>`
`function long chart.set.axis.type( long chart, long axis, long type )`

## Description
Set the data type for the indicated axis.
In case the x-axis is of type string, the advised initial chart type is: CHART_BAR, CHART_BAR_HORIZONTAL or CHART_PIE.
In case the x-axis has a numeric, date or time type, the advised initial chart type is: CHART_LINE or CHART_AREA.

## Arguments
| | | |
|---|---|---|
| `long` | `chart` |  The identifier of the chart. The identifier must be returned by the function dialog.add.chart().  |
| `long` | `axis` |  Identifies the axis for which the type must be set: CHART_XAXIS, CHART_YAXIS.  |
| `long` | `type` |  Data type for the indicated axis. Possible values: DB.LONG, DB.DOUBLE, DB.STRING, DB.DATE or DB.TIME. The y-axis can only be of type DB.LONG or DB.DOUBLE.  |

## Return values
0 in case of success.
-1 in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [dialog.add.chart()](dialog.add.chart.md)
- [Programmable dialogs synopsis](synopsis.md)
- [Example chart](examplechart.md)
