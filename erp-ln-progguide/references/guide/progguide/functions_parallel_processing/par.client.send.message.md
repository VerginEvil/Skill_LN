# par.client.send.message()

## Syntax:
`function boolean par.client.send.message( long group.id, [ string comm.string, long server.number ] )`

## Description
Send a message to the indicated group or application server. When a server.number is passed, the message is sent to that particular server. Otherwise the message is sent to the first server in the group which is ready. This function will wait until the message has been sent to a server. This does however not mean that the message is already processed by this server when this function returns.
When not in CONTINUE_ON_SERVER_ERRORS mode, this function will return false when one or more servers are in error state. When in CONTINUE_ON_SERVER_ERRORS mode the following rules are applied:
- When a specific server.number is supplied and this particular server is in an error state, this function will return false.
- When no server.number is supplied this function will return true as long as there is one server available to which this message can be sent.

## Arguments
| | | |
|---|---|---|
| `long` | `group.id` |  ID which is returned by a previous call to [par.init.client.to.server()](par.init.client.to.server.md).  |
| `[ string` | `comm.string ]` |  This string contains the message to be sent to the server. There is no maximum length for this string. The string must contain only textual data (so no binary data like a complete record buffer).  |
| `[ long` | `server.number ]` |  Optional argument which can be used to send a message to a specific server within a group. Server numbers start with number 1  |

## Return values
| | |
|---|---|
| true | When message was sent successfully |
| false | When sending the message failed |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
