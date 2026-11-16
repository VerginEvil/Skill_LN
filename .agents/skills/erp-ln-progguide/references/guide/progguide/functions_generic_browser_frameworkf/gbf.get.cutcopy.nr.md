# gbf.get.cutcopy.nr()

## Syntax:
`function long gbf.get.cutcopy.nr( )`

## Description
This function returns the number of objects that have been pasted into the so-called cut, copy and paste buffers. You can use the following user actions to fill the cut, copy and paste buffers:

- The menu commands Edit->Cut and Edit->Copy

- The keystrokes Ctrl+X and Ctrl+C

- The buttons Cut and Paste

- And all user defined menu commands that return a GBF.DO.CUTCOPY.INSERT (see [gbf.menu.selected()](gbf.menu.selected.md))

## Return values
| | |
|---|---|
| 0 | Successful completion, but cut, copy & paste buffers are empty |
| > 0 | Successful completion, returned value is number of objects in cut, copy & paste buffers |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [gbf.get.cutcopy()](gbf.get.cutcopy.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
