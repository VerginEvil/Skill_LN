# chm.title.out()

## Syntax:
`function long chm.title.out( ref string main_title(), ref string sub_title() )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves the main title and subtitle of the current chart. If the client application modifies the information and saves it to the source table or file, the new information is included the next time the chart is started.

## Arguments
| | | |
|---|---|---|
| `ref string` | `main_title()` |  |
| `ref string` | `sub_title()` |  |

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
