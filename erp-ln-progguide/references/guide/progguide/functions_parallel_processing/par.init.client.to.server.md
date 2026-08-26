# par.init.client.to.server()

## Syntax:
`function long par.init.client.to.server( long nr.of.servers, string server.session, [ string support.session ] )`

## Description
This function is used to initialize the client to server communication for one group. Starting the application servers (Bshells) will be done when the function [par.client.start.servers()](par.client.start.servers.md) is called.

## Arguments
| | | |
|---|---|---|
| `long` | `nr.of.servers` |  Specifies the number of servers to be started within this group. If this argument is <= 0, the configured number of servers will be used.  |
| `string` | `server.session` |  Specifies the server session to be started for this group.  |
| `[ string` | `support.session ]` |  Optional argument in which a session name can be passed which is responsible for handling questions from server sessions (see [par.server.question()](par.server.question.md)).  |

## Return values
| | |
|---|---|
| > 0 | The id of the server group |
| < 0 | When parallel processing is not configured for the current session and nr.of.servers is <= 0 |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
