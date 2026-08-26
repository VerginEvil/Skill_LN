# chart.add.line.series()

## Syntax:
`#include <bic_dialog>`
`function long chart.add.line.series( long chart, const string title )`

## Description
Create a new serie of type line (CHART_TYPE_LINE). Only to be used if the chart is of type CHART_TYPE_BAR or CHART_TYPE_BARHORIZONTAL. A series is the container for a set of data points which belong together and form a chart.

## Arguments
| | | |
|---|---|---|
| `long` | `chart` |  The identifier of the chart. The identifier must be returned by the function dialog.add.chart().  |
| `const string` | `title` |  Title (label) for this series.  |

## Return values
Series id which must be used in following functions to add data points to this series.
0 in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [chart.add.series()](chart.add.series.md)
- [dialog.add.chart()](dialog.add.chart.md)
- [Programmable dialogs synopsis](synopsis.md)
- [Example chart](examplechart.md)
