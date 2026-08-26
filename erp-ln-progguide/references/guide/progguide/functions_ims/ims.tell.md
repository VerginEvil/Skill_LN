# ims.tell()

## Syntax:
`function long ims.tell( long byetarray )`

## Description
Returns the current offset within the byte array relative to the begin of the byte array.

## Arguments
| | | |
|---|---|---|
| `long` | `byetarray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream.  |
| >= 0 | Offset, in number of bytes, within the byte array.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)
- [Byte arrays synopsis](byte_arrays_synopsis.md)
