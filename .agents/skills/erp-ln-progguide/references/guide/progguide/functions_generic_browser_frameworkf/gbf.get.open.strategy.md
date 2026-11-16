# gbf.get.open.strategy()

## Syntax:
`function long gbf.get.open.strategy( ref long open.type )`

## Description
Returns the current automatic open and close schema.
This function may be used after the GBF run has finished to get the setting for this specific user, and restore them at the next run.

## Arguments
| | | |
|---|---|---|
| `ref long` | `open.type` |  Returns the current automatic open and close schema.  |

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
