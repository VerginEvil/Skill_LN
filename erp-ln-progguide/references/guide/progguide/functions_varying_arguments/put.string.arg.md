# put.string.arg()

## Syntax:
`function long put.string.arg( long arg_no, string value )`

## Description
The function put.string.arg() assigns the supplied string value to the specified argument, after conversion to the type of the argument.

## Arguments
| | | |
|---|---|---|
| `long` | `arg_no` |  The sequence number of an argument supplied to the currently executing function (i.e. the function in which *put.string.arg()* is called). The allowed range for this sequence number is 1 ... *get.argc()*.  |
| `string` | `value` |  The value to assign to the specified argument. Implicit conversion of the supplied string value to the type of the specified argument is performed.  |

## Return values
| | |
|---|---|
| 0 | The function terminated successfully. |
| -1 | The function terminated with an error: *arg_no* is out of range or it is not possible to assign a value to the specified argument.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Functions with variable number of arguments: overview](overview.md)
- [Functions with variable number of arguments: synopsis](synopsis.md)
- [Functions with variable number of arguments: sample program](example.md)
