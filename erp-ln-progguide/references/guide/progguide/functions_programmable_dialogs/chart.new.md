# chart.new()

## Syntax:
`#include <bic_dialog>`
`function long chart.new( long type, [ long width, long height ] )`

## Description
Creates a new chart.
Note that this function only effects the *LN UI* User Interface.
Note that this function can only be used for fields of type *Picture in a Session Extension or in the callback function for a Graph field.*
Chart data is set using the other chart functions.

## Arguments
| | | |
|---|---|---|
| `long` | `type` |  Type of the chart. Supported types: CHART_TYPE_BAR, CHART_TYPE_BARHORIZONTAL, CHART_TYPE_LINE, CHART_TYPE_LINE_STAIR, CHART_TYPE_PIE, CHART_TYPE_AREA, CHART_TYPE_STACKEDBAR  |
| `[ long` | `width ]` |  Width of the graph in pixels. Default is 300. Dependent of the sizes defined for the graph on the form and the shape of the graph (a square, or wider than high, or higher than wide) the sizes can be adjusted to optimize the visual quality.  |
| `[ long` | `height ]` |  Height of the chart in pixels. Default is 300. Dependent of the sizes defined for the graph on the form and the shape of the graph (a square, or wider than high, or higher than wide) the sizes can be adjusted to optimize the visual quality.  |

## Return values
The id of the created chart. This id identifies the chart in further dialog calls. It is the id of an XML document that can be debugged during the whole process.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2320.

## Related topics
- [chart.write()](chart.write.md)

- [chart.delete()](chart.delete.md)

- [chart.set.title()](chart.set.title.md)

- [chart.set.axis.type()](chart.set.axis.type.md)

- [chart.set.axis.title()](chart.set.axis.title.md)

- [chart.add.series()](chart.add.series.md)

- [chart.add.data.point()](chart.add.data.point.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
