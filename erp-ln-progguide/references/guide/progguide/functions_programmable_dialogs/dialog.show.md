# dialog.show()

## Syntax:
`#include <bic_dialog>`
`function long dialog.show( long dlg, [ long previous_window, long load_defaults ] )`

## Description
Displays the created dialog and start interaction with the user. This function returns when the user clicks the OK or Cancel button. Created dialogs can be used multiple times.

## Arguments
| | | |
|---|---|---|
| `long` | `dlg` |  The identifier of the dialog. The identifier must be created with the function [dialog.new()](dialog.new.md).  |
| `[ long` | `previous_window ]` |  This can be used in wizards (see DSBUTTONWIZARD in [dialog.new()](dialog.new.md). It should be passed to dialog.show for every dialog. It contains information about the position and dimensions of the window which is passed from one dialog to the next.  |
| `[ long` | `load_defaults ]` |  When load_defaults = 1 then the saved defaults are load when the dialog is started.  |

## Return values
| | |
|---|---|
| END.PROGRAM | The user pressed the *OK* (or Finish) button  |
| 0 | The user pressed the *Cancel* button  |
| NEXT.FRM | The user pressed the *Next* button  |
| PREV.FRM | The user pressed the *Back* button  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
- [Programmable Dialogs Example](example.md)
