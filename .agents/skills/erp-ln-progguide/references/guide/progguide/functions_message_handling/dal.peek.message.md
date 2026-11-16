# dal.peek.message()

## Syntax:
`function void dal.peek.message( long i.type, long i.index, ref string o.code, ref string o.text, [ ref long o.type ] )`

## Description
Returns the code and text of the message of the specified type that is located at the given index in the message buffer. In case you specify `MSG.ALL` as the type, the type of the message is returned in the 5th argument.

## Arguments
| | | |
|---|---|---|
| `long` | `i.type` |  A message type. Parameter i.type should be one of the following values: `MSG.ALL, MSG.ERROR, MSG.WARNING, MSG.INFO`.  |
| `long` | `i.index` |  The position of the message in the buffer.  |
| `ref string` | `o.code` |  The returned code of the message.  |
| `ref string` | `o.text` |  The returned text of the message.  |
| `[ ref long` | `o.type ]` |  Optional, the returned type of the message, in case `MSG.ALL` was passed as the first argument.  |

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.

- The message is *not* removed from the buffer.

- In case an invalid index is passed, empty strings will be returned in the code and text arguments and `MSG.ALL` is returned in the 5th argument.

## Example
Suppose you want to write all DAL messages to a file without removing them from the DAL message buffer:
```

string  msg.code(14)
string  msg.text(132) mb
long    msg.type
long    i
long    num.messages

num.messages = dal.count.messages(MSG.ALL)

for i = 1 to num.messages
    dal.peek.message(MSG.ALL, i, msg.code, msg.text, msg.type)
    | Write the message code, text and type to a file...
    ...
endfor
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
