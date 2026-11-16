# sleep()

## Syntax:
`function void sleep( long processno )`

## Description
This suspends execution of the specified process and places it in the sleeping process queue. To suspend execution of the your own process, specify the predefined variable *pid* in the argument.
Use [reactivate()](reactivate.md) to activate a sleeping process. When a child process of a sleeping parent process exits, the parent process wakens automatically. When the last process is put in a sleeping state, the program automatically stops.

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Do not confuse this function with the UNIX *sleep* command. The latter suspends a process for a specified amount of time. In Infor Enterprise Server scripts, you use [suspend()](suspend.md) to do this.

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
