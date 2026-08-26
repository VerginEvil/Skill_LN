# dal.set.message()

## Syntax:
`function void dal.set.message( long i.type, const string i.mess.or.code, [ void arg ... ] )`

## Description
Adds a message of the specified type to the DAL message buffer.

## Arguments
| | | |
|---|---|---|
| `long` | `i.type` |  A message type. Parameter i.type should be one of the following values: `MSG.ERROR, MSG.WARNING, MSG.INFO`.  |
| `const string` | `i.mess.or.code` |  Specifies either the data dictionary code for the message or a literal string. In the latter case, the value of *i.mess.or.code* must start with the at sign [@]. Note that using a literal string makes the script language dependent.  |
| `[ void` | `arg ... ]` |  The literal string or message specified with *i.mess.or.code* can contain format characters for parameter substitution. The values which must be substituted are specified in the 2nd, 3rd, ... arguments of the function. The number of these arguments is variable. For details about formatting a string see the [sprintf$()](../functions_formatting_io/sprintf.md).  |

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.
Note  Empty messages are not added to the DAL message buffer.
The message is not added to the DAL message buffer if messages are disabled by using [dal.set.messages.off()](dal.set.messages.off.md) and the message has type MSG.ERROR.

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
