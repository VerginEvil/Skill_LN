# par.server.send.message()

## Syntax:
`function boolean par.server.send.message( string comm.string )`

## Description
Send a message to the client. This function will return as soon as the message has been sent.
Note  This function is not intended to send a high volume of messages from the server to the client. This function is also not intended to ask the client for additional information during processing a client message.

## Arguments
| | | |
|---|---|---|
| `string` | `comm.string` |  This string contains the message to be sent to the client. There is no maximum length for this string. The string must contain only textual data (so no binary data like a complete record buffer).  |

## Return values
| | |
|---|---|
| true | when message was sent successfully |
| false | when sending the message failed |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)

- [Parallel Application Processing Examples](examples.md)
