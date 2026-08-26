# par.init.server.to.client()

## Syntax:
`function boolean par.init.server.to.client( ref long group.number, ref long server.number, [ ref long tot.nr.servers ] )`

## Description
This function is used to initialize the communication to the client. This function must be called rather in the beginning of a program which can be started as server. This because of the fact that the client function has a time out time (default 2 minutes) on starting each server (receiving the 'known' command).

## Arguments
| | | |
|---|---|---|
| `ref long` | `group.number` |  Output argument which will be set to the current group number of which this server will be a member.  |
| `ref long` | `server.number` |  Output argument which will be set to the current server number assigned to this server.  |
| `[ ref long` | `tot.nr.servers ]` |  Output argument which will be set to the total number of servers in this group.  |

## Return values
| | |
|---|---|
| true | When this session is running in parallel processing server mode. |
| false | When this session is not running in parallel processing server mode. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
