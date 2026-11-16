# get.var()

## Syntax:
`function [long] get.var( long processno, string variable_name, ref void destination )`

## Description
This retrieves the value of the specified variable. The variable can be a single variable of any type or an array.

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |  The process from which the variable is to be retrieved. You can specify the process ID, or you can use the predefined variables *pid* or *parent*.  |
| `string` | `variable_name` |  The name of the variable to be retrieved (this must be a lower case string).  |
| `ref void` | `destination` |  Reference argument to which the value of the retrieved variable must be assigned. [Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of the value of the retrieved variable from its original type to the type of the reference argument is performed.  |

## Return values
| | |
|---|---|
| 0 | error; probably variable not found |
| 1 | success |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

extern domain ttaad.cjob  cjob
form.1:
init.form:
        get.var( parent, "cjob", ttaad500.cjob )
```

## Related topics
- [Variables (inter-process transfer) overview and synopsis](overview_and_synopsis.md)
