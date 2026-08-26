# get_function()

## Syntax:
`function long get_function( long dll_id, string funct_name )`

## Description
This loads a specified function from a previously loaded DLL. It returns an identification number for the function.

## Arguments
| | | |
|---|---|---|
| `long` | `dll_id` |  The identification number of the DLL that contains the function, as returned by [load_dll()](load_dll.md).  |
| `string` | `funct_name` |  The function name.  |

## Return values
| | |
|---|---|
| > 0 | Function identifier. |
| 0 | Error; Function not found or DLL not loaded. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [DLL functions (executing) overview and synopsis](overview_and_synopsis.md)
