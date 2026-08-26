# seq.w.short()

## Syntax:
`function long seq.w.short( long value, long fp )`

## Description
Writes a 16-bit integer value into the file.
The function seq.w.short() writes the 16 least significant bits of the two’s complement representation of the supplied integer value into the first 2 bytes of the supplied file.
The inverse function [seq.r.short()](seq.r.short.md) will retrieve the original supplied integer value, wrapped to the *unsigned* 16-bit value range [0 … 2^16 - 1] (i.e. [0 … 65,535]) by repeatedly adding or subtracting 2^16 until the value is in the *unsigned* 16-bit value range.
More specifically, the inverse function [seq.r.short()](seq.r.short.md) will retrieve the exact original supplied integer value if and only if that integer value is within the *unsigned* 16-bit value range [0 … 2^16 - 1] (i.e. [0 … 65,535]).

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the file It is not an error (but it is not encouraged) to supply a value outside the unsigned 16-bit value range [0 … 2^16 - 1] (i.e. [0 … 0xffff] or [0 … 65,535]), for which the inverse function [seq.r.short()](seq.r.short.md) will retrieve the original supplied integer value. Explicit wrapping of the input value may be done beforehand by means of the 'remainder after division by 0x10000' operator `\ 0x10000`. However, for a negative input value, the result of the expression `value \ 0x10000` is still not in the desired range [0 … 0xffff] but in the range [-0xffff] … 0]. For complete wrapping to the desired range [0 … 0xffff], the following expression may be used: `(value \ 0x10000 + 0x10000) \ 0x10000`. In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, it *is* a fatal error to supply a value outside the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened. This function writes 2 bytes to the file.  |

## Return values
| | |
|---|---|
| -1 | Error, most probably *fp* is not a valid file pointer. The last system error is available in [predefined variable](../misc/predefined_variables.md) *e*.  |
| 0 | Success. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- Related operations: [seq.w.long()](seq.w.long.md)
- Inverse operations: [seq.r.long()](seq.r.long.md), [seq.r.short()](seq.r.short.md)
- Special operations for UTC long format values: [seq.r.utc()](seq.r.utc.md), [seq.w.utc()](seq.w.utc.md)
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
