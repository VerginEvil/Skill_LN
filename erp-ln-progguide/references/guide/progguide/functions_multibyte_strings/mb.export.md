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
| >= 0 |   |
| -1 |  An incomplete TSS multibyte character was found at the end of the input string value, or an illegal code sequence was detected. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)), the already generated output is available in the *target$* ref argument string. In earlier versions, an empty string is returned in *target$*. This return value may hide other exceptional cases. Replacement of problematic characters may have taken place (otherwise indicated by return value -3). More importantly, the *target$* ref argument string or one of the internal buffers may be too small to contain the already generated output (otherwise indicated by return value get.size.in.bytes( *target$*)).  |
| -3 | At least one input character could not be converted, because it is not part of the character set of the indicated locale; such input characters were replaced by some replacement character, e.g by a question mark '?'. Examples of characters that cause this return value are Japanese characters in a non-Japanese locale, Cyrillic characters in a Greek locale, etc.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Remarks
Before the conversion to the external, native character set, several ASCII characters and TSS-specific characters are converted to ASCII escape sequences. This is shown in the following table.
When preprocessing the input (replacing certain characters by escape sequences), premature end of data does not trigger an error message (otherwise indicated by return value -1), but cuts off the string.
| | | | |
|---|---|---|---|
|  TSS code point range (hexadecimal)  |  Character  |  Escape sequence  |  Description  |
| 01 | [ASCII](../misc/ascii_table.md) character SOH  | ^A | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 02 | [ASCII](../misc/ascii_table.md) character STX  | ^B | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 03 | [ASCII](../misc/ascii_table.md) character ETX  | ^C | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 04 | [ASCII](../misc/ascii_table.md) character EOT  | ^D | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 05 | [ASCII](../misc/ascii_table.md) character ENQ  | ^E | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 06 | [ASCII](../misc/ascii_table.md) character ACK  | ^F | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 07 | [ASCII](../misc/ascii_table.md) character BEL  | ^G | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 08 | [ASCII](../misc/ascii_table.md) character BS (backspace)  | \b | backslash \ followed by latin small letter b |
| 09 | [ASCII](../misc/ascii_table.md) character HT (horizontal tab)  | \t | backslash \ followed by latin small letter t |
| 0A | [ASCII](../misc/ascii_table.md) character LF (line feed, new line)  | \n | backslash \ followed by latin small letter n |
| 0B | [ASCII](../misc/ascii_table.md) character VT (vertical tab)  | \v | backslash \ followed by latin small letter v |
| 0C | [ASCII](../misc/ascii_table.md) character FF (form feed)  | \f | backslash \ followed by latin small letter f |
| 0D | [ASCII](../misc/ascii_table.md) character CR (carriage return)  | \r | backslash \ followed by latin small letter r |
| 0E | [ASCII](../misc/ascii_table.md) character SO  | ^N | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 0F | [ASCII](../misc/ascii_table.md) character SI  | ^O | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 10 | [ASCII](../misc/ascii_table.md) character DLE  | ^P | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 11 | [ASCII](../misc/ascii_table.md) character DC1  | ^Q | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 12 | [ASCII](../misc/ascii_table.md) character DC2  | ^R | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 13 | [ASCII](../misc/ascii_table.md) character DC3  | ^S | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 14 | [ASCII](../misc/ascii_table.md) character DC4  | ^T | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 15 | [ASCII](../misc/ascii_table.md) character NAK  | ^U | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 16 | [ASCII](../misc/ascii_table.md) character SYN  | ^V | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 17 | [ASCII](../misc/ascii_table.md) character ETB  | ^W | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 18 | [ASCII](../misc/ascii_table.md) character CAN  | ^X | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 19 | [ASCII](../misc/ascii_table.md) character EM  | ^Y | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1A | [ASCII](../misc/ascii_table.md) character SUB  | ^Z | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1B | [ASCII](../misc/ascii_table.md) character ESC (escape)  | \e | backslash \ followed by latin small letter e |
| 1C | [ASCII](../misc/ascii_table.md) character FS  | ^\ | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1D | [ASCII](../misc/ascii_table.md) character GS  | ^] | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1E | [ASCII](../misc/ascii_table.md) character RS  | ^^ | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 1F | [ASCII](../misc/ascii_table.md) character US  | ^_ | circumflex accent ^ followed by the ASCII character at an offset of 64 positions |
| 5C | [ASCII](../misc/ascii_table.md) character \ (reverse solidus, backslash)  | \\ | backslash \ followed by the original ASCII character |
| 5E | [ASCII](../misc/ascii_table.md) character ^ (circumflex accent)  | \^ | backslash \ followed by the original ASCII character |
| 80 … 8A | [TSS](../misc/tss.md) line drawing characters  | \0x80 … \0x8a | backslash \ followed by digit zero 0, followed by latin small letter x, followed by two small hexadecimal digits  |
| 8B … 9A | [TSS](../misc/tss.md) code features  | \0x8b … \0x9a | backslash \ followed by digit zero 0, followed by latin small letter x, followed by two small hexadecimal digits  |

## Related topics
- A similar function, but without conversion of certain characters to ASCII escape sequences: [mb.export.raw()](mb.export.raw.md)
- Inverse operation: [mb.import$()](mb.import.md)
- [mb.locale.enumerate()](mb.locale.enumerate.md)
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
