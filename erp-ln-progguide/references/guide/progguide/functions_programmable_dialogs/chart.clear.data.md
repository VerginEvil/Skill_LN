# chart.clear.data()

## Syntax:
`#include <bic_dialog>`
`function long chart.clear.data( long chart )`

## Description
Remove all series including its datapoints for the indicated chart. This function is typically used in a callback function before new series and datapoints are added.

## Arguments
| | | |
|---|---|---|
| `long` | `chart` |  The identifier of the chart. The identifier must be returned by the function dialog.add.chart().  |

## Return values
0 in case of success.
-1 in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [dialog.add.chart()](dialog.add.chart.md)
- [Programmable dialogs synopsis](synopsis.md)
- [Example chart](examplechart.md)
