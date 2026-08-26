# chart.add.series()

## Syntax:
`#include <bic_dialog>`
`function long chart.add.series( long chart, const string title )`

## Description
Create a new series. A series is the container for a set of data points which belong together and form a chart. For a chart of type CHART_PIE exactly one series must be defined. For then other chart types one or more series can be added.Set the chart title and optionally the sub-title.

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
- [dialog.add.chart()](dialog.add.chart.md)
- [Programmable dialogs synopsis](synopsis.md)
- [Example chart](examplechart.md)
