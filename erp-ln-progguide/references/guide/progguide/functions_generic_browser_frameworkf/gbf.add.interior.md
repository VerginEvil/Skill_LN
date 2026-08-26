# gbf.add.interior()

## Syntax:
`function long gbf.add.interior( const string object.key(), string object.description() mb, long object.value )`

## Description
Adds an interior node to the object tree.
Same as: gbf.add.object(key, desc, value, GBF.INTERIOR)

## Arguments
| | | |
|---|---|---|
| `const string` | `object.key()` |  The key of the object by which it is known in the application.  |
| `string` | `object.description() mb` |  The text that is displayed in the browser to describe the object.  |
| `long` | `object.value` |  The object.value can be used to further identify this object, which may be needed in case the object appears more than once in the tree. This object.value will be returned on subsequent function calls, such as gbf.get.children() or [gbf.menu.selected()](gbf.menu.selected.md). Note that a value of 0 means something special, see gbf.update.object().  |

## Return values
| | |
|---|---|
| >= 0 | Successful completion, returned value is the new obj.id  |
| GBF.NO.MEMORY | Not enough memory |
| GBF.ILL.ICON | Illegal icon.set identification |
| GBF.ILL.FUNCTION | Illegal default.function.id, help.function.id or drop.function.id identification  |
| GBF.ILL.LENGTH | Length of object.key exceeds the stored key length in GBF  |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |
| GBF.NOT.EXPECTED | Function called when GBF did not expect this |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Restriction
This function may only be called by the application when the GBF issues a gbf.get.top.level() or a gbf.get.children() call.

## Related topics
- [gbf.add.header()](gbf.add.header.md)
- [gbf.add.leaf()](gbf.add.leaf.md)
- [gbf.add.object()](gbf.add.object.md)
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
