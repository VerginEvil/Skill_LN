# chart.line.series.set.marker()

## Syntax:
`#include <bic_dialog>`
`function long chart.line.series.set.marker( long line.series, string marker )`

## Description
Sets the marker of datapoints on the line series. Default a standard marker will be shown.

## Arguments
| | | |
|---|---|---|
| `long` | `line.series` |  The id returned by the function chart.add.line.series..  |
| `string` | `marker` |  Marker to be used on the line series, possible values: CHART.LINE.SERIES.MARKER.NONE CHART.LINE.SERIES.MARKER.STANDARD  |

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
