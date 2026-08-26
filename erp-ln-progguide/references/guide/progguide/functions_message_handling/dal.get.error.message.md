# dal.get.error.message()

## Syntax:
`function long dal.get.error.message( ref string mesg )`

## Description
This retrieves the most recent DAL message of type `MSG.ERROR` from the message buffer. The message is removed from the buffer.

## Arguments
| | | |
|---|---|---|
| `ref string` | `mesg` |  |

## Return values
The number of error messages that remain in the message buffer, or -1 if the buffer is empty. (In the latter case the returned message is "".)

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and In a not trusted process

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
