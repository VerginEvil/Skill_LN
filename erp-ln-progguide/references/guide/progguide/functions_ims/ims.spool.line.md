# ims.spool.line()

## Syntax:
`function long ims.spool.line( ref string line, long bytearray )`

## Description
Spools a line and writes it to the byte array. The characters in the line are copied to the byte array until the last non-white character in the line is encountered. After that, the contents of the line is cleared.

## Arguments
| | | |
|---|---|---|
| `ref string` | `line` |  The line to spool to the byte array.  |
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba or ims.openfba.  |

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
