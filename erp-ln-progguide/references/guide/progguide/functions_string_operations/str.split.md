# str.split()

## Syntax:
`function long str.split( const string string$, const string separator$, long limit, ref string parts )`

## Description
Splits a string into an array of strings by separating the string into substrings, using a specified separator string to determine where to make each split.
The `parts` string array will be resized as required. In order to be able to resize `parts`, the variable passed must be declared as a based string array.
The found substrings are stored in the `parts` string array in such a way, that any trailing spaces are preserved. This reduces the need to use ` [strip$()](strip.md)` on the elements of the string array.
If `separator$` is an empty string, `string$` is split into characters. In that case the following limitations apply:
- if `string$` is a multibyte string containing multibyte characters, and `parts` is a single-byte string array, multibyte characters will not be copied. Instead, an empty string is stored in `parts`.
- if `string$` is a single-byte string containing high ASCII characters, and `parts` is a multibyte string array, high ASCII characters will not be copied. Instead, an empty string is stored in `parts`.

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |
| `const string` | `separator$` |  the separator to search for to split the string into substrings; if an empty string is passed, the string is split into characters  |
| `long` | `limit` |  when > 0, this is used to limit the number of parts being returned; the last part of the string (that was not split) is returned as the last element in the array when <= 0, the number of returned parts is determined by this function  |
| `ref string` | `parts` |  pass a resizable array; this stores the found substrings; substrings are stored in this array as null terminated strings, which means that trailing spaces belonging to the found substrings are preserved  |

## Return values
the number of found substrings

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2340.

## Preconditions
- Parameter `parts` must be a resizable string array

## Examples
```

string source(50)
string parts(1,1) based
long num.parts

|                  1         2         3         4         5
| pos     12345678901234567890123456789012345678901234567890
source = "the quick brown fox jumps over the lazy dog"

num.parts = str.split(source, " ", 0, parts)
| parts contains the following 9 elements:
| parts(1,1) : "the"
| parts(1,2) : "quick"
| parts(1,3) : "brown"
| parts(1,4) : "fox"
| parts(1,5) : "jumps"
| parts(1,6) : "over"
| parts(1,7) : "the"
| parts(1,8) : "lazy"
| parts(1,9) : "dog"

| split using the comma; in this case there is no data between the separators
source = ",,"

num.parts = str.split(source, ",", 0, parts)
| parts now contains 3 elements:
| parts(1,1) : ""	(this is the empty string found before the first separator)
| parts(1,2) : ""	(this is the empty string found between the two separators)
| parts(1,3) : ""	(this is the empty string found after the last separator)

| see that trailing spaces are preserved:
|                  1         2
| pos     12345678901234567890123456789
source = "monkey, see  , monkey, do"

| limit the split to max 3 parts
num.parts = str.split(source, ", ", 3, parts)
| parts contains 3 elements:
| parts(1,1) = "monkey"
| parts(1,2) = "see  "	(this has trailing spaces)
| parts(1,3) = "monkey, do"	(the rest of the string is not splitted)

| try split a string into 10 characters
source = "abcd"

| use empty string as separator
num.parts = str.split(source, "", 10, parts)
| parts contains only 4 elements:
| parts(1,1) = "a"
| parts(1,2) = "b"
| parts(1,3) = "c"
| parts(1,4) = "d"
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
