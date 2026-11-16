# signal()

## Syntax:
`function void signal( long type, long action )`

## Description
This specifies whether the process in which it is called ignores child process signals or not.

## Arguments
| | | |
|---|---|---|
| `long` | `type` |  The signal type. Currently there is only one value for this argument: SIGCHLD Sent by a child process to its parent process when the child process exits.  |
| `long` | `action` |  SIGIGN Ignore signals. The child exits without any action by the parent. The child exits, sends an exit signal to its parent, and is removed. This is the default action. SIGNOIGN Do not ignore signals. The child exits and waits until its parent catches its exit signal. The parent catches the signal with the [wait()](wait.md) function. While the child process is waiting, it is a zombie process.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
