# import()

## Syntax:
`function [long] import( string variable_name, ref void value )`

## Description
Import retrieves the value of the specified variable of the parent process. This parent process is not always identified by the variable *parent* in case of dynamic index switching. When using dynamic index switching, the parent process is sometimes killed and restarted. This causes a different parent process, whereas the variable *parent* is not updated.
For all other circumstances, import is equivalent to get.var( parent, "variable", value).

## Arguments
| | | |
|---|---|---|
| `string` | `variable_name` |  The name of the variable to be retrieved (this must be a lower case string). Alternately, you can specify a variable in which the name is stored.  |
| `ref void` | `value` |  This stores the value of the retrieved variable.  |

## Return values
| | |
|---|---|
| 0 | error; probably variable not found in the parent process |
| 1 | success |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Variables (inter-process transfer) overview and synopsis](overview_and_synopsis.md)
