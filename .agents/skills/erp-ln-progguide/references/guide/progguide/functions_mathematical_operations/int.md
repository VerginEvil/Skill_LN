# int()

## Syntax:
`function long int( double x )`

## Description
The function int() performs [explicit](../3gl_features/type_conversions.md#explicit_type_conversion) [double to long type conversion](../3gl_features/type_conversions.md#double_to_long_type_conversion).
If the supplied double value is positive, it is incremented by 0.0000001 as the first step of the conversion. If the supplied value is negative, it is decremented by 0.0000001 as the first step of the conversion. This is done to avoid rounding problems.
The next step of the explicit conversion uses the same algorithm as implicit double to long type conversion: discarding the fractional part of the double value, leaving only its integer part.
If the exact resulting integer value is outside the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range of the long data type, then the result is undefined.

## Arguments
| | | |
|---|---|---|
| `double` | `x` |    |

## Return values
The long value resulting from the described explicit [double to long type conversion](../3gl_features/type_conversions.md#double_to_long_type_conversion) applied to the supplied input value.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  Straightforward [assignment](../3gl_features/assignment_operator.md) of a floating point value to a variable of type long is allowed. The [implicit](../3gl_features/type_conversions.md#implicit_type_conversion) [double to long type conversion](../3gl_features/type_conversions.md#double_to_long_type_conversion) performed during such an assignment does not include the additional rounding applied beforehand by the [explicit](../3gl_features/type_conversions.md#explicit_type_conversion) [double to long type conversion](../3gl_features/type_conversions.md#double_to_long_type_conversion) performed by the function int().

## Related topics
- [Mathematical operations overview](overview.md)

- [Mathematical operations synopsis](synopsis.md)
