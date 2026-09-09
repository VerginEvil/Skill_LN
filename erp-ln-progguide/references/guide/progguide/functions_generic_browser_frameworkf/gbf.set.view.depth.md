# gbf.set.view.depth()

## Syntax:
`function long gbf.set.view.depth( long view.depth )`

## Description
Sets the current view depth.

## Arguments
| | | |
|---|---|---|
| `long` | `view.depth` |  The number of levels the GBF will display when the Open Level option in the File Menu is executed. The value must be > 0. If the value is 1, only the top-level node with its direct children remain open. Special value GBF.READ.ALL can be specified to open all levels.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.LEVEL | Open.depth is not a valid number of levels: < 0 |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2100.
Note  This function must be called before calling function [gbf.init()](gbf.init.md). Otherwise, the Open Level option will not be visible within the File Menu.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
