# ims.read()

## Syntax:
`function long ims.read( ref string buffer, long nrBytes, long bytearray )`

## Description
Reads a number of bytes from the byte array into a buffer.

## Arguments
| | | |
|---|---|---|
| `ref string` | `buffer` |  The buffer that stores the bytes read from the byte array.  |
| `long` | `nrBytes` |  The number of bytes to read from the byte array into the buffer.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream. |
| 0 | End-of-byte-array. |
| > 0 | Number of bytes actually read. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
