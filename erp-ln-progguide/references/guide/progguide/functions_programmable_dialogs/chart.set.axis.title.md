# chart.set.axis.title()

## Syntax:
`#include <bic_dialog>`
`function long chart.set.axis.title( long chart, long axis, const string title )`

## Description
Set the title for the indicated axis.

## Arguments
| | | |
|---|---|---|
| `long` | `chart` |  The identifier of the chart. The identifier must be returned by the function dialog.add.chart().  |
| `long` | `axis` |  Identifies the axis for which the type must be set: CHART_XAXIS, CHART_YAXIS.  |
| `const string` | `title` |  The title set for the indicated axis.  |

## Return values
0 in case of success.
-1 in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [dialog.add.chart()](dialog.add.chart.md)
- [Programmable dialogs synopsis](synopsis.md)
- [Example chart](examplechart.md)
