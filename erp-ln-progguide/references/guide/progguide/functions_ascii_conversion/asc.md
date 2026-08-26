# asc()

## Syntax:
`function long asc( string characters )`

## Description
This function returns the sum of the code point values encoded in the supplied string.

## Arguments
| | | |
|---|---|---|
| `string` | `characters` |  Input string. The code points of the characters in the string are summed. If the supplied string is a single-byte string, then each byte of the supplied string is treated as a separate code point, so effectively the sum of all the bytes of the string is returned. If the supplied string is a multibyte string, then a byte with hexadecimal value 0x9B is treated as the beginning of a four-byte [TSS-encoded](../misc/tss.md) character 9B *pp* *qq* *rr*. The four-byte sequence contributes the hexadecimal value 9B *ppqqrr* to the summation. Other bytes contribute their own value to the summation.  |

## Return values
The sum of the code points in the supplied string. The summation is done modulo 2^32 and the resulting value is in the signed 32-bit range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]). In other words: before being returned, the exact summation value is wrapped to the signed 32-bit range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]) by repeatedly adding or subtracting 2^32 until the value is in the signed 32-bit value range.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string  select(10)
asc_b = asc("B")      | asc_b is set to 66.
asc("abc")            | Returns 294 (that is, 97 + 98 + 99).
asc(select)           | Returns the sum of the ASCII codes for each character
                      | in the string variable select.

asc(mb.cast$("♔"))
        | Use mb.cast$() to cast the string literal to type 'multibyte'.
        | Exact result: 0x9bbcccd4 (Unicode character U+2654 WHITE CHESS KING).
        | This is outside the signed 32-bit range.
        | Therefore, before being returned, 2^32 (i.e. 0x100000000) is subtracted.
        | The resulting wrapped value -0x6443332c is returned.
        | This wrapped result may also be written as:
        | 0x9bbcccd4 - 0x10000000
        | or 0x9b000000 + 0xbcccd4 - 0x10000000
        | or -0x65000000 + 0xbcccd4
        | or -(0x65000000 - 0xbcccd4).
        | When using a wider hexadecimal notation
        | (e.g. using the %016lx substitution symbol of sprintf$()),
        | the exact result would be displayed as 0x000000009bbcccd4,
        | whereas the resulting wrapped value would be displayed as 0xffffffff9bbcccd4.
```
**

## Related topics
- Inverse functionality: [chr$()](chr.md)
- [ASCII Conversion - Overview and Synopsis](ascii_conversion_overview_and_synopsis.md)
- [ASCII Table](../misc/ascii_table.md)
- [TSS Encoding](../misc/tss.md)
