# pipe.read()

## Syntax:
`function long pipe.read( ref string buffer, long nr_of_bytes, long pipe_id )`

## Description
This reads a specified number of bytes from the specified pipe.

## Arguments
| | | |
|---|---|---|
| `ref string` | `buffer` |  This stores the characters read from the pipe.  |
| `long` | `nr_of_bytes` |  This specifies the maximum number of bytes to be read from the pipe. The function stops reading when it has read the number of bytes specified by this argument or when it reaches the end of the file, whichever comes first.  |
| `long` | `pipe_id` |  The pipe ID, as returned by [pipe.open()](pipe.open.md).  |

## Return values
> 0: the number of bytes read
0: end-of-file
-1: error; most probably no connected stream on *pipe_id*

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)

- [Interprocess communication (OS level) synopsis](synopsis.md)
