# dir.select.dialog.local()

## Syntax:
`#include <bic_desktop>`
`function long dir.select.dialog.local( ref string dirname )`

## Description
*Deprecated.* This shows the Windows *Browse For Folder* dialog, to allow the user to select one new or existing folder (directory) on the client.

## Arguments
| | | |
|---|---|---|
| `ref string` | `dirname` |  Output argument which will contain the full path of the directory selected by the user.  |

## Return values
| | |
|---|---|
| 1 | A directory selected by the user |
| 0 | No directory selected. Folder browser dialog canceled by the user.  |
| -1 | Error occurred |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
