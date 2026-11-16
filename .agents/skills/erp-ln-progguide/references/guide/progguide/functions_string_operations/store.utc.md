# store.utc()

## Syntax:
`function void store.utc( long value, ref string rec$, [ long byte.count ] )`

## Description
The function store.utc() treats the supplied string merely as a sequence of bytes.
The function store.utc() writes the *byte.count* least significant bytes of the two’s complement representation of the supplied integer value into the first *byte.count* bytes of the supplied string.
The inverse function [load.utc()](load.utc.md) will retrieve the original supplied integer value, wrapped to the signed *byte.count*-byte value range [-(256^ *byte.count*)/2 … (256^ *byte.count*)/2 - 1] by repeatedly adding or subtracting 256^ *byte.count* until the value is in the signed *byte.count*-byte value range.
More specifically, the inverse function [load.utc()](load.utc.md) will retrieve the exact original supplied integer value if and only if that integer value is within the signed *byte.count*-byte value range [-(256^ *byte.count*)/2 … (256^ *byte.count*)/2 - 1].
This function is machine independent and can be used (for example) in network communications.

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the string. Typically, this is a (non-negative) [UTC](../functions_date_time_zones/overview.md#utc) long format value. In [64-bit mode](../3gl_features/data_types.md#Long64), the bshell is less forgiving than in [32-bit mode](../3gl_features/data_types.md#Long32). When the bshell is in 64-bit mode, it is a fatal error to supply a negative *value*. When the bshell is in 64-bit mode, it is a fatal error to supply a *value* which cannot be stored in the available *byte.count* bytes without loss of information. Typically, this is the case when *byte.count* is 4 and the supplied *value* is outside the signed 32-bit value range, i.e. is greater than 2,147,483,647 (0x7fff,ffff), which corresponds to January 19, 2038, 03:14:07 UTC. When the bshell is in 64-bit mode, it is a fatal error to supply a *value* which is a [UTC](../functions_date_time_zones/overview.md#utc) long format value greater than the current maximum DB.TIME domain value. Typically, this maximum is 253,402,214,400 (0x3a,fff2,f000), which corresponds to the begin of the last day of the last four-digit year, i.e. December 31, 9999, 00:00:00 UTC.  |
| `ref string` | `rec$` |  String of which the first *byte.count* bytes will be filled. Any further bytes of the string are left unchanged. It is an error to supply a string with a [byte capacity](../3gl_features/data_types.md#byte capacity) less than *byte.count*. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |
| `[ long` | `byte.count ]` |  Optional argument specifying the number of bytes to be written to *rec$*. Allowed values are 4, 5, and 8. Any other value is interpreted as 4. Default value is [ByteCountOfUtc](../functions_date_time_zones/overview.md#ByteCountOfUtc). According to the value of this argument, the (big endian) byte layout of the [Utc32 mode](../functions_date_time_zones/overview.md#Utc32), the [Utc40 mode](../functions_date_time_zones/overview.md#Utc40), or the [Utc64 mode](../functions_date_time_zones/overview.md#Utc64) is used.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- [store.byte()](store.byte.md)

- [store.double()](store.double.md)

- [store.float()](store.float.md)

- [store.long()](store.long.md)

- [store.short()](store.short.md)

- [load.byte()](load.byte.md)

- [load.double()](load.double.md)

- [load.float()](load.float.md)

- [load.long()](load.long.md)

- [load.short()](load.short.md)

- [load.utc()](load.utc.md)

- [capacity in bytes](../3gl_features/data_types.md#byte capacity)

- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)

- [Universal Coordinated Time](../functions_date_time_zones/overview.md#utc)

- [BitCountOfUtc](../functions_date_time_zones/overview.md#BitCountOfUtc)

- [ByteCountOfUtc](../functions_date_time_zones/overview.md#ByteCountOfUtc)

- [Utc32 mode](../functions_date_time_zones/overview.md#Utc32)

- [Utc40 mode](../functions_date_time_zones/overview.md#Utc40)

- [Utc64 mode](../functions_date_time_zones/overview.md#Utc64)
