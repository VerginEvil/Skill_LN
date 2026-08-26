# par.server.question()

## Syntax:
`function boolean par.server.question( string question, ref string answer )`

## Description
This function can be used by a server session to send a question message to the "support" session in the client. The "support" session in the client must use function [par.support.get.question()](par.support.get.question.md) to receive questions from server processes and function [par.support.send.answer()](par.support.send.answer.md) to send an answer message to the server. The function par.server.question() waits until an answer message is received from the "support" session.

## Arguments
| | | |
|---|---|---|
| `string` | `question` |  This string contains the message (question) to be sent to the support session. There is no maximum length for this string  |
| `ref string` | `answer` |  Output argument which will contain the answer returned by the support session  |

## Return values
| | |
|---|---|
| true | when an answer is returned by the support session |
| false | when an error occurred |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
