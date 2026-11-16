# halfadj()

## Syntax:
`function double halfadj( double value, long diga )`

## Description
This rounds a given value to a specified number of decimal places.

## Arguments
| | | |
|---|---|---|
| `double` | `value` |  The value to be rounded.  |
| `long` | `diga` |  The number of decimal places to which *value* is to be rounded.  |

## Return values
The rounded value. Or the original value ( *value*) if an error occurs.
Because the return value is of type double, the number of digits after the decimal sign is always 6. For example, halfadj(1.345, 2) returns 1.350000. The function is identical to round( value, diga, 1)

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Mathematical operations overview](overview.md)

- [Mathematical operations synopsis](synopsis.md)
