# ims.r.short()

## Syntax:
`function long ims.r.short( long bytearray )`

## Description
Reads a 16-bit value from the byte array. The 2 bytes read from the byte array are interpreted as the 16-bit binary representation of an unsigned integer value.

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba. This function reads 2 bytes from the byte array.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream, or end-of-byte-array reached. |
| >= 0 | The numerical value of the 2 bytes read from the supplied byte array. This is a value in the *unsigned* 16-bit range [0 … 2^16 - 1] (i.e. [0 … 65,535]). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [ims.r.long()](ims.r.long.md)

- [ims.w.long()](ims.w.long.md)

- [ims.w.short()](ims.w.short.md)

- [UTC](../functions_date_time_zones/overview.md#utc)

- [ims.r.utc()](ims.r.utc.md)

- [ims.w.utc()](ims.w.utc.md)

- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
