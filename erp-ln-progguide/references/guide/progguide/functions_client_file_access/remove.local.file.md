# remove.local.file()

## Syntax:
`#include <bic_desktop>`
`function long remove.local.file( string filename )`

## Description
*Deprecated.* This deletes a specified file on the client system.

## Arguments
| | | |
|---|---|---|
| `string` | `filename` |  The name of the file that must be deleted. The name must include the full path tot the file, including the drive. For example: `remove.local.file("C:\Program Files\Mydir\Myfile.txt")` The filename parameter may include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error; The negative value of the operating system error.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
