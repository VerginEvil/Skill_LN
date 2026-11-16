# parse_and_exec_function()

## Syntax:
`function long parse_and_exec_function( string dll_name, string function_call, [ ref void return_value, ref string return_call ] )`

## Description
This function is similar to [exec_dll_function()](exec_dll_function.md). It loads a specified DLL and parses and executes a specified function within that DLL. If the DLL is already loaded, the identification number of the loaded DLL is used to search for the specified function. Otherwise, a load_dll(dll_name, 0) call is executed automatically.
Use this function only when the function and its arguments are known only at runtime. The function is intended for handing function calls received as strings from other processes.

## Arguments
| | | |
|---|---|---|
| `string` | `dll_name` |  The name of the DLL that must be loaded.  |
| `string` | `function_call` |  A string containing the function name and arguments. You can specify any function in this argument, except one that contains array arguments. To execute a function with array arguments, use *exec_dll_function()* instead. For each argument value, [implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of its string representation to the type of the function argument is performed.  |
| `[ ref void` | `return_value ]` |  Reference argument to which the return value of the function call must be assigned. [Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of the return value of the function call from its original type to the type of the reference argument is performed. If the function to be called is of type void (this means that no value is returned), then this argument must be omitted.  |
| `[ ref string` | `return_call ]` |  Reference argument which receives a representation of the function call after its execution. For reference arguments of the function, the resulting argument value is given. [Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of the represented values from their original type to the string type is performed.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error; DLL not found. |
| -2 | Error; Function not found. |
| -3 | Error; Syntax error in function call. |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  If the function call contains reference arguments, the result of the function call (stored in *return_call*) cannot become longer than the length of the *function_call* argument.

## Example
```

| assume the function my_max in DLL ttstdlib which returns the
| maximum of the two given arguments.
| object ottstdlib belongs to DLL ttstdlib

long   ret, ret2
long   a, b
string ret_call(80)
string funccall(80)

a = 30
b = 40

funccall = sprintf$("my_max(%d,%d)", a, b)

ret = parse_and_exec_function( "ottstdlib", funccall, ret2, ret_call )
| ret2 becomes 40
| ret_call becomes "my_max(30,40)"
```

## Related topics
- [DLL functions (executing) overview and synopsis](overview_and_synopsis.md)
