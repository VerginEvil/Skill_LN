# store.byte()

## Syntax:
`function void store.byte( long value, ref string rec$ )`

## Description
The function store.byte() treats the supplied string merely as a sequence of bytes.
The function store.byte() writes the 8 least significant bits of the two’s complement representation of the supplied integer value into the first byte of the supplied string.
The inverse function [load.byte()](load.byte.md) will retrieve the original supplied integer value, wrapped to the *unsigned* 8-bit value range [0 … 2^8 - 1] (i.e. [0 … 255]) by repeatedly adding or subtracting 2^8 until the value is in the *unsigned* 8-bit value range.
More specifically, the inverse function [load.byte()](load.byte.md) will retrieve the exact original supplied integer value if and only if that integer value is within the *unsigned* 8-bit value range [0 … 2^8 - 1] (i.e. [0 … 255]).
This function is machine independent and can be used (for example) in network communications.

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the string. It is not an error (but it is not encouraged) to supply a value outside the unsigned 8-bit value range [0 … 2^8 - 1] (i.e. [0 … 255]), for which the inverse function [load.byte()](load.byte.md) will retrieve the original supplied integer value. Explicit wrapping of the input value may be done beforehand by means of the 'remainder after division by 256' operator `\ 256`. However, for a negative input value, the result of the expression `value \ 256` is still not in the desired range [0 … 255] but in the range [-255 … 0]. For complete wrapping to the desired range [0 … 255], the following expression may be used: `(value \ 256 + 256) \ 256`. A different approach of the complete wrapping to the desired range [0 … 255] would be to use the following expression: `bit.and( 255, value )`. In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, it *is* a fatal error to supply a value outside the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).  |
| `ref string` | `rec$` |  String of which the first byte will be filled. Any further bytes of the string are left unchanged. It is an error to supply a string with a byte limit less than 1. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Store a byte at position 2 in a string
string tmp(4)
store.byte(65,tmp(2))
| tmp(2;1) will now contain the byte 65 (in the debugger it shows "A")
```

## Related topics
- Related operations: [store.double()](store.double.md), [store.float()](store.float.md), [store.long()](store.long.md), [store.short()](store.short.md)
- Inverse operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.float()](load.float.md), [load.long()](load.long.md), [load.short()](load.short.md)
- Special operations for UTC long format values: [load.utc()](load.utc.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
