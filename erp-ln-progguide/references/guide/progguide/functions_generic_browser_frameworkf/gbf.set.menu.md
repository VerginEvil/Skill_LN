# gbf.set.menu.state()

## Syntax:
`function long gbf.set.menu.state( long menu.id, long item.id, long disable, long checked, [ long radio ] )`

## Description
The following functions are in fact defines and they are defined as:
| | |
|---|---|
| gbf.set.menu.checked(item.id) | gbf.set.menu.state(0, item.id, false, true) |
| gbf.set.menu.disabled(item.id) | gbf.set.menu.state(0, item.id, true, false) |
| gbf.set.menu.enabled(item.id) | gbf.set.menu.state(0, item.id, false, false) |
| gbf.set.menu.not.checked(item.id) | gbf.set.menu.state(0, item.id, false, false) |
| gbf.set.menu.not.radio(item.id) | gbf.set.menu.state(0, item.id, false, false, false)  |
| gbf.set.menu.radio(item.id) | gbf.set.menu.state(0, item.id, false, false, true)  |
This function can disable a menu head or menu item and place or remove a ticmark on a menu item, which has been created using the [gbf.set.menu.head()](gbf.set.menu.head.md) and/or [gbf.set.menu.item()](gbf.set.menu.item.md) functions. Also a radio button (small circle) can be put in front of a menu items which has been created with the [gbf.set.menu.item()](gbf.set.menu.item.md) function. For changing of the standard GBF menu items see function: gbf.set.std.menu(). To change only a item give 0 for the menu.id and to only change an menu give 0 for the item.id. When both values are 0 nothing will change.
The menu.id is the return value of the function [gbf.set.menu.head()](gbf.set.menu.head.md) when that function was successfully completed.

## Arguments:gbf.set.menu.[enabled,disabled,radio,not radio, checked and not checked]
| | |
|---|---|
| item.id | The return value of the function [gbf.set.menu.item()](gbf.set.menu.item.md) when that function was successful completed.  |

## Arguments
| | | |
|---|---|---|
| `long` | `menu.id` |  The menu identification  |
| `long` | `item.id` |  The return value of the function [gbf.set.menu.item()](gbf.set.menu.item.md) when that function was successful completed.  |
| `long` | `disable` |  When disable is set to true then the menu.id (if not 0) and item.id (if not 0) will become insensitive, that is white, which does not allow the end-user to select it. Also the associated keystroke with this item.id is not useable as long as this menu.id is disabled. The menu.id and item.id can become selectable again by using false for disable.  |
| `long` | `checked` |  When checked is true a ticmark will be added in front of the menu.id (if not 0) and item.id (if not 0). When checked is false these ticmarks will be removed again.  |
| `[ long` | `radio ]` |  When radio is given and true and checked is false and item.id is not 0, then a radio button (small circle) will be added in front of this menu.id. These radio buttons should be used to indicate which of the possible alternatives is the current selected option. See, for example, the standard Find or Sort menu.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.MENU.ID | Unknown menu.id or item.id specified |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## gbf.set.menu.checked(), gbf.set.menu.disabled(),gbf.set.menu.enabled(), gbf.set.menu.not.checked(), gbf.set.menu.not.radio(),gbf.set.menu.radio()

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
