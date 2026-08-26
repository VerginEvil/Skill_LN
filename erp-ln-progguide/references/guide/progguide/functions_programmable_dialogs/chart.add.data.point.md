# chart.add.data.point()

## Syntax:
`#include <bic_dialog>`
`function long chart.add.data.point( long series, (long|string|double) x, (long|double) y )`

## Description
Add a datapoint to the indicated series. The x and y datatypes must correspond with the datatypes set for the indicated axis with the function: chart.set.axis.type().

## Arguments
| | | |
|---|---|---|
| `long` | `series` |  The identifier of the series. The identifier must be returned by the function chart.add.series().  |
| `(long|string|double)` | `x` |  X-value of the data point.  |
| `(long|double)` | `y` |  Y-value of the data point.  |

## Return values
0 in case of success.
-1 in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [chart.add.series()](chart.add.series.md)
- [Programmable dialogs synopsis](synopsis.md)
- [Example chart](examplechart.md)
