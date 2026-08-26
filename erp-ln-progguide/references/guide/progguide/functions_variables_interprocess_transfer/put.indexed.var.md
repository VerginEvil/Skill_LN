# put.indexed.var()

## Syntax:
`function [long] put.indexed.var( long processno, string variable_name, void value, long dim1 [, dim2, dim3, dim4 ] )`

## Description

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |  The process to which the destination variable belongs. You can specify the process ID, or you can use the predefined variables *pid* or *parent*.  |
| `string` | `variable_name` |  The name of the external variable in the other process (this must be a lower case string).  |
| `void` | `value` |  The value to be assigned to the variable. Implicit conversion of the supplied value from its original type to the type of the specified variable is performed.  |
| `long` | `dim1 [, dim2, dim3, dim4 ]` |  Use these to specify a particular array element to which the new value is to be assigned. To assign a single variable value, set dim1 to 1 and omit the other *dim* arguments.  |

## Return values
| | |
|---|---|
| 0 | success |
| 1 | general error |
| 2 | incorrect number of dimensions |
| 3 | variable not found |
| 4 | array element not available |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and processno is a non trusted process

## Example
```

extern string tst_str(25)
extern long   ltbl(10,5)

string ret_str(10)
long ret_lng
long e

ret_str = "Hello"
e = put.indexed.var( pid, "tst_str", ret_str, 1 )

ret_lng = 8
e = put.indexed.var( pid, "ltbl", ret_lng, 1, 1 )
ret_lng = 10
e = put.indexed.var( pid, "ltbl", ret_lng, 1, 2 )
ret_lng = 4
e = put.indexed.var( pid, "ltbl", ret_lng, 2, 1 )
ret_lng = 2
e = put.indexed.var( pid, "ltbl", ret_lng, 2, 2 )
        | table is filled as follows:
        | ltbl(1,1) = 8
        | ltbl(1,2) = 10
        | ltbl(2,1) = 4
        | ltbl(2,2) = 2
```

## Related topics
- [Variables (inter-process transfer) overview and synopsis](overview_and_synopsis.md)
