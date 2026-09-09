# chm.data.in()

## Syntax:
`function long chm.data.in( double series_value, double category_value, long data_number, double data_value, long footnote_no, [ long duplicate_option ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This sends a data point to the Business Chart Manager. You must call this function for each data point that you want to send.

## Arguments
| | | |
|---|---|---|
| `double` | `series_value` |  This specifies the series to which the data point belongs.  |
| `double` | `category_value` |  This specifies the category to which the data point belongs.  |
| `long` | `data_number` |  If there is more than one data point per category (a high-low graph, for example), this indicates the sequence number of the data point within the category. If there is only one data point per category, the sequence number is 1.  |
| `double` | `data_value` |  The data value for the specified series and category. The data value must lie within the scope of the data domain.  |
| `long` | `footnote_no` |  If you want to include a footnote for the data point, specify the number of the footnote here. Use [chm.footnote.in()](chm.footnote.in.md) to create the footnote  |
| `[ long` | `duplicate_option ]` |    |

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
