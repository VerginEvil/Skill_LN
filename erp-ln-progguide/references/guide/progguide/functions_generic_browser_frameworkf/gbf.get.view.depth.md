# gbf.get.view.depth()

## Syntax:
`function long gbf.get.view.depth( ref long view.depth )`

## Description
Gets the current view depth.

## Arguments
| | | |
|---|---|---|
| `ref long` | `view.depth` |  The number of levels the GBF will display when the Open Level option in the File Menu is executed.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
