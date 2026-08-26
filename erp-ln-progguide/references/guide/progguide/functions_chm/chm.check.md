# chm.check()

## Syntax:
`function long chm.check( sting chart_manager(14), string user(14), string chart_type(16) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This checks whether a specified user can access a particular chart type within a specified Business Chart Manager application.

## Arguments
| | | |
|---|---|---|
| `sting` | `chart_manager(14)` |  |
| `string` | `user(14)` |  The user name.  |
| `string` | `chart_type(16)` |  The chart type.  |

## Return values
| | |
|---|---|
| true | The user can select the specified chart type. |
| false | The user cannot select the specified chart type |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)
- [Chart manager synopsis](synopsis.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
