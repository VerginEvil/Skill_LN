# par.client.close.servers()

## Syntax:
`function boolean par.client.close.servers( long group.id )`

## Description
This function will close all servers in a group. Normally this call should only be done when all servers are ready, so after a call to [par.client.wait.ready()](par.client.wait.ready.md). Closing the servers means that the application servers will terminate.

## Arguments
| | | |
|---|---|---|
| `long` | `group.id` |  ID which is returned by a previous call to [par.init.client.to.server()](par.init.client.to.server.md).  |

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
