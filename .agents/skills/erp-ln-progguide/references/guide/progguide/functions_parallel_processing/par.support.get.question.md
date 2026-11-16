# par.support.get.question()

## Syntax:
`function long par.support.get.question( ref string question )`

## Description
This function will wait for a question message from any server. When this function returns -1, the support session must end processing and exit.

## Arguments
| | | |
|---|---|---|
| `ref string` | `question` |  Output argument which will contain the question message from a server when there is one available.  |

## Return values
| | |
|---|---|
| > 0 | The server number which has sent the question string |
| -1 | The client called the function [par.client.close.servers()](par.client.close.servers.md) to indicate that all servers (and support sessions) should end processing and exit. |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)

- [Parallel Application Processing Examples](examples.md)
