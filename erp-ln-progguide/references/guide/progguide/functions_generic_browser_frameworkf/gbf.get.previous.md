# gbf.get.previous()

## Warning
This function should not be used during a refresh, so not during a [gbf.get.top.level()](gbf.get.top.level.md) or a [gbf.get.children()](gbf.get.children.md) since that may lead to unpredictable results when for example using this function to get the children of the object for which the [gbf.get.children()](gbf.get.children.md) was started in the first place. Not refreshed children (in other words the dirty children) will not be returned.

## Syntax:
`function long gbf.get.previous( long obj.id, ref long prev.id, ref string prev.key, ref long prev.value, ref long prev.type )`

## Description
This function returns the previous brother object of the given object. The returned *prev.id* is the GBF identification, to be used on subsequent [gbf.get.parent()](gbf.get.parent.md), [gbf.get.first.child()](gbf.get.first.child.md), [gbf.get.next()](gbf.get.next.md) and [gbf.update.object() *](gbf.update.md) function call. The previous brother is further identified by the *prev.key* and *prev.value*, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call.
The special successful completion return value GBF.LAST indicates that the *prev.id* object returned is the last object, which means that this *prev.id* cannot be used in a subsequent [gbf.get.next()](gbf.get.next.md) function call. If this is attempted, that is a gbf.get.previous() on this last brother, then GBF.ILL.OBJECT will be returned.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The unique object identification.  |
| `ref long` | `prev.id` |  Returns the unique previous (object) identification.  |
| `ref string` | `prev.key` |  Returns the key of the previous (object) by which it is known in the application.  |
| `ref long` | `prev.value` |  Returns the value of the previous (object) that is used to further identify this object (in case the object is more than once in the tree). Note that a value of 0 means something special, see [gbf.update.object() *](gbf.update.md).  |
| `ref long` | `prev.type` |  The type of node *prev.id*: GBF.HEADER the returned *prev.id* is a header node GBF.INTERIOR the returned *prev.id* is an interior node. GBF.LEAF the returned *prev.id* is a leaf node  |
-
-
-

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.LAST | Successful completion, and *prev.id* is the first previous brother  |
| GBF.ILL.OBJECT | Illegal *obj.id* given, or *obj.id* has no further brothers  |
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
