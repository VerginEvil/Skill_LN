# gbf.set.drop.function()

## Syntax:
`function long gbf.set.drop.function( const string dll_id(), const string drop.function.name(), long is.default )`

## Description
Adds a new drag and drop function to the drag and drop functions. If the drop.function.name resides in the same source file as in which the call to this gbf.set.drop.function() is made, then the function [gbf.current.library()](gbf.current.library.md) can be used, so use: gbf.set.drop.function(gbf.current.library(), …). Note that the drop.function.name function must be defined as:
function extern long drop.function.name(long drag.obj, const string drag.key(), long drag.value, long drag.leaf, long drop.obj, const string drop.key(), long drop.value, long drop.leaf, long button.mode)
The dll_id is tried to be loaded with the load_dll() function call, without overload. The value, if non negative, which is returned by gbf.set.drop.function() may be used in subsequent [gbf.add.object()](gbf.add.object.md) and/or [gbf.update.object() *](gbf.update.md) calls to identify this special drag and drop function.

## Arguments
| | | |
|---|---|---|
| `const string` | `dll_id()` |  The name of the DLL.  |
| `const string` | `drop.function.name()` |  The name of the drag and drop function to find in the DLL.  |
| `long` | `is.default` |  If set to true this drag and drop function is used as the default, instead of a previous defined default drag and drop function or the standard [gbf.drag.drop()](gbf.drag.drop.md) function.  |

## Return values
| | |
|---|---|
| > 1 | The identification of this drag and drop function  |
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
