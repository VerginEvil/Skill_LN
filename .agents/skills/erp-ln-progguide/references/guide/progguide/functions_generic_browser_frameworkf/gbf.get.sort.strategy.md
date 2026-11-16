# gbf.get.sort.strategy()

## Syntax:
`function long gbf.get.sort.strategy( ref long sort.strategy )`

## Description
This function returns the current sort strategy in sort.strategy. For more details about the sort.strategy see function [gbf.set.sort.strategy()](gbf.set.sort.strategy.md).
This function may be used after the GBF run has finished to get the setting for this specific user, and restore them at the next run.

## Arguments
| | | |
|---|---|---|
| `ref long` | `sort.strategy` |  Returns the current sort strategy. For more information on the sort strategies see the [gbf.set.sort.strategy()](gbf.set.sort.strategy.md) call.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [gbf.get.sort.strategy()](gbf.get.sort.strategy.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
