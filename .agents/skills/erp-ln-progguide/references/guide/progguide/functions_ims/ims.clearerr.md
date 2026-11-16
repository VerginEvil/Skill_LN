# ims.clearerr()

## Syntax:
`function long ims.clearerr( long bytearray )`

## Description
Resets the error and end-of-byte-array indicator.

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream. |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
