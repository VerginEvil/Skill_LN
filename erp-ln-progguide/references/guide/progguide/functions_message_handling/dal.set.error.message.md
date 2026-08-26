# dal.set.error.message(), dal.set.warning.message(), dal.set.info.message()

## Syntax:
`function void dal.set.error.message( string mess.or.code, [ void arg ... ] )`
`function void dal.set.warning.message( string mess.or.code, [ void arg ... ] )`
`function void dal.set.info.message( string mess.or.code, [ void arg ... ] )`

## Description
These functions add a message to the DAL message buffer of type `MSG.ERROR`, `MSG.WARNING`, or `MSG.INFO`.
They are short versions for function [dal.set.message()](dal.set.message.md).

## Arguments
| | | |
|---|---|---|
| `string` | `mess.or.code` |  Specifies either the data dictionary code for the message or a literal string. In the latter case, the value of *mess.or.code* must start with the at sign [@]. Note that using a literal string makes the script language dependent.  |
| `[ void` | `arg ... ]` |  The literal string or message specified with *mess.or.code* can contain format characters for parameter substitution. The values which must be substituted are specified in the 2nd, 3rd, ... arguments of the function. The number of these arguments is variable. For details about formatting a string see the [sprintf$()](../functions_formatting_io/sprintf.md).  |

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.
Note  Empty messages are not added to the DAL message buffer.
For dal.set.error.message(), the message is not added to the DAL message buffer if messages are disabled by using [dal.set.messages.off()](dal.set.messages.off.md).

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
