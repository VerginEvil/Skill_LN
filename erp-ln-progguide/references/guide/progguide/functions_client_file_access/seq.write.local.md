# seq.write.local()

## Syntax:
`#include <bic_desktop>`
`function long seq.write.local( long buf, long size, long lfn )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use function: [server2client()](server2client.md).
This writes data from the specified buffer to the specified file, beginning at the current file position.

## Arguments
| | | |
|---|---|---|
| `long` | `buf` |  The data that must be written to the file.  |
| `long` | `size` |  The number of bytes that must be written to the file.  |
| `long` | `lfn` |  The file pointer, as returned by [seq.open.local()](seq.open.local.md) when the file was opened.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. Probably *lfn* not connected.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  You cannot use [Client file access overview](overview.md) functions in combination with the *seq.*.local()* functions. So, you cannot use *seq.write.local()* on a file that was opened with *seq.open()*.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
