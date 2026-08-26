# gbf.get.refresh.strategy()

## Syntax:
`function long gbf.get.refresh.strategy( ref long refresh.rate, ref long refresh.type )`

## Description
Returns the current automatic refreshing schema. The two arguments will be used to store the values. If refresh.rate is 0, then the refresh.type may not be a valid type (see also gbf.set.refresh.strategy()).
This function may be used after the GBF run has finished to get the setting for this specific user, and restore them at the next run.

## Arguments
| | | |
|---|---|---|
| `ref long` | `refresh.rate` |  Retuns the refresh rate.  |
| `ref long` | `refresh.type` |  Returns the refresh type.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
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
