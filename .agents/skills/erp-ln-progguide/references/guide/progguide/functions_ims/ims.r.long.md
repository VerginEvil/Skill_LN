# ims.r.long()

## Syntax:
`function long ims.r.long( long bytearray )`

## Description
Reads a 32-bit value from the byte array. The 4 bytes read from the byte array are interpreted as the 32-bit two’s complement representation of a signed integer value.

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba. This function reads 4 bytes from the byte array.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream, or end-of-byte-array reached. Notice that this error value -1 cannot be distinguished from normal value -1. This is problematic, unless it is known that value -1 is not expected as a normal value to be read from the byte array. |
| >= -2^31 and < 2^31 | The numerical value of the 4 bytes read from the supplied byte array. This is a value in the signed 32-bit range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [ims.r.short()](ims.r.short.md)

- [ims.w.long()](ims.w.long.md)

- [ims.w.short()](ims.w.short.md)

- [UTC](../functions_date_time_zones/overview.md#utc)

- [ims.r.utc()](ims.r.utc.md)

- [ims.w.utc()](ims.w.utc.md)

- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
