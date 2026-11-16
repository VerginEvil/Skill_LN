# mb.long.to.str$()

## Syntax:
`function string mb.long.to.str$( long code_point )`

## Description
This function returns a single-character string corresponding to the supplied [TSS](../misc/tss.md) code point.

## Arguments
| | | |
|---|---|---|
| `long` | `code_point` |  The [TSS](../misc/tss.md) code point of the single character in the string to be returned. Before being interpreted as a TSS code point, the supplied value is wrapped to the unsigned 32-bit value range [0 … 2^32 - 1] (i.e. [0 … 0xffffffff]) by repeatedly adding or subtracting 2^32 until the value is in the unsigned 32-bit value range. It is not checked whether the resulting value is a valid TSS code point.  |

## Return values
A string containing exactly one character, specifically the character determined by the specified code point.
| | |
|---|---|
| Code point range | Description of the return value |
| [0 … 0xff] | In the context of the function mb.long.to.str$, all code point values in the considered range are regarded as valid, except code point 0x9b (the lead-byte value for four-byte TSS sequences). For valid code point values the resulting string is a single-byte string; the supplied code point is encoded as a single byte; in most cases the [byte capacity](../3gl_features/data_types.md#byte capacity) of the result is 1; however, the byte capacity of the result is 0 for code point 0 (the code point of the [NULL character](../3gl_features/null_characters_in_strings.md), usually interpreted as the end of the string value and as such not part of the string value). For code point 0x9b the result is left unspecified and may change in the future. |
| [0x100 … 0x9affffff] | In the context of the function mb.long.to.str$, all code point values in the considered range are regarded as invalid. For these code point values, the behavior of this function is left unspecified and may change in the future. |
| [0x9b000000 … 0x9bffffff] | For valid code point values in the considered range the resulting string is a multibyte string; the supplied code point is encoded as a four-byte sequence; the [byte capacity](../3gl_features/data_types.md#byte capacity) of the result is 4. For other code point values, the behavior of this function is left unspecified and may change in the future. In the context of the function mb.long.to.str$, a code point value in the considered range is regarded as valid when the last three bytes of the resulting four-byte sequence are non-zero; notice that the first byte is 0x9b. |
| [0x9c000000 … 0xffffffff] | In the context of the function mb.long.to.str$, all code point values in the considered range are regarded as invalid. For these code point values, the behavior of this function is left unspecified and may change in the future. |
Notice that for valid code point values the behavior of mb.long.to.str$ is very similar to that of [chr$](../functions_ascii_conversion/chr.md). For invalid code point values the behavior of mb.long.to.str$ is left unspecified and, above that, may be different from that of chr$.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
See [chr$()](../functions_ascii_conversion/chr.md), of which the behavior is very similar to that of mb.long.to.str$. Notice that code point value 0x9b is regarded as valid in the context of chr$, but not in the context of mb.long.to.str$. Further notice a difference in the [byte capacity](../3gl_features/data_types.md#byte capacity) of the result for code point value 0. Use [array.info()](../functions_memory_operations/array.info.md) to demonstrate the byte capacity of the strings returned by the functions chr$ and mb.long.to.str$.
```

long nr.dims
long dim.info(1)

array.info( chr$( 0 ), nr.dims, dim.info )              | dim.info(1) now contains: 1.
array.info( mb.long.to.str$( 0 ), nr.dims, dim.info )   | dim.info(1) now contains: 0.
```

## Related topics
- [chr$()](../functions_ascii_conversion/chr.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
