# mb.export.raw()

## Syntax:
`function long mb.export.raw( ref string target$, const string source$, [ long setid ] )`

## Description
This function converts a string from the [TSS](../misc/tss.md) character set to the external, native character set. This function is very similar to mb.export$(), but in contrast to that function, no escape sequences are used; instead of that, all ASCII characters are passed unmodified and the TSS-specific line drawing characters and code features are replaced by some replacement character.

## Arguments
| | | |
|---|---|---|
| `ref string` | `target$` |  Ref string argument that receives at most 4096 bytes of the external, native encoding of the supplied input string value. As its contents will not be encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string.  |
| `const string` | `source$` |  The source string that must be converted. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS.  |
| `[ long` | `setid ]` |  Optional argument for the specification of the ID of the TSS character set, as returned for example by the function [mb.locale.info](mb.locale.info.md) when info_flag value TSS_GET_TSS_CHARACTERSET_ID is specified. This setting determines the external, native character set to which the string is converted. By default, the setting of the current locale is used.  |

## Return values
| | |
|---|---|
| >= 0 |   |
| -1 |  An incomplete TSS multibyte character was found at the end of the input string value, or an illegal code sequence was detected. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)), the already generated output is available in the *target$* ref argument string. In earlier versions, an empty string is returned in *target$*. This return value may hide other exceptional cases. Replacement of problematic characters may have taken place (otherwise indicated by return value -3). More importantly, the *target$* ref argument string or the internal buffer may be too small to contain the already generated output (otherwise indicated by return value get.size.in.bytes( *target$*)).  |
| -3 | At least one input character could not be converted, because it is not part of the character set of the indicated locale; such input characters were replaced by some replacement character, e.g by a question mark '?'. Examples of characters that cause this return value are Japanese characters in a non-Japanese locale, Cyrillic characters in a Greek locale, etc., but also the TSS specific line drawing characters and code features.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- A similar function, but with conversion of certain characters to ASCII escape sequences: [mb.export$()](mb.export.md)
- Inverse operation: [mb.import.raw()](mb.import.raw.md)
- [mb.locale.enumerate()](mb.locale.enumerate.md)
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
