# utf8.export()

## Syntax:
`function long utf8.export( ref string target$, const string source$, long option_mask )`

## Description
This function converts a string from the [TSS](../misc/tss.md) character set to [Unicode](../misc/unicode.md), using a [UTF-8](../misc/utf8.md) encoding.

## Arguments
| | | |
|---|---|---|
| `ref string` | `target$` |  Ref string argument that receives the UTF-8 encoding of the supplied input string value. As its contents will not be encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string. In many cases – as explained for each return value separately – the end of the output data is indicated by an additional appended NULL-character (encoded as a single 0-byte). The value of any remaining bytes of the *target$* ref argument string is undefined, i.e. each of the remaining bytes may either or not be modified to an unspecified value. The actual behavior may be different for different [porting set TIV levels](../tiv/tiv_overview.md). Specifically: no zero-padding of the unused part of the receiving string is guaranteed. Also, do not rely on any earlier postponed zero-padding; the *dirty* mark is ignored and is removed from the supplied string.  |
| `const string` | `source$` |  The source string that must be converted. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS.  |
| `long` | `option_mask` |  This specifies the specific UTF-8 encoding that must be used.  |

## Return values
| | |
|---|---|
| >= 0 |  The resulting number of bytes stored in the *target$* ref argument string. The end of the output data is also indicated by an additional appended NULL-character (encoded as a single 0-byte), if output space allows so. This 0-byte is not counted in the returned value.  |
| -1 |  The *target$* ref argument string was too small to contain the UTF-8 encoding of the supplied input string value. The already generated output is available in the *target$* ref argument string. The supplied buffer may be not completely filled: when the bytes of the UTF-8 encoding of a character cannot all be put in the output buffer, then none of them is put there and the remaining (at most three or – in case of using Java modified UTF-8 – at most five) bytes are left undefined or (as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)) are set to 0. This return value may hide another exceptional case: replacement of problematic characters may have taken place (otherwise indicated by return value -3).  |
| -2 |  An incomplete TSS multibyte character was found at the end of the input string value, or an illegal code sequence was detected. The already generated output is available in the *target$* ref argument string. The end of the output data is indicated by an additional appended NULL-character (encoded as a single 0-byte), if output space allows so. This return value may hide other exceptional cases. Replacement of problematic characters may have taken place (otherwise indicated by return value -3). More importantly, the *target$* ref argument string may be too small to contain the already generated output (otherwise indicated by return value -1).  |
| -3 |  At least one input character could not be converted, because it represented a TSS code point for which no Unicode code point is defined; such input characters were replaced by some replacement character, e.g by the unicode character U+26A0 WARNING SIGN ⚠. Examples of characters that cause this return value are TSS characters corresponding to unmapped code points in native character sets, e.g. TSS character 9B 21 22 32, corresponding to valid but unmapped Japanese Shift JIS code point 81 B0. The generated output is available in the *target$* ref argument string. The end of the output data is indicated by an additional appended NULL-character (encoded as a single 0-byte), if output space allows so.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- Inverse operation: [utf8.import()](utf8.import.md)
- [TSS Encoding](../misc/tss.md)
- [Unicode](../misc/unicode.md)
- [UTF-8 Encoding](../misc/utf8.md)
- Java modified UTF-8
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
