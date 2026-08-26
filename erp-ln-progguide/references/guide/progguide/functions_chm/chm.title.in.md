# chm.title.in()

## Syntax:
`function long chm.title.in( string main_title(80), string sub_title(80) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This function defines a main title and a subtitle for the current chart.

## Arguments
| | | |
|---|---|---|
| `string` | `main_title(80)` |  |
| `string` | `sub_title(80)` |  |

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
