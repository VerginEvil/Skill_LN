# dialog.new()

## Syntax:
`#include <bic_dialog>`
`function long dialog.new( string dialogName, [ long attribute, value, ... ] )`

## Description
Creates a new dialog. *dialog.name* will be used for the title bar of the new dialog. Possible attributes are:

## Arguments
| | | |
|---|---|---|
| `string` | `dialogName` |  |
| `[ long` | `attribute, value, ... ]` |  Possible attributes are: DLG_FIELD_WIDTH: The number of characters to be displayed on one line.  |

## Return values
The id of the created dialog. This id identifies the dialog in further dialog calls. It is the id of an XML tree that can be debugged during the whole process.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Attributes
| | | |
|---|---|---|
| Attribute | Type | Description |
| DLG_BUTTONS | Long |  DSBUTTONOK: show only an OK button. DSBUTTONCANCEL: show only a Cancel button. DSBUTTONOKCANCEL: show an OK and Cancel button (default value). DSBUTTONWIZARD: Show Cancel, Back, Next and Finish button at the bottom.  |
| DLG_STATUSBAR | Boolean | If attribute is true, a status bar is added to the window. The left area can be filled with the function footnote() and the status field with the function fill.status.field(2, "text")  |
| DLG_OK_TEXT | String | The text that should appear on the OK button |
| DLG_SCROLLBARS | Boolean | When set to *true*, the fields will appear in a window with scrollbars if the initial window is larger than the display size. Be careful with this option, because if this option is set, the initial window size will be retained. Subsequent changes to the window size (larger description fields) will cause the scrollbars to appear as well. This is probably an unwanted side-effect.  |
| DLG_SAVE_GET_DFLTS | String |  When set, two extra buttons will be added to the dialog: "Save Defaults" and "Get Defaults". The first button will save the current values of all fields on the dialog. The next time the dialogs open, the user can click on the "Get Defaults" button to restore these values. The values are stored in a location, identified by the user's login code and the code of the running program. If the running program supports multiple dialogs, the identification can be made unique by setting the *string* argument for this property. This argument will then be part of the identifying key. If there is only one dialog in the program, the argument can be an empty string.  |

## Related topics
- [Programmable dialogs synopsis](synopsis.md)
- [Programmable Dialogs Example](example.md)
