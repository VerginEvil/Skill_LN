# dialog.add.text()

## Syntax:
`#include <bic_dialog>`
`function long dialog.add.text( long dlg, string text(), [ long attribute, value, ... ] )`

## Description
This function creates static texts on the dialog. Purpose of this text can be for explanation or additional help.

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `string` | `text()` |  The text to be displayed.  |
| `[ long` | `attribute, value, ... ]` |  Possible attributes are: DLG_FIELD_WIDTH: The number of characters to be displayed on one line.  |

## Return values
None.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
- [Programmable Dialogs Example](example.md)
