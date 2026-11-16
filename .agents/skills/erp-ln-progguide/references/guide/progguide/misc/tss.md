# TSS Encoding
TSS is the default [character encoding](../3gl_features/data_types.md#character encoding) in the 3GL language. Several types of TSS-encoded characters can be distinguished. The first distinction is between single-byte and multibyte.

- A single-byte TSS-encoded character occupies exactly one byte and that byte has a value different from 0x9B.

- A multibyte TSS-encoded character occupies exactly four subsequent bytes and the first byte has the value 0x9B.

Both single-byte and multibyte TSS-encoded characters can be further distinguished.

## Single-byte TSS-encoded characters
| | |
|---|---|
| TSS range (hexadecimal) | Meaning |
| 00 … 7F | [ASCII](ascii_table.md) character. |
| 80 … 8A | Line drawing character. |
| 8B … 9A | Code feature (see [cf$()](../functions_char_b_win/cf.md)). |
| 9B | Lead-byte value for four-byte TSS sequence. |
| 9C … 9E | Reserved for future use. |
| 9F | Used to encode the Euro Sign € in the rare circumstance (i.e. only in a Cyrillic context) that none of the byte values in the range A0 … FF can be used for it. |
| A0 … FF | Used to encode characters from one of the ISO 8859 subsets, dependent on the character set of the current locale. If possible, one of the values is used to encode the Euro Sign €, which normally is not part of the supported ISO 8859 subsets. This usage of the range A0 … FF is ambiguous. For example, in ISO 8859-1 the byte value E7 encodes the character Latin Small Letter C With Cedilla ç, but in ISO 8859-7 it encodes the character Greek Small Letter Eta η. |

## Multibyte TSS-encoded characters
Multibyte TSS-encoded characters are exactly four bytes long, and their first byte has hexadecimal value 9B. They are distinguished by the value of their second byte.
| | |
|---|---|
| TSS range (hexadecimal) | Meaning |
| 9B 21 *pp qq* | Japanese full width character. |
| 9B 23 21 *pp* | Japanese half width character. |
| 9B 25 *pp qq* | Simplified Chinese character. |
| 9B 27 *pp qq* | Traditional Chinese character. |
| 9B 31 *pp qq* | Korean (Wansung) character. |
| 9B 32 *pp qq* | Korean (Johab) character. |
| 9B 9C 9D *nn* | Used to encode characters from one of the single-byte Windows Code Pages that cannot be unified with one of the characters of the corresponding ISO 8859 subset. The fourth byte *nn* is 64 (0x40) less than the Windows Code Page encoding of the character. For example, the character Horizontal Ellipsis … (encoded with hexadecimal byte value 85 in Windows Code Page 1252) is not available in the corresponding character set ISO 8859-1, and therefore it is encoded in multibyte TSS as 9B 9C 9D 45. In principle, this usage is ambiguous. However, in practice it appears that only 3 of the 52 used encodings in this range are ambiguous. For example, TSS-encoding 9B 9C 9D 74 is used in two different cases: In Windows Code Page 1251 (Cyrillic), hexadecimal byte value B4 encodes the character Cyrillic Small Letter Ghe With Upturn ґ. This character is not available in the corresponding Cyrillic character set ISO 8859-5. Therefore, it is encoded in TSS as 9B 9C 9D 74. In Windows Code Pages 1256 (Arabic) and 1257 (Baltic Rim) hexadecimal byte value B4 encodes the character Acute Accent ´. This character is neither available in the Arabic character set ISO 8859-6, nor in the Baltic Rim character set ISO 8859-13. Therefore, it is encoded in TSS as 9B 9C 9D 74. |
| 9B BC *pp qq* … 9B BF *pp qq* | Used to encode the Basic Multilingual Plane (BMP), i.e. the first 2^16 Unicode code points (U+0000 … U+FFFF). See [UTF-T Encoding](utft.md). For a Unicode code point in this range, its [UTF-16](utf16.md) encoding consists of a single 16-bit word. The first 128 Unicode code points correspond to the [ASCII](ascii_table.md) character set. For ASCII characters, this multibyte TSS encoding must not be used. Instead, for ASCII characters the single-byte TSS encoding must be used. |
| 9B C0 *pp qq* … 9B FF *pp qq* | Used to encode the Supplementary Characters, i.e. the remaining 2^20 Unicode code points (U+010000 … U+10FFFF). See [UTF-T Encoding](utft.md). For a Unicode code point in this range, its [UTF-16](utf16.md) encoding consists of two 16-bit words. |

## Ambiguity
Two areas of the TSS encoding are ambiguous: the single-byte range A0 … FF and the multibyte range 9B 9C 9D *nn*. For several TSS encodings in these ranges it is not completely clear which character is meant. In slightly other words: it depends on the context which character is meant.
For example, in a West-European context the byte value E7 encodes the character Latin Small Letter C With Cedilla ç, but in a Greek context it encodes the character Greek Small Letter Eta η. And, in a Cyrillic context, the four-byte sequence 9B 9C 9D 74 encodes the character Cyrillic Small Letter Ghe With Upturn ґ, but in an Arabic or Baltic context it encodes the character Acute Accent ´.
The required context information is contained in the current locale, especially in the character set used by that locale. See [mb.locale.info()](../functions_multibyte_strings/mb.locale.info.md).

## Aliasing
Many characters can be encoded in TSS in more than one way. Such characters have several 'aliases', therefore this phenomenon is called 'aliasing'. For example, the character Greek Small Letter Alpha α can be encoded in TSS (in a Greek context) by means of the single-byte value E1, or it can be encoded by means of each of the multibyte TSS sequences 9B 21 26 41 (in the area for Japanese full width characters), 9B 25 A6 C1 (in the area for Simplified Chinese characters), 9B 27 A3 5C (in the area for Traditional Chinese characters), 9B 31 A5 E1 (in the area for Korean (Wansung) characters), or 9B BC 87 B1 (in the UTF-T area).
When such a character must be encoded in TSS, then it depends on the context which of the available aliases is chosen. If the environment is running in Unicode mode, then the UTF-T encoding is chosen. Otherwise, the character set of the current locale is used to select the appropriate TSS area to encode the character in.

## Unification
More or less the inverse of the phenomenon of aliasing is called 'unification'. Code points from different character sets may represent the same character, and may be mapped to the same TSS code point.
For example, code point B3 in character set ISO 8859-5 and code point C3 in Windows Code Page 1251 both represent the character Cyrillic Capital Letter Ghe Г and are mapped to the single TSS code point B3.
As another example, consider the Japanese TSS code point 9B 21 25 22, which represents the character Katakana Letter A ア. Each one of the Kanji EUC code point A5 A2, the Shift JIS code point 83 41, and the Windows Code Page 932 code point 83 41 represents that same character Katakana Letter A ア, so each one of them is mapped to TSS code point 9B 21 25 22.

## Unicode mode
If the environment is running in Unicode mode, then the phenomena of ambiguity and aliasing almost disappear. Some ambiguity remains possible when old TSS-encoded data is used, either received from external parties not running in Unicode mode, or retained in the system itself from before it was switched to Unicode mode.
TSS data generated when running in Unicode mode (e.g. by means of one of the functions [mb.import$()](../functions_multibyte_strings/mb.import.md), [mb.import.raw()](../functions_multibyte_strings/mb.import.raw.md), [uni.import()](../functions_multibyte_strings/uni.import.md), and [utf8.import()](../functions_multibyte_strings/utf8.import.md)) is restricted to the single-byte range 00 … 9A (for ASCII, line drawing characters, and code features) and the multibyte UTF-T range 9B BC *pp qq* … 9B FF *pp qq* (for non-ASCII Unicode).
This implies that the phenomenon of unification occurs very often. For example, the character Greek Small Letter Alpha α is mapped to UTF-T code point 9B BC 87 B1, regardless whether it was originally represented by a code point in a Greek character set (code point E1 in ISO 8859-7 or Windows Code Page 1253), or in a Japanese character set (code point A6 C1 in Kanji EUC, or code point 83 BF in Shift JIS or Windows Code Page 932), or in a Simplified Chinese character set (code point A6 C1 in GB2312 or Windows Code Page 936), or in a Traditional Chinese character set (code point A3 5C in Big 5 or Windows Code Page 950), or in a Korean character set (code point A5 E1 in Wansung or Windows Code Page 949).

## Related topics
- [ASCII table (C0 Controls and Basic Latin)](ascii_table.md)

- [UTF-T Encoding](utft.md)
