# val()

## Syntax:
`function double val( string expr )`

## Description
This function converts the supplied textual representation to the represented floating point value or to the floating point value corresponding to the represented integer value.

## Arguments
| | | |
|---|---|---|
| `string` | `expr` |  |

## Return values
The numerical value of the supplied textual representation, or 0 if the supplied string cannot be interpreted as the textual representation of a numerical value.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- Inverse operation: [str$()](str.md)
- Conversion to integer type, with implicit bounds: [lval()](lval.md)
- Conversion to integer type, with explicit bounds: [string.to.bounded.long()](string.to.bounded.long.md)
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
