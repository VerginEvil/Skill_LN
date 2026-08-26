# mb.import.raw()

## Syntax:
`function long mb.import.raw( ref string target$, const string source$, [ long setid ] )`

## Description
This function converts a string from the external, native character set to the [TSS](../misc/tss.md) character set. This function is very similar to mb.import$(), but in contrast to that function, escape sequences in the input are not recognized and are not replaced by their indicated characters.

## Arguments
| | | |
|---|---|---|
| `ref string` | `target$` |  Ref string argument that receives at most 4096 bytes of the TSS encoding of the supplied input string value. As its contents will be encoded in TSS, it is desirable that this argument is of type multibyte string, rather than type string.  |
| `const string` | `source$` |  The source string that must be converted. Its contents are considered to be encoded in the external, native character set. As its contents are not encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string.  |
| `[ long` | `setid ]` |  Optional argument for the specification of the ID of the TSS character set, as returned for example by the function [mb.locale.info](mb.locale.info.md) when info_flag value TSS_GET_TSS_CHARACTERSET_ID is specified. This setting determines the external, native character set from which the string is converted. By default, the setting of the current locale is used.  |

## Return values
| | |
|---|---|
| >= 0 |   |
| -1 |  An incomplete or illegal code sequence was detected in the input string value. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)), the already generated output is available in the *target$* ref argument string. In earlier versions, an empty string is returned in *target$*. This return value may hide other exceptional cases. Replacement of problematic characters may have taken place (otherwise indicated by return value -3). More importantly, the *target$* ref argument string or the internal buffer may be too small to contain the already generated output (otherwise indicated by return value get.size.in.bytes( *target$*)).  |
| -3 | At least one input character could not be converted, because no character definition is known for the specified native code point; such input characters were replaced by some replacement character, e.g by a question mark '?'.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- A similar function, but with conversion of escape sequences to their specified TSS-characters: [mb.import$()](mb.import.md)
- Inverse operation: [mb.export.raw()](mb.export.raw.md)
- [mb.locale.enumerate()](mb.locale.enumerate.md)
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
