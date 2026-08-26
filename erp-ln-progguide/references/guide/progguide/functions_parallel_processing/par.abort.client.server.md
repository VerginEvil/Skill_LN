# par.abort.client.server()

## Syntax:
`function void par.abort.client.server( string error.message )`

## Description
This function can be used in the client as well in the server. When there are (application) problems in the client or server, an abort message will be sent to the client and all servers. After this function call, all servers are stopped and all communication will be ended.

## Arguments
| | | |
|---|---|---|
| `string` | `error.message` |  This string contains the message which will be logged in the error log.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
