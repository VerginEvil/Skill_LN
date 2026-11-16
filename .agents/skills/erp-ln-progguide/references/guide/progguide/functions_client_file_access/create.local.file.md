# create.local.file()

## Syntax:
`#include <bic_desktop>`
`function long create.local.file( string filename )`

## Description
*Deprecated.* This creates a specified file on a client system. You must have write permission in the parent directory to do this. Access permissions for the new file are set to read and write, for all users. When the file does already exist, it will be truncated.

## Arguments
| | | |
|---|---|---|
| `string` | `filename` |  The full path name of the file. For example: `create.local.file("C:\Program Files\mydir\myfile")` The filename parameter may include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. Probably no permission. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
