# mb.import$()

## Syntax:
`function long mb.import$( ref string target$, const string source$, [ long setid ] )`

## Description
This function converts a string from the external, native character set to the [TSS](../misc/tss.md) character set. Certain escape sequences in the input are recognized and replaced by their indicated characters.

## Arguments
| | | |
|---|---|---|
| `ref string` | `target$` |  Ref string argument that receives at most 4096 bytes of the TSS encoding of the supplied input string value. As its contents will be encoded in TSS, it is desirable that this argument is of type multibyte string, rather than type string.  |
| `const string` | `source$` |  The source string that must be converted. Its contents are considered to be encoded in the external, native character set. Certain escape sequences are recognized and are converted to their indicated TSS characters. See the Remarks section for further details. As its contents are not encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string.  |
| `[ long` | `setid ]` |  Optional argument for the specification of the ID of the TSS character set, as returned for example by the function [mb.locale.info](mb.locale.info.md) when info_flag value TSS_GET_TSS_CHARACTERSET_ID is specified. This setting determines the external, native character set from which the string is converted. By default, the setting of the current locale is used.  |

## Return values
| | |
|---|---|
| <= get.size.in.bytes( *target$*) | The resulting number of bytes stored in the *target$* ref argument string. Notice that value get.size.in.bytes( *target$*) also may indicate an overflow condition. |
| get.size.in.bytes( *target$*) | This can be an indication of an overflow condition! This behavior is retained for compatibility reasons. The term *overflow* is used to indicate that some processing step was finished prematurely, because the output of that step was larger than would fit in the (intermediate) buffer that was available for the output of that step. It does *not* mean that any data was actually written outside the borders of the available buffer. If the supplied buffer is too small, the number of output bytes that fits in the supplied buffer is returned, with no clear indication of the overflow condition. In such a case, when the *target$* ref argument is a multibyte string (as opposed to a single-byte string), the supplied buffer may be not completely filled: when the TSS encoding of a character consists of multiple bytes that cannot all be put in the output buffer, then none of them is put there and the remaining (at most three) bytes are left undefined or (as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)) are set to 0. This conversion function uses fixed size internal temporary buffers, which can overflow. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), overflow of such an internal buffer is also indicated by returning the value get.size.in.bytes( *target$*). In earlier versions, such an overflow is certainly noticed, but the returned value is not well-defined. Any of the described cases of signaling an overflow may hide another exceptional case: replacement of problematic characters may have taken place (otherwise indicated by return value -3). In most cases, overflow situations can be avoided by supplying a sufficiently large output buffer. However, overflow of a fixed size internal temporary buffer can only be avoided by supplying a sufficiently short input string. The size of the internal temporary buffers is 4096 bytes. That is why the *target$* ref argument string receives at most 4096 bytes of output. After the conversion to the TSS character set, several escape sequences are converted to their specified TSS characters. Each escape sequence (consisting of multiple single-byte ASCII characters) results in one single-byte TSS character in the second internal buffer. This means that intermediate results can be larger than the final result and that internal buffer overflow can occur even when the size of the final result would be less than 4096 bytes. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Remarks
After the conversion to the TSS character set, several escape sequences are converted to their specified TSS characters. This conversion is the inverse of the introduction of escape sequences as done by the function [mb.export$()](mb.export.md), but also several other escape sequences are recognized. This is shown in the following table. Especially notice that each escape sequence can be converted to upper case (capital letters) or to lower case (small letters) without changing its meaning.
| |
|---|
| \0x *[0-9a-fA-F]** |
| \0X *[0-9a-fA-F]** |
| |
|---|
| \0 *[0-7]** |
| |
|---|
| \ *[1-9][0-9]** |
| |
|---|
| \b |
| \B |
| |
|---|
| \e |
| \E |
| |
|---|
| \f |
| \F |
| |
|---|
| \n |
| \N |
| |
|---|
| \r |
| \R |
| |
|---|
| \s |
| \S |
| |
|---|
| \t |
| \T |
| |
|---|
| \v |
| \V |
| |
|---|
| \\ |
| |
|---|
| \^ |
| |
|---|
| ^A |
| ^a |
| ^! |
| |
|---|
| ^B |
| ^b |
| ^" |
| |
|---|
| ^C |
| ^c |
| ^# |
| |
|---|
| ^D |
| ^d |
| ^$ |
| |
|---|
| ^E |
| ^e |
| ^% |
| |
|---|
| ^F |
| ^f |
| ^& |
| |
|---|
| ^G |
| ^g |
| ^' |
| |
|---|
| ^H |
| ^h |
| ^( |
| |
|---|
| ^I |
| ^i |
| ^) |
| |
|---|
| ^J |
| ^j |
| ^* |
| |
|---|
| ^K |
| ^k |
| ^+ |
| |
|---|
| ^L |
| ^l |
| ^, |
| |
|---|
| ^M |
| ^m |
| ^- |
| |
|---|
| ^N |
| ^n |
| ^. |
| |
|---|
| ^O |
| ^o |
| ^/ |
| |
|---|
| ^P |
| ^p |
| ^0 |
| |
|---|
| ^Q |
| ^q |
| ^1 |
| |
|---|
| ^R |
| ^r |
| ^2 |
| |
|---|
| ^S |
| ^s |
| ^3 |
| |
|---|
| ^T |
| ^t |
| ^4 |
| |
|---|
| ^U |
| ^u |
| ^5 |
| |
|---|
| ^V |
| ^v |
| ^6 |
| |
|---|
| ^W |
| ^w |
| ^7 |
| |
|---|
| ^X |
| ^x |
| ^8 |
| |
|---|
| ^Y |
| ^y |
| ^9 |
| |
|---|
| ^Z |
| ^z |
| ^: |
| |
|---|
| ^[ |
| ^{ |
| ^; |
| |
|---|
| ^\ |
| ^| |
| ^< |
| |
|---|
| ^] |
| ^} |
| ^= |
| |
|---|
| ^^ |
| ^~ |
| ^> |
| |
|---|
| ^_ |
| ^? |

## Related topics
- [mb.import.raw()](mb.import.raw.md)

- [mb.export$()](mb.export.md)

- [mb.locale.enumerate()](mb.locale.enumerate.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
