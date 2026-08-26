# UTF-T Encoding
UTF-T is a proprietary way to encode [Unicode](unicode.md) characters in a stream of [TSS-encoded](tss.md) characters
Each Unicode character is encoded by a sequence of one or four bytes. The Unicode standard defines 2^16 + 2^20 code points, numbered U+0000 … U+10FFFF. With a straightforward binary numbering of the complete Unicode range, 21 bits are needed. Name the 21 bits as follows:
`b_20 b_19 b_18 b_17 b_16 b_15 b_14 b_13 b_12 b_11 b_10 b_9 b_8 b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0`
For a slightly different numbering, first add an amount of 0x0F0000 (binary 0 1111 0000 0000 0000 0000) to the code point value. Name the resulting 21 bits as follows:
`c_20 c_19 c_18 c_17 c_16 c_15 c_14 c_13 c_12 c_11 c_10 c_9 c_8 c_7 c_6 c_5 c_4 c_3 c_2 c_1 c_0`
Notice the following properties of the two groups of bits:
- `b_` *i* = `c_` *i* for each *i* in the range 0 … 15.
- Bits `b_20 b_19 b_18 b_17 b_16` run through only the first 17 of the 32 combinations (that is to say: 00000 … 10000).
- Bits `c_20 c_19 c_18 c_17 c_16` run through only the last 17 of the 32 combinations (that is to say: 01111 … 11111).
- The single bit `c_20` is enough to distinguish between the Basic Multilingual Plane (Unicode range U+0000 … U+FFFF, `c_20` = 0) and the Supplementary Characters (Unicode range U+010000 … U+10FFFF, `c_20` = 1).   In the explanation below,
- each small box represents a single bit;
- each group of four horizontally adjacent small boxes represents a hexadecimal digit;
- each row (containing two groups of four horizontally adjacent boxes) represents a byte.   After these preliminaries, the UTF-T encoding is defined as follows.

## Single-byte UTF-T
Single-byte UTF-T is used for Unicode characters in the range U+0000 … U+007F. For a Unicode character in this range, bit `b_` *i* is zero for each *i* in the range 7 … 20, and the remaining 7 bits are represented in single-byte UTF-T as follows:
| |
|---|
|   |
Notice that this Unicode range corresponds with the [ASCII](ascii_table.md) range. and that each character in this range is encoded by a byte with the corresponding ASCII value.

## Example
- ASCII character 'A' (ASCII value 0x41)
- is assigned to Unicode code point U+0041,
- which corresponds to the 21-bit sequence 0 0000 0000 0000 0100 0001,
- which is represented in single-byte UTF-T as 0100 0001,
- or in hexadecimal notation: 41.

## Four-byte UTF-T
Four-byte UTF-T is used for Unicode characters in the range U+0080 … U+10FFFF. For a Unicode character in this range the 21 bits `c_` *i* are represented in four-byte UTF-T as follows:
| |
|---|
|   |
|   |
|   |
|   |
Notice the following details:
- this Unicode range corresponds with the non-ASCII Characters;
- the first byte of the four-byte UTF-T representation has the value 0x9B, i.e. the normal lead-byte value for four-byte TSS sequences;
- as the bits `c_20 c_19 c_18 c_17 c_16` run through only the last 17 of the 32 combinations (that is to say: 01111 … 11111), the second byte of the four-byte UTF-T representation is in the range 0xBC … 0xFF;
- as the single bit `c_20` is enough to distinguish between the Basic Multilingual Plane and the Supplementary Characters, the range 0xBC … 0xBF for the second byte corresponds to the non-ASCII BMP characters;
- for the same reason, the range 0xC0 … 0xFF for the second byte corresponds to the Supplementary Characters.

## Example
- the Latin Small Letter C With Cedilla ç
- is assigned to Unicode code point U+00E7,
- which corresponds to the 21-bit sequence 0 0000 0000 0000 1110 0111,
- with an extra offset of 0x0F0000, this becomes the 21-bit sequence 0 1111 0000 0000 1110 0111,
- which is represented in four-byte UTF-T as 1001 1011 1011 1100 1000 0001 1110 0111
- or in hexadecimal notation: 9B BC 81 E7.

## Example
- the Euro Sign €
- is assigned to Unicode code point U+20AC,
- which corresponds to the 21-bit sequence 0 0000 0010 0000 1010 1100,
- with an extra offset of 0x0F0000, this becomes the 21-bit sequence 0 1111 0010 0000 1010 1100,
- which is represented in four-byte UTF-T as 1001 1011 1011 1100 1100 0001 1010 1100
- or in hexadecimal notation: 9B BC C1 AC.

## Example
- the Musical Symbol G Clef
- is assigned to Unicode code point U+01D11E,
- which corresponds to the 21-bit sequence 0 0001 1101 0001 0001 1110,
- with an extra offset of 0x0F0000, this becomes the 21-bit sequence 1 0000 1101 0001 0001 1110,
- which is represented in four-byte UTF-T as 1001 1011 1100 0011 1010 0010 1001 1110
- or in hexadecimal notation: 9B C3 A2 9E.

## Related topics
- [ASCII table (C0 Controls and Basic Latin)](ascii_table.md)
- [Unicode](unicode.md)
- [UTF-16 Encoding](utf16.md)
- [UTF-8 Encoding](utf8.md)
