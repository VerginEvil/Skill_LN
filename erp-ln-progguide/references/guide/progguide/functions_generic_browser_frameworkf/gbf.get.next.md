# gbf.get.next()

## Warning
This function should not be used during a refresh. In other words, not during a gbf.get.top.level() or a gbf.get.children() since that may lead to unpredictable results when, for example, you use this function to get the children of the object for which the gbf.get.children() was started in the first place. Not refreshed children (in other words the dirty children) will not be returned.

## Syntax:
`function long gbf.get.next( long obj.id, ref long next.id, ref string next.key(), ref long next.value, ref long next.type )`

## Description
Returns the next brother object of the given object. The returned next.id is the GBF identification, to be used on subsequent gbf.get.parent(), [gbf.get.first.child()](gbf.get.first.child.md), gbf.get.next() and gbf.update.object() function calls. The next brother is further identified by the next.key and next.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call.
The special successful completion return value GBF.LAST indicates that the next.id object returned is the last object, which means that this next.id cannot be used in a subsequent gbf.get.next() function call. If this is attempted, that is a gbf.get.next() on this last brother, then GBF.ILL.OBJECT will be returned.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The unique object identification.  |
| `ref long` | `next.id` |  Returns the unique child (object) identification.  |
| `ref string` | `next.key()` |  Returns the key of the child (object) by which it is known in the application.  |
| `ref long` | `next.value` |  Returns the value of the child (object) that is used to further identify this object (in case the object appears more than once in the tree). Note that a value of 0 means something special, see gbf.update.object().  |
| `ref long` | `next.type` |  The type of node child.id: GBF.HEADER the returned child.id is a header node GBF.INTERIOR the returned child.id is an interior node. GBF.LEAF the returned child.id is a leaf node  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.LAST | Successful completion, and next.id is the last brother |
| GBF.ILL.OBJECT | Illegal obj.id given, or obj.id has no further brothers |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [gbf.get.first.child()](gbf.get.first.child.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
