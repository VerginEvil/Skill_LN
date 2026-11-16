# ims.openfba()

## Syntax:
`function long ims.openfba( string buffer, long size, string type )`

## Description
Opens a Fixed Byte Array (FBA).
The following code fragment shows an example of how to create an FBA:
```

string  buffer(1)       based
long    size
long    stream.id

size = 1024
alloc.mem(buffer, size)
stream.id = ims.openFBA(buffer, size, "r+")
```

## Arguments
| | | |
|---|---|---|
| `string` | `buffer` |  Stores the byte array. It may already contain information before the invocation of this function.  |
| `long` | `size` |  Size of the buffer.  |
| `string` | `type` |  The mode in which the byte array must be opened. This can be one of the following options: "r": Open for reading. The current position is placed at the start of the byte array. "w": Open for writing. The byte array is created if it does not already exist. The current position is placed at the start of the byte array. "a": Open for writing. The byte array is created if it does not already exist. The current position is placed at the end of the byte array. "x": Open for writing. This is the same as "w", except that the function fails if the byte array already exists. "r+": Same as "r", but it can also be written to. "w+": Same as "w", but it can also be read. "a+": Same as "a", but it can also be read. "x+": Same as "x", but it can also be read.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *buffer* is not a valid stream, the *type* is invalid or the byte array is full. |
| > 0 | Success. A byte array identifier was returned.. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Important
Do *not* reallocate *buffer* when it is already in use by an FBA. This will cause the Bshell to crash. In the code above, do not call an alloc.mem(buffer, newSize) after the FBA has been opened.

## Related topics
- [Byte arrays overview](byte_arrays_overview.md)

- [Byte arrays synopsis](byte_arrays_synopsis.md)
