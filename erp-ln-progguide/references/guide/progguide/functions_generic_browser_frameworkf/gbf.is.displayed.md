# gbf.is.displayed()

## Syntax:
`function long gbf.is.displayed( const long obj.id )`

## Description
Returns whether or not the given object is currently displayed. That is whether the obj.id can be seen and is not hidden because its parent is closed. This function can be used when walking through the object tree (see [gbf.get.first.child()](gbf.get.first.child.md), [gbf.get.next()](gbf.get.next.md), [gbf.get.parent()](gbf.get.parent.md) and so on.). It is only checked whether the Generic Browser Framework has drawn the object on the virtual window, but note that it may not actually be visible (on the physical window) because the current view is currently displaying another part of that virtual window.

## Arguments
| | | |
|---|---|---|
| `const long` | `obj.id` |  The object identification.  |

## Return values
| | |
|---|---|
| true | Successful completion, obj.id is currently displayed  |
| false | Successful completion, obj.id is currently not displayed  |
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
