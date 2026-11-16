# chart.set.title()

## Syntax:
`#include <bic_dialog>`
`function long chart.set.title( long chart, const string title, [ const string subtitle ] )`

## Description
Set the chart title and optionally the sub-title.

## Arguments
| | | |
|---|---|---|
| `long` | `chart` |  The identifier of the chart. The identifier must be returned by the function dialog.add.chart().  |
| `const string` | `title` |  The chart title which will be shown in the chart area. Note that this might differ from the dialog title, which will be shown in the dialog caption (title bar).  |
| `[ const string` | `subtitle ]` |  Optional chart sub-title which will be shown in the chart area.  |

## Return values
0 in case of success.
-1 in case of an error.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [dialog.add.chart()](dialog.add.chart.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
