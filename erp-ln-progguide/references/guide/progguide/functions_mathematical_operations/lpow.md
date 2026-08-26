# lpow()

## Syntax:
`function long lpow( long x, long y )`

## Description
This computes the value of *x* raised to the power of *y*. The *y* argument must be positive.

## Arguments
| | | |
|---|---|---|
| `long` | `x` |  |
| `long` | `y` |  |

## Return values
The value of x^y, (i.e. *x* to the power of *y*).
If *y* is zero, the return value is always 1.
When the exact resulting value is outside the signed BitCountOfLong-bit value range, then the result is undefined.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Mathematical operations overview](overview.md)
- [Mathematical operations synopsis](synopsis.md)
