# store.short()

## Syntax:
`function void store.short( long value, ref string rec$ )`

## Description
The function store.short() treats the supplied string merely as a sequence of bytes.
The function store.short() writes the 16 least significant bits of the two’s complement representation of the supplied integer value into the first 2 bytes of the supplied string.
The inverse function [load.short()](load.short.md) will retrieve the original supplied integer value, wrapped to the signed 16-bit value range [-2^15 … 2^15 - 1] (i.e. [-32,768 … 32,767]) by repeatedly adding or subtracting 2^16 until the value is in the signed 16-bit value range.
More specifically, the inverse function [load.short()](load.short.md) will retrieve the exact original supplied integer value if and only if that integer value is within the signed 16-bit value range [-2^15 … 2^15 - 1] (i.e. [-32,768 … 32,767]).
This function is machine independent and can be used (for example) in network communications.

## Arguments
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the string. It is not an error (but it is not encouraged) to supply a value outside the signed 16-bit value range [-2^15 … 2^15 - 1] (i.e. [-0x8000 … 0x7fff] or [-32,768 … 32,767]), for which the inverse function [load.short()](load.short.md) will retrieve the original supplied integer value. Explicit wrapping of the input value may be done beforehand by means of the 'remainder after division by 0x10000' operator `\ 0x10000`. However, the result of the expression `value \ 0x10000` is still not in the desired range [-0x8000 … 0x7fff]. For a positive value, the result is in the range [0 … 0xffff], for a negative value it is in the range [-0xffff … 0]. For complete wrapping to the desired range [-0x8000 … 0x7fff], the following expression may be used: `(value \ 0x10000 + 0x18000) \ 0x10000 - 0x8000`. A different approach of the complete wrapping to the desired range [-0x8000 … 0x7fff] would be to use the following expression: `bit.exor( 0x8000, bit.and( 0xffff, value ) ) - 0x8000`. In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, it *is* a fatal error to supply a value outside the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).  |
| `ref string` | `rec$` |  String of which the first 2 bytes will be filled. Any further bytes of the string are left unchanged. It is an error to supply a string with a byte limit less than 2. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Store a short at position 2 in a string
string tmp(4)
store.short( 0x6164, tmp(2) )
| tmp(2;2) will now contain the short 0x6164 (in the debugger it shows "ad")
```

## Related topics
- Related operations: [store.byte()](store.byte.md), [store.double()](store.double.md), [store.float()](store.float.md), [store.long()](store.long.md)
- Inverse operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.float()](load.float.md), [load.long()](load.long.md), [load.short()](load.short.md)
- Special operations for UTC long format values: [load.utc()](load.utc.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
