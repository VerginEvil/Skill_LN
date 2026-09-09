# seq.open.dialog.next()

## Syntax:
`#include <bic_desktop>`
`function long seq.open.dialog.next( ref string filename )`

## Description
*Deprecated.* Retrieve the next full pathname of the file selected by the user in a previous [seq.open.dialog.local()](seq.open.dialog.local.md) function. This function should only be used when a previous call to seq.open.dialog.local() returned a value greater than 1.

## Arguments
| | | |
|---|---|---|
| `ref string` | `filename` |  Output argument which will contain the next full path of the file selected by the user.  |

## Return values
| | |
|---|---|
| true | Successfully retrieved next filename |
| false | No more filenames to be retrieved |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
