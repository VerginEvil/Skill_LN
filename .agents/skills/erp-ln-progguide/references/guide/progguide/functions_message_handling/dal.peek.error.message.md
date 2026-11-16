# dal.peek.error.message()

## Syntax:
`function string dal.peek.error.message( long n )`

## Description
This retrieves the DAL message of type `MSG.ERROR` from the message buffer at position n. The message is *not* removed from the buffer.

## Arguments
| | | |
|---|---|---|
| `long` | `n` |    |

## Return values
The message from the message buffer at position *n*, where n = 1 is the oldest message.

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
