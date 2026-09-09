# gbf.set.read.levels()

## Syntax:
`function long gbf.set.read.levels( long read.levels, [ long show.levels ] )`

## Description
Sets the current number of levels that will be read (and shown) when an application returns one of the *restart* return values (see: [gbf.menu.selected()](gbf.menu.selected.md): for example the GBF.DO.RESTART.TREE).

## Arguments
| | | |
|---|---|---|
| `long` | `read.levels` |  The number of levels that will be read.  |
| `[ long` | `show.levels ]` |  The number of levels that will be shown. (if not given show.levels will be set to the value of read.levels)  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.LEVEL | Read.levels and/or show.levels < 0 |
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
