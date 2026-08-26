# create.local.directory()

## Syntax:
`#include <bic_desktop>`
`function long create.local.directory( string dirent )`

## Description
*Deprecated.* This creates a specified directory on a client system. You must have write permission in the parent directory to do this. Access permissions for the new directory are set to read and write for all users.

## Arguments
| | | |
|---|---|---|
| `string` | `dirent` |  |

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
