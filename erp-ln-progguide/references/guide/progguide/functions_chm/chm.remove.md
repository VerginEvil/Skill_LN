# chm.remove()

## Syntax:
`function long chm.remove( string chart_manager(80), string owner_from(14), string ower_to(14) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This removes all charts from the chart list for the specified users. It is not necessary to start the Business Chart Manager in order to use this function.

## Arguments
| | | |
|---|---|---|
| `string` | `chart_manager(80)` |  This specifies the name of a relevant Business Chart Manager application. The name takes the following format: pp package code mmm module code xxx the name of the application  |
| `string` | `owner_from(14)` |  These specify the range of users for whom the charts are to be removed.  |
| `string` | `ower_to(14)` |  |

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
