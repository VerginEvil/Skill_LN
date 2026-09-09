# get.string.arg()

## Syntax:
`function string get.string.arg( long arg_no )`

## Description
The function get.string.arg() returns the value of the specified argument, converted to a string.

## Arguments
| | | |
|---|---|---|
| `long` | `arg_no` |  The sequence number of an argument supplied to the currently executing function (i.e. the function in which *get.string.arg()* is called). The allowed range for this sequence number is 1... *get.argc()*.  |

## Return values
The value of the specified argument, converted to a string.
[Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of the value of the specified argument from its original type to type string is performed.
If arg_no is out of range, the empty string is returned.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Functions with variable number of arguments: overview](overview.md)

- [Functions with variable number of arguments: synopsis](synopsis.md)

- [Functions with variable number of arguments: sample program](example.md)
