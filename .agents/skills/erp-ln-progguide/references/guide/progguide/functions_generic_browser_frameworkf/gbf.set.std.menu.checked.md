# gbf.set.std.menu.checked() *

## Syntax:
`function long gbf.set.std.menu.checked( )`

## Description
This function is in fact a define and is defined as:
| | |
|---|---|
| gbf.set.std.menu.checked(menu.pattern): | gbf.set.std.menu(menu.pattern, false, true) |
This function can place a ticmark on a menu item, which has been created using the [gbf.init()](gbf.init.md) function.
See [gbf.set.std.menu() *](gbf.set.std.menu.md) for more details.

## Arguments:
| | |
|---|---|
| menu.pattern | The menu.pattern holds the pattern of all standard menu items which should be updated. |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

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
