# pipe.open()

## Syntax:
`function long pipe.open( string pathnm, string openmode )`

## Description
This creates a UNIX process with the specified name and links an input and/or output stream to it. It returns a pointer to the pipe; this is used to identify the pipe in subsequent operations.

## Arguments
| | | |
|---|---|---|
| `string` | `pathnm` |  The path name for the UNIX process.  |
| `string` | `openmode` |  Use this to specify whether the pipe is opened for reading, writing, or both. The possible values are: "r" create for reading "w" create for writing "rw" create for reading and writing  |

## Return values
>= 1: success; a pointer to the pipe is returned
< 1: error; that is, the negative value of the system error (for example, for a permission error, the system returns 13 and the function returns -13, or if the internal table is full, the function returns -EAGAIN).

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)
- [Interprocess communication (OS level) synopsis](synopsis.md)
