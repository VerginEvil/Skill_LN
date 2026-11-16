# round()

## Syntax:
`function double round( double value, long diga, long mode )`

## Description
This rounds a given value to a specified number of decimal places.

## Arguments
| | | |
|---|---|---|
| `double` | `value` |  The value to be rounded.  |
| `long` | `diga` |  The number of decimal places to which *value* is to be rounded.  |
| `long` | `mode` |  0 truncate (for example, both 1.5 and 1.49 are rounded down to 1) 1 normal round (for example, 1.5 is rounded up to 2; 1.49 is rounded down to 1) 2 round up (for example, both 1.5 and 1.49 are rounded up to 2)  |

## Return values
The rounded value. Or the original value ( *value*) if an error occurs.
Because the return value is of type double, the number of digits after the decimal sign is always 6. For example, round(1.345, 2, 1) returns 1.350000.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Mathematical operations overview](overview.md)

- [Mathematical operations synopsis](synopsis.md)
