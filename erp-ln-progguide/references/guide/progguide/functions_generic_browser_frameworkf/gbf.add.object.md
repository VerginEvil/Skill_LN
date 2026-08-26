# gbf.add.object()

## Syntax:
`function long gbf.add.object( const string object.key(), const string object.description() mb, long object.value, long obj.type, [ long icon.set, long default.function.id, long help.function.id, long drop.function.id, long menumask, long text.color, long line.style, long context.menu.id ] )`

## Description
Adds a header, interior, or leaf node to the object tree.

## Arguments
| | | |
|---|---|---|
| `const string` | `object.key()` |  The key of the object by which it is known in the application.  |
| `const string` | `object.description() mb` |  The text that is displayed in the browser to describe the object.  |
| `long` | `object.value` |  The object.value can be used to further identify this object, which may be needed in case the object appears more than once in the tree. This object.value will be returned on subsequent function calls, such as gbf.get.children() or [gbf.menu.selected()](gbf.menu.selected.md). Note that a value of 0 means something special, see gbf.update.object().  |
| `long` | `obj.type` |  Specify the object type by choosing one of the following: GBF.HEADER GBF.INTERIOR GBF.LEAF  |
| `[ long` | `icon.set ]` |  The value returned by a function depending on the obj.type: GBF.HEADER or GBF.LEAF: [gbf.set.leaf.icon()](gbf.set.leaf.icon.md) GBF.INTERIOR: [gbf.set.interior.icon()](gbf.set.interior.icon.md)  |
| `[ long` | `default.function.id ]` |  The default.function.id is an overloaded function identification. The actual function depends on whether or not this object is a leaf object. See Table default.function.id.  |
| `[ long` | `help.function.id ]` |  The help.function.id, if given and > 0, is the function to be called when help is asked and this object is currently selected. The value of help.function.id must be a value returned by a preceding [gbf.set.help.function()](gbf.set.help.function.md) call. When this help.function.id has an illegal value an error will be returned, and when GBF.OPT.DEBUG has been set then a debug error message will be given.  |
| `[ long` | `drop.function.id ]` |  The drop.function.id, if given and > 0, is the function to be called when other objects are dragged and dropped on this object. The value of drop.function.id must be a value returned by a preceding [gbf.set.help.function()](gbf.set.help.function.md) call. When this drop.function.id has an illegal value an error will be returned and when GBF.OPT.DEBUG has been set then a debug error message will be given.  |
| `[ long` | `menumask ]` |  The menumask is a bitmask to indicate which menu options should be disabled. Which bit disables which option is defined by setting a maskbit with [gbf.set.menu.item()](gbf.set.menu.item.md).  |
| `[ long` | `text.color ]` |  The text.color, if given and <> 0, is the color with which the object.description will be written in the tree. The value must be given as an RGB (red-green-blue) value. The standard defines are RGB.RED, RGB.GREEN, RGB.YELLOW, RGB.CYAN, RGB.MAGENTA, RGB.BLUE, RGB.WHITE RGB.GRAY, RGB.DGRAY. There is a limited number of colors possible, so that when this limit is exceeded the standard colors will be used. Note that the RGB.BLACK happens to be 0, so that value is mapped onto the standard foreground color of the GBF (see also: gbf.get.resource() and [gbf.set.resource()](gbf.set.resource.md)) which by default is black. All used colors must have a description so in case the end user asks for Help on Colors they will get a short explanation of these colors, see also [gbf.set.color()](gbf.set.color.md).  |
| `[ long` | `line.style ]` |  The line.style, if given and <> GBF.LINE.SOLID (which is defined as: 0), indicates that the linestyle to the parent node must be used rather than a solid line. Currently only GBF.LINE.DASHED must be used, which draws dashed lines. Note that this information is not used when this [gbf.add.object()](gbf.add.object.md) call is made during a gbf.get.top.level() function call.  |
| `[ long` | `context.menu.id ]` |  The *context.menu.id* is used to couple a context menu to this specific object. The context menu and its context should be known before the call to [gbf.start()](gbf.start.md). The *context.menu.id* is aquired through the function gbf.create.context.menu(). When used properly the end user can right-click on an item which makes a context menu appear for this specific node. When the option GBF.OPT.TREE.CONTROL is used, i.e. microsoft treeview, the functions [gbf.set.leaf.icon()](gbf.set.leaf.icon.md) and [gbf.set.interior.icon()](gbf.set.interior.icon.md) have to be used to add the context menu. This is because the Microsoft Treeview couples the context menus to the icon groups.  |

## Return values
| | |
|---|---|
| >= 0 | Successful completion, returned value is the new obj.id  |
| GBF.NO.MEMORY | Not enough memory |
| GBF.ILL.ICON | Illegal icon.set identification |
| GBF.ILL.FUNCTION | Illegal default.function.id, help.function.id or drop.function.id identification  |
| GBF.ILL.LENGTH | Length of object.key exceeds the stored key length in GBF  |
| GBF.ILL.STATE | GBF is not in the correct state to deal with this function  |
| GBF.NOT.EXPECTED | Function called when GBF did not expect this |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Restriction
This function may only be called by the application when the GBF issues a gbf.get.top.level() or a gbf.get.children() call.

## Related topics
- [gbf.add.header()](gbf.add.header.md)
- [gbf.add.interior()](gbf.add.interior.md)
- [gbf.add.leaf()](gbf.add.leaf.md)
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
