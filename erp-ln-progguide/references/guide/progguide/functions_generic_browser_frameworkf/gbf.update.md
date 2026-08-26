# gbf.update.object() *

## Syntax:
`#include <bic_gbf>`
`function long gbf.update.object( long obj.id, string object.description() mb, [ long icon.set, long default.function.id, long drop.function.id, long menumask, long text.color, long line.style ] )`

## Description
All but gbf.update.object() are defines and these functions are defined as:
| | |
|---|---|
| gbf.update.deffunc(obj.id, def.func) | gbf.update.object(obj.id, GBF.NO.UPD.DESC, GBF.NO.UPD.ICON, def.func, GBF.NO.UPD.FUNC, GBF.NO.UPD.MENU)  |
| gbf.update.dropfunc(obj.id, drop.func) | gbf.update.object(obj.id, GBF.NO.UPD.DESC, GBF.NO.UPD.ICON, GBF.NO.UPD.FUNC, drop.func, GBF.NO.UPD.MENU)  |
| gbf.update.desc(obj.id, description) | gbf.update.object(obj.id, description, GBF.NO.UPD.ICON, GBF.NO.UPD.FUNC, GBF.NO.UPD.FUNC, GBF.NO.UPD.MENU)  |
| gbf.update.icon(obj.id, icon.set) | gbf.update.object(obj.id, GBF.NO.UPD.DESC, icon.set, GBF.NO.UPD.FUNC, GBF.NO.UPD.FUNC, GBF.NO.UPD.MENU)  |
| gbf.update.menumask(obj.id, menumask) | gbf.update.object(obj.id, GBF.NO.UPD.DESC, GBF.NO.UPD.ICON, GBF.NO.UPD.FUNC, GBF.NO.UPD.FUNC, menumask)  |
The gbf.update.object() function updates the given object, that is one or more of the attributes of the given obj.id are changed from what it was on its [gbf.add.object()](gbf.add.object.md) call, or any preceding call. The items that can be updated are:

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The object identification  |
| `string` | `object.description() mb` |  If GBF.NO.UPD.DESC, then the description will not be changed. Otherwise this will be the new description for this object. Note that any other value for which isspace() returns true, such as for example: “ ”, the description will be invisible on the screen  |
| `[ long` | `icon.set ]` |  If GBF.USE.DEF.ICON then use the default icon, otherwise If GBF.NO.UPD.ICON, then the icon will not be changed, else this icon set will now be used  |
| `[ long` | `default.function.id ]` |  If GBF.USE.DEF.FUNC then use the default function, otherwise If GBF.NO.UPD.FUNC, then this function will not be changed, else this function will be used as the new default function (see gbf.add.object() for what the default function is supposed to do).  |
| `[ long` | `drop.function.id ]` |  If GBF.USE.DEF.FUNC then use the default function, otherwise If GBF.NO.UPD.FUNC, then this function will not be changed, else this function will be used as the new drag and drop function (see gbf.add.object() for what the drag and drop function is supposed to do).  |
| `[ long` | `menumask ]` |  If GBF.NO.UPD.MENU then the menumask will not be changed, otherwise this will be the new menu mask  |
| `[ long` | `text.color ]` |  If 0 then the color of the text will not be changed (note: not even set to the default color), otherwise this will be the new color of the object.description text.  |
| `[ long` | `line.style ]` |  If given and GBF.LINE.SOLID (which happens to be 0) then a solid line will be used, otherwise a GBF.LINE.DASHED will draw dashed line to the parent. When this item is not given the object will use the line style it already had.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.ICON | Illegal icon.set identification |
| GBF.ILL.FUNCTION | Illegal default.function.id or drop.function.id value  |
| GBF.ILL.OBJECT | Illegal obj.id given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

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
