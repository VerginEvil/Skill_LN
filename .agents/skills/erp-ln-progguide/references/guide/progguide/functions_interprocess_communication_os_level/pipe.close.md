# pipe.close()

## Syntax:
`function long pipe.close( long pipe_id )`

## Description
This clears any buffers associated with the specified pipe and closes the file. Buffers allocated by the standard input/output system are also cleared. Note that *pipe.close()* is performed automatically when the process exits.

## Arguments
| | | |
|---|---|---|
| `long` | `pipe_id` |  The pipe ID, as returned by [pipe.open()](pipe.open.md).  |

## Return values
-1: error
-2: child process is not allowed to read/write anymore
>= 0: exit value of child process (0 is OK)

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)

- [Interprocess communication (OS level) synopsis](synopsis.md)
