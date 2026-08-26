# chr$()

## Syntax:
`function string chr$( long code_point )`

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
| [0 … 0xff] | In the context of the function chr$, all code point values in the considered range are regarded as valid. For these code point values the resulting string is a single-byte string; the supplied code point is encoded as a single byte; the byte limit of the result is 1, also for code point 0 (the code point of the [NULL character](../3gl_features/null_characters_in_strings.md), usually interpreted as the end of the string value and as such not part of the string value) and also for code point 0x9b (the lead-byte value for four-byte TSS sequences).  |
| [0x100 … 0x9affffff] | In the context of the function chr$, all code point values in the considered range are regarded as invalid. For these code point values, the behavior of this function is left unspecified and may change in the future.  |
| [0x9b000000 … 0x9bffffff] | For valid code point values in the considered range the resulting string is a multibyte string; the supplied code point is encoded as a four-byte sequence; the byte limit of the result is 4. For other code point values, the behavior of this function is left unspecified and may change in the future. In the context of the function chr$, a code point value in the considered range is regarded as valid when the last three bytes of the resulting four-byte sequence are non-zero; notice that the first byte is 0x9b.  |
| [0x9c000000 … 0xffffffff] | In the context of the function chr$, all code point values in the considered range are regarded as invalid. For these code point values, the behavior of this function is left unspecified and may change in the future.  |
-
-
-
-
-
-
Notice that for valid code point values the behavior of chr$ is very similar to that of [mb.long.to.str$](../functions_multibyte_strings/mb.long.to.str.md). For invalid code point values the behavior of chr$ is left unspecified and, above that, may be different from that of mb.long.to.str$.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

chr$( 65 )           | Returns "A".
chr$( asc( "A" ) )   | Returns "A".
chr$( 27 )           | Returns the escape character.

chr$( -(0x65000000 - 0xbcccd4) )
        | Returns "♔" (Unicode character U+2654 WHITE CHESS KING).
        | Notice that the expression 0x65000000 - 0xbcccd4 will be evaluated at compile time.
        | The result is 0x6443332c.
        | The unary minus before that expression is evaluated at runtime
        | and results in the negative value -0x6443332c, which
        | (using a wider hexadecimal notation, e.g. using the %016lx substitution symbol of sprintf$())
        | can also be displayed as 0xffffffff9bbcccd4.
        | The function chr$() wraps this negative value
        | to the unsigned 32-bit value 0x000000009bbcccd4 or simply 0x9bbcccd4,
        | which is the TSS code point for the character '♔' (Unicode character U+2654 WHITE CHESS KING).
```
Define some macros using the method above to specify a TSS multibyte code point
```

#define TssCodePoint0x9bWithTrailBytes(aTrailBytes)     ( -( 0x65000000 - (aTrailBytes) ) )
#define TssCharacter0x9bWithTrailBytes$(aTrailBytes)    chr$( TssCodePoint0x9bWithTrailBytes( aTrailBytes ) )
```
Use [mb.type()](../functions_multibyte_strings/mb.type.md) to demonstrate the type of the string returned by the function chr$.
```

mb.type( chr$( 0 ) )      | Result: 0.
mb.type( chr$( 65 ) )     | Result: 0.
mb.type( chr$( 0x9b ) )   | Result: 0.

mb.type( TssCharacter0x9bWithTrailBytes$( 0xbcccd4 ) )   | Result: 1.
```
Use [array.info()](../functions_memory_operations/array.info.md) to demonstrate the byte limit of the string returned by the function chr$.
```

long nr.dims
long dim.info(1)

array.info( chr$( 0 ), nr.dims, dim.info )      | dim.info(1) now contains: 1.
array.info( chr$( 65 ), nr.dims, dim.info )     | dim.info(1) now contains: 1.
array.info( chr$( 0x9b ), nr.dims, dim.info )   | dim.info(1) now contains: 1.

array.info( TssCharacter0x9bWithTrailBytes$( 0xbcccd4 ), nr.dims, dim.info )
                                                | dim.info(1) now contains: 4.
```
Use [asc()](asc.md) to demonstrate the internal representation of the code points. Use [mb.cast.to.str$()](../functions_multibyte_strings/mb.cast.to.str.md) to cast a multibyte value returned by chr$ to type 'single-byte'.
```

asc( chr$( 0 ) )      | Result: 0.
asc( chr$( 65 ) )     | Result: 65.
asc( chr$( 0x9b ) )   | Result: 0x9b.

asc( TssCharacter0x9bWithTrailBytes$( 0xbcccd4 ) )
                      | Result: 0x9bbcccd4
                      | or, in a wider hexadecimal notation: 0xffffffff9bbcccd4
                      | or, showing that it is a negative value: -0x6443332c
                      | or, using one of the macros: TssCodePoint0x9bWithTrailBytes( 0xbcccd4 ).

asc( mb.cast.to.str$( TssCharacter0x9bWithTrailBytes$( 0xbcccd4 ) ) )
                      | Result: 0x2f7, i.e. 0x9b + 0xbc + 0xcc + 0xd4.
```

## Related topics
- Almost the same functionality: [mb.long.to.str$()](../functions_multibyte_strings/mb.long.to.str.md)
- Inverse functionality: [asc()](asc.md)
- [ASCII Conversion - Overview and Synopsis](ascii_conversion_overview_and_synopsis.md)
- [ASCII Table](../misc/ascii_table.md)
- [TSS Encoding](../misc/tss.md)
