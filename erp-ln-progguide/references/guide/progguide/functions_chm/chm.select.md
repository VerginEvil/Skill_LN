# chm.select()

## Syntax:
`function long chm.select( string chart_manager(80), string title(80), long mode, string user(14), string owner(14), ref string chart_name(16), ref string chart_type(16) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This starts a session in which the user can select or create another chart or chart type. It is not necessary to start the Business Chart Manager in order to use this function.

## Arguments
| | | |
|---|---|---|
| `string` | `chart_manager(80)` |  This specifies the name of a Business Chart Manager application. This corresponds to a particular record in the Chart Manager application data session (ttchm1500m000). The name takes the following format: pp package code mmm module code xxx the name of the application  |
| `string` | `title(80)` |  This specifies the window title.  |
| `long` | `mode` |  This specifies whether the session enables selection or creation of a chart or chart type. The possible values are: CHM_SELECT_CHARTTYPE select another chart type CHM_CREATE_CHART create another chart CHM_SELECT_CHART select another chart CHM_CREATESELECT_CHART create or select another chart  |
| `string` | `user(14)` |  This specifies the name of the user. The session is started with this user's option set.  |
| `string` | `owner(14)` |  This specifies the name of the relevant owner. When a list of charts is called, the system displays the charts that this user owns.  |
| `ref string` | `chart_name(16)` |  This returns the name of the selected chart.  |
| `ref string` | `chart_type(16)` |  This returns the type of the selected chart.  |

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
