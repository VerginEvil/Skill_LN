# chm.data2domain.in()

## Syntax:
`function long chm.data2domain.in( double series_value )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Data domain II defines the start value, end value, and step size for the data II axis. You use the second data domain and axis when you want to draw two different series to different scales in order to facilitate comparison. You use [chm.domain.in()](chm.domain.in.md) to define a domain. You use this function to specify which series uses the second data domain. By default, the other series uses the normal data domain.

## Arguments
| | | |
|---|---|---|
| `double` | `series_value` |    |

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
