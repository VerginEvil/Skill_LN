# gbf.set.help.function()

## Syntax:
`function long gbf.set.help.function( const string dll_id(), const string help.function.name(), long is.default )`

## Description
This function adds a new help function to the help functions. If the help.function.name resides in the same source file as in which the call to this [gbf.set.help.function()](gbf.set.help.function.md) is made, then the function [gbf.current.library()](gbf.current.library.md) can be used, so use: gbf.set.help.function(gbf.current.library(), …). Note that the help.function.name function must be defined as:
function extern help.function.name(long obj.id, const string object.key(), long obj.value, long help.value)
The dll_id is tried to be loaded with the load_dll() function call, without overload. The value, if positive, which is returned by gbf.set.help.function() may be used in subsequent [gbf.add.object()](gbf.add.object.md) calls to identify this special help function.

## Arguments
| | | |
|---|---|---|
| `const string` | `dll_id()` |  The name of the DLL.  |
| `const string` | `help.function.name()` |  The name of the help function to find in the DLL.  |
| `long` | `is.default` |  If set to true the function is used as the default help function instead of a previous defined default or the standard [gbf.help.selected()](gbf.help.selected.md) function.  |

## Return values
| | |
|---|---|
| > 1 | The identification of this help function |
| 1 | Should never be returned, as 1 is the GBF default  |
| GBF.ILL.DLL | Illegal DLL specified |
| GBF.ILL.FUNCTION | Illegal function specified, or function not known in given DLL  |
| GBF.NO.MEMORY | Not enough memory |
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
