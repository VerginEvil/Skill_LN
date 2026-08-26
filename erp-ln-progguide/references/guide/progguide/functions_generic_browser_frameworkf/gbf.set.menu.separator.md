# gbf.set.menu.separator()

## Syntax:
`function long gbf.set.menu.separator( long menu.id )`

## Description
This function (actually: define) adds a separator to the given menu. A menu separator line is drawn in the menu which can never be selected and will generate a 0 return value. Also only BW supports these menu separator lines, but no error is generated when using this under BX.

## Arguments
| | | |
|---|---|---|
| `long` | `menu.id` |  The menu identification.  |

## Return values
| | |
|---|---|
| 0 | Menu separator line added |
| GBF.NO.MEMORY | Not enough memory |
| GBF.MENU.EMPTY | Empty menu text is not allowed |
| GBF.ILL.MENU.ID | Illegal menu.id value |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |
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
