# ims.close()

## Syntax:
`function long ims.close( long bytearray )`

## Description
Closes the byte array. This is done automaticallly when you leave your process.
For a variable byte array (VBA), the claimed memory will be freed.
For a fixed byte array (FBA), the used memory buffer has to be freed manually (or is freed automatically when you leave your process).

## Arguments
| | | |
|---|---|---|
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
