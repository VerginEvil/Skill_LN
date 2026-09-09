# seq.fstat.local()

## Syntax:
`#include <bic_desktop>`
`function long seq.fstat.local( string filename, ref long nr.bytes )`

## Description
*Deprecated.* This retrieves information about a specified file on a client system.

## Arguments
| | | |
|---|---|---|
| `string` | `filename` |  The path argument must include the full path to the *file*, including the drive name. This parameter may include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |
| `ref long` | `nr.bytes` |  This returns the size of the file in bytes.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. Probably file does not exist. The number is operating system dependent and varies according to the type of filesystem and type of file that is queried. Common values are: -2: File not found -3: Path not found -5: Permission denied -32: Sharing violation See windows error codes (on MSDN, for example) for details on a specific error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

seq.fstat.local("C:\Program Files\Test.txt", len.in.bytes)
```
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
