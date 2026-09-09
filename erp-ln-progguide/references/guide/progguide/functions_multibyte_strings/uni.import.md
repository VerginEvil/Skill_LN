# uni.import()

## Syntax:
`function long uni.import( ref string target$, const string source$, [ long sb_flag ] )`

## Description
This function converts a string from [Unicode](../misc/unicode.md) (encoded according to a [byte serialized UTF-16](../misc/utf16.md) encoding scheme) to the [TSS](../misc/tss.md) character set. The default encoding scheme is UTF-16BE, i.e. each UTF-16 code unit is assumed to be serialized with the most significant byte first.
Unicode Normalization Form C (NFC: Canonical Decomposition, followed by Canonical Composition) is applied during the conversion. See [Unicode Standard Annex #15: Unicode Normalization Forms](http://www.unicode.org/reports/tr15/tr15-23.html)

## Arguments
| | |
|---|---|
| UNI_DEF_ORDER | Consider the *source$* string to be encoded according to the default byte order of the underlying operating system. |
| UNI_MSB_ORDER | Consider the *source$* string to be encoded with the most significant byte first, i.e. use UTF-16BE. |
| UNI_LSB_ORDER | Consider the *source$* string to be encoded with the least significant byte first, i.e. use UTF-16LE. |

## Return values
| | |
|---|---|
| >= 0 | The resulting number of bytes stored in the *target$* ref argument string. |
| -1 | The *target$* ref argument string was too small to contain the TSS encoding of the supplied input string value. The already generated output is available in the *target$* ref argument string. When the *target$* ref argument is a multibyte string (as opposed to a single-byte string), the supplied buffer may be not completely filled: when the TSS encoding of a character consists of multiple bytes that cannot all be put in the output buffer, then none of them is put there and the remaining (at most three) bytes are left undefined or (as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)) are set to 0. This return value may hide another exceptional case: replacement of problematic characters may have taken place (otherwise indicated by return value -3). |
| -2 | An incomplete UTF-16 code sequence was found at the end of the input string value, or an illegal code sequence was detected. The already generated output is available in the *target$* ref argument string. This return value may hide other exceptional cases. Replacement of problematic characters may have taken place (otherwise indicated by return value -3). More importantly, the *target$* ref argument string may be too small to contain the already generated output (otherwise indicated by return value -1). |
| -3 | At least one input character could not be converted, because it represented a Unicode code point for which no TSS code point is defined; such input characters were replaced by some replacement character, e.g by a question mark '?'. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [uni.export()](uni.export.md)

- [TSS Encoding](../misc/tss.md)

- [Unicode](../misc/unicode.md)

- [UTF-16 Encoding](../misc/utf16.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
