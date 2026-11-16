# import.4gl.var()

## Syntax:
`function void import.4gl.var( string variable_name, ref void value )`

## Description
Imports a 'predefined' 4GL variable. Like number.of.marks which is actually a macro.

## Arguments
| | | |
|---|---|---|
| `string` | `variable_name` |  The name of the variable to be retrieved (this must be a lower case string). Alternately, you can specify a variable in which the name is stored.  |
| `ref void` | `value` |  This stores the value of the retrieved variable.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Currently only the following predefined variables can be imported:
number.of.marks
curr.key
In case an unknown variable is passed to this function, an ASSERT message pops up.

## Related topics
- [Variables (inter-process transfer) overview and synopsis](overview_and_synopsis.md)
