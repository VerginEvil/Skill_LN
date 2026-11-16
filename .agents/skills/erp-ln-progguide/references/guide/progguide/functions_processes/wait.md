# wait()

## Syntax:
`function string wait( ref long process_id, long option )`

## Description
This waits for one or all child processes to exit.

## Arguments
| | | |
|---|---|---|
| `ref long` | `process_id` |  This returns the process number of the child process that exited. If no child exited, it returns 0. If there are no child processes, or if all child processes were already ended before the function was called, it returns -1.  |
| `long` | `option` |  This can have one of the following values: WTHANG If the parent process ignores child signals (see [signal()](signal.md)), the function waits until all children have exited. The process_id argument returns the process ID of the last child process to exit. If the parent process does not ignore child signals (see [signal()](signal.md)), the function waits until one child exits. The process_id argument returns the process ID of that child process. WTNOHANG If the parent process ignores child signals (see [signal()](signal.md)), the function does not block. If one or more child processes have previously exited and are in a zombie state, the process_id argument returns the process of the last child process that exited. If the parent process does not ignore child signals (see [signal()](signal.md)), the function waits until one child exits. The process_id argument returns the process ID of that child process.  |

## Return values
The exit value of the child process identified by the *process_id* argument.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
