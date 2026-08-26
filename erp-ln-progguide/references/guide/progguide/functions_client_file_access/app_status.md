# app_status()

## Syntax:
`function long app_status( long app.id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use function: [start.application.local()](start.application.local.md).
This retrieves information about a specified application.

## Arguments
| | | |
|---|---|---|
| `long` | `app.id` |  The ID of the application for which you want to retrieve information, as returned by [app_start()](app_start.md).  |

## Return values
| | |
|---|---|
| <> 0 | Application is running. |
| 0 | Error. Application is not running – probably crashed after activating. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
