# gbf.get.selected.nr()

## Syntax:
`function long gbf.get.selected.nr( )`

## Description
This function returns the current number of selected objects. It can be used to obtain the maximum allowed index for [gbf.get.selected()](gbf.get.selected.md).

## Return values
| | |
|---|---|
| > 0 | Successful completion, the actual number of selected objects is returned  |
| 0 | Successful completion, but currently no objects are selected  |
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
