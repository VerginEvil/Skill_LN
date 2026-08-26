# par.server.get.message()

## Syntax:
`function long par.server.get.message( ref string comm.string )`

## Description
This function will inform the client that this server is ready and wait for a new message from the client.

## Arguments
| | | |
|---|---|---|
| `ref string` | `comm.string` |  Output argument which will contain the received message when there is one available.  |

## Return values
| | |
|---|---|
| 1 | a message is available in comm.string |
| 0 | an error occurred |
| -1 | the client called the function [par.client.close.servers()](par.client.close.servers.md) to indicate that all servers should end processing and exit.  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
