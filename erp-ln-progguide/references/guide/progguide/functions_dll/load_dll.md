# load_dll()

## Syntax:
`function long load_dll( string dll_name, [ long overload ] )`

## Description
This loads a specified DLL.
You can use it in combination with [get_function()](get_function.md) and [exec_function()](exec_function.md) to call and execute a function in a DLL. These three functions provide a fast algorithm for accessing a function that is to be executed more than once. You load the DLL and function only once and can then execute the function any number of times. *load_dll()* returns an identification number that the other functions use to identify a particular DLL.
You can also use *load_dll()* to replace one or more functions within a DLL by overloading a different DLL containing functions with the same names and arguments. But note that once a function has been loaded from a DLL, that DLL cannot subsequently be overloaded.
For a full discussion on function overloading, see [Function overloading](../dynamic_link_libraries/function_overloading.md).

## Arguments
| | | |
|---|---|---|
| `string` | `dll_name` |  The name of the DLL.  |
| `[ long` | `overload ]` |  This optional argument sets the overload flag for the specified DLL. The possible values are:  |

## Return values
| | |
|---|---|
| > 0 | DLL identifier. |
| 0 | Error; DLL not found or No license to run object |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  You cannot load the same DLL more than once within the same process. If you call *load_dll()* a second time, it returns the same identification number as it did the first time. However, you can use subsequent calls to *load_dll()* to change the value of the overload flag.
The *load_dll()* function must be called before the first function call to the DLL. Once a function has been found in one of the loaded DLLs, the function address is resolved. That address is used for all subsequent function calls; it cannot be replaced by overloading another DLL.

## Related topics
- [DLL functions (executing) overview and synopsis](overview_and_synopsis.md)
