# gbf.set.child.function()

## Syntax:
`function long gbf.set.child.function( const string dll_id(), const string child.function.name(), long is.default )`

## Description
Adds a function to get children, to the set of all get children functions. If the child.function.name resides in the same source file as in which the call to this [gbf.set.child.function()](gbf.set.child.function.md) is made, then the function [gbf.current.library()](gbf.current.library.md) can be used, so use: gbf.set.child.function(gbf.current.library(), …).
Note that the child.function.name function must be defined as:
function extern long child.function.name(const string object.key(), long obj.value, long cur.level)
The dll_id is tried to be loaded with the load_dll() function call, without overload. The value, if positive, which is returned by [gbf.set.child.function()](gbf.set.child.function.md) may be used in subsequent [gbf.add.object()](gbf.add.object.md) and/or [gbf.update.object() *](gbf.update.md) calls to identify this child function.

## Arguments
| | | |
|---|---|---|
| `const string` | `dll_id()` |  The name of the DLL.  |
| `const string` | `child.function.name()` |  The name of the child function to find in the DLL.  |
| `long` | `is.default` |  If set to true this child function is set as the default child function. Only if it is successfully added.  |

## Return values
| | |
|---|---|
| > 1 | The identification of this child function |
| 1 | Should never be returned, as 1 is the GBF default |
| GBF.ILL.DLL | llegal DLL specified |
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
