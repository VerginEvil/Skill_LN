# chart.line.series.set.curving()

## Syntax:
`#include <bic_dialog>`
`function long chart.line.series.set.curving( long line.series, string curving )`

## Description
Sets the curving (smoothing) of a line series part of a combined line-bar chart.
Default a line series has no curving.

## Arguments
| | | |
|---|---|---|
| `long` | `line.series` |  The id returned by the function chart.add.line.series..  |
| `string` | `curving` |  Curving to be used on the line series, possible values: CHART.LINE.SERIES.CURVE.NONE CHART.LINE.SERIES.CURVE.NORMAL  |

## Return values
0 in case of success.
-1 in case of an error, probably line.series identification is not correct.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2521.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [chart.new()](chart.new.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
