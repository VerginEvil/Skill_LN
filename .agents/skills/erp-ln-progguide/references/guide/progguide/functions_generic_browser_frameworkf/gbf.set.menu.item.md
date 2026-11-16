# gbf.set.menu.item()

## Syntax:
`function long gbf.set.menu.item( long menu.id, const string menu.text(), const string keystroke(), [ long is.default, long menu.function.id ], long maskbit, [ long multi.mask ], long std.button )`

## Description
Adds a menu item to the set of menu items under the heading as identified by menu.id, as well as it allows to assign a keystroke combination (such as <Ctrl>+A and so on.) and connect it to a standard GBF button which the GBF does not service itself.

## Arguments
| | |
|---|---|
| Ctrl | indicates that the Control key should be pressed |
| Shift | indicates that the Shift key should be pressed |
| Alt | indicates that the Alt key should be pressed |
| <single char> | is the single character to be pressed |
| F<nr> | denominates the function key with number <nr>, where 1 <= nr <= 12 on most keyboards. |
| <special key> | indicates a special key on the keyboard |
So to make a Keystroke for <control><shift>F1 use: Ctrl+Shift+F1.
Note that the Shift should only be used for special keys or in combination with other modifiers, for example: Ctrl+F<nr> and Ctrl+Shift+A, not with single characters, as for example GBF cannot differentiate between ‘ A’ and ‘Shift+A’ (but of course GBF differentiates between ‘a’;;;; and ‘A’). These ‘Shift+a’ and ‘Shift+A’ are both converted to ‘A’. In debug mode (see [gbf.init()](gbf.init.md), using GBF.OPT.DEBUG) these changes will be noted with a debug pop-up message.
The supported special keys are:
| | | |
|---|---|---|
| Special key | Key on keyboard | Needs modifier |
| Backspace | Backspace | yes |
| DEL or Delete | DEL or Delete | no |
| END | END | yes |
| ESC | ESC or ESCAPE | no |
| HOME | HOME | yes |
| INS | INS or Insert | no |
| PgDn | Page Down | yes |
| PgUp | Page Up | yes |
| Return or Enter | Return or Enter | yes |
| Space | space bar | no |
| TAB | Tab | no |
The last column of the above table tells whether this key can be used by itself, for example ESC, or whether it needs a modifier, for example PgDn, since the standard key is already defined by the GBF. These modifiers are Ctrl, Shift, Alt or any combination of these. The denotations ‘Return’ and ‘Enter’ are two different names for the same key.
| | | |
|---|---|---|
| GBF mnemonic | GBF menu text | GBF keystroke |
| GBF.BUTTON.UNDO | Undo or Redo | Ctrl+Z |
| GBF.BUTTON.INSERT | Insert | Insert |
| GBF.BUTTON.COPY | Copy | Ctrl+C |
| GBF.BUTTON.DELETE | Delete | Delete |
| GBF.BUTTON.TEXT | Text | Ctrl+T |
| GBF.BUTTON.GRP.NEW |  | Ctrl+Shift+N |

## Return values
| | |
|---|---|
| > 1 | The identification of this new menu entry |
| 1 | Should never be returned, as 1 is the GBF default |
| 0 | Menu separator line added |
| GBF.NO.MEMORY | Not enough memory |
| GBF.MENU.EMPTY | Empty menu text is not allowed |
| GBF.ILL.MENU.ID | Illegal menu.id value |
| GBF.ILL.FUNCTION | Illegal menu.function.id value |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.MAX.MENU | Too many submenus for this menu defined |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
