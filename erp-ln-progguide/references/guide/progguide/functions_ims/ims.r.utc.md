# ims.r.utc()

## Syntax:
`function long ims.r.utc( long bytearray, [ long byte.count ] )`

## Description
Reads a specified amount of bytes from the byte array. The bytes read from the byte array are interpreted as the two’s complement representation of a signed integer value.

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba. This function reads an amount of bytes from the byte array as specified by *byte.count*.  |
| `[ long` | `byte.count ]` |  Optional argument specifying the amount of bytes to be read from the byte array. Allowed values are 4, 5, and 8. Any other value is interpreted as 4. Default value is ByteCountOfUtc. According to the value of this argument, the (big endian) byte layout of the Utc32 mode, the Utc40 mode, or the Utc64 mode is used.  |

## Return values
| | |
|---|---|
| -1 |  Error, most probably *bytearray* is not a valid stream, or end-of-byte-array reached. Notice that this error value -1 cannot be distinguished from normal value -1. This is problematic, unless it is known that value -1 is not expected as a normal value to be read from the byte array.  |
| >= -(256^ *byte.count*)/2 and < (256^ *byte.count*)/2  |  The numerical value of the bytes read from the supplied byte array. Typically, this is a (non-negative) UTC long format value stored earlier by the function [ims.w.utc()](ims.w.utc.md), or prepared by any other means. This function does not perform any value check.  |

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2000.

## Related topics
- Related operations: [ims.r.long()](ims.r.long.md), [ims.r.short()](ims.r.short.md)
- Inverse operations: [ims.w.long()](ims.w.long.md), [ims.w.short()](ims.w.short.md), [ims.w.utc()](ims.w.utc.md)
- [Byte arrays overview](byte_arrays_overview.md)
- [Byte arrays synopsis](byte_arrays_synopsis.md)
- Universal Coordinated Time
- BitCountOfUtc
- ByteCountOfUtc
- Utc32 mode
- Utc40 mode
- Utc64 mode
