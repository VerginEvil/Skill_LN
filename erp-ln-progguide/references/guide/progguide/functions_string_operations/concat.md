# concat$()

## Syntax:
`function string concat$( string separator, void value... )`

## Description
The function concat$ converts one or more values to strings and concatenates them, separated by a separator, to a single string. You can use [string.scan()](../functions_formatting_io/string.scan.md) to split the string again into its individual parts.
This function is used mainly by the report processor to save unsorted records in a sequential file for subsequent sorting.

## Arguments
| | | |
|---|---|---|
| `string` | `separator` |  The first character of this string is placed as a separator between individual values in the result string. Even individual empty string values are separated by that character (see example). When the supplied string value is empty, the [NULL character](../3gl_features/null_characters_in_strings.md) is used as the separator character. As of [bshell TIV](../tiv/tiv_overview.md) [level 2340](../tiv/tiv_2340.md), when this string is of type multibyte string, the separator character (i.e. the first character of this argument) may be a multibyte character (4 bytes, starting with byte 0x9b). In all other cases (i.e. when this string is of type single-byte string or when the [bshell TIV level](../tiv/tiv_overview.md) is less than [2340](../tiv/tiv_2340.md)) the uninterpreted first byte of this string is used as the separator character. The byte value of the separator character may even be 0x9b (the lead-byte value for four-byte TSS sequences) or 0 (normally used as an [end of string marker](../3gl_features/null_characters_in_strings.md)).  |
| `void` | `value...` |  Zero or more values of type long, double, or string. [Implicit conversion](../3gl_features/type_conversions.md#implicit_type_conversion) of each value from its original type to type string is performed. The resulting string value is placed in the output string.  |

## Return values
The return value is the concatenation of the supplied values (implicitly converted to string values), separated by the specified separator character.
As of [bshell TIV](../tiv/tiv_overview.md) [level 2340](../tiv/tiv_2340.md), the resulting string is of type multibyte string if and only if the supplied separator string or any of the supplied values is of type multibyte string.
In all other cases (i.e. when the supplied separator string and all supplied string values are of type single-byte string or when the [bshell TIV level](../tiv/tiv_overview.md) is less than [2340](../tiv/tiv_2340.md)) the resulting string is of type single-byte string.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string    ret(100)
long      a
string    b(5)
double    d
string    e(5)
string    f(5)

a = 10
b = "hello"
d = 1.123456
e = ""
f = "there"

ret = concat$( "|",a*10,b,d,e,f )     | ret now contains "100|hello|1.123456||there"
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
