# pipe.gets()

## Syntax:
`function long pipe.gets( ref string line, long nr_of_bytes, long pipe_id )`

## Description
This reads a maximum of one line from the specified pipe.

## Arguments
| | | |
|---|---|---|
| `ref string` | `line` |  This stores the characters read from the pipe.  |
| `long` | `nr_of_bytes` |  This specifies the maximum number of bytes to be read from the pipe. The function stops reading when it encounters a newline character or when it has read the number of bytes specified by this argument, whichever comes first.  |
| `long` | `pipe_id` |  The pipe ID, as returned by [pipe.open()](pipe.open.md).  |

## Return values
0: success
-1: error; most probably no connected stream on *pipe_id*

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)
- [Interprocess communication (OS level) synopsis](synopsis.md)
