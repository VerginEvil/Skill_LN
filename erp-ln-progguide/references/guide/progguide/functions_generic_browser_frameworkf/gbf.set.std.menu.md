# gbf.set.std.menu() *

## Syntax:
`function long gbf.set.std.menu( long menu.pattern, long disabled, checked Parameter )`

## Description
The following functions are in fact defines and they are defined as:
| | |
|---|---|
| gbf.set.std.menu.checked(menu.pattern): | gbf.set.std.menu(menu.pattern, false, true) |
| gbf.set.std.menu.disabled(menu.pattern): | gbf.set.std.menu(menu.pattern, true, false) |
| gbf.set.std.menu.enabled(menu.pattern): | gbf.set.std.menu(menu.pattern, false, false) |
| gbf.set.std.menu.not.checked(menu.pattern): | gbf.set.std.menu(menu.pattern, false, false) |
This function can disable standard GBF menu headings and/or menu items and place or remove a ticmark on a menu item, which has been created using the [gbf.init()](gbf.init.md) function. For changing of the customized menu headings and items see function: gbf.set.menu.state().
The menu.pattern holds the pattern of all standard menu items which should be updated. The pattern is build the same way as the argument in the [gbf.init()](gbf.init.md) function. So for example to disable all menu items one could use:
gbf.set.std.menu.disabled(GBF.MENU.ALL)
to disable the “Read All” and “Using Session”:
gbf.set.std.menu.disabled(GBF.MENU.FILE.READ + GBF.MENU.HELP.SESS)
When disable is set to true then all of the specified standard GBF menu items and headings will become insensitive, that is white, which does not allow the end-user to select it. Also the associated keystroke with this menu.pattern is NOT usable as long as these menu items are disabled. These standard GBF menu items can become selectable again by using false for disable.
When checked is true a ticmark will be added in front of all of the specified standard GBF menu items and headings. When checked is false these ticmarks will be removed again.
You can change a menu heading and/or menu item which has not been created during the [gbf.init()](gbf.init.md). In this case no error will be returned, but of course nothing will be changed. Also all other created menu headings and items which are not specified in this menu.pattern will be left unchanged.
Note
It is strongly discouraged to manipulate menu entries that are otherwise dealt with by the GBF. These menu items are: all of the GBF.MENU.SRCH and GBF.MENU.SORT, as well as GBF.MENU.PRINT.

## Arguments:gbf.set.std.menu
| | |
|---|---|
| menu.pattern | The menu.pattern holds the pattern of all standard menu items which should be updated.  |
| disabled | When disable is set to true all of the specified standard GBF menu items and headings will be disabled. Also the associated keystroke with this menu.pattern is not usable as long as these menu items are disabled. These standard GBF menu items can become selectable again by setting this parameter to false.  |
| checked | If true a ticmark will be added in front of all of the specified standard GBF menu items and headings. When checked is set to false these ticmarks will be removed again.  |

## Arguments:gbf.set.std.menu.checked, gbf.set.std.menu.not.checked, gbf.set.std.menu.enabled,gbf.set.std.menu.disabled
| | |
|---|---|
| menu.pattern | The menu.pattern holds the pattern of all standard menu items which should be updated.  |

## Arguments
| | | |
|---|---|---|
| `long` | `menu.pattern` |  The menu.pattern holds the pattern of all standard menu items which should be updated.  |
| `long` | `disabled` |  When disable is set to true all of the specified standard GBF menu items and headings will be disabled. Also the associated keystroke with this menu.pattern is not usable as long as these menu items are disabled. These standard GBF menu items can become selectable again by setting this parameter to false.  |
| `checked` | `Parameter` |  If true a ticmark will be added in front of all of the specified standard GBF menu items and headings. When checked is set to false these ticmarks will be removed again.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## gbf.set.std.menu.checked(), gbf.set.std.menu.not.checked(),gbf.set.std.menu.enabled(), gbf.set.std.menu.disabled()

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
