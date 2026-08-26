# pipe.puts()

## Syntax:
`function long pipe.puts( string line, long pipe_id )`

## Description
This writes data to the specified pipe. It automatically appends a newline character to the data.

## Arguments
| | | |
|---|---|---|
| `string` | `line` |  The data to be written to the pipe.  |
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
