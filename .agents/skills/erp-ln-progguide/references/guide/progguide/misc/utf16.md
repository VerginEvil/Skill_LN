# UTF-16 Encoding
UTF-16 is a standard way to encode [Unicode](unicode.md) characters by means of a stream of 16-bit words. First the 'normal' UTF-16 standard is explained, then 'byte-serialized UTF-16' is explained.
In early versions of the Unicode standard, there was a one-to-one correspondence between Unicode characters and 16-bit words. Consequently, in older parts of this Programmers Guide, the term 'Unicode' is often used more or less as a synonym for single-word UTF-16.
Later on, when the need for more than 2^16 Unicode characters arose, the surrogate characters were introduced. At one side they were normal 16-bit Unicode characters, at the other side correct pairs of surrogate characters might be interpreted as new 'supplementary' characters.
Nowadays, the Unicode character model has changed such that certain 16-bit words do not at all represent any Unicode character. A correct pair of such 16-bit words does represent a single (supplementary) Unicode character.
Each Unicode character is encoded by a sequence of one to two 16-bit words. The Unicode standard defines 2^16 + 2^20 code points, numbered U+0000 … U+10FFFF. With a straightforward binary numbering of the complete Unicode range, 21 bits are needed. Name the 21 bits as follows:
`b_20 b_19 b_18 b_17 b_16 b_15 b_14 b_13 b_12 b_11 b_10 b_9 b_8 b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0`
For a slightly different numbering, first add an amount of 0x0F0000 (binary 0 1111 0000 0000 0000 0000) to the code point value. Name the resulting 21 bits as follows:
`c_20 c_19 c_18 c_17 c_16 c_15 c_14 c_13 c_12 c_11 c_10 c_9 c_8 c_7 c_6 c_5 c_4 c_3 c_2 c_1 c_0`
Notice the following properties of the two groups of bits:

- `b_` *i* = `c_` *i* for each *i* in the range 0 … 15.

- Bits `b_20 b_19 b_18 b_17 b_16` run through only the first 17 of the 32 combinations (that is to say: 00000 … 10000).

- Bits `c_20 c_19 c_18 c_17 c_16` run through only the last 17 of the 32 combinations (that is to say: 01111 … 11111).

- The single bit `c_20` is enough to distinguish between the Basic Multilingual Plane (Unicode range U+0000 … U+FFFF, `c_20` = 0) and the Supplementary Characters (Unicode range U+010000 … U+10FFFF, `c_20` = 1).

In the explanation below,

- each small box represents a single bit;

- each group of four horizontally adjacent small boxes represents a hexadecimal digit;

- each row (containing four groups of four horizontally adjacent boxes) represents a 16-bit word.

After these preliminaries, the UTF-16 encoding is defined as follows.

## Single-word UTF-16
Single-word UTF-16 is used for Unicode characters in the Basic Multilingual Plane (BMP), i.e. the range U+0000 … U+FFFF. For a Unicode character in this range, bit `b_` *i* is zero for each *i* in the range 16 … 20, and the remaining 16 bits are represented in single-word UTF-16 as follows:
| | | | |
|---|---|---|---|
| b_15 | b_14 | b_13 | b_12 |
| | | | |
|---|---|---|---|
| b_11 | b_10 | b_9 | b_8 |
| | | | |
|---|---|---|---|
| b_7 | b_6 | b_5 | b_4 |
| | | | |
|---|---|---|---|
| b_3 | b_2 | b_1 | b_0 |
Notice that this means that each character in the BMP is encoded by a 16-bit word with the corresponding Unicode code point value.
No characters are assigned to code points in the Surrogates Area, i.e. the Unicode range U+D800 … U+DFFF. This means that the values 0xD800 … 0xDFFF will not occur in single-word UTF-16. Instead, they are used for double-word UTF-16.

## Example 1
- ASCII character 'A' (ASCII value 0x41)

- is assigned to Unicode code point U+0041,

- which corresponds to the 21-bit sequence 0 0000 0000 0000 0100 0001,

- which is represented in single-word UTF-16 as 0000 0000 0100 0001

- or in hexadecimal notation: 0041.

## Example 2
- the Latin Small Letter C With Cedilla ç

- is assigned to Unicode code point U+00E7,

- which corresponds to the 21-bit sequence 0 0000 0000 0000 1110 0111,

- which is represented in single-word UTF-16 as 0000 0000 1110 0111

- or in hexadecimal notation: 00E7.

## Example 3
- the Euro Sign €

- is assigned to Unicode code point U+20AC,

- which corresponds to the 21-bit sequence 0 0000 0010 0000 1010 1100,

- which is represented in single-word byte UTF-16 as 0010 0000 1010 1100

- or in hexadecimal notation: 20AC.

## Double-word UTF-16
Double-word UTF-16 is used for Unicode characters in the range U+010000 … U+10FFFF. For a Unicode character in this range, bit `c_20` = 1 and the remaining 20 bits are represented in double-word UTF-16 as follows:
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
Notice that this Unicode range corresponds with the range of the Supplementary Characters. Further notice that the first word of the double-word UTF-16 representation is in the range 0xD800 … 0xDBFF (corresponding to the single-word UTF-16 representation of the high surrogate code points U+D800 … U+DBFF), and that the second word is in the range 0xDC00 … 0xDFFF (corresponding to the single-word UTF-16 representation of the low surrogate code points U+DC00 … U+DFFF).

## Example
- the Musical Symbol G Clef

- is assigned to Unicode code point U+01D11E,

- which corresponds to the 21-bit sequence 0 0001 1101 0001 0001 1110,

- with an extra offset of 0x0F0000, this becomes the 21-bit sequence 1 0000 1101 0001 0001 1110,

- which is represented in double-word UTF-16 as 1101 1000 0011 0100 1101 1101 0001 1110

- or in hexadecimal notation: D834 DD1E.

## Byte-serialized UTF-16
The UTF-16 standard is concerned with the internal machine representation of Unicode characters by means of a sequence of 16-bit words. The exact way the words are stored internally (perhaps breaking each word into two bytes) is irrelevant for most processing. However, interchange of textual data, particularly between computers of different architectural types, requires consideration of the exact ordering of the transmitted sequence of bytes.
The Unicode standard provides two different orders to serialize the 16-bit words of UTF-16 encoded Unicode characters into a stream of bytes:

- big-endian serialization (UTF-16BE) first adds the most significant byte of a word to the stream and then the least significant byte;

- little-endian serialization (UTF-16LE) first adds the least significant byte of a word to the stream and then the most significant byte.

In the absence of a protocol by means of which sender and receiver may come to an agreement about the byte order, big-endian serialization must be used.
As an example, consider the following sequence of Unicode characters:

- ASCII character 'A'

- Latin Small Letter C With Cedilla ç

- Euro Sign €

- Musical Symbol G Clef.

In the examples above, the UTF-16 representation of each of these characters is given.
Taken together, the hexadecimal UTF-16 representation of the sequence of the four characters is: 0041 00E7 20AC D834 DD1E.
The UTF-16BE (big-endian byte-serialized UTF-16) representation of the four characters is: 00 41 00 E7 20 AC D8 34 DD 1E.
The UTF-16LE (little-endian byte-serialized UTF-16) representation of the four characters is: 41 00 E7 00 AC 20 34 D8 1E DD.

## Related topics
- [ASCII table (C0 Controls and Basic Latin)](ascii_table.md)

- [Unicode](unicode.md)

- [UTF-8 Encoding](utf8.md)

- [UTF-T Encoding](utft.md)
