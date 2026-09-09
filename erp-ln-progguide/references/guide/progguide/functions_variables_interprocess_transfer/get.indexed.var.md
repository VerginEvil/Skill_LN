# get.indexed.var()

## Syntax:
`function [long] get.indexed.var( long processno, string variable_name, ref void destination, long dim1 [, dim2, dim3, dim4 ] )`

## Description
This retrieves the value of the specified variable. It is the same as [get.var()](get.var.md) except that it enables retrieval of individual array elements.

## Arguments
| | | |
|---|---|---|
| `long` | `processno` |  The process from which the variable is to be retrieved. You can specify the process ID, or you can use the predefined variables *pid* or *parent*.  |
| `string` | `variable_name` |  The name of the variable to be retrieved (this must be a lower case string). The variable can be a single variable or an array and must be declared as external.  |
| `ref void` | `destination` |  Reference argument to which the value of the retrieved variable must be assigned. [Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of the value of the retrieved variable from its original type to the type of the reference argument is performed.  |
| `long` | `dim1 [, dim2, dim3, dim4 ]` |  Use these to specify a particular array element to be retrieved. To retrieve a single variable, set dim1 to 1 and omit the other *dim* arguments.  |

## Return values
| | |
|---|---|
| 0 | success |
| 1 | general error |
| 2 | incorrect number of dimensions |
| 3 | variable not found |
| 4 | array element not available |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

extern long ltbl(10,5)
extern string block(10,5,5)

string ret_str(10)
long ret_lng
long e

ltbl(1,1) = 1
ltbl(2,2) = 2
ltbl(3,3) = 3

block(1,1,1) = "The"
block(1,1,2) = "quick"
block(1,2,1) = "brown"
block(1,2,2) = "jumps"

e = get.indexed.var( pid, "block", ret_str, 1, 2 )
        | ret_str contains "quick     "
e = get.indexed.var( pid, "ltbl", ret_lng, 3, 3 )
        | ret_lng is equal to 3
```

## Related topics
- [Variables (inter-process transfer) overview and synopsis](overview_and_synopsis.md)
