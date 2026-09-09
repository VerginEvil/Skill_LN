# gbf.get.selected()

## Syntax:
`function long gbf.get.selected( long index, ref long obj.id, string obj.key(), ref long obj.value, ref long obj.type )`

## Description
This function must only be used when a call back to the main application indicates that there is one or more currently selected objects (see [gbf.init()](gbf.init.md), [gbf.menu.selected()](gbf.menu.selected.md), gbf.drag.drop() and so on). The function [gbf.get.selected.nr()](gbf.get.selected.nr.md) can be used to get the current number of selected objects. A further use of this function is immediately after the GBF has stopped (in other words the [gbf.start()](gbf.start.md) function call has completed) to get the current selected objects, so in this case the GBF can be used as zoom session to pick a specific object. This function then allows you to retrieve all the selected objects one by one as it returns the selected object at the given index. The returned obj.id is the GBF identification, to be used on subsequent gbf.get.parent(), [gbf.get.first.child()](gbf.get.first.child.md), [gbf.get.next()](gbf.get.next.md) and [gbf.update.object() *](gbf.update.md) function call. The object is further identified by the obj.key and obj.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call.
The obj.type flag indicates the type of node obj.id:
| | |
|---|---|
| GBF.LEAF | Returned obj.id is a leaf node |
| GBF.HEADER | Returned obj.id is a header node |
| GBF.INTERIOR | Returned obj.id is an interior node. |
In case the functions [gbf.menu.selected()](gbf.menu.selected.md), gbf.drag.drop(), and so on. indicate that there is only one object selected (in other words obj.id in those functions is greater than 0) then this [gbf.get.selected()](gbf.get.selected.md) function may only be called with index set to 1.
Note that the order of objects, as well as the maximum valid index, changes when objects are deleted from the list using [gbf.delete.object()](gbf.delete.object.md).

## Arguments
| | | |
|---|---|---|
| `long` | `index` |  The index in the range of selected objects  |
| `ref long` | `obj.id` |  Returns the object identification  |
| `string` | `obj.key()` |  Returns the object key  |
| `ref long` | `obj.value` |  Returns the object value  |
| `ref long` | `obj.type` |  Returns the object type  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.OBJECT | Illegal index given |
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
