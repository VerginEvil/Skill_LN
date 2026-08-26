# gbf.set.menu.checked()

## Syntax:
`function long gbf.set.menu.checked( )`

## Description
This function is in fact a define and is defined as:
| | |
|---|---|
| gbf.set.menu.checked(item.id) | gbf.set.menu.state(0, item.id, false, true) |
This function can place a ticmark on a menu item.
The menu.id is the return value of the function [gbf.set.menu.head()](gbf.set.menu.head.md) when that function was successfully completed.
See [gbf.set.menu.state()](gbf.set.menu.md) for more details.

## Arguments:
| | |
|---|---|
| item.id | The return value of the function [gbf.set.menu.item()](gbf.set.menu.item.md) when that function was successful completed.  |

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
