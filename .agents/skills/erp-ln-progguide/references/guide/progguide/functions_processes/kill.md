# kill()

## Syntax:
`function void kill( long processno )`

## Description
This deletes the specified process from the bshell process queue. If the process is in a running state, it is interrupted.

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |    |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2120 and The process to kill should be a not trusted process

Notes  Do not confuse this function with the *kill* command of the operating system. You can use *kill()* to kill process within the same bshell only. You cannot use it to kill the processes of other users.
If you kill a child process while the parent process is sleeping, the parent process is automatically wakened, provided that both processes are in the same process group.

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
