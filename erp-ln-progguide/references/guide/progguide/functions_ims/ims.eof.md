# ims.eof()

## Syntax:
`function long ims.eof( long bytearray )`

## Description
Detects if the end of the byte array is reached.

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream.  |
| 0 | Not at the end of the byte array. |
| > 0 | The end of the byte array is detected. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)
- [Byte arrays synopsis](byte_arrays_synopsis.md)
