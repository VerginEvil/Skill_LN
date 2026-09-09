# chm.chartman()

## Syntax:
`function long chm.chartman( long chart_manager(80), string title(80), string user(14), string owner(14), [ string version(4), string release(2), string cust(4) ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This starts the Business Chart Manager for a specified Business Chart Manager application, user, owner, and, optionally, VRC code.
Window preferences, fonts, charts, chart types, and option sets are defined by Business Chart Manager application. For a particular application, authorizations, option sets, and window preferences are defined by user (see the Chart Manager Application Data session (ttchm1500m000)). You can also assign the same option set to a group of users. The owner is the creator of the charts; the charts are stored under the owner name (for example, a login name). Users can change only those charts they have created themselves.

## Arguments
| | | |
|---|---|---|
| `long` | `chart_manager(80)` |    |
| `string` | `title(80)` |  This specifies the window title.  |
| `string` | `user(14)` |  This specifies the name of the relevant user.  |
| `string` | `owner(14)` |  This specifies the name of the relevant owner.  |
| `[ string` | `version(4) ]` |  It is possible to assign a VRC code to a chart. These optional arguments specify the relevant VRC codes.  |
| `[ string` | `release(2) ]` |    |
| `[ string` | `cust(4) ]` |    |

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
