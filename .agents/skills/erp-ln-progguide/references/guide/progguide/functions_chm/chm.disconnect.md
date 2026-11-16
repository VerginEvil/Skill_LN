# chm.disconnect()

## Syntax:
`function long chm.disconnect( )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This disconnects the Business Chart Manager from the application, enabling independent user interaction. The user can now work with the Chart Manager and modify data, without affecting the data in the application.

## Return values
| | |
|---|---|
| CHM_OK | Success. |
| CHM_ERROR | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [chm.get.request()](chm.get.request.md)

- [Chart manager overview](overview.md)

- [Chart manager synopsis](synopsis.md)

- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)

- [Chart manager example](example.md)
