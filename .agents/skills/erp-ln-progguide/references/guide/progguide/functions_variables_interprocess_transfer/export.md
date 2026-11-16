# export()

## Syntax:
`function [long] export( string var_name, void value )`

## Description
Export assigns the value of the specified variable of the parent process. This parent process is not always identified by the variable *parent* in case of dynamic index switching. When using dynamic index switching, the parent process is sometimes stopped and restarted. This causes a different parent process, whereas the variable *parent* is not updated.
For all other circumstances, export is equivalent to put.var( parent, "variable", value).

## Arguments
| | | |
|---|---|---|
| `string` | `var_name` |  The name of the variable in the parent process export the value to  |
| `void` | `value` |  The value to export to the parent process  |

## Return values
| | |
|---|---|
| 0 | error; probably variable not found in the parent process |
| 1 | success |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Variables (inter-process transfer) overview and synopsis](overview_and_synopsis.md)
