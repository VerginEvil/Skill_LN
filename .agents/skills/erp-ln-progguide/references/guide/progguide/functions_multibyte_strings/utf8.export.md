# utf8.export()

## Syntax:
`function long utf8.export( ref string target$, const string source$, long option_mask )`

## Description
This function converts a string from the [TSS](../misc/tss.md) character set to [Unicode](../misc/unicode.md), using a [UTF-8](../misc/utf8.md) encoding.

## Arguments
| | |
|---|---|
| UTF8_STD_MODE | Use the [standard UTF-8](../misc/utf8.md) encoding. |
| UTF8_JAVA_MODE | Use the [Java modified UTF-8](../misc/utf8.md#java modified utf8) encoding. However, no embedded [NULL-characters](../3gl_features/null_characters_in_strings.md) are supported. The first NULL-character in the supplied *source$* argument string value (i.e. a single 0-byte, according to the TSS-encoding) is interpreted as an end of string marker and no further characters are read from the input string. NULL-termination of the *target$* ref argument string is done by means of the standard UTF-8 encoding of the NULL-character: a single 0-byte, rather than by means of its Java modified UTF-8 encoding: the two-byte sequence C0 80. |

## Return values
| | |
|---|---|
| >= 0 | The resulting number of bytes stored in the *target$* ref argument string. The end of the output data is also indicated by an additional appended NULL-character (encoded as a single 0-byte), if output space allows so. This 0-byte is not counted in the returned value. |
| -1 | The *target$* ref argument string was too small to contain the UTF-8 encoding of the supplied input string value. The already generated output is available in the *target$* ref argument string. The supplied buffer may be not completely filled: when the bytes of the UTF-8 encoding of a character cannot all be put in the output buffer, then none of them is put there and the remaining (at most three or – in case of using Java modified UTF-8 – at most five) bytes are left undefined or (as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)) are set to 0. This return value may hide another exceptional case: replacement of problematic characters may have taken place (otherwise indicated by return value -3). |
| -2 | An incomplete TSS multibyte character was found at the end of the input string value, or an illegal code sequence was detected. The already generated output is available in the *target$* ref argument string. The end of the output data is indicated by an additional appended NULL-character (encoded as a single 0-byte), if output space allows so. This return value may hide other exceptional cases. Replacement of problematic characters may have taken place (otherwise indicated by return value -3). More importantly, the *target$* ref argument string may be too small to contain the already generated output (otherwise indicated by return value -1). |
| -3 | At least one input character could not be converted, because it represented a TSS code point for which no Unicode code point is defined; such input characters were replaced by some replacement character, e.g by the unicode character U+26A0 WARNING SIGN ⚠. Examples of characters that cause this return value are TSS characters corresponding to unmapped code points in native character sets, e.g. TSS character 9B 21 22 32, corresponding to valid but unmapped Japanese Shift JIS code point 81 B0. The generated output is available in the *target$* ref argument string. The end of the output data is indicated by an additional appended NULL-character (encoded as a single 0-byte), if output space allows so. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [utf8.import()](utf8.import.md)

- [TSS Encoding](../misc/tss.md)

- [Unicode](../misc/unicode.md)

- [UTF-8 Encoding](../misc/utf8.md)

- [Java modified UTF-8](../misc/utf8.md#java modified utf8)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
