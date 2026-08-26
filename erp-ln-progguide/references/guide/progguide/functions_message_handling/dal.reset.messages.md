# dal.reset.messages()

## Syntax:
`function void dal.reset.messages( long i.type, long i.count )`

## Description
Removes the most recent messages of the given type from the DAL message buffer. The 2nd argument determines how many messages will remain in the buffer.

## Arguments
| | | |
|---|---|---|
| `long` | `i.type` |  A message type. Parameter i.type should be one of the following values: `MSG.ALL, MSG.ERROR, MSG.WARNING, MSG.INFO`.  |
| `long` | `i.count` |   |

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and In a not trusted process

## Preconditions

## Examples
```

dal.reset.messages(MSG.WARNING, -4)   | clears the 4 most recent warning messages
dal.reset.messages(MSG.ALL, 2)        | leave only the 2 oldest messages, regardless of type
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
