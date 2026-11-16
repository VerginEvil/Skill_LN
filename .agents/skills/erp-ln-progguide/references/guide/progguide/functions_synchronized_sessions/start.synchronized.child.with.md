# start.synchronized.child.with()

## Syntax:
`function long start.synchronized.child.with( const long cmd )`

## Description
To start a synchronized child with a command other than the default synchronization command, call this function before calling [start.synchronized.child()](start.synchronized.child.md).
Although you normally use this function to synchronize sessions that act on different main tables, it is also possible to use it to synchronize sessions that act on the same main table.

## Arguments
| | | |
|---|---|---|
| `const long` | `cmd` |  This specifies the ID of the required command that is executed immediately after startup. Possible values are [FIRST.SET](../4gl_features/4gl_choice_sections.md), [FIND.DATA](../4gl_features/4gl_choice_sections.md) and [ADD.SET](../4gl_features/4gl_choice_sections.md).  |

## Return values
The function returns the specified command or 0 if the command is illegal.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  The specified command is *not* reset after the next synchronized child is started. To reset the synchronization command, call this function with command 0 (after the child was started).

## Related help topics
- [Synchronized sessions overview](overview.md)

- [Synchronized sessions synopsis](synopsis.md)

- [Child synchronization sample program](example.md)
