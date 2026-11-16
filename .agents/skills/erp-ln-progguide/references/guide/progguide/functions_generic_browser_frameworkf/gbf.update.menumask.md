# gbf.update.menumask()

## Syntax:
`#include <bic_gbf>`
`function long gbf.update.menumask( long obj.id, long menumask )`

## Description
This function is in fact a define and is defined as:
| | |
|---|---|
| gbf.update.menumask(obj.id, menumask) | gbf.update.object(obj.id, GBF.NO.UPD.DESC, GBF.NO.UPD.ICON, GBF.NO.UPD.FUNC, GBF.NO.UPD.FUNC, menumask) |
See [gbf.update.object() *](gbf.update.md) for more details.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The object identification  |
| `long` | `menumask` |  If GBF.NO.UPD.MENU then the menumask will not be changed, otherwise this will be the new menu mask  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.ICON | Illegal icon.set identification |
| GBF.ILL.FUNCTION | Illegal default.function.id or drop.function.id value |
| GBF.ILL.OBJECT | Illegal obj.id given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## gbf.update.dropfunc(), gbf.update.desc(),gbf.update.icon(), gbf.update.menumask(), gbf.update.object()

## Restriction
These functions may only be called by the application when the GBF issues a call back to the main application, thus on a [gbf.drag.drop()](gbf.drag.drop.md), [gbf.menu.selected()](gbf.menu.selected.md), [gbf.help.selected()](gbf.help.selected.md) or [gbf.menu.selected()](gbf.menu.selected.md) call. The object to be updated is identified by the given obj.id.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
