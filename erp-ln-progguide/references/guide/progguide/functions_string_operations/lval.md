# lval()

## Syntax:
`function long lval( string string$ )`

## Description
This function performs explicit string to long type conversion. If the resulting value is within the limits of the signed BitCountOfLong-bit range, that value is returned. Otherwise, the concerned bound is returned.

## Arguments
| | | |
|---|---|---|
| `string` | `string$` |  String value to be converted to a long value.  |

## Return values
| | | |
|---|---|---|
| Condition on exact conversion result | Description | Value returned by lval |
| >= -2^( BitCountOfLong-1) and < 2^( BitCountOfLong-1)  | success | exact conversion result |
| < -2^( BitCountOfLong-1)  | lower bound is applied | -2^( BitCountOfLong-1)  |
| >= 2^( BitCountOfLong-1)  | upper bound is applied | 2^( BitCountOfLong-1) - 1  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- A similar function, but with explicit bounds: [string.to.bounded.long()](string.to.bounded.long.md)
- Inverse operation: [str$()](str.md)
- Conversion to floating point type: [val()](val.md)
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
