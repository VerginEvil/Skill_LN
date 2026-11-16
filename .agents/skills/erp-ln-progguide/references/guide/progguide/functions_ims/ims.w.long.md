# ims.w.long()

## Syntax:
`function long ims.w.long( long value, long bytearray )`

## Description
Writes a 32-bit integer value into the byte array.
The function ims.w.long() writes the 32 least significant bits of the two’s complement representation of the supplied integer value into the first 4 bytes of the supplied byte array.
The inverse function [ims.r.long()](ims.r.long.md) will retrieve the original supplied integer value, wrapped to the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]) by repeatedly adding or subtracting 2^32 until the value is in the signed 32-bit value range.
More specifically, the inverse function [ims.r.long()](ims.r.long.md) will retrieve the exact original supplied integer value if and only if that integer value is within the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the byte array. In [64-bit mode](../3gl_features/data_types.md#Long64), the bshell is less forgiving than in [32-bit mode](../3gl_features/data_types.md#Long32). When the bshell is in 64-bit mode, it is a fatal error to supply a value outside the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-0x80000000 … 0x7fffffff] or [-2,147,483,648 … 2,147,483,647]). See [store.long()](../functions_string_operations/store.long.md) for a description of explicit wrapping that might be done beforehand.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba. This function writes 4 bytes into the byte array.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream. |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [ims.w.short()](ims.w.short.md)

- [ims.r.long()](ims.r.long.md)

- [ims.r.short()](ims.r.short.md)

- [UTC](../functions_date_time_zones/overview.md#utc)

- [ims.r.utc()](ims.r.utc.md)

- [ims.w.utc()](ims.w.utc.md)

- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
