# gbf.get.parent()

## Syntax:
`function long gbf.get.parent( long obj.id, ref long parent.id, ref string parent.key(), ref long parent.value )`

## Description
Returns the parent of the given object. The returned parent.id is the GBF parent identification, to be used on subsequent gbf.get.parent(), [gbf.get.first.child()](gbf.get.first.child.md), [gbf.get.next()](gbf.get.next.md) and gbf.update.object() function calls. The parent is further identified by the parent.key and parent.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call.
The special successful completion return value GBF.TOP.LEVEL indicates that the parent.id object returned resides at the top level, which means that this parent.id cannot be used in a subsequent gbf.get.parent() function call. In this case the parent.id, parent.key and the parent.value are not valid for the main application, since there is no parent of a top level object. Note that in case the GBF has added a special extra parent then this extra node will NOT be returned by this function.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The unique object identification.  |
| `ref long` | `parent.id` |  Returns the parent object identification.  |
| `ref string` | `parent.key()` |  Returns the parent object key.  |
| `ref long` | `parent.value` |  Returns the parent object value.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.TOP.LEVEL | Successful completion, and parent.id is at top level  |
| GBF.ILL.OBJECT | Illegal obj.id given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [gbf.get.current.parent()](gbf.get.current.parent.md)
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
