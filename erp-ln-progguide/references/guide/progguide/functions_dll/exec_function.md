# exec_function()

## Syntax:
`function long exec_function( long dll_id, long funct_id, [ ref void return_value, void ... ] )`

## Description
This executes a function previously loaded by a call to [get_function()](get_function.md). After the function has been loaded, you can call *exec_function()* any number of times to execute the function.

## Arguments
| | | |
|---|---|---|
| `long` | `dll_id` |  The identification number of the DLL that contains the function, as returned by [load_dll()](load_dll.md).  |
| `long` | `funct_id` |  The identification number of the function, as returned by [get_function()](get_function.md).  |
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

long dll_id, func_id
long ret, ret2

dll_id = load_dll("otisfc0220")
if dll_id then
       func_id = get_function( dll_id, "tisfc0220.store.quantities"
)
       if func_id then
           select tibom010.noun, tibom010.qana, tibom010.scpf
           from tibom010
           selectdo
               ret = exec_function( dll_id, func_id, ret2,
tibom010.noun,
                                    tibom010.qana, tibom010.scpf )
           endselect
       endif
endif
```

## Related topics
- [DLL functions (executing) overview and synopsis](overview_and_synopsis.md)
