# remove.local.directory()

## Syntax:
`#include <bic_desktop>`
`function long remove.local.directory( string dirent )`

## Description
This deletes a specified directory on the client system.

## Arguments
| | | |
|---|---|---|
| `string` | `dirent` |  directory, including the drive name. For example: `remove.local.directory("C:\Program Files\Mydir")` The directory will only be removed when the directory is empty. The dirent parameter may include the string ${BSE_TMP} which indicates the ${BSE}\tmp directory in case of Baan Windows or Windows temp directory in case of WebUI.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. Probably directory not empty or no permission.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
