# act.and.sleep()

## Syntax:
`function long act.and.sleep( string procname(.), [ string arg1, arg2,... ] )`

## Description
This activates the specified process and places it in the sleeping process queue. It remains there until it is activated by calling the [reactivate()](reactivate.md) function. You can remove the process with the [kill()](kill.md) function. The process is automatically removed when the process group to which it belongs is killed.

## Arguments
| | | |
|---|---|---|
| `string` | `procname(.)` |  The process to be activated. The argument can contain a session name (4GL programs) or the name of an object file (3GL programs).  |
| `[ string` | `arg1, arg2,... ]` |  Use these optional arguments to pass arguments to the new process. The arguments are always converted to strings. The new process can access these arguments with the [argv$()](argv.md) function.  |

## Return values
| | |
|---|---|
| 0 | Error, process cannot be activated. |
| > 0 and < 2^31 | Process ID of activated process. This is a value in the positive part of the signed 32-bit range: [1 … 2^31 - 1] (i.e. [1 … 2,147,483,647]). |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2120 and Value of argument procname starts with "tx" or "otx"

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
