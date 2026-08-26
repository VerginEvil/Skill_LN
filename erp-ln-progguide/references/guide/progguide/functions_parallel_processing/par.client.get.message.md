# par.client.get.message()

## Syntax:
`function long par.client.get.message( long group.id, ref string comm.string )`

## Description
This function will check whether a message has been sent by one of the servers in the indicated server group. A server process can send a message back to the client with the function: [par.server.send.message()](par.server.send.message.md). This function will not wait for any messages from a server process.

## Arguments
| | | |
|---|---|---|
| `long` | `group.id` |  ID which is returned by a previous call to [par.init.client.to.server()](par.init.client.to.server.md).  |
| `ref string` | `comm.string` |  Output argument which will contain the message from a server when there is one available.  |

## Return values
| | |
|---|---|
| 0 | When no message is received (so no message was sent by any server) |
| > 0 | Server number from which this message is received. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
