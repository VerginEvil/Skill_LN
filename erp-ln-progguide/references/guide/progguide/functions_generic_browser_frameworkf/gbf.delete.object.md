# gbf.delete.object()

## Syntax:
`function long gbf.delete.object( long obj.id )`

## Description
Deletes the given object, identified by obj.id, including all its child objects. When obj.id is GBF.ROOT.OBJECT then all child objects will be deleted.Note that in most cases a return value from [gbf.menu.selected()](gbf.menu.selected.md) will do better than using this function. The object identified by obj.id is deleted from the object tree, including all its children. Deleting obj.id in case when it is part of a multiple selection has some complications. If the obj.id is in the list of current selected objects, then it will also be removed from that list, which implies that the list is now at least one element shorter than it used to be and all elements that follow this element now have a smaller index. For example, if this obj.id used to have an index of 3 (see [gbf.get.selected()](gbf.get.selected.md)) then the object which used to have index 4 will now have index 3, object 5 will now be object 4 and so on. Take care that when this to be deleted obj.id, has child objects that are also in the current selection, then these will be removed to. So that the list will get even shorter and the indices of the remaining objects may have changed more than just with 1.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The unique object identification.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.OBJECT | Illegal obj.id given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

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
