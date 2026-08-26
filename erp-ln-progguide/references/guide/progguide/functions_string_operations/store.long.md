# store.long()

## Syntax:
`function void store.long( long value, ref string rec$ )`

## Description
The function store.long() treats the supplied string merely as a sequence of bytes.
The function store.long() writes the 32 least significant bits of the two’s complement representation of the supplied integer value into the first 4 bytes of the supplied string.
The inverse function [load.long()](load.long.md) will retrieve the original supplied integer value, wrapped to the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]) by repeatedly adding or subtracting 2^32 until the value is in the signed 32-bit value range.
More specifically, the inverse function [load.long()](load.long.md) will retrieve the exact original supplied integer value if and only if that integer value is within the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]).
This function is machine independent and can be used (for example) in network communications.

## Arguments
```

long x7fff_ffff
long x8000_0000
long xffff_ffff

x7fff_ffff = 0x7fff_ffff
x8000_0000 = x7fff_ffff + 1
xffff_ffff = x7fff_ffff + x8000_0000

value = bit.exor( x8000_0000, bit.and( xffff_ffff, value ) ) - x8000_0000

| or, alternatively:

long x1_0000_0000
long x1_8000_0000

x1_0000_0000 = x8000_0000 + x8000_0000
x1_8000_0000 = x1_0000_0000 + x8000_0000

value = (value \ x1_0000_0000 + x1_8000_0000) \ x1_0000_0000 - x8000_0000
```
| | | |
|---|---|---|
| `long` | `value` |  The value to write into the string. In 64-bit mode, the bshell is less forgiving than in 32-bit mode. When the bshell is in 64-bit mode, it is a fatal error to supply a value outside the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-0x80000000 … 0x7fffffff] or [-2,147,483,648 … 2,147,483,647]). Explicit wrapping of the input value may be done beforehand by means of the 'remainder after division by 0x100000000' operator `\ 0x100000000`. However, the result of the expression `value \ 0x100000000` is still not in the desired range [-0x80000000 … 0x7fffffff]. For a positive value, the result is in the range [0 … 0xffffffff], for a negative value it is in the range [-0xffffffff … 0]. For complete wrapping to the desired range [-0x80000000 … 0x7fffffff], the following expression may be used: `(value \ 0x100000000 + 0x180000000) \ 0x100000000 - 0x80000000`. A different approach of the complete wrapping to the desired range [-0x80000000 … 0x7fffffff] would be to use the following expression: `bit.exor( 0x80000000, bit.and( 0xffffffff, value ) ) - 0x80000000`. Notice that the [long constants](../3gl_features/numeric_constants.md) 0x80000000, 0xffffffff, 0x100000000 and 0x180000000 used above are outside the signed 32-bit value range supported by the compiler. Therefore, these values must be computed at runtime. See the following example.  |
| `ref string` | `rec$` |  String of which the first 4 bytes will be filled. Any further bytes of the string are left unchanged. It is an error to supply a string with a byte limit less than 4. In such a case, at least a log message will be generated. Above that, it may cause (now or in a future bshell version) the current 3GL process to be terminated. When a multibyte string is supplied, the behavior is undefined.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

| Store a long at position 1 in a string
string tmp(4)
store.long( 0x62616265, tmp )
| tmp(1;4) will now contain the long 0x62616265 (in the debugger it shows "babe")
```

## Related topics
- Related operations: [store.byte()](store.byte.md), [store.double()](store.double.md), [store.float()](store.float.md), [store.short()](store.short.md)
- Inverse operations: [load.byte()](load.byte.md), [load.double()](load.double.md), [load.float()](load.float.md), [load.long()](load.long.md), [load.short()](load.short.md)
- Special operations for UTC long format values: [load.utc()](load.utc.md), [store.utc()](store.utc.md)
- Definition of the byte limit of a string variable: length limit in bytes
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
