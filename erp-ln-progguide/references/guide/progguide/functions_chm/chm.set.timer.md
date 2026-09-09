# chm.set.timer()

## Syntax:
`function long chm.set.timer( long time )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This starts a timer. The Business Chart Manager sends a CHM_TIMER signal to the application every specified number of milliseconds. When the application retrieves the signal, it can perform appropriate actions (see [chm.get.request()](chm.get.request.md)). You can turn off the timer by calling *chm.set.timer()* with a time of zero.

## Arguments
| | | |
|---|---|---|
| `long` | `time` |    |

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
