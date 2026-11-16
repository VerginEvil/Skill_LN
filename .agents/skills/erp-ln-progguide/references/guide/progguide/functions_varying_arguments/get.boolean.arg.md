# get.boolean.arg()

## Syntax:
`function boolean get.boolean.arg( long arg_no )`

## Description
The function get.boolean.arg() returns the value of the specified argument, converted to a boolean.

## Arguments
| | | |
|---|---|---|
| `long` | `arg_no` |  The sequence number of an argument supplied to the currently executing function (i.e. the function in which *get.boolean.arg()* is called). The allowed range for this sequence number is 1... *get.argc()*.  |

## Return values
The value of the specified argument, converted to a boolean.
[Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of the value of the specified argument from its original type to type boolean is performed.
If arg_no is out of range, the value false is returned.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Functions with variable number of arguments: overview](overview.md)

- [Functions with variable number of arguments: synopsis](synopsis.md)

- [Functions with variable number of arguments: sample program](example.md)
