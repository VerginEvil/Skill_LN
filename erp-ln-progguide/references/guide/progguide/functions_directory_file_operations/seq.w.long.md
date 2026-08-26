# seq.w.long()

## Syntax:
`function long seq.w.long( long value, long fp )`

## Description
Writes a 32-bit integer value into the file.
The function seq.w.long() writes the 32 least significant bits of the two’s complement representation of the supplied integer value into the first 4 bytes of the supplied file.
The inverse function [seq.r.long()](seq.r.long.md) will retrieve the original supplied integer value, wrapped to the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]) by repeatedly adding or subtracting 2^32 until the value is in the signed 32-bit value range.
More specifically, the inverse function [seq.r.long()](seq.r.long.md) will retrieve the exact original supplied integer value if and only if that integer value is within the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the file. In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, it is a fatal error to supply a value outside the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-0x80000000 … 0x7fffffff] or [-2,147,483,648 … 2,147,483,647]). See [store.long()](../functions_string_operations/store.long.md) for a description of explicit wrapping that might be done beforehand.  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened. This function writes 4 bytes to the file.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *fp* is not a valid file pointer. The last system error is available in [predefined variable](../misc/predefined_variables.md) *e*.  |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- Related operations: [seq.w.short()](seq.w.short.md)
- Inverse operations: [seq.r.long()](seq.r.long.md), [seq.r.short()](seq.r.short.md)
- Special operations for UTC long format values: [seq.r.utc()](seq.r.utc.md), [seq.w.utc()](seq.w.utc.md)
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
