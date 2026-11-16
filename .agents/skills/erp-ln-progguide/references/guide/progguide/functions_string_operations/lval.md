# lval()

## Syntax:
`function long lval( string string$ )`

## Description
This function performs explicit [string to long type conversion](../3gl_features/type_conversions.md#string_to_long_type_conversion). If the resulting value is within the limits of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range, that value is returned. Otherwise, the concerned bound is returned.

## Arguments
| | | |
|---|---|---|
| `string` | `string$` |  String value to be converted to a long value.  |

## Return values
| | | |
|---|---|---|
| Condition on exact conversion result | Description | Value returned by lval |
| >= -2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) and < 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) | success | exact conversion result |
| < -2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) | lower bound is applied | -2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) |
| >= 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) | upper bound is applied | 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) - 1 |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [string.to.bounded.long()](string.to.bounded.long.md)

- [str$()](str.md)

- [val()](val.md)

- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
