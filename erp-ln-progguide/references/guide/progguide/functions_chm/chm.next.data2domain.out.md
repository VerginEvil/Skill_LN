# chm.next.data2domain.out()

## Syntax:
`function long chm.next.data2domain.out( ref double series_value )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
You use [chm.first.data2domain.out()](chm.first.data2domain.out.md) to retrieve the sequence number of the first graph series that is linked to the second data domain of the current chart. You use *chm.next.data2domain.out()* to retrieve the sequence number of the next graph series that is linked to the second data domain of the same chart. To retrieve information about all subsequent graph series that are linked to the second domain, you can place this function in a loop that executes as long as the return value is CHM_OK.
If the client application modifies the information and saves it to the source table or file, the new information is included the next time the chart is started.

## Arguments
| | | |
|---|---|---|
| `ref double` | `series_value` |    |

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
