# ims.write()

## Syntax:
`function long ims.write( string buffer, long nrBytes, long bytearray )`

## Description
Appends a given number of bytes from the buffer into the byte array, beginning at the current position in the byte array.

## Arguments
| | | |
|---|---|---|
| `string` | `buffer` |  The buffer that contains the bytes to write into the byte array relative to the current position in the byte array.  |
| `long` | `nrBytes` |  The number of bytes to write from the buffer into the byte array.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream.  |
| 0 | End-of-byte-array. |
| > 0 | Number of bytes actually written. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)
- [Byte arrays synopsis](byte_arrays_synopsis.md)
