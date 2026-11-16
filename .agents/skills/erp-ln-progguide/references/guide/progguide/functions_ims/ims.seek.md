# ims.seek()

## Syntax:
`function long ims.seek( long offset, long opt, long bytearray )`

## Description
Changes the current position within the byte array.

## Arguments
| | | |
|---|---|---|
| `long` | `offset` |  The number of bytes  |
| `long` | `opt` |  Can be set to the following values: 0 New position is set *offset* bytes from the beginning of the *bytearray*. 1 New position is set *offset* bytes from the current position. 2 New position is set *offset* bytes from the end of the *bytearray*.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream. |
| >= 0 | New offset position from beginning of the byte array. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
