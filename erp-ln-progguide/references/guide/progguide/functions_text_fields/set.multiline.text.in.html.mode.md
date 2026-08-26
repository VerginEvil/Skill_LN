# set.multiline.text.in.html.mode()

## Syntax:
`function long set.multiline.text.in.html.mode( string text_field )`

## Description
This switches the editing of a *text_field* to html mode in a Rich Text Editor. Text edited in this way is saved in html format.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field. See [Text fields overview](overview.md). The  |

## Return values
0 Success
-1 Not in LnUI
-2 LnUI version too old, minimum version is 12.0.5
-3 Object TIV too low, it should be >= 2150

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Note  This function should be used in the before.program section.
Do not use it for text that must be printed on a standard report. Printing is not supported for html code
This function works only for Multi Line Text fields. If the same text is displayed or editable on another session then there it must also be a Multi Line Text field.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
