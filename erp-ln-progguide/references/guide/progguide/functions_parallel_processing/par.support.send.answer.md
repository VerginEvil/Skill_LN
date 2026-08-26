# par.support.send.answer()

## Syntax:
`function boolean par.support.send.answer( string answer, long server.number )`

## Description
Send an answer message to a server session. This function will return as soon as the message has been sent.
Note  This function should only be used after a successful call of function: [par.support.get.question()](par.support.get.question.md)

## Arguments
| | | |
|---|---|---|
| `string` | `answer` |  This string contains the answer message to be sent to the server session. There is no maximum length for this string.  |
| `long` | `server.number` |  Indicates the server to which this answer must be sent. This must be the return value of a previous call to [par.support.get.question()](par.support.get.question.md).  |

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
