# abs()

## Syntax:
`function double abs( void value )`

## Description
This function returns the absolute value of the supplied numeric value.

## Arguments
| | | |
|---|---|---|
| `void` | `value` |  Numeric value of which the absolute value must be returned.  |

## Return values
If the type of the input value is not double, then implicit type conversion of the input value to type long is performed.
Then, if the resulting value (of type double or of type long) is negative, the unary minus operator is applied to it.
Finally, the resulting value (of type double or of type long) is returned.
Notice that, even though the return type is specified as 'double', the run time type of the return value can be 'long'. No implicit type conversion to double is performed at this point!

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Mathematical operations overview](overview.md)
- [Mathematical operations synopsis](synopsis.md)
