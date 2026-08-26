# ims.error()

## Syntax:
`function long ims.error( long bytearray )`

## Description
Detects if an error has occurred while reading from or writing to the byte array.

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream.  |
| 0 | No errors. |
| > 0 | An error occurred. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)
- [Byte arrays synopsis](byte_arrays_synopsis.md)
