# dialog.add.chart()

## Syntax:
`#include <bic_dialog>`
`function long dialog.add.chart( long dlg, long initial.type, [ long allowed.types ] )`

## Description
Note that this function only effects the *WebUI and LN UI* User Interface.
Add a chart to the indicated dialog. Chart data and other attributes must be set using other chart functions. The initial chart type is set with argument initial.type. The user can modify this type when the dialog is shown. Below an illustration of each supported type is given.

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `long` | `initial.type` |  Initial type of the chart. Supported types: CHART_TYPE_BAR, CHART_TYPE_BARHORIZONTAL, CHART_TYPE_LINE, CHART_TYPE_LINE_STAIR, CHART_TYPE_LINE_SPLINE, CHART_TYPE_LINE_SCATTER, CHART_TYPE_PIE, CHART_TYPE_AREA.  |
| `[ long` | `allowed.types ]` |  Chart types from which the user might choose at runtime. Value is the sum of the supported type values (e.g. CHART_TYPE_BAR + CHART_TYPE_LINE).  |

## Return values
This function returns a chart id which must be used in further chart calls. In case of an error the value 0 is returned.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [chart.set.title()](chart.set.title.md)

- [chart.set.axis.type()](chart.set.axis.type.md)

- [chart.set.axis.title()](chart.set.axis.title.md)

- [chart.add.series()](chart.add.series.md)

- [chart.add.data.point()](chart.add.data.point.md)

- [chart.clear.data()](chart.clear.data.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
