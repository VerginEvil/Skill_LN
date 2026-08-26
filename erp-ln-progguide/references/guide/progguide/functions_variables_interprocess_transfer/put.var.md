# put.var()

## Syntax:
`function [long] put.var( long processno, string variable_name, void value )`

## Description

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |  The process to which the destination variable belongs. You can specify the process ID, or you can use the predefined variables *pid* or *parent*.  |
| `string` | `variable_name` |  The name of the external variable in the other process (this must be a lower case string).  |
| `void` | `value` |  The value to be assigned to the variable. Implicit conversion of the supplied value from its original type to the type of the specified variable is performed.  |

## Return values
| | |
|---|---|
| 0 | error; probably variable not found |
| 1 | success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and processno is a non trusted process

## Related topics
- [Variables (inter-process transfer) overview and synopsis](overview_and_synopsis.md)
