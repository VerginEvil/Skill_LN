# dal.reset.error.messages()

## Syntax:
`function void dal.reset.error.messages( long amt )`

## Description
This clears the most recent DAL messages of type `MSG.ERROR` from the message buffer.

## Arguments
| | | |
|---|---|---|
| `long` | `amt` |  0: clear the entire buffer > 0: leave the specified number of oldest messages in the buffer; the rest are cleared. < 0: clear the specified number of the most recent messages (the absolute value of *amt* is used).  |

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2120 and In a not trusted process

## Examples
If there are 6 error messages in the message buffer, the following examples have the same result:
```

dal.reset.error.messages(-4)    | clears the 4 most recent error messages
dal.reset.error.messages(2)     | leave only the 2 oldest error messages
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
