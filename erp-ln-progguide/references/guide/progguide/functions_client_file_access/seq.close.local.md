# seq.close.local()

## Syntax:
`#include <bic_desktop>`
`function void seq.close.local( long lfn )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use functions: [server2client()](server2client.md) or [client2server()](client2server.md).
This empties the buffers associated with the specified file and closes the file. If the *remove.after.use* flag was set when the file was opened, the file is removed after it is closed.

## Arguments
| | | |
|---|---|---|
| `long` | `lfn` |  The file pointer to the file that must be closed, as returned by [seq.open.local()](seq.open.local.md) when the file was opened.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  You cannot use [Client file access overview](overview.md) functions in combination with the *seq.*.local()* functions. So, you cannot use *seq.close.local()* on a file that was opened with *seq.open()*.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
