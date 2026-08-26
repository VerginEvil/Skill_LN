# chm.first.data.out()

## Syntax:
`function long chm.first.data.out( long option, ref double series_value, ref double category_value, ref long data_number, ref double data_value, ref long footnote_no )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
*This retrieves information from the Business Chart Manager about the first data point in the current chart. If the client application modifies the information and saves it to the source table or file, the new information is included the next time the chart is started.*
Use [chm.next.data.out()](chm.next.data.out.md) to retrieve information about the next and subsequent data points.

## Arguments
| | | |
|---|---|---|
| `long` | `option` |  Use this argument to indicate whether the function retrieves data for the absolute first data point or for the first data point that has been modified. The possible values are: CHM_ALL_DATA CHM_CHANGED_DATA  |
| `ref double` | `series_value` |  This returns the series to which the data point belongs.  |
| `ref double` | `category_value` |  This returns the category to which the data point belongs.  |
| `ref long` | `data_number` |  If there is more than one data point per category (a high-low graph, for example), this returns the sequence number of the data point within the category. If there is only one data point per category, the sequence number is 1.  |
| `ref double` | `data_value` |  This returns the value of the data point.  |
| `ref long` | `footnote_no` |  This returns the number of the footnote (if any) associated with the data point.  |

## Return values
| | |
|---|---|
| CHM_OK | Success. |
| CHM_ERROR | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)
- [Chart manager synopsis](synopsis.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
