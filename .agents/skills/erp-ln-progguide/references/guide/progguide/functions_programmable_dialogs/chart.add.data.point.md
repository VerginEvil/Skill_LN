# chart.add.data.point()

## Syntax:
`#include <bic_dialog>`
`function long chart.add.data.point( long series, (long|string|double) x, (long|double) y, string pointid )`

## Description
Add a datapoint to the indicated series. The x and y datatypes must correspond with the datatypes set for the indicated axis with the function: chart.set.axis.type().
If interactive graphs are active and the type of the chart is CHART_TYPE_PIE, the id of the created series will be returned if successful.
If the series is set to be clickable and pointid is not supplied an assert will be given and the data point will not be added.
If not successful -1 will be returned.

## Arguments
| | | |
|---|---|---|
| `long` | `series` |  The identifier of the series. The identifier must be returned by the function chart.add.series().  |
| `(long|string|double)` | `x` |  X-value of the data point.  |
| `(long|double)` | `y` |  Y-value of the data point.  |
| `string` | `pointid` |  Optional identification of the data point. Mandatory if the series is clickable. Not applicable if the chart is of type pie. An assert will be given if pointid is supplied while the chart is of type pie.  |

## Return values
-1 in case of an error.
0 in case of success.
otherwise Id of the created series.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Note: The argument pointid is supported from TIV level 2521.

## Related topics
- [chart.add.series()](chart.add.series.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
