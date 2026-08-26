# chm.set.option()

## Syntax:
`function long chm.set.option( long option, long flag )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use this to switch an application option on and off. Applications options are defined in the Applications Options session (ttchm1120s000). Actions can be linked to an application option using the [chm.get.request()](chm.get.request.md) function

## Arguments
| | | |
|---|---|---|
| `long` | `option` |  The option that must be switched on or off.  |
| `long` | `flag` |  This specifies whether the option is be switched on or off. The possible values are: true: option enabled false: option disabled  |

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
