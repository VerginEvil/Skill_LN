# bit.shiftl(), bit.shiftr()

## bit.shiftl

## Syntax:
`function long bit.shiftl( long bitpattern, long no_of_bits )`

## Description
Bitwise shift left function

## Arguments
| | | |
|---|---|---|
| `long` | `bitpattern` |  The value of which the bits of its two’s complement representation must be shifted. Preferably, this value should not be negative. For negative values, the normal shift behavior can be expected for bits which remain in the result. However, the behavior with respect to bits shifted out at the left side of the bit pattern is declared to be unspecified.  |
| `long` | `no_of_bits` |  The number of positions to shift. This value must not be negative. Do not expect any well-defined behavior for negative values. For example, shifting left over a negative number of bit positions is not specified as a right shift operation. This value must be less than the width of the bitpattern, i.e. it must be less than BitCountOfLong. Do not expect that shifting left over at least BitCountOfLong positions will result in value 0. Also, do not expect any other well-defined behavior.  |

## Return values
The function bit.shiftl returns the value bitpattern * 2^no_of_bits.
This is only specified for non-negative values of no_of_bits, less than BitCountOfLong.
If the exact result of this multiplication is not in the signed BitCountOfLong-bit range, then the result is unspecified. In practice, the same wrap around behavior can be expected as in normal arithmetic: repeatedly add or subtract 2^ BitCountOfLong until the result is in the allowed range.
In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, any case described above as not allowed or not specified, is considered as a fatal error and may (now or in a future version of the bshell) cause the current 3GL process to be terminated.

## Context
This function is implemented in the porting set and can be used in all script types.

## bit.shiftr

## Syntax:
`function long bit.shiftr( long bitpattern, long no_of_bits )`

## Description
Bitwise shift right function

## Arguments
| | | |
|---|---|---|
| `long` | `bitpattern` |  The value of which the bits of its two’s complement representation must be shifted. Preferably, this value should not be negative. For negative values, the normal shift behavior can be expected for bits which remain in the result. However, the behavior with respect to bits shifted in at the left side of the bit pattern is declared to be unspecified.  |
| `long` | `no_of_bits` |  The number of positions to shift. This value must not be negative. Do not expect any well-defined behavior for negative values. For example, shifting right over a negative number of bit positions is not specified as a left shift operation. This value must be less than the width of the bitpattern, i.e. it must be less than BitCountOfLong. Do not expect that shifting right over at least BitCountOfLong positions will result in value 0. Also, do not expect any other well-defined behavior.  |

## Return values
The function bit.shiftr returns the value bitpattern / 2^no_of_bits.
This is only specified for non-negative values of no_of_bits, less than BitCountOfLong.
Further, this return value is only specified for non-negative values of bitpattern. For negative values of bitpattern, normal shift behavior can be expected for bits which remain in the result. However, the behavior with respect to bits shifted in at the left side of the bit pattern is declared to be unspecified; it depends on the platform on which the bshell runs: fill vacated bits with zeroes or with the sign bit of the original value. Do not rely on it! Different versions of the bshell may behave differently and the same bshell version may behave differently on different platforms.
In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, any case described above as not allowed or not specified, is considered as a fatal error and may (now or in a future version of the bshell) cause the current 3GL process to be terminated.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long result
result = bit.shiftr( 0x63f, 2 )
```

## Related topics
- [Bit operations: overview and synopsis](bit_operations_overview_and_synopsis.md)
