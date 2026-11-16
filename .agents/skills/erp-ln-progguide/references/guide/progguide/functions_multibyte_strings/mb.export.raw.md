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
| <= get.size.in.bytes( *target$*) | The resulting number of bytes stored in the *target$* ref argument string. Notice that values get.size.in.bytes( *target$*) and 4095 also may indicate an overflow condition. |
| get.size.in.bytes( *target$*) | This can be an indication of an overflow condition! This behavior is retained for compatibility reasons. The term *overflow* is used to indicate that some processing step was finished prematurely, because the output of that step was potentially larger than would fit in the (intermediate) buffer that was available for the output of that step. It does *not* mean that any data was actually written outside the borders of the available buffer. If the supplied buffer is too small, the number of output bytes that fits in the supplied buffer is returned, with no clear indication of the overflow condition. In such a case, the supplied buffer may be not completely filled. When the native encoding of a character consists of multiple bytes that cannot all be put in the output buffer, then none of them is put there and the remaining bytes are left undefined or (as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)) are set to 0. This conversion function uses a fixed size internal temporary buffer, which can overflow. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), overflow of the internal buffer is also indicated by returning the value get.size.in.bytes( *target$*). Before that TIV level, such an overflow is indicated by returning the value 4095 (i.e. 1 less than the size of the internal buffer). Any of the described cases of signaling an overflow may hide another exceptional case: replacement of problematic characters may have taken place (otherwise indicated by return value -3). In most cases, overflow situations can be avoided by supplying a sufficiently large output buffer. However, overflow of the fixed size internal temporary buffer can only be avoided by supplying a sufficiently short input string. |
| 4095 | This can be an indication of an overflow condition! Before [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), overflow of the internal buffer is signaled by returning value 4095 (i.e. 1 less than the size of the internal buffer). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [mb.export$()](mb.export.md)

- [mb.import.raw()](mb.import.raw.md)

- [mb.locale.enumerate()](mb.locale.enumerate.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
