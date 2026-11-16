# gbf.get.open.depth()

## Syntax:
`function long gbf.get.open.depth( ref long open.depth )`

## Description
Returns the current open and read depth. This open.depth is the number of levels the GBF will display when opening an interior node. When not all of these levels have been read yet, the GBF will read the necessary levels. The default value for open.depth is 1.
This function may be used after the GBF run has finished to get the setting for this specific user, and restore them at the next run.

## Arguments
| | | |
|---|---|---|
| `ref long` | `open.depth` |  Returns the current open and read depth.  |

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
