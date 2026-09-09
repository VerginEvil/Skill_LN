# ims.w.short()

## Syntax:
`function long ims.w.short( long value, long bytearray )`

## Description
Writes a 16-bit integer value into the byte array.
The function ims.w.short() writes the 16 least significant bits of the two’s complement representation of the supplied integer value into the first 2 bytes of the supplied byte array.
The inverse function [ims.r.short()](ims.r.short.md) will retrieve the original supplied integer value, wrapped to the *unsigned* 16-bit value range [0 … 2^16 - 1] (i.e. [0 … 65,535]) by repeatedly adding or subtracting 2^16 until the value is in the *unsigned* 16-bit value range.
More specifically, the inverse function [ims.r.short()](ims.r.short.md) will retrieve the exact original supplied integer value if and only if that integer value is within the *unsigned* 16-bit value range [0 … 2^16 - 1] (i.e. [0 … 65,535]).

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the byte array It is not an error (but it is not encouraged) to supply a value outside the unsigned 16-bit value range [0 … 2^16 - 1] (i.e. [0 … 0xffff] or [0 … 65,535]), for which the inverse function [ims.r.short()](ims.r.short.md) will retrieve the original supplied integer value. Explicit wrapping of the input value may be done beforehand by means of the 'remainder after division by 0x10000' operator `\ 0x10000`. However, for a negative input value, the result of the expression `value \ 0x10000` is still not in the desired range [0 … 0xffff] but in the range [-0xffff] … 0]. For complete wrapping to the desired range [0 … 0xffff], the following expression may be used: `(value \ 0x10000 + 0x10000) \ 0x10000`. In [64-bit mode](../3gl_features/data_types.md#Long64), the bshell is less forgiving than in [32-bit mode](../3gl_features/data_types.md#Long32). When the bshell is in 64-bit mode, it *is* a fatal error to supply a value outside the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba. This function writes 2 bytes into the byte array.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream. |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [ims.w.long()](ims.w.long.md)

- [ims.r.long()](ims.r.long.md)

- [ims.r.short()](ims.r.short.md)

- [UTC](../functions_date_time_zones/overview.md#utc)

- [ims.r.utc()](ims.r.utc.md)

- [ims.w.utc()](ims.w.utc.md)

- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
