# chart.datapoint.add.tooltipline()

## Syntax:
`function long chart.datapoint.add.tooltipline( long series, const string pointid, const string tooltip )`

## Description
This function adds a tooltip line to the datapoint. LN UI will display each line as a separate line below each other. If the chart is of type pie, the tooltip is only added to the series. This function will return an error if called while the chart is of type pie.

## Arguments
| | | |
|---|---|---|
| `long` | `series` |  The id returned by the function chart.add.series or chart.add.line.series.  |
| `const string` | `pointid` |  The pointid given when the datapoint was added to the chart by function chart.add.data.point.  |
| `const string` | `tooltip` |  A tooltip description. Multiple added lines are displayed as separate lines by LN UI.  |

## Return values
| | |
|---|---|
| 0 | Success |
| -1 | Failure, probably series identification is not correct. |
| -2 | Failure, datapoint with the argument pointid not found. |
| -3 | Failure, chart is of type pie, not allowed to add a tooltip on a datapoint. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
