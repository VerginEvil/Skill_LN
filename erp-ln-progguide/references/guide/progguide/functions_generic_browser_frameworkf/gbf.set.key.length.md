# gbf.set.key.length()

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.key.length( long key.length )`

## Description
The following functions are actually defines and they are defined as:
`gbf.set.key.length(key.length) : gbf.set.key.desc.length(key.length, 0)`
The [gbf.set.key.desc.length()](gbf.set.key.desc.length.md) function adjusts the length of the key of an object and/or the length of the description of the object. The default length for the object key is 64 and for the object description is 60. A new value of 0 means that the associated length is not changed. So, for example, gbf.set.key.desc.length(100, 0) will increase the key length to 100 and leave the description length at 64 (see also the two macros defined at the top of this description).
All objects will use the same key length and description length. That is regardless of the object, for example: top level, interior, leaf object, the key length will always be the same. The same holds for the object description.
Note the bigger these lengths are made, the more memory is needed to store the objects. This means that making these too big will lead to memory problems further on. So, this function should also be used to shrink these lengths if they are too large for the current application. For example, if it is known that the key will never exceed 10 characters, then a gbf.set.key.length(10) should be made.
This function can only be called before any object has been created, so once a [gbf.start()](gbf.start.md) has been given, this function will always return an error.

## Arguments
| | | |
|---|---|---|
| `long` | `key.length` |  The new key length.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.LENGTH | Key.length and/or desc.length < not enough memory  |
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
