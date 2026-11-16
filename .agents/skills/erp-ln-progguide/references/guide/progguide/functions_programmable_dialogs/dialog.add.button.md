# dialog.add.button()

## Syntax:
`#include <bic_dialog>`
`function long dialog.add.button( long dlg, const string btnFunction(), const string btnLabel )`

## Description
Creates a button on the dialog.

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `const string` | `btnFunction()` |  Name of the function that is called when the button is pressed.  |
| `const string` | `btnLabel` |  The label used for the button.  |

## Return values
The id of the button. Negative value indicates an error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)

- [Programmable Dialogs Example](example.md)
