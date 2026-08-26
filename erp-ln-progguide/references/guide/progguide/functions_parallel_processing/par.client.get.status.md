# par.client.get.status()

## Syntax:
`function long par.client.get.status( long group.id, long server.number, ref long messages )`

## Description
Returns the current status of the specified server.

## Arguments
| | | |
|---|---|---|
| `long` | `group.id` |  ID which is returned by a previous call to [par.init.client.to.server()](par.init.client.to.server.md).  |
| `long` | `server.number` |  The server number within this group, for which the status is requested. Server numbers start with number 1.  |
| `ref long` | `messages` |  Output argument which contains the number of messages send by this server to the client which should be retrieved by calling [par.client.get.message()](par.client.get.message.md).  |

## Return values
This function returns the current state of this server, which can be one of the following
| | |
|---|---|
| STATE_SRV_CLOSED | Initial state after [par.init.client.to.server()](par.init.client.to.server.md) was called  |
| STATE_SRV_LISTEN | [par.client.start.servers()](par.client.start.servers.md) called, waiting for connect from server  |
| STATE_SRV_KNOWN | Server called: [par.init.server.to.client()](par.init.server.to.client.md) |
| STATE_SRV_IDLE | Server ready to accept a new message and waiting in [par.server.get.message()](par.server.get.message.md) |
| STATE_SRV_PROCESSING | Server busy processing a message. |
| STATE_SRV_QUESTION | Server waiting in function [par.server.question()](par.server.question.md) |
| STATE_SRV_CLOSING | [par.client.close.servers()](par.client.close.servers.md) called, waiting for server to close  |
| STATE_SRV_ERROR | Server in error state |
| -1 | Invalid group id or group already closed |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
