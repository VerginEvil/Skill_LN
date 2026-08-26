# ims.skip()

## Syntax:
`function long ims.skip( long nrbytes, long bytearray )`

## Description
Skips forward a number of bytes in the byte array.

## Arguments
| | | |
|---|---|---|
| `long` | `nrbytes` |  The number of bytes to skip in the byte array  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream.  |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Restrictions
Can only be used in read mode.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)
- [Byte arrays synopsis](byte_arrays_synopsis.md)
