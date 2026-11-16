# UTF-8 Encoding
UTF-8 is a standard way to encode [Unicode](unicode.md) characters by means of a stream of bytes. First the 'normal' UTF-8 standard is explained, then the slightly different 'Java modified UTF-8' standard is explained.
Each Unicode character is encoded by a sequence of one to four 8-bit bytes. The Unicode standard defines 2^16 + 2^20 code points, numbered U+0000 … U+10FFFF. With a straightforward binary numbering of the complete Unicode range, 21 bits are needed. Name the 21 bits as follows:
`b_20 b_19 b_18 b_17 b_16 b_15 b_14 b_13 b_12 b_11 b_10 b_9 b_8 b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0`
In the explanation below,

- each small box represents a single bit;

- each group of four horizontally adjacent small boxes represents a hexadecimal digit;

- each row (containing two groups of four horizontally adjacent boxes) represents a byte.

After these preliminaries, the UTF-8 encoding is defined as follows.

## Single-byte UTF-8
Single-byte UTF-8 is used for Unicode characters in the range U+0000 … U+007F. For a Unicode character in this range, bit `b_` *i* is zero for each *i* in the range 7 … 20, and the remaining 7 bits are represented in single-byte UTF-8 as follows:
| | | | |
|---|---|---|---|
| 0 | b_6 | b_5 | b_4 |
| | | | |
|---|---|---|---|
| b_3 | b_2 | b_1 | b_0 |
Notice that this Unicode range corresponds with the [ASCII](ascii_table.md) range. and that each character in this range is encoded by a byte with the corresponding ASCII value.

## Example
- ASCII character 'A' (ASCII value 0x41)

- is assigned to Unicode code point U+0041,

- which corresponds to the 21-bit sequence 0 0000 0000 0000 0100 0001,

- which is represented in single-byte UTF-8 as 0100 0001

- or in hexadecimal notation: 41.

## Two-byte UTF-8
Two-byte UTF-8 is used for Unicode characters in the range U+0080 … U+07FF. For a Unicode character in this range, bit `b_` *i* is zero for each *i* in the range 11 … 20, and the remaining 11 bits are represented in two-byte UTF-8 as follows:
| | | | |
|---|---|---|---|
| 1 | 1 | 0 | b_10 |
| | | | |
|---|---|---|---|
| b_9 | b_8 | b_7 | b_6 |
| | | | |
|---|---|---|---|
| 1 | 0 | b_5 | b_4 |
| | | | |
|---|---|---|---|
| b_3 | b_2 | b_1 | b_0 |

## Example
- the Latin Small Letter C With Cedilla ç

- is assigned to Unicode code point U+00E7,

- which corresponds to the 21-bit sequence 0 0000 0000 0000 1110 0111,

- which is represented in two-byte UTF-8 as 1100 0011 1010 0111

- or in hexadecimal notation: C3 A7.

## Three-byte UTF-8
Three-byte UTF-8 is used for Unicode characters in the range U+0800 … U+FFFF. For a Unicode character in this range, bit `b_` *i* is zero for each *i* in the range 16 … 20, and the remaining 16 bits are represented in three-byte UTF-8 as follows:
| | | | |
|---|---|---|---|
| 1 | 1 | 1 | 0 |
| | | | |
|---|---|---|---|
| b_15 | b_14 | b_13 | b_12 |
| | | | |
|---|---|---|---|
| 1 | 0 | b_11 | b_10 |
| | | | |
|---|---|---|---|
| b_9 | b_8 | b_7 | b_6 |
| | | | |
|---|---|---|---|
| 1 | 0 | b_5 | b_4 |
| | | | |
|---|---|---|---|
| b_3 | b_2 | b_1 | b_0 |

## Example
- the Euro Sign €

- is assigned to Unicode code point U+20AC,

- which corresponds to the 21-bit sequence 0 0000 0010 0000 1010 1100,

- which is represented in three-byte UTF-8 as 1110 0010 1000 0010 1010 1100

- or in hexadecimal notation: E2 82 AC.

## Four-byte UTF-8
Four-byte UTF-8 is used for Unicode characters in the range U+010000 … U+10FFFF. For a Unicode character in this range, the 21 bits are represented in four-byte UTF-8 as follows:
| | | | |
|---|---|---|---|
| 1 | 1 | 1 | 1 |
| | | | |
|---|---|---|---|
| 0 | b_20 | b_19 | b_18 |
| | | | |
|---|---|---|---|
| 1 | 0 | b_17 | b_16 |
| | | | |
|---|---|---|---|
| b_15 | b_14 | b_13 | b_12 |
| | | | |
|---|---|---|---|
| 1 | 0 | b_11 | b_10 |
| | | | |
|---|---|---|---|
| b_9 | b_8 | b_7 | b_6 |
| | | | |
|---|---|---|---|
| 1 | 0 | b_5 | b_4 |
| | | | |
|---|---|---|---|
| b_3 | b_2 | b_1 | b_0 |
Notice that this Unicode range corresponds with the range of the Supplementary Characters.

## Example
- the Musical Symbol G Clef

- is assigned to Unicode code point U+01D11E,

- which corresponds to the 21-bit sequence 0 0001 1101 0001 0001 1110,

- which is represented in four-byte UTF-8 as 1111 0000 1001 1101 1000 0100 1001 1110

- or in hexadecimal notation: F0 9D 84 9E.

## Java modified UTF-8
Java modified UTF-8 is a variant of UTF-8, differing from it in the following two aspects.

## NULL character
The NULL character U+0000 is not (as in 'normal' UTF-8) encoded as a single byte (with value 0), but as a two-byte sequence (according to the normal definition of a two-byte sequence: 1100 0000 1000 0000 or in hexadecimal notation: C0 80).

## Supplementary characters
Supplementary characters are not supported. Instead of that, surrogate characters are supported, as explained in [UTF-16 Encoding](utf16.md). Nevertheless, surrogate characters should only appear in correct surrogate pairs. This means the following.
No four-byte sequences are allowed in Java modified UTF-8.
A supplementary character is encoded in Java modified UTF-8 as if it were a correct surrogate character pair, that is as a six-byte sequence consisting of the three-byte sequence corresponding to the high surrogate character followed by the three-byte sequence corresponding to the low surrogate character. So, the supplementary character is first represented in double-word [UTF-16](utf16.md):
| | | | |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| | | | |
|---|---|---|---|
| 1 | 0 | c_19 | c_18 |
| | | | |
|---|---|---|---|
| c_17 | c_16 | c_15 | c_14 |
| | | | |
|---|---|---|---|
| c_13 | c_12 | c_11 | c_10 |
| | | | |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| | | | |
|---|---|---|---|
| 1 | 1 | c_9 | c_8 |
| | | | |
|---|---|---|---|
| c_7 | c_6 | c_5 | c_4 |
| | | | |
|---|---|---|---|
| c_3 | c_2 | c_1 | c_0 |
Then, this is interpreted as the single-word UTF-16 encoding of the surrogate characters corresponding to the 21-bit sequences
`0 0000 1101 10 c_19 c_18 c_17 c_16 c_15 c_14 c_13 c_12 c_11 c_10`
and
`0 0000 1101 11 c_9 c_8 c_7 c_6 c_5 c_4 c_3 c_2 c_1 c_0`.
Finally, this is represented in three-byte UTF-8 as
| | | | |
|---|---|---|---|
| 1 | 1 | 1 | 0 |
| | | | |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| | | | |
|---|---|---|---|
| 1 | 0 | 1 | 0 |
| | | | |
|---|---|---|---|
| c_19 | c_18 | c_17 | c_16 |
| | | | |
|---|---|---|---|
| 1 | 0 | c_15 | c_14 |
| | | | |
|---|---|---|---|
| c_13 | c_12 | c_11 | c_10 |
| | | | |
|---|---|---|---|
| 1 | 1 | 1 | 0 |
| | | | |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| | | | |
|---|---|---|---|
| 1 | 0 | 1 | 1 |
| | | | |
|---|---|---|---|
| c_9 | c_8 | c_7 | c_6 |
| | | | |
|---|---|---|---|
| 1 | 0 | c_5 | c_4 |
| | | | |
|---|---|---|---|
| c_3 | c_2 | c_1 | c_0 |

## Example
- the Musical Symbol G Clef

- is assigned to Unicode code point U+01D11E,

- which is encoded in double-word UTF-16 by means of the words D834 DD1E (see the example in [UTF-16 Encoding](utf16.md)),

- which might be interpreted as the single-word UTF-16 encoding of the surrogate characters U+D834 and U+DD1E,

- which correspond to the 21-bit sequences 0 0000 1101 1000 0011 0100 and 0 0000 1101 1101 0001 1110,

- which is represented in three-byte UTF-8 as 1110 1101 1010 0000 1011 0100 1110 1101 1011 0100 1001 1110

- or in hexadecimal notation: ED A0 B4 ED B4 9E

## Related topics
- [ASCII table (C0 Controls and Basic Latin)](ascii_table.md)

- [Unicode](unicode.md)

- [UTF-16 Encoding](utf16.md)

- [UTF-T Encoding](utft.md)
