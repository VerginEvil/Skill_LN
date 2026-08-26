# gbf.file.to.library()

## Syntax:
`function string gbf.file.to.library( const string filename() )`

## Description
Uses the given filename to guess the object name of the session. It replaces the first "p" (of program file) in the file name with an "o" (of object file) and removes the trailing digit (usually a 0, but in fact the variant number). This macro can be used when all session functions, such as gbf.get.top.level(), gbf.get.children(), [gbf.menu.selected()](gbf.menu.selected.md) and so on, reside in the source file name filename. When these functions gbf.get.top.level() and so on reside in the current file, [gbf.current.library()](gbf.current.library.md) should be used.

## Arguments
| | | |
|---|---|---|
| `const string` | `filename()` |  The program file name.  |

## Return values
The run time object name of the object file.

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
