# gbf.update.deffunc()

## Syntax:
`#include <bic_gbf>`
`function long gbf.update.deffunc( long obj.id, long def.func )`

## Description
This function is in fact a define and is defined as:
| | |
|---|---|
| gbf.update.deffunc(obj.id, def.func) | gbf.update.object(obj.id, GBF.NO.UPD.DESC, GBF.NO.UPD.ICON, def.func, GBF.NO.UPD.FUNC, GBF.NO.UPD.MENU) |
See [gbf.update.object() *](gbf.update.md) for more details.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The object identification  |
| `long` | `def.func` |  If GBF.USE.DEF.FUNC then use the default function, otherwise If GBF.NO.UPD.FUNC, then this function will not be changed, else this function will be used as the new default function (see gbf.add.object() for what the default function is supposed to do).  |

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
