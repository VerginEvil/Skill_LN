# ims.putc$()

## Syntax:
`function string ims.putc$( string char, long bytearray )`

## Description
Writes a character to the current position in the byte array.

## Arguments
| | | |
|---|---|---|
| `string` | `char` |  The character to write to the byte array.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

## Return values
If no error occurs, the written character is returned. Otherwise, an empty string is returned.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
