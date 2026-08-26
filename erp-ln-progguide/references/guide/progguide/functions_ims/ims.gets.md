# ims.gets()

## Syntax:
`function long ims.gets( ref string line, long size, long bytearray, [ long skip.mode, long there.was.more ] )`

## Description
Reads characters from the byte array into a buffer ( *line*).

## Arguments
| | | |
|---|---|---|
| `ref string` | `line` |  Stores the retrieved characters.  |
| `long` | `size` |  The maximum number of bytes to be read. Note that the function stops retrieving characters when a new line character is read or when the end-of-file is reached.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |
| `[ long` | `skip.mode ]` |  If *skip.mode* is set to: 0: read until a new-line character 1: read until *size* or until end-of-byte-array is reached.  |
| `[ long` | `there.was.more ]` |  There are more characters in the byte array than there were read.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearray* is not a valid stream.  |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)
- [Byte arrays synopsis](byte_arrays_synopsis.md)
