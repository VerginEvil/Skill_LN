# dialog.refresh.field()

## Syntax:
`#include <bic_dialog>`
`function long dialog.refresh.field( long dlg, const string fldName() )`

## Description
Refreshes the value of a field. This function can be used in a button function if the value for a field has changed.

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `const string` | `fldName()` |  Name of the field that needs to be refreshed.  |

## Return values
| | |
|---|---|
| 0 | OK |
| -1 | The dialog doesn't exist |
| -2 | The field doesn't exist. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
- [Programmable Dialogs Example](example.md)
