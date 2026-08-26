# get.long.arg()

## Syntax:
`function long get.long.arg( long arg_no )`

## Description
The function get.long.arg() returns the value of the specified argument, converted to a long.

## Arguments
| | | |
|---|---|---|
| `long` | `arg_no` |  The sequence number of an argument supplied to the currently executing function (i.e. the function in which *get.long.arg()* is called). The allowed range for this sequence number is 1 ... *get.argc()*.  |

## Return values
The value of the specified argument, converted to a long.
Implicit conversion of the value of the specified argument from its original type to type long is performed.
If arg_no is out of range, the value 0 is returned.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Functions with variable number of arguments: overview](overview.md)
- [Functions with variable number of arguments: synopsis](synopsis.md)
- [Functions with variable number of arguments: sample program](example.md)
