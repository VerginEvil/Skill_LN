# pipe.error()

## Syntax:
`function long pipe.error( long pipe_id )`

## Description
This checks the error indicator on the specified pipe to determine whether an error has occurred when reading or writing to the pipe. Note that the error indicator lasts until the pipe is closed, unless you explicitly clear it by calling [pipe.clearerr()](pipe.clearerr.md).

## Arguments
| | | |
|---|---|---|
| `long` | `pipe_id` |  The pipe ID, as returned by [pipe.open()](pipe.open.md).  |

## Return values
<> 0: error has occurred when reading or writing to the pipe
0: no error has occurred

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)

- [Interprocess communication (OS level) synopsis](synopsis.md)
