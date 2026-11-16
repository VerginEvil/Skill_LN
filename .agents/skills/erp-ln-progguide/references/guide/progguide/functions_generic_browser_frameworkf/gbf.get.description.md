# gbf.get.description()

## Syntax:
`function long gbf.get.description( long obj.id, ref string description() mb )`

## Description
This function returns the description of the given object. In other words the description with which the object has been created ( [gbf.add.object()](gbf.add.object.md)) or last updated (gbf.update.object()).

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  The unique object identification.  |
| `ref string` | `description() mb` |  A reference to the description of the object.  |

## Return values
| | |
|---|---|
| 0 | Successful completion, description is valid |
| GBF.ILL.OBJECT | Illegal obj.id given, description is invalid |
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
