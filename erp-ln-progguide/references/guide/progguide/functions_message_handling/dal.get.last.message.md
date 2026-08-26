# dal.get.last.message()

## Syntax:
`function boolean dal.get.last.message( long i.type, ref string o.code, ref string o.text, [ ref long o.type ] )`

## Description
Returns the code and text of the most recent message of the given type. In case `MSG.ALL` is passed as the type, then the type of the message is returned in the 4th argument. The message is removed from the buffer.

## Arguments
| | | |
|---|---|---|
| `long` | `i.type` |  A message type. Parameter i.type should be one of the following values: `MSG.ALL, MSG.ERROR, MSG.WARNING, MSG.INFO`.  |
| `ref string` | `o.code` |  The returned code of the message.  |
| `ref string` | `o.text` |  The returned text of the message.  |
| `[ ref long` | `o.type ]` |  Optional, the returned type of the message, in case `MSG.ALL` was passed as the first argument.  |

## Return values
This function returns TRUE if a message could be retrieved, else FALSE is returned.

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and In a not trusted process

## Example
Suppose you want to retrieve all messages from the DAL buffer and write them to a file in LIFO order:
```

string  msg.code(14)
string  msg.text(132) mb
long    msg.type

while dal.get.last.message(MSG.ALL, msg.code, msg.text, msg.type)
    | Write the message code, text and type to the file ...
    ...
endwhile
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
