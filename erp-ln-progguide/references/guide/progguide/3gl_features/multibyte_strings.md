# Multibyte strings
By means of the keyword MB, a string variable can be declared as a multibyte string. The purpose of the concept of a 'multibyte string' is to support the use of a larger domain of characters than available in the [ASCII](../misc/ascii_table.md) character set. Multibyte strings are not only meant for the support of typical multibyte scripts like Japanese, Chinese, and Korean, but also for the support of non-ASCII single-byte scripts, like Greek, Cyrillic, Hebrew, Arabic, and Thai.
It should be noticed that the attribute 'single-byte' or 'multibyte', when applied to a character, has a different meaning than when applied to a string.
- When applied to a character, the attribute 'single-byte' means that the character is encoded in one byte and the attribute 'multibyte' means that the character is encoded in multiple bytes. The used character encoding may be left unspecified. In the context of the [TSS encoding](../misc/tss.md), multibyte characters are encoded in four bytes. In the context of other encodings, multibyte characters may be encoded also in other amounts of bytes; e.g. in the [UTF-8 encoding](../misc/utf8.md) multibyte characters may be encoded in two, three, or four bytes.
- When applied to a string, the attribute 'single-byte' or 'multibyte' does not say anything about the contents of the string; such an attribute only indicates how the string contents must be interpreted. Any single-byte string as well as any multibyte string can contain any mixture of single-byte and multibyte characters. However, in a multibyte string the [TSS encoding](../misc/tss.md) is assumed and the four bytes of a multibyte character will be counted as one character, whereas in a single-byte string they will be counted as four characters.   All supported scripts contain the ASCII character set as a subset and encode the ASCII characters in the 'traditional' way. Notice that [ASCII](../misc/ascii_table.md) is a 7-bit character set, i.e. all ASCII characters are encoded by means of 'low' byte values in the range [0 … 127]. The remaining 'high' byte values in the range [128 … 255] are used by each script in its own way for the encoding of single-byte or multibyte characters. In the [TSS encoding](../misc/tss.md) these bytes are used in a proprietary way, but bytes in the hexadecimal range [0xa0 … 0xff] are used to mimic the (single-byte) encodings of the various supported ISO 8859 character sets.
When a single-byte string is known to possibly contain any TSS-encoded non-ASCII content (other than the TSS line drawing characters in the range [0x80 … 0x8a] and the TSS code features in the range [0x8b … 0x9a]), then either consider to change the type of the string to multibyte or be prepared that the string may contain not only single-byte characters in the range [0x9f … 0xff] but also multibyte lead bytes 0x9b, followed by three trail bytes.
For a further discussion, the difference between a single-byte string and a multibyte string may well be explained by discussing the following four properties:
- the byte count;
- the byte limit;
- the character count;
- the character limit.   The following general remarks about these properties can be made, as also illustrated in the following table. First of all, it can be said that for single-byte strings there is *no* difference between the byte count and the character count and also *no* difference between the byte limit and the character limit. Further, it can be said that for multibyte strings there *is* a difference between the byte count and the character count and also between the byte limit and the character limit.
| | | | |
|---|---|---|---|
|  | single-byte | multibyte |  |
| byte | character | byte | character |
| count | There is no difference between the three properties single-byte byte count, single-byte character count, multibyte byte count.  | multibyte character count |  |
| limit | There is no difference between the two properties single-byte byte limit, single-byte character limit.  | multibyte byte limit | multibyte character limit |
-
-
-
-
-
Each of these properties is now discussed separately,

## The byte count of a multibyte string value
For any string value, its *byte count* is defined as the total number of bytes of the string representation. Regarding the byte count, there is no difference between a single-byte string value and a multibyte string value. In other words: casting a single-byte string value to a multibyte string value (or vice versa) does not change its byte count.

## The byte limit of a multibyte string variable
For any string variable, its *byte limit* is defined as the maximal byte count for the string values that can be stored in the string variable. Regarding the byte limit, there is a difference between a single-byte string variable and a multibyte string variable.
The byte limit of a single-byte string variable is equal to its declared size, e.g. the byte limit of the variable `my_singlebyte_string`, declared as `STRING my_singlebyte_string(10)`, is 10.
For the byte limit of a multibyte string variable, its declared size is multiplied with a certain factor, the *internal mb factor*. For example, the byte limit of the variable `my_multibyte_string`, declared as `STRING my_multibyte_string(10) MB`, is 10 times the internal mb factor.
Historically, the declared size of a multibyte string variable (10 in the above example) was considered as the number of *display positions* available for the string values to be stored in the variable. Enough memory is reserved for the variable in order to contain any reasonable [TSS-encoded](../misc/tss.md) string that needs at most the specified number of positions to be displayed. One TSS-encoded character occupies 1 or 4 bytes of memory and needs 0, 1, or 2 positions to be displayed. The interpretation of when a TSS-encoded string is 'reasonable' differs, dependent on the system configuration.
Typical values for the internal mb factor are as follows.
-  1 In a pure single-byte configuration, only single-byte characters and no 4-byte TSS characters are expected. Further, all single-byte characters need at most 1 position to be displayed. In such a case, the internal multibyte factor is set to 1.
-  2 In a pure multibyte configuration, both single-byte and 4-byte TSS characters are expected. In such a configuration, the 4-byte TSS characters typically are fullwidth East Asian characters, which need 2 positions to be displayed. In such a case, the internal multibyte factor is set to 2.
-  4 In a Unicode configuration, both single-byte and 4-byte TSS characters are expected. In such a configuration, the 4-byte TSS encoding is used for all non-ASCII characters, without any indication that such characters typically are fullwidth East Asian characters. In such a case, the internal multibyte factor is set to 4.

## The character count of a multibyte string value
For any string value, its *character count* is defined as the total number of characters of the string representation. Regarding the character count, there is a difference between a single-byte string value and a multibyte string value.
The character count of a single-byte string value is equal to its byte count, i.e. each byte of a single-byte string value counts as a separate character. Notice that for other purposes a single-byte string value may be interpreted according to the default character encoding: [TSS](../misc/tss.md), but *not* for the purpose of determining its character count.
The character count of a multibyte string value is determined by interpreting the bytes of the string value according to the default character encoding: [TSS](../misc/tss.md). According to that encoding, the byte value 0x9b is considered as the lead byte value of a four-byte sequence, encoding a single character.

## The character limit of a multibyte string variable
For any string variable, its *character limit* is defined as the maximal character count for the string values that can be stored in the string variable. Regarding the character limit, there is a difference between a single-byte string variable and a multibyte string variable.
The character limit of a single-byte string variable is equal to its byte limit. Just as the byte limit, also the character limit of a single-byte string variable is equal to its declared size, e.g. both the byte limit and the character limit of the variable `my_singlebyte_string`, declared as `STRING my_singlebyte_string(10)`, is 10.
For a multibyte string variable, no single universal definition of its character limit is available. In practice, a mixture of the following different approaches is used.
- The weak approach: use all available bytes.
- The strong approach: restrict the display width to the (estimated) available display width.

## Weak approach: use all available bytes
The *weak approach* is to make the character limit equal to the byte limit. In this approach there is no objection against filling all the available bytes with encoded characters. The consequence of that might be that the string variable contains a string value that has a much greater character count and also a much greater display width than the declared size of the variable.
For example, consider the variable `my_multibyte_string`, declared as `STRING my_multibyte_string(10) MB`, in a configuration where the internal mb factor is set to 4. The byte limit of `my_multibyte_string` is then 40, i.e. the product of its declared size and the internal mb factor. Several extreme ways to fill `my_multibyte_string` are as follows.
-  Zero-width multibyte characters Fill `my_multibyte_string` with 10 zero-width multibyte characters, for example 10 times the Unicode character U+0E3A (the Thai character Phinthu): `"↮↮↮↮↮↮↮↮↮↮"`, (each ↮ representing one zero-width Thai character Phinthu). Encoded in [UTF-T](../misc/utft.md), each character occupies 4 bytes, filling all the available 40 bytes. The display width of each character is 0, resulting in a display width of 0 for the complete string value.
-  Halfwidth multibyte characters Fill `my_multibyte_string` with 10 halfwidth multibyte characters, for example the first ten (small) letters of the Greek alphabet: `"αβγδεζηθικ"`. Encoded in [UTF-T](../misc/utft.md), each character occupies 4 bytes, filling all the available 40 bytes. The display width of each character is 1, resulting in a display width of 10 for the complete string value.
-  Fullwidth multibyte characters Fill `my_multibyte_string` with 10 fullwidth multibyte characters, for example the Unicode characters U+AC00 … U+AC09 (the first ten Hangul syllables of the Korean script): `"가각갂갃간갅갆갇갈갉"`. Encoded in TSS, each character occupies 4 bytes, filling all the available 40 bytes. The display width of each character is 2, resulting in a display width of 20 for the complete string value.
-  Single-byte characters Fill `my_multibyte_string` with 40 single-byte characters, for example four times the ASCII characters 0 … 9: `"0123456789012345678901234567890123456789"` or 40 space characters `"␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣"`, (each ␣ representing one space character). Encoded in TSS, each character occupies 1 byte, filling all the available 40 bytes. The display width of each character is 1, resulting in a display width of 40 for the complete string value.    Summarized, we see in these examples character counts of 10 and 40 and display widths of 0, 10, 20, and 40.
```

| character count 10, display width 0 (each ↮ represents one zero-width Thai character Phinthu):
"↮↮↮↮↮↮↮↮↮↮"

| character count 10, display width 10:
"αβγδεζηθικ"

| character count 10, display width 20:
"가각갂갃간갅갆갇갈갉"

| character count 40, display width 40 (each ␣ represents one space character):
"0123456789012345678901234567890123456789"
"␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣"
```

## Strong approach: restrict to available display width
The *strong approach* is to compute the character limit from the byte limit by dividing it by a certain factor, the *external mb factor*, which in practice is often equal to the *internal mb factor* discussed above. This may be seen as an attempt to estimate the available display width for which the available byte limit may be intended. The resulting character limit value is in fact not a limit on the character count, but a limit on the display width. For example, a fullwidth East Asian character ‘fills’ 2 display positions from this ‘display width limit’ and a zero-width Thai character does not ‘fill’ any display position.
The strong approach is used during the assignment of a string value to a string variable. Therefore, continuing the example discussed above for the weak approach, such an assignment cannot be used to fill the variable `my_multibyte_string` with the extreme values discussed there. This is shown in the following example code. Assume *internal mb factor* = 4.
```

STRING my_multibyte_string(10) MB
```
For the variable `my_multibyte_string`, we have:
- the byte limit is 40;
- the weak character limit is 40;
- the strong character limit is 10.
```

my_multibyte_string = "0123456789012345678901234567890123456789"
```
The strong character limit restricts the assignment to a display width of 10 positions, so only 10 characters are copied. The variable `my_multibyte_string` now contains the value `"0123456789"`, of which the byte count and the character count are both 10; the display width is 10.
```

my_multibyte_string(1) = "0123456789012345678901234567890123456789"
```
The substring `my_multibyte_string(1)` denotes the substring of `my_multibyte_string`, starting from position 1 and extending to the end, so it is simply the complete string variable `my_multibyte_string`. The strong character limit restricts the assignment to a display width of 10 positions, so only 10 characters are copied. The substring is considered as fixed, so it is subject to space padding. For the space padding the strong character limit is not applied! Instead of that, the weak character limit is applied: use all available bytes. The variable `my_multibyte_string` now contains the value `"0123456789␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣"`, of which the byte count and the character count are both 40; the display width is 40.
```

my_multibyte_string(1) = ""
```
An empty string value is assigned. The substring is considered as fixed, so it is subject to space padding of the unused bytes. The variable `my_multibyte_string` now contains the value `"␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣"`, of which the byte count and the character count are both 40; the display width is 40.
```

my_multibyte_string = "αβγδεζηθικ" | the first ten Greek small letters
```
The variable `my_multibyte_string` now contains the value `"αβγδεζηθικ"`, of which the byte count is 40 and the character count is 10; the display width is 10.
```

my_multibyte_string = "가각갂갃간갅갆갇갈갉" | the first ten Hangul syllables of the Korean script
```
The strong character limit restricts the assignment to a display width of 10 positions, so only 5 characters are copied. The variable `my_multibyte_string` now contains the value `"가각갂갃간"` (the first five Hangul syllables of the Korean script), of which the byte count is 20 and the character count is 5; the display width is 10.
```

my_multibyte_string(1) = "가각갂갃간갅갆갇갈갉" | the first ten Hangul syllables of the Korean script
```
The substring `my_multibyte_string(1)` denotes the substring of `my_multibyte_string`, starting from position 1 and extending to the end, so it is simply the complete string variable `my_multibyte_string`. The strong character limit restricts the assignment to a display width of 10 positions, so only 5 characters are copied. The substring is considered as fixed, so it is subject to space padding of the unused bytes. The variable `my_multibyte_string` now contains the value `"가각갂갃간␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣"`, of which the byte count is 40 and the character count is 25; the display width is 30.
```

my_multibyte_string = "↮↮↮↮↮↮↮↮↮↮" | each ↮ represents one zero-width Thai character Phinthu
```
The variable `my_multibyte_string` now contains the value `"↮↮↮↮↮↮↮↮↮↮"`, of which the byte count is 40 and the character count is 10; the display width is 0.
```

my_multibyte_string(10;1) = "6789xx"
```
Before the assignment, the substring `my_multibyte_string(10;1)` contains the value `"↮"`, of which the byte count is 4 and the character count is 1; the display width is 0. When a new value is assigned to it, it is important to notice that its byte limit is 4 and its strong character limit is 10. The strong character limit of a substring is roughly calculated as
- the strong character limit of the surrounding string (in this case: 10)
- minus the display width of the prefix of the substring (in this case 0, i.e. the display width of `my_multibyte_string(1;9)`).   The byte limit restricts the assignment to only 4 bytes. After the assignment, the substring contains the value `"6789"`, of which the byte count and the character count are both 4; the display width is 4.
The variable `my_multibyte_string` now contains the value `"↮↮↮↮↮↮↮↮↮6789"`, of which the byte count is 40 and the character count is 13; the display width is 4.
Notice that after this assignment the original substring notation `my_multibyte_string(10;1)` can no longer be used to address the new value `"6789"`. That part of the string now must be addressed as `my_multibyte_string(10;4)`
```

my_multibyte_string(9;1) = "2345xx"
```
Before the assignment, the substring `my_multibyte_string(9;1)` contains the value `"↮"`, of which the byte count is 4 and the character count is 1; the display width is 0. Its byte limit is 4 and its strong character limit is 10.
The byte limit restricts the assignment to only 4 bytes. After the assignment, the substring contains the value `"2345"`, of which the byte count and the character count are both 4; the display width is 4.
The variable `my_multibyte_string` now contains the value `"↮↮↮↮↮↮↮↮23456789"`, of which the byte count is 40 and the character count is 16; the display width is 8.
Notice that after this assignment the part `"2345"` of the string must be addressed as `my_multibyte_string(9;4)` and the part `"6789"` of the string must be addressed as `my_multibyte_string(13;4)`
```

my_multibyte_string(8;1) = "8901xx"
my_multibyte_string(7;1) = "4567xx"
my_multibyte_string(6;1) = "0123xx"
my_multibyte_string(5;1) = "6789xx"
my_multibyte_string(4;1) = "2345xx"
my_multibyte_string(3;1) = "8901xx"
my_multibyte_string(2;1) = "4567xx"
my_multibyte_string(1;1) = "0123xx"
```
The variable `my_multibyte_string` subsequently contains the following values.
- Character count 19, display width 12: `"↮↮↮↮↮↮↮890123456789"`
- Character count 22, display width 16: `"↮↮↮↮↮↮4567890123456789"`
- Character count 25, display width 20: `"↮↮↮↮↮01234567890123456789"`
- Character count 28, display width 24: `"↮↮↮↮678901234567890123456789"`
- Character count 31, display width 28: `"↮↮↮2345678901234567890123456789"`
- Character count 34, display width 32: `"↮↮89012345678901234567890123456789"`
- Character count 37, display width 36: `"↮456789012345678901234567890123456789"`
- Character count 40, display width 40: `"0123456789012345678901234567890123456789"`  Notice that after these assignments the rightmost part `"2345"` of the string must be addressed as `my_multibyte_string(33;4)` and the rightmost part `"6789"` of the string must be addressed as `my_multibyte_string(37;4)`.

## Related topics
- [3GL programming language features: overview](overview.md)
- [Variables](variables.md)
