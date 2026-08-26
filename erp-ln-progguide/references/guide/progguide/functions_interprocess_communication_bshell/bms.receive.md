# bms.receive$()

## Syntax:
`function string bms.receive$( [ ref long level, long wait.flag, ref string mask ] )`

## Description
Use this to receive a broadcast message. If no arguments are included, the function returns the first broadcast message sent to the process.

## Arguments
| | | |
|---|---|---|
| `[ ref long` | `level ]` |  This optional argument specifies a message level. The following values are available: 0: the function returns the first broadcast message sent to the process > 0: the function returns the first broadcast message sent with the specified level < 0: the function returns the first broadcast message sent with a level less than or equal to the absolute value of the specified level This argument returns the process ID of the sending process. The process ID overwrites the specified level.  |
| `[ long` | `wait.flag ]` |  This optional argument indicates whether the process must wait for a broadcast message if no message has yet been sent: 0: wait <> 0: do not wait If you include this argument, you must also include the *level* argument.  |
| `[ ref string` | `mask ]` |  This optional argument returns the mask (if any) sent with the message.  |

## Return values
The received broadcast message.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Interprocess communication (OS level) overview](../functions_interprocess_communication_os_level/overview.md)
- [Interprocess communication (bshell) overview](overview.md)
- [Interprocess communication (bshell) synopsis](synopsis.md)
