# exec_dll_function()

## Syntax:
`function long exec_dll_function( string dll_name, string function_name, [ ref void return_value, void ... ] )`

## Description
This loads a specified DLL and executes a specified function within that DLL. It provides a fast algorithm for executing a DLL function that is to be executed only once. If the DLL is already loaded, the identification number of the loaded DLL is used to search for the specified function. Otherwise, a load_dll(dll_name, 0) call is executed automatically. If a function is to be called more than once, it is faster to use the [load_dll()](load_dll.md), [get_function()](get_function.md), and [exec_function()](exec_function.md) combination.

## Arguments
| | | |
|---|---|---|
| `string` | `dll_name` |  The name of the DLL that must be loaded.  |
| `string` | `function_name` |  The name of the function that must be executed.  |
| `[ ref void` | `return_value ]` |  Optional reference argument to which the return value of the function call must be assigned. Implicit conversion of the return value of the function call from its original type to the type of the reference argument is performed. This argument can be omitted only if the function is called without any arguments and the function is either of type void (this means that no value is returned) or its return value is not needed. If the function is of type void and is called with any arguments, then the *return_value* argument must be supplied. No value will be assigned to the supplied reference argument.  |
| `[ void` | `... ]` |  The values to be passed as arguments to the function call. An error occurs when any of the supplied values is of a different type than the required type of the corresponding argument of the function to be called. If any argument values for the function call are supplied, then first the *return_value* argument must be supplied.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error; DLL not found. |
| -2 | Error; Function not found. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long ret, ret2

ret=exec_dll_function("otisfc0220", "ptisfc0220.store.quantities",
                       ret2, tibom010.noun, tibom010.qana,
tibom010.scpf )
```

## Related topics
- [DLL functions (executing) overview and synopsis](overview_and_synopsis.md)
