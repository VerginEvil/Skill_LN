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
| <= get.size.in.bytes( *target$*) | The resulting number of bytes stored in the *target$* ref argument string. Notice that values get.size.in.bytes( *target$*) and 4096 also may indicate an overflow condition. |
| get.size.in.bytes( *target$*) | This can be an indication of an overflow condition! This behavior is retained for compatibility reasons. The term *overflow* is used to indicate that some processing step was finished prematurely, because the output of that step was larger than would fit in the (intermediate) buffer that was available for the output of that step. It does *not* mean that any data was actually written outside the borders of the available buffer. If the supplied buffer is too small, the number of output bytes that fits in the supplied buffer is returned, with no clear indication of the overflow condition. In such a case, the supplied buffer may be not completely filled: when the TSS encoding of a character consists of multiple bytes that cannot all be put in the output buffer, then none of them is put there and the remaining (at most three) bytes are left undefined or (as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)) are set to 0. This conversion function uses a fixed size internal temporary buffer, which can overflow. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), overflow of the internal buffer is also indicated by returning the value get.size.in.bytes( *target$*). Before that TIV level, such an overflow is indicated by returning the value 4096 (i.e. the size of the internal buffer). Any of the described cases of signaling an overflow may hide another exceptional case: replacement of problematic characters may have taken place (otherwise indicated by return value -3). In most cases, overflow situations can be avoided by supplying a sufficiently large output buffer. However, overflow of a fixed size internal temporary buffer can only be avoided by supplying a sufficiently short input string. |
| 4096 | This can be an indication of an overflow condition! Before [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), overflow of the internal buffer is signaled by returning value 4096 (i.e. the size of the internal buffer). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [mb.import$()](mb.import.md)

- [mb.export.raw()](mb.export.raw.md)

- [mb.locale.enumerate()](mb.locale.enumerate.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
