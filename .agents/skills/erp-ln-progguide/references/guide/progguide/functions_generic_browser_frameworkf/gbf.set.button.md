# gbf.set.button()

## Syntax:
`function long gbf.set.button( const string button.group(), const string normal.button(), const string selected.button(), const string insensitive.button(), const string button.name(), long menu.item, long add.space )`

## Description
Adds a button to the button bar.
A button needs three icons. These icons are all in the group identified by button.group.
For Baan IV these three icons are for when the button is in the normal state (normal.button), when it is pushed (selected.button) and when it is currently not selectable (button.insensitive). When one or more of these icons do not exist, then another will be used instead. When no icon is available then an empty button will be used. The icons should be 20 x 20 pixels.
For Baan V only the normal.button icon is used, since the GUI will take care of creating a selected icon and an insensitive icon based on this normal.button. For compatibility reasons with older versions of the GBF the arguments selected.button and insensitive.button should nevertheless be given, but may of course be empty (in other words: “”) or the same as the normal.button. The normal.button icons should be 16 x 15 pixels. When it is larger all buttons on the button bar will have this larger size.
The menu.item is the menu item that will be used when the button is pushed. This menu.item should be a valid value from a preceding call to the function: [gbf.set.menu.item()](gbf.set.menu.item.md).
In general the message used to get the for that function should be used as button.name for this function. The button has a name, identified by the button.name. Note that the Help associated with this button.name will be given as help when topic Help is asked for this button and this button is not associated to a menu item, in other words menu.item is 0 in this function call. In case help is asked for the button which is associated to a menu item, then the Help of that menu item will be activated rather than the Help for this button. When the button is pushed the value of the button.name will be shown in the left-most message box and the function [gbf.menu.selected()](gbf.menu.selected.md) is called with this menu.item as identification. So for the application there is no difference whether the menu item is selected or this button is pushed.

## Arguments
| | | |
|---|---|---|
| `const string` | `button.group()` |  A group name for the normal, selected and insensitive icon.  |
| `const string` | `normal.button()` |  Baan(IV) The icon(20x20) to represent a button in its normal state Baan (V) The icon (16x15) to represent all states.  |
| `const string` | `selected.button()` |  Baan(IV) The icon(20x20) to represent a button in its selected state Baan(V) -  |
| `const string` | `insensitive.button()` |  Baan(IV) The icon(20x20) to represent a button in its insensitive (not selectable) state Baan (V) -  |
| `const string` | `button.name()` |  The name of the button that is shown when the cursor is above this button or when help is asked on this button and No menu item is associated with this button.  |
| `long` | `menu.item` |  The associated menu command. This menu.item should be a valid value from a preceding call to the function: [gbf.set.menu.item()](gbf.set.menu.item.md).  |
| `long` | `add.space` |  When the add.space is TRUE, then some extra white space is added before the button. When the add.space is FALSE then no extra white space is added before this new button.  |

## Return values
| | |
|---|---|
| > 0 | Successful completion, actual button identification is returned |
| 0 | Should never happen |
| GBF.NO.MEMORY | Not enough memory |
| GBF.ILL.MENU.ID | Illegal menu.item value given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

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
