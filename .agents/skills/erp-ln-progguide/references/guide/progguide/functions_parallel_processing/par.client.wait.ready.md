# par.client.wait.ready()

## Syntax:
`function boolean par.client.wait.ready( [ long group.id, long server.number ] )`

## Description
This function will wait until servers are ready with processing messages. When no group.id and no server.number are specified, this function will wait for all servers in all groups to become ready. When only a group.id is specified, this function will wait for all servers in the specified group to become ready. When both a group.id and a server.number is specified, this function will wait for one specific server to become ready.
When not in CONTINUE_ON_SERVER_ERRORS mode (this can be specified in [par.client.start.servers()](par.client.start.servers.md)), this function will return false when one or more servers are in error state. When in CONTINUE_ON_SERVER_ERRORS mode the following rules are applied:

- When a specific server.number is supplied and this particular server is in an error state, this function will return false.

- When no server.number is supplied this function will return true as long as there is one server available to which messages can be sent.

## Arguments
| | | |
|---|---|---|
| `[ long` | `group.id ]` |  ID which is returned by a previous call to [par.init.client.to.server()](par.init.client.to.server.md).  |
| `[ long` | `server.number ]` |  The server number within this group. Server numbers start with number 1.  |

## Return values
| | |
|---|---|
| true | When successful |
| false | When an error occurred |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)

- [Parallel Application Processing Examples](examples.md)
