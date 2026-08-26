# wait.and.activate()

## Syntax:
`function long wait.and.activate( string procname(.), [ long arg1, arg2, ... ] )`

## Description
This activates the specified program. The calling program is put in a waiting state. Because the calling program has not ended, it retains all its values.
In the called program, the predefined variable *background* is set to 1. By testing this variable, the program can check whether it is running as a foreground or background process. If required, the functioning of the program can be made dependent on this.
When the called program ends, the calling program is fetched from the waiting state and reactivated, starting from the statement immediately following the *wait.and.activate()* call. Note that this happens only when the two processes belong to the same process group.

## Arguments
| | | |
|---|---|---|
| `string` | `procname(.)` |  The process to be activated. The argument can contain a session name (4GL programs) or the name of an object file (3GL programs).  |
| `[ long` | `arg1, arg2, ... ]` |  Use these optional arguments to pass arguments to the new process. The arguments are always converted to strings. The new process can access these arguments with the [argv$()](argv.md) function.  |

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
