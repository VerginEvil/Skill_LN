# dal.get.first.message()

## Syntax:
`function boolean dal.get.first.message( long i.type, ref string o.code, ref string o.text, [ ref long o.type ] )`

## Description
Returns the code and text of the oldest message of the given type. In case `MSG.ALL` is passed as the type, then the type of the message is returned in the 4th argument.

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

## Example
Suppose you want to retrieve only warning messages from the DAL buffer and write them to a file in FIFO order:
```

string  msg.code(14)
string  msg.text(132) mb

while dal.get.first.message(MSG.WARNING, msg.code, msg.text)
    | Write the message code and text to a file...
    ...
endwhile
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
