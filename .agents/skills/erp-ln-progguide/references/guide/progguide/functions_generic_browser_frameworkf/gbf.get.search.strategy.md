# gbf.get.search.strategy()

## Syntax:
`function long gbf.get.search.strategy( ref long search.strategy )`

## Description
Returns the current search strategy. The argument will be used to store the value. For more details about the search.strategy see function gbf.set.search.strategy().
This function may be used after the GBF run has finished, to get the setting for this specific user, and to restore the search.strategy at the next run.

## Arguments
| | | |
|---|---|---|
| `ref long` | `search.strategy` |  The current search strategy. For a list of search strategies, see gbf.set.search.strategy().  |

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
