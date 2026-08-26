# seq.open.local()

## Syntax:
`#include <bic_desktop>`
`function long seq.open.local( string filename, string mode(2), [ long remove.after.use ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use functions: [server2client()](server2client.md) or [client2server()](client2server.md).
This opens a specified file on the client system. It returns a file pointer, which you can use to identify the file in subsequent operations.

## Arguments
| | | |
|---|---|---|
| `string` | `filename` |  The name of the file that must be opened. If you do not specify a path name, the file is searched for in the directory where BW is loaded.  |
| `string` | `mode(2)` |  The mode in which the file must be opened. This can be one of the following options: "r" Open for reading. w" Create for writing. "a" Open for writing at end of file, or create for writing. In addition, you can add "t" to any of the above options if you want the file to be opened in text mode.  |
| `[ long` | `remove.after.use ]` |  Use this optional argument to specify whether or not the file must be removed after it has been closed by [seq.close.local()](seq.close.local.md): <> 0: file is removed 0: file is not removed  |

## Return values
| | |
|---|---|
| >= 0 | Success. File pointer is returned. |
| < 0 | Error. File could not be opened. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  You cannot use [Client file access overview](overview.md) functions in combination with the *seq.*.local()* functions. So, you cannot use *seq.seek()* or *seq.rewind()*, for example, on a file that was opened with *seq.open.local()*.

## Example
```

seq.open.local("C:\Program Files\Test.txt", "rt", false)
```

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
