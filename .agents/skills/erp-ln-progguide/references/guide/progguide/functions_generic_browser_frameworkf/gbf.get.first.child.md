# gbf.get.first.child()

## Warning
This function should not be used during a refresh, so not during a gbf.get.top.level() or a gbf.get.children() since that may lead to unpredictable results when, for example, using this function to get the children of the object for which the gbf.get.children() was started in the first place. Not refreshed children (in other words the dirty children) will not be returned.

## Syntax:
`function long gbf.get.first.child( long obj.id, long force.read, ref long child.id, ref string child.key, ref long child.value, ref long child.type )`

## Description
This function returns the first child of the given object if the children are read by the GBF (see below). The returned child.id is the GBF child identification, to be used on subsequent gbf.get.parent(), gbf.get.first.child(), [gbf.get.next()](gbf.get.next.md) and gbf.update.object() function calls. The child is further identified by the child.key and child.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call.
If the obj.id has no children at all, then GBF.NO.CHILDREN will be returned (and of course the other return values, such as child.id and so on. will not contain any valid information).
The force.read tells the GBF what to do when the children are not yet read:
| | |
|---|---|
| Force.read | Description |
| true | First the children are read, using the gbf.get.children() function call, and the first read child is returned by this [gbf.get.first.child()](gbf.get.first.child.md) call as described above. That is, in this case it does not matter whether or not the children are already read before the main application issued this call (except for the GBF.NO.MEMORY return call). |
| false | The special return value GBF.NO.READ.CHILDREN is returned, and of course the child.id, child.key, child.value and obj.type are all invalid and should not be used |
A very special value of obj.id may be used to indicate that the first child of the root object should be used. This special value is: GBF.ROOT.OBJECT. In this case an object which has been given to the GBF on the preceding [gbf.add.object()](gbf.add.object.md) from within the gbf.get.top.level() will be returned. The special successful completion return value GBF.LAST indicates that the child.id object returned is the only child object, which means that this child object has no further brothers, or in other words child.id cannot be used in a subsequent [gbf.get.next()](gbf.get.next.md) function call.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The unique object identification.  |
| `long` | `force.read` |  Tells the GBF what to do when the children are not yet read. See table above with an explanation.  |
| `ref long` | `child.id` |  Returns the unique child (object) identification.  |
| `ref string` | `child.key` |  Returns the key of the child (object) by which it is known in the application.  |
| `ref long` | `child.value` |  Returns the value of the child (object) that is used to further identify this object (in case the object is more than once in the tree). Note that a value of 0 means something special, see gbf.update.object().  |
| `ref long` | `child.type` |  The type of node child.id: GBF.HEADER the returned child.id is a header node GBF.INTERIOR the returned child.id is an interior node. GBF.LEAF the returned child.id is a leaf node  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.CYCLE | Successful completion, but child.id reflects the same object as obj.id in this subtree due to a cycle. |
| GBF.LAST | Successful completion, and child.id is the only child |
| GBF.NO.CHILDREN | Successful completion, but obj.id does not have any children |
| GBF.NO.READ.CHILDREN | Successful completion, but the children of obj.id are not yet read |
| GBF.ILL.OBJECT | Illegal obj.id given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.NO.MEMORY | Not enough memory to store all children |
| GBF.NOT.INTERIOR | Given obj.id is not an interior node, so it has no children |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [gbf.get.next()](gbf.get.next.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
