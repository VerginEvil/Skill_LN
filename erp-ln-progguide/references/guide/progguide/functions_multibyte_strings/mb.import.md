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
| >= 0 |   |
| -1 |  An incomplete or illegal code sequence was detected in the input string value. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md)), the already generated output is available in the *target$* ref argument string. In earlier versions, an empty string is returned in *target$*. This return value may hide other exceptional cases. Replacement of problematic characters may have taken place (otherwise indicated by return value -3). More importantly, the *target$* ref argument string or some internal buffer may be too small to contain the already generated output (otherwise indicated by return value get.size.in.bytes( *target$*)).  |
| -3 | At least one input character could not be converted, because no character definition is known for the specified native code point; such input characters were replaced by some replacement character, e.g by a question mark '?'.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Remarks
After the conversion to the TSS character set, several escape sequences are converted to their specified TSS characters. This conversion is the inverse of the introduction of escape sequences as done by the function [mb.export$()](mb.export.md), but also several other escape sequences are recognized. This is shown in the following table. Especially notice that each escape sequence can be converted to upper case (capital letters) or to lower case (small letters) without changing its meaning.
| | | | |
|---|---|---|---|
|  Escape sequence  |  Description  |  TSS code point (hexadecimal)  |  Character  |
|   | backslash \ followed by digit zero 0, followed by latin (small or capital) letter x, followed by at most two (small or capital) hexadecimal digits  | the value of the hexadecimal number formed by the digits | Any single-byte [TSS](../misc/tss.md) character, including line drawing characters and code features  |
|   | backslash \ followed by digit zero 0, followed by at most three octal digits  | the value (modulo 256) of the octal number formed by the digits | Any single-byte [TSS](../misc/tss.md) character, including line drawing characters and code features  |
|   | backslash \ followed by at least one and at most three decimal digits, of which the first one is not digit zero 0  | the value (modulo 256) of the decimal number formed by the digits | Any single-byte [TSS](../misc/tss.md) character, including line drawing characters and code features  |
|   | backslash \ followed by latin (small or capital) letter b | 08 | [ASCII](../misc/ascii_table.md) character BS (backspace)  |
|   | backslash \ followed by latin (small or capital) letter e | 1B | [ASCII](../misc/ascii_table.md) character ESC (escape)  |
|   | backslash \ followed by latin (small or capital) letter f | 0C | [ASCII](../misc/ascii_table.md) character FF (form feed)  |
|   | backslash \ followed by latin (small or capital) letter n | 0A | [ASCII](../misc/ascii_table.md) character LF (line feed, new line)  |
|   | backslash \ followed by latin (small or capital) letter r | 0D | [ASCII](../misc/ascii_table.md) character CR (carriage return)  |
|   | backslash \ followed by latin (small or capital) letter s | 20 | [ASCII](../misc/ascii_table.md) character SP (space)  |
|   | backslash \ followed by latin (small or capital) letter t | 09 | [ASCII](../misc/ascii_table.md) character HT (horizontal tab)  |
|   | backslash \ followed by latin (small or capital) letter v | 0B | [ASCII](../misc/ascii_table.md) character VT (vertical tab)  |
|   | backslash \ followed by backslash \ | 5C | [ASCII](../misc/ascii_table.md) character \ (reverse solidus, backslash)  |
|   | backslash \ followed by circumflex accent ^ | 5E | [ASCII](../misc/ascii_table.md) character ^ (circumflex accent)  |
|   | circumflex accent ^ followed by latin (capital or small) letter a or exclamation mark ! | 01 | [ASCII](../misc/ascii_table.md) character SOH (start of heading)  |
|   | circumflex accent ^ followed by latin (capital or small) letter b or quotation mark " | 02 | [ASCII](../misc/ascii_table.md) character STX (start of text)  |
|   | circumflex accent ^ followed by latin (capital or small) letter c or number sign # | 03 | [ASCII](../misc/ascii_table.md) character ETX (end of text)  |
|   | circumflex accent ^ followed by latin (capital or small) letter d or dollar sign $ | 04 | [ASCII](../misc/ascii_table.md) character EOT (end of transmission)  |
|   | circumflex accent ^ followed by latin (capital or small) letter e or percent sign % | 05 | [ASCII](../misc/ascii_table.md) character ENQ (enquiry)  |
|   | circumflex accent ^ followed by latin (capital or small) letter f or ampersand & | 06 | [ASCII](../misc/ascii_table.md) character ACK (acknowledge)  |
|   | circumflex accent ^ followed by latin (capital or small) letter g or apostrophe ' | 07 | [ASCII](../misc/ascii_table.md) character BEL (bell)  |
|   | circumflex accent ^ followed by latin (capital or small) letter h or left parenthesis ( | 08 | [ASCII](../misc/ascii_table.md) character BS (backspace)  |
|   | circumflex accent ^ followed by latin (capital or small) letter i or right parenthesis ) | 09 | [ASCII](../misc/ascii_table.md) character HT (horizontal tab)  |
|   | circumflex accent ^ followed by latin (capital or small) letter j or asterisk * | 0A | [ASCII](../misc/ascii_table.md) character LF (line feed, new line)  |
|   | circumflex accent ^ followed by latin (capital or small) letter k or plus sign + | 0B | [ASCII](../misc/ascii_table.md) character VT (vertical tab)  |
|   | circumflex accent ^ followed by latin (capital or small) letter l or comma , | 0C | [ASCII](../misc/ascii_table.md) character FF (form feed)  |
|   | circumflex accent ^ followed by latin (capital or small) letter m or hyphen-minus - | 0D | [ASCII](../misc/ascii_table.md) character CR (carriage return)  |
|   | circumflex accent ^ followed by latin (capital or small) letter n or full stop . | 0E | [ASCII](../misc/ascii_table.md) character SO (shift out)  |
|   | circumflex accent ^ followed by latin (capital or small) letter o or solidus (slash) / | 0F | [ASCII](../misc/ascii_table.md) character SI (shift in)  |
|   | circumflex accent ^ followed by latin (capital or small) letter p or digit zero 0 | 10 | [ASCII](../misc/ascii_table.md) character DLE (data link escape)  |
|   | circumflex accent ^ followed by latin (capital or small) letter q or digit one 1 | 11 | [ASCII](../misc/ascii_table.md) character DC1 (device control one)  |
|   | circumflex accent ^ followed by latin (capital or small) letter r or digit two 2 | 12 | [ASCII](../misc/ascii_table.md) character DC2 (device control two)  |
|   | circumflex accent ^ followed by latin (capital or small) letter s or digit three 3 | 13 | [ASCII](../misc/ascii_table.md) character DC3 (device control three)  |
|   | circumflex accent ^ followed by latin (capital or small) letter t or digit four 4 | 14 | [ASCII](../misc/ascii_table.md) character DC4 (device control four)  |
|   | circumflex accent ^ followed by latin (capital or small) letter uor digit five 5 | 15 | [ASCII](../misc/ascii_table.md) character NAK (negative acknowledge)  |
|   | circumflex accent ^ followed by latin (capital or small) letter v or digit six 6 | 16 | [ASCII](../misc/ascii_table.md) character SYN (synchronous idle)  |
|   | circumflex accent ^ followed by latin (capital or small) letter w or digit seven 7 | 17 | [ASCII](../misc/ascii_table.md) character ETB (end of transmission block)  |
|   | circumflex accent ^ followed by latin (capital or small) letter x or digit eight 8 | 18 | [ASCII](../misc/ascii_table.md) character CAN (cancel)  |
|   | circumflex accent ^ followed by latin (capital or small) letter y or digit nine 9 | 19 | [ASCII](../misc/ascii_table.md) character EM (end of medium)  |
|   | circumflex accent ^ followed by latin (capital or small) letter z or colon : | 1A | [ASCII](../misc/ascii_table.md) character SUB (substitute)  |
|   | circumflex accent ^ followed by left square bracket [ or left curly bracket { or semicolon ; | 1B | [ASCII](../misc/ascii_table.md) character ESC (escape)  |
|   | circumflex accent ^ followed by backslash (reverse solidus) \ or vertical line | or less-than sign < | 1C | [ASCII](../misc/ascii_table.md) character FS (file separator)  |
|   | circumflex accent ^ followed by right square bracket ] or right curly bracket } or equals sign = | 1D | [ASCII](../misc/ascii_table.md) character GS (group separator)  |
|   | circumflex accent ^ followed by circumflex accent ^ or tilde ~ or greater-than sign > | 1E | [ASCII](../misc/ascii_table.md) character RS (record separator)  |
|   | circumflex accent ^ followed by low line _ or question mark ? | 1F | [ASCII](../misc/ascii_table.md) character US (unit separator)  |

## Related topics
- A similar function, but without conversion of escape sequences to their specified TSS-characters: [mb.import.raw()](mb.import.raw.md)
- Inverse operation: [mb.export$()](mb.export.md)
- [mb.locale.enumerate()](mb.locale.enumerate.md)
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
