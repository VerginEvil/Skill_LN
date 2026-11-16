# gbf.set.menu.function()

## Syntax:
`function long gbf.set.menu.function( const string dll_id(), const string menu.function.id(), long is.default )`

## Description
This function adds a function to the menu functions. For more information about dll_id and menu.function.id see the standard dll manual page in the programmers manual. The dll_id is tried to be loaded with the load_dll() function call, without overload. The return value, if positive, may be used in subsequent [gbf.set.menu.item()](gbf.set.menu.item.md) calls to identify this special menu function.

## Arguments
| | | |
|---|---|---|
| `const string` | `dll_id()` |  The name of the DLL.  |
| `const string` | `menu.function.id()` |  The menu function to find in the DLL.  |
| `long` | `is.default` |  Indicates whether (if the value is true) or not (if the value is false) to use this menu function (if it could successfully be added) as the default menu function instead of a previous defined default or the standard [gbf.menu.selected()](gbf.menu.selected.md) function.  |

## Return values
| | |
|---|---|
| > 1 | The identification of this menu function |
| 1 | Should never be returned, as 1 is the GBF default |
| GBF.ILL.DLL | Illegal DLL specified |
| GBF.ILL.FUNCTION | Illegal function specified, or function not known in given DLL |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.NO.MEMORY | Not enough memory |

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
