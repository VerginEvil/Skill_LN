# gbf.get.current.parent()

## Syntax:
`function long gbf.get.current.parent( )`

## Description
Returns the object identification (obj.id) of the current parent, which is the parent for which the children are now asked for by the GBF. In other words, the current parent is the parent to which objects will be added with the [gbf.add.object()](gbf.add.object.md) function. This function can thus only be called during a call back to gbf.get.top.level() (in which case the return value will be the special value: GBF.ROOT.OBJECT), or during a gbf.get.children(). Unlike with gbf.get.parent() function the parents key and value are not returned by this gbf.get.current.parent() function, since that information has already been supplied with the original (gbf.get.top.level() and) gbf.get.children() function call. In case the GBF has added a special extra parent then this extra node will not be returned by this function.
Note that since this function is available while the GBF is reading children, it may very well be that the tree is different than you would expect it to be. For example, not all children are already present, no deeper children are available and so on.

## Return values
| | |
|---|---|
| other | Object id of current object, function called during gbf.get.children() |
| GBF.ROOT.OBJECT | Successful completion, no parent (or root is parent), function called during gbf.get.top.level() |
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
