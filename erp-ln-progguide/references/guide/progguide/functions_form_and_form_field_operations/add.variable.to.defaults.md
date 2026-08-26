# add.variable.to.defaults()

## Syntax:
`function void add.variable.to.defaults( string var_name, long var_type )`

## Description
Save other variables in the user defaults which are not on the form. All form fields are stored automatically in the user’s defaults when the save.defaults command is executed.

## Arguments
| | | |
|---|---|---|
| `string` | `var_name` |  The name of the variable to be added, this must be declared as an external variable in the script. To save a particular element of an array variable to the user default, append the element number (in parentheses) to the variable name. The element number must be an integer, formatted as a string. It cannot be a variable. For example: “a_array(5)”.  |
| `long` | `var_type` |  The database type of the variable to be added.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  This function should only be used in the before.program section.
This functionality is not supported for satellite sessions, as for satellites key values are not saved. Satellites are started by a "get defaults". On the overview variant, the saved default could result in inconsistent values if no record had been saved in the satellite.

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
