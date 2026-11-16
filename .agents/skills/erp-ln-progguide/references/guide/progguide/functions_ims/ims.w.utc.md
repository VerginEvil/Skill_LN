# ims.w.utc()

## Syntax:
`function long ims.w.utc( long value, long bytearray, [ long byte.count ] )`

## Description
Writes an integer value into the byte array.
The function ims.w.utc() writes the *byte.count* least significant bytes of the two’s complement representation of the supplied integer value into the first *byte.count* bytes of the supplied byte array.
The inverse function [ims.r.utc()](ims.r.utc.md) will retrieve the original supplied integer value, wrapped to the signed *byte.count*-byte value range [-(256^ *byte.count*)/2 … (256^ *byte.count*)/2 - 1] by repeatedly adding or subtracting 256^ *byte.count* until the value is in the signed *byte.count*-byte value range.
More specifically, the inverse function [ims.r.utc()](ims.r.utc.md) will retrieve the exact original supplied integer value if and only if that integer value is within the signed *byte.count*-byte value range [-(256^ *byte.count*)/2 … (256^ *byte.count*)/2 - 1].

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the byte array. Typically, this is a (non-negative) [UTC](../functions_date_time_zones/overview.md#utc) long format value. In [64-bit mode](../3gl_features/data_types.md#Long64), the bshell is less forgiving than in [32-bit mode](../3gl_features/data_types.md#Long32). When the bshell is in 64-bit mode, it is a fatal error to supply a negative *value*. When the bshell is in 64-bit mode, it is a fatal error to supply a *value* which cannot be stored in the available *byte.count* bytes without loss of information. Typically, this is the case when *byte.count* is 4 and the supplied *value* is outside the signed 32-bit value range, i.e. is greater than 2,147,483,647 (0x7fff,ffff), which corresponds to January 19, 2038, 03:14:07 UTC. When the bshell is in 64-bit mode, it is a fatal error to supply a *value* which is a [UTC](../functions_date_time_zones/overview.md#utc) long format value greater than the current maximum DB.TIME domain value. Typically, this maximum is 253,402,214,400 (0x3a,fff2,f000), which corresponds to the begin of the last day of the last four-digit year, i.e. December 31, 9999, 00:00:00 UTC.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba. This function writes a number of bytes to the byte array as specified by *byte.count*.  |
| `[ long` | `byte.count ]` |  Optional argument specifying the number of bytes to be written to the byte array. Allowed values are 4, 5, and 8. Any other value is interpreted as 4. Default value is [ByteCountOfUtc](../functions_date_time_zones/overview.md#ByteCountOfUtc). According to the value of this argument, the (big endian) byte layout of the [Utc32 mode](../functions_date_time_zones/overview.md#Utc32), the [Utc40 mode](../functions_date_time_zones/overview.md#Utc40), or the [Utc64 mode](../functions_date_time_zones/overview.md#Utc64) is used.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream. |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [ims.w.long()](ims.w.long.md)

- [ims.w.short()](ims.w.short.md)

- [ims.r.long()](ims.r.long.md)

- [ims.r.short()](ims.r.short.md)

- [ims.r.utc()](ims.r.utc.md)

- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)

- [Universal Coordinated Time](../functions_date_time_zones/overview.md#utc)

- [BitCountOfUtc](../functions_date_time_zones/overview.md#BitCountOfUtc)

- [ByteCountOfUtc](../functions_date_time_zones/overview.md#ByteCountOfUtc)

- [Utc32 mode](../functions_date_time_zones/overview.md#Utc32)

- [Utc40 mode](../functions_date_time_zones/overview.md#Utc40)

- [Utc64 mode](../functions_date_time_zones/overview.md#Utc64)
