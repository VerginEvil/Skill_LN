# ims.getproperties()

## Syntax:
`function long ims.getproperties( long bytearray, ref string buffer, [ ref long size ] )`

## Description
Returns the properties of the byte array.

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |
| `ref string` | `buffer` |  The contents of the byte array, this buffer must be declared BASED.  |
| `[ ref long` | `size ]` |  The number of bytes in the byte array, if specified.  |

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
