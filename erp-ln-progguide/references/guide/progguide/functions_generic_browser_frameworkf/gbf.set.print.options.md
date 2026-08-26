# gbf.set.print.options()

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.print.options( long print.options )`

## Description
This function sets the print options.

## Arguments
| | | |
|---|---|---|
| `long` | `print.options` |  The print.options is a combination of the following options. All these options should be added (bitwise) to construct the actual print.options value: Whether or not icon descriptions must be printed:  |

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
