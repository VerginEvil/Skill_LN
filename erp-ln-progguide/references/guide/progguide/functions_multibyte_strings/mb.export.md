# mb.export$()

## Syntax:
`function long mb.export$( ref string target$, const string source$, [ long setid ] )`

## Description
This function converts a string from the [TSS](../misc/tss.md) character set to the external, native character set. Several ASCII characters and TSS-specific characters are converted to ASCII escape sequences.

## Arguments
| | | |
|---|---|---|
| `ref string` | `target$` |  Ref string argument that receives at most 4096 bytes of the external, native encoding of the supplied input string value. As its contents will not be encoded in TSS, it is desirable that this argument is of type string, rather than type multibyte string.  |
| `const string` | `source$` |  The source string that must be converted. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS. Several ASCII characters and TSS-specific characters are converted to ASCII escape sequences. See the Remarks section for further details.  |
| `[ long` | `setid ]` |  Optional argument for the specification of the ID of the TSS character set, as returned for example by the function [mb.locale.info](mb.locale.info.md) when info_flag value TSS_GET_TSS_CHARACTERSET_ID is specified. This setting determines the external, native character set to which the string is converted. By default, the setting of the current locale is used.  |

## Return values
| | |
|---|---|
| <= get.size.in.bytes( *target$*) | The resulting number of bytes stored in the *target$* ref argument string. Notice that values get.size.in.bytes( *target$*) and 4095 also may indicate an overflow condition. |
| get.size.in.bytes( *target$*) | This can be an indication of an overflow condition! This behavior is retained for compatibility reasons. The term *overflow* is used to indicate that some processing step was finished prematurely, because the output of that step was potentially larger than would fit in the (intermediate) buffer that was available for the output of that step. It does *not* mean that any data was actually written outside the borders of the available buffer. If the supplied buffer is too small, the number of output bytes that fits in the supplied buffer is returned, with no clear indication of the overflow condition. In such a case, the supplied buffer may be not completely filled. When the native encoding of a character consists of multiple bytes that cannot all be put in the output buffer, then none of them is put there and the remaining bytes are left undefined or (as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)) are set to 0. This conversion function uses fixed size internal temporary buffers, which can overflow. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), (potential) overflow of such an internal buffer is also indicated by returning the value get.size.in.bytes( *target$*). Before that TIV level, such an overflow is indicated by returning the value 4095 (i.e. 1 less than the size of the internal buffer) or the overflow is left unnoticed. When overflow of an internal buffer occurs (noticed or unnoticed), then the remaining input may not be handled and any exceptional cases in it (otherwise indicated by return value -1 or -3) may be left unnoticed. Any of the described cases of signaling an overflow may hide another exceptional case: replacement of problematic characters may have taken place (otherwise indicated by return value -3). In most cases, overflow situations can be avoided by supplying a sufficiently large output buffer. However, overflow of a fixed size internal temporary buffer can only be avoided by supplying a sufficiently short input string. |
| 4095 | This can be an indication of an overflow condition! Before [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), overflow of a certain internal buffer is signaled by returning value 4095 (i.e. 1 less than the size of the internal buffer). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Remarks
Before the conversion to the external, native character set, several ASCII characters and TSS-specific characters are converted to ASCII escape sequences. This is shown in the following table.
When preprocessing the input (replacing certain characters by escape sequences), premature end of data does not trigger an error message (otherwise indicated by return value -1), but cuts off the string.
| | | | |
|---|---|---|---|
| TSS code point range (hexadecimal) | Character | Escape sequence | Description |
| 01 | [ASCII](../misc/ascii_table.md) character SOH | ^A | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 02 | [ASCII](../misc/ascii_table.md) character STX | ^B | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 03 | [ASCII](../misc/ascii_table.md) character ETX | ^C | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 04 | [ASCII](../misc/ascii_table.md) character EOT | ^D | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 05 | [ASCII](../misc/ascii_table.md) character ENQ | ^E | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 06 | [ASCII](../misc/ascii_table.md) character ACK | ^F | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 07 | [ASCII](../misc/ascii_table.md) character BEL | ^G | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 08 | [ASCII](../misc/ascii_table.md) character BS (backspace) | \b | backslash \ followed by latin small letter b |
| 09 | [ASCII](../misc/ascii_table.md) character HT (horizontal tab) | \t | backslash \ followed by latin small letter t |
| 0A | [ASCII](../misc/ascii_table.md) character LF (line feed, new line) | \n | backslash \ followed by latin small letter n |
| 0B | [ASCII](../misc/ascii_table.md) character VT (vertical tab) | \v | backslash \ followed by latin small letter v |
| 0C | [ASCII](../misc/ascii_table.md) character FF (form feed) | \f | backslash \ followed by latin small letter f |
| 0D | [ASCII](../misc/ascii_table.md) character CR (carriage return) | \r | backslash \ followed by latin small letter r |
| 0E | [ASCII](../misc/ascii_table.md) character SO | ^N | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 0F | [ASCII](../misc/ascii_table.md) character SI | ^O | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 10 | [ASCII](../misc/ascii_table.md) character DLE | ^P | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 11 | [ASCII](../misc/ascii_table.md) character DC1 | ^Q | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 12 | [ASCII](../misc/ascii_table.md) character DC2 | ^R | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 13 | [ASCII](../misc/ascii_table.md) character DC3 | ^S | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 14 | [ASCII](../misc/ascii_table.md) character DC4 | ^T | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 15 | [ASCII](../misc/ascii_table.md) character NAK | ^U | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 16 | [ASCII](../misc/ascii_table.md) character SYN | ^V | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 17 | [ASCII](../misc/ascii_table.md) character ETB | ^W | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 18 | [ASCII](../misc/ascii_table.md) character CAN | ^X | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 19 | [ASCII](../misc/ascii_table.md) character EM | ^Y | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1A | [ASCII](../misc/ascii_table.md) character SUB | ^Z | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1B | [ASCII](../misc/ascii_table.md) character ESC (escape) | \e | backslash \ followed by latin small letter e |
| 1C | [ASCII](../misc/ascii_table.md) character FS | ^\ | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1D | [ASCII](../misc/ascii_table.md) character GS | ^] | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1E | [ASCII](../misc/ascii_table.md) character RS | ^^ | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1F | [ASCII](../misc/ascii_table.md) character US | ^_ | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 5C | [ASCII](../misc/ascii_table.md) character \ (reverse solidus, backslash) | \\ | backslash \ followed by the original ASCII character |
| 5E | [ASCII](../misc/ascii_table.md) character ^ (circumflex accent) | \^ | backslash \ followed by the original ASCII character |
| 80 … 8A | [TSS](../misc/tss.md) line drawing characters | \0x80 … \0x8a | backslash \ followed by digit zero 0, followed by latin small letter x, followed by two small hexadecimal digits |
| 8B … 9A | [TSS](../misc/tss.md) code features | \0x8b … \0x9a | backslash \ followed by digit zero 0, followed by latin small letter x, followed by two small hexadecimal digits |

## Related topics
- [mb.export.raw()](mb.export.raw.md)

- [mb.import$()](mb.import.md)

- [mb.locale.enumerate()](mb.locale.enumerate.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
