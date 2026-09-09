# seq.read.local()

## Syntax:
`#include <bic_desktop>`
`function long seq.read.local( ref string buf, ref long size, long lfn )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use function: [client2server()](client2server.md).
This reads a specified number of bytes from a specified file into *buf*.

## Arguments
| | | |
|---|---|---|
| `ref string` | `buf` |  This returns the data read from the file.  |
| `ref long` | `size` |  This returns the number of bytes read from the file.  |
| `long` | `lfn` |  The file pointer, as returned by [seq.open.local()](seq.open.local.md) when the file was opened.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. Probably *lfn* not connected. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  You cannot use [Client file access overview](overview.md) functions in combination with the *seq.*.local()* functions. So, you cannot use *seq.read.local()* on a file that was opened with *seq.open()*.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
