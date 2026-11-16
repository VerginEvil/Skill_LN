# ims.openvba()

## Syntax:
`function long ims.openvba( string type, [ long initialSize, long increment ] )`

## Description
Opens a Variable Byte Array (VBA).

## Arguments
| | | |
|---|---|---|
| `string` | `type` |  The mode in which the byte array must be opened. This can be one of the following options: "r": Open for reading. The current position is placed at the start of the byte array. "w": Open for writing. The byte array is created if it does not already exist. The current position is placed at the start of the byte array. "a": Open for writing. The byte array is created if it does not already exist. The current position is placed at the end of the byte array. "x": Open for writing. This is the same as "w", except that the function fails if the byte array already exists. "r+": Same as "r", but it can also be written to. "w+": Same as "w", but it can also be read. "a+": Same as "a", but it can also be read. "x+": Same as "x", but it can also be read.  |
| `[ long` | `initialSize ]` |  The initial buffer size for the VBA. If not specified, the initial buffer size is 4096 bytes.  |
| `[ long` | `increment ]` |  Specifies the number of bytes to increment the VBA with, in case the VBA is full. If not specified, the buffer will be doubled in size.  |

## Return values
| | |
|---|---|
| -11 | Error, more than 512 streams are in use. |
| -1 | Error, most probably *bytearrray* is not a valid stream or the byte array is full. |
| > 0 | Success. A byte array identifier was returned. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
