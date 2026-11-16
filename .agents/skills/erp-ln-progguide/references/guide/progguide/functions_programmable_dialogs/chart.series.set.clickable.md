# chart.series.set.clickable()

## Syntax:
`#include <bic_dialog>`
`function long chart.series.set.clickable( long series, boolean is.clickable, string seriesname )`

## Description
Sets the series to be clickable or not clickable. Default a series is not clickable. If a series is clickable this is shown in the display of the chart. If the series is set to be clickable, a check will be done on already added datapoints whether a pointid was supplied. If not all datapoints have a pointid, the set to be clickable will not be done.

## Arguments
| | | |
|---|---|---|
| `long` | `series` |  The id returned by the function chart.add.series or function chart.add.line.series.  |
| `boolean` | `is.clickable` |  True: series is clickable, a click will result in a visible action by the script. False: series is not clickable, no linked action.  |
| `string` | `seriesname` |  Name of the series that will be used in the callback function to tell which series has been clicked.  |

## Return values
Return values 0 Success. -1 Failure, probably series identification is not correct. -2 Failure, series is set to clickable while not all already added datapoints have a pointid.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2521.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
