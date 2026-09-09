# ims.setvbaproperties()

## Syntax:
`function long ims.setvbaproperties( long bytearray, long increment )`

## Description
Sets the properties of the Variable Byte Array (VBA).

## Arguments
| | | |
|---|---|---|
| `long` | `bytearray` |  The byte array identifier that is returned by ims.openvba.  |
| `long` | `increment` |  The number of bytes to increase the VBA with when needed.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *bytearrray* is not a variable byte array. |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
