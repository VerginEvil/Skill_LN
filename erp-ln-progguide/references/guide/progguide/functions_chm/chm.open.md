# chm.open()

## Syntax:
`function long chm.open( string chart_name(16) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This opens the specified chart with its associated data.

## Arguments
| | | |
|---|---|---|
| `string` | `chart_name(16)` |    |

## Return values
| | |
|---|---|
| > 0 | The ID of the opened chart. |
| CHM_ERROR | Error. The Business Chart Manager cannot find or cannot open the specified chart |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)

- [Chart manager synopsis](synopsis.md)

- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)

- [Chart manager example](example.md)
