# qss.sort()

## Syntax:
`function long qss.sort( ref void array, const long def(,), [ long dept ] )`

## Description
This function performs a fast sort of a specified array.
Note that the order in the result array of two elements that compare identical is unpredictable.

## Arguments
```
void  qss.start(
   ref long def,
   long     field_number,
   long     position
)
```
```
void qss.way(
   ref long def,
   long     field_number,
   long     way
)
```
| | |
|---|---|
| QSS.UP | Ascending field comparison order. Smaller field values compare before greater field values. |
| QSS.DOWN | Descending field comparison order. Greater field values compare before smaller field values. |
When the sort field type is a string type, then at most one of the following values can be added. As of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md), the value QSS.ALFA.MASK is available as the [bitwise OR](../functions_bit/bit_and_exor_in_inv_or.md#bit_or) of all these values.
| | |
|---|---|
| default value 0 | The string field is compared as a fixed-length byte sequence, with a byte length as specified by qss.length(). The bytes are compared as values in the unsigned 8-bit value range [0 … 255]. |
| QSS.ALFA | The string field is compared as a null-terminated string. In addition to the byte length limitation specified by qss.length(), any bytes after the first 0-byte are ignored. Notice that strings in a string array are usually space padded. In Unicode mode, the [Unicode Collation Algorithm](http://www.unicode.org/reports/tr10/tr10-11.html) is used. This is a multi-level comparison algorithm, which roughly works as follows. At the first level the strings are compared while ignoring accents (e.g. all five characters a, á, à, ä, and â compare equal), case differences (e.g. characters A and a compare equal) and punctuation (characters like.,:; " ' ! ? are left out from the comparison). When strings compare equal at the first level, the comparison is extended to higher levels, each next level ignoring less of the available information in the strings. When not in Unicode mode, a string field of type DB.STRING is compared as a null-terminated and byte length limited byte sequence. The bytes are compared as values in the unsigned 8-bit value range [0 … 255]. When not in Unicode mode, a string field of type DB.MULTIBYTE is compared as a null-terminated and byte length limited character sequence. The bytes are interpreted as a sequence of [TSS-encoded](../misc/tss.md) characters. The characters are compared from left to right according to their character weight. Character weights are assigned according to the external, native byte encoding of the characters. The result is the same as if the string field is converted to the external, native encoding and then compared as a byte sequence. |
| QSS.ALFA.SPACE.STRIPPING | This value is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md). The behavior is the same as for QSS.ALFA, but the comparison is done as if all trailing space characters are stripped from the string field. |
| QSS.ALFA.SPACE.PADDING | This value is available as of [porting set TIV](../tiv/tiv_overview.md) [level 2420](../tiv/tiv_2420.md). The behavior is the same as for QSS.ALFA, but the comparison is done as if the string field is padded with spaces until the byte length specified by qss.length(). Notice that strings in a string array are usually space padded. |
```
void qss.type(
   ref long def,
   long     field_number,
   long     type
)
```
| |
|---|
| DB.BYTE |
| DB.ENUM |
| |
|---|
| DB.INTEGER |
| |
|---|
| DB.LONG |
| DB.BITSET |
| DB.DATE |
| DB.MAIL |
| DB.TEXT |
| |
|---|
| DB.TIME |
| |
|---|
| DB.FLOAT |
| |
|---|
| DB.DOUBLE |
| |
|---|
| DB.STRING |
| DB.MULTIBYTE |
```
void qss.length(
   ref long def,
   long     field_number,
   long     length
)
```
If you define fewer sort fields than you have declared, you must close the *def* argument by calling *qss.start()* with a start position of zero. For example, if you have declared three sort fields, as follows:def(3,4)but then create only two sort fields, you must close the definition with the following call:qss.start(def,3,0)

## Return values
| | |
|---|---|
| 0 | success |
| -1 | error, *array* and/or *def* is empty |
| -11 | *def* is not of type long array or *array* not of type array |
| -12 | *array* of strings must have > 1 dimension |
| -13 | *dept* must be positive |
| -14 | *def* argument not correctly declared |
| -15 | *def* size exceeds *array* size |
| -16 | QSS.TYPE not correct |
| -17 | *array* argument not correct |
| -18 | no definition found in *def* |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Searching and sorting data overview and synopsis](overview_and_synopsis.md)

- [Table searching and sorting sample programs](example.md)
