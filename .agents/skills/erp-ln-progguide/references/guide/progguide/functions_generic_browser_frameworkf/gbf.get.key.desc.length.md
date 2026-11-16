# gbf.get.key.desc.length()

## Syntax:
`function long gbf.get.key.desc.length( ref long key.length, ref long desc.length )`

## Description
Returns the length of the key of the object and the length of the description of the object. The default length for the object key is 64 and for the object description 60.

## Arguments
| | | |
|---|---|---|
| `ref long` | `key.length` |  Returns the length of the object key.  |
| `ref long` | `desc.length` |  Returns the length of the object description.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
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
