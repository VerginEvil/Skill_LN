# sprintf$()

## Syntax:
`function string sprintf$( string format, [ void ... ] )`

## Description
This formats a string and returns the formatted string. The *format* argument contains zero or more ordinary characters and substitution symbols. The ordinary characters are copied directly to the output string. The substitution symbols specify formats for the values specified in the additional arguments and are substituted by these formatted values.
The substitution symbols are used in the order in which they are specified. The first substitution symbol formats the first additional argument. The second substitution symbol formats the second additional argument, and so on.
In addition to a range of numeric types, the function supports dates, amounts, single-byte strings, multibyte strings, bidirectional strings, and combined normal and bidirectional strings. Input strings that contain bidirectional strings must be specified in logic order. The result is also returned in logic order.

## Arguments
| | | |
|---|---|---|
| `string` | `format` |  contains zero or more ordinary characters and substitution symbols  |
| `[ void` | `... ]` |  One or more values to be placed in the format Implicit conversion of the input value is performed from its original type to the type expected according to the corresponding substitution symbol.  |

## Return values
The formatted string. If you specify an invalid format, *sprintf$()* returns a percentage character [%].

## Context
This function is implemented in the porting set and can be used in all script types.

## Substitution symbols
Substitution strings have the following syntax:
%[ *index*][-][+][0][ *width*][ *.precision*] *type*

## Substitution string elements
The elements of a substitution string have the following meanings:
-
-
-
-
-
-
-
-
| | |
|---|---|
| % | All substitution strings begin with a percentage character [%]. To output the percentage character itself, specify it as ‘%%’. |
| *index* |  An index can be used for setting the order of application of the additional arguments in a formatted string. Setting the order might be needed for translation purposes, because sentences do not have a similar word order for all languages. Index specifiers are in the form 1$ (meaning first in sequence), 2$ etc. As an example take message ppmmm0001, which has the following text in language 1 and 2: 1: Item %s cannot be found in warehouse %s 2: In warehouse %s, item %s cannot be found The accompanying output for mess("ppmmm0001", 1, item, warehouse ) would be 1: Item BIKE cannot be found in warehouse WH01 2: In warehouse BIKE, item WH01 cannot be found | This is wrong! With indexed arguments, this can be solved: 1: Item %1$s cannot be found in warehouse %2$s 2: In warehouse %2$s, item %1$s cannot be found | Note: the 1$ and 2$ are interchanged The accompanying output for mess("ppmmm0001", 1, item, warehouse ) would be 1: Item BIKE cannot be found in warehouse WH01 2: In warehouse WH01, item BIKE cannot be found | This is correct Note that the arguments following the unformatted string are language independent when *indexing* is used. Remark: *If you are using indexes, it is mandatory to use them for all substitution symbols!*  |
| *-* | An optional flag indicating that the output string is to be left justified. If this is omitted, the output string is right justified by default.  |
| *+* |  An optional flag which adds a '+' sign before the formatted string if *type* is one of the %d, %e, %f, %g, %o, %lo, %x or %lx substitution types and the value represented is positive. For all other *types* the '+' sign is ignored.  |
| *0* |  An optional flag which adds one or more zeroes before the formatted string if *type* is one of the %d, %e, %f, %g, %o, %lo, %x or %lx substitution types, up to the available space in the formatted string as specified by the *width* element. For all other *types* the '0' flag is ignored.  |
| *width* |  Specifies the minimum length of the output field. If the output string has fewer characters than the minimum field width, it is filled out with spaces. By default, these are inserted at the start of the field. If the ‘-‘ flag is specified, the spaces are inserted at the end of the string. Instead of an integer constant, you can specify the length with an asterisk '*'. In this case, the corresponding additional argument must supply the length. The corresponding argument can also be determined using an index, using e.g. '*1$'. Remember: *When using an index, it is mandatory to use indexes for all arguments!*.  |
| *precision* |  Specifies either the maximum number of digits after the decimal sign (for ‘%e’, ‘%f’ and ‘%@’(double argument only) substitution types), the maximum number of digits (for ‘%g’ substitution types), or the maximum string length (for ‘%s’, ‘%A’, ‘%D’, ‘%u’, and ‘%U’, and substitution types). For the '%d' substitution type it is the minimal number of digits, for completion leading zeroes are inserted. Instead of an integer constant, you can specify the length with an asterisk [*]. In this case, the corresponding additional argument must supply the length. The corresponding argument can also be determined using an index, using e.g. '*2$'. Remember: *When using an index, it is mandatory to use indexes for all arguments!*.  |
| *type* | The type of conversion to be applied to the substituted value (see below). |

## Substitution types
There are substitution types for different value types:
- For string values the %s substitution type is available.
- For long values the %d, %o, %lo, %x and %lx substitution types are available.
- For double values the %e, %f and %g substitution types are available.
- For date/time values the %D, %u and %U substitution types are available.
- For amounts the %A substitution type is available.
- A special substitution type behaves similar to the edit$() function: %@<format>@.  These substitution types are explained in more detail in the following subsections.
Implicit conversion of the input value is performed from its original type to the type expected according to the substitution symbol.

## String substitution types
The following type element can be used for substituting string values:
```

word = "word"
result = sprintf$( "'%6.2s'", word )
    | result will contain "'␣␣␣␣wo'"
```
| | |
|---|---|
| %s | Use for single-byte and multibyte strings. Implicit conversion of the supplied value from its original type to a string value is performed. Remark: The precision may be less than the width. This results in precision characters being represented from the string, filled out with spaces to make the number of characters width again. An example (result and word are sufficiently large strings): |

## Long substitution types
The following type elements can be used for substituting long values:
-
-
-
-
| | |
|---|---|
| %d |  Use for decimal representation of long values. First, implicit conversion of the supplied value from its original type to a long value is performed. Then, explicit conversion of the long value to its decimal representation is performed. For this explicit long to string type conversion, the same considerations apply as for implicit long to string type conversion, especially concerning the string length to be expected. Additional elements of the substitution string may be used to control certain details of the conversion, e.g. minimum field width, left or right adjustment, zero-padding, and prepending a '+' sign to non-negative values. The precision element of the substitution string defines a minimal number of digits to use for the string representing the value before the effects of the other substitution elements, using leading zeroes to complete the number of digits to precision digits. When the string already is at least precision digits long, no leading zeroes will be added. This can be combined with the minimum width element to get a number of leading spaces followed by a number of leading zeroes, of course dependent on the actual long value of the argument and the values of the width and precision elements.  |
| %o |  Use for octal representation of long values. The same as %d, except for the following differences: The long value is converted from a signed BitCountOfLong-bit value to an unsigned 32-bit value before the explicit conversion. This is done by wrapping around from the signed value range [-2^(BitCountOfLong-1) … 2^(BitCountOfLong-1) - 1] to the *unsigned* 32-bit value range [0 … 2^32 - 1] by repeatedly adding or subtracting 2^32. The explicit conversion converts the integer value to its octal representation. For the implicit long to string type conversion, the powers of 10 must be replaced by powers of 8. The precision element of the substitution string is ignored. Notice that the octal notation of the unsigned 32-bit value range is [0 … 377,7777,7777], implying that 11 string positions must be reserved to cover the complete range. Notice that small negative input values are wrapped to the high part of the unsigned 32-bit value range. E.g. the value -1 is wrapped to 2^32 - 1, such that the resulting octal representation uses the maximal string width of 11 positions.  |
| %lo |  The same as %o, but the wrapping is done to the unsigned 64-bit value range [0 … 2^64 - 1] by repeatedly adding or subtracting 2^64. Notice that the octal notation of the unsigned 64-bit value range is [0 … 17,7777,7777,7777,7777,7777], implying that 22 string positions must be reserved to cover the complete range. Notice that small negative input values are wrapped to the high part of the unsigned 64-bit value range. E.g. the value -1 is wrapped to 2^64 - 1, such that the resulting octal representation uses the maximal string width of 22 positions.  |
| %x |  The same as %o, but hexadecimal representation is used and powers of 8 are replaced by powers of 16. Lower case letters are used for digits greater than 9: 'a', 'b', 'c', 'd', 'e', and 'f'. Notice that the hexadecimal notation of the unsigned 32-bit value range is [0 … ffff,ffff], implying that 8 string positions must be reserved to cover the complete range. Notice that small negative input values are wrapped to the high part of the unsigned 32-bit value range. E.g. the value -1 is wrapped to 2^32 - 1, such that the resulting hexadecimal representation uses the maximal string width of 8 positions.  |
| %lx |  The same as %x, but the wrapping is done to the unsigned 64-bit value range [0 … 2^64 - 1] by repeatedly adding or subtracting 2^64. Notice that the hexadecimal notation of the unsigned 64-bit value range is [0 … ffff,ffff,ffff,ffff], implying that 16 string positions must be reserved to cover the complete range. Notice that small negative input values are wrapped to the high part of the unsigned 64-bit value range. E.g. the value -1 is wrapped to 2^64 - 1, such that the resulting hexadecimal representation uses the maximal string width of 16 positions.  |

## Double substitution types
The following type elements can be used for substituting double values:
| | |
|---|---|
| %e | Use for double values with exponent. First, implicit conversion of the supplied value from its original type to a double value is performed. Then, explicit conversion of the double value to its decimal representation is performed. For this substitution type the precision is the number of decimals to be used after the decimal point. The default value for the precision is 7, and this is also used when the provided precision is '-1'.  |
| %f | Use for doubles values with a decimal point and no exponent. First, implicit conversion of the supplied value from its original type to a double value is performed. Then, explicit conversion of the double value to its decimal representation is performed. For this substitution type the precision is the number of decimals to be used after the decimal point. The default value for the precision is 6, and this is also used when the provided precision is '-1'.  |
| %g |  Use for double values. The style used depends on the value converted. The exponent style ('%e') is used only if the exponent resulting from the conversion is less than -4 or greater than or equal to the precision. Otherwise the decimal point style ('%f') is used. First, implicit conversion of the supplied value from its original type to a double value is performed. Then, explicit conversion of the double value to its decimal representation is performed. For this substitution type the precision is the number of digits to be used, whether before or after the decimal point. The default value for the precision is 6, and this is also used when the provided precision is '-1'.  |

## Date/time substitution types
The following type elements can be used for substituting date/time values:
| | |
|---|---|
| %D *xxx* [ *,lang*]  |  Use for dates. *xxx* is the code for a date format defined in the data ictionary. *lang* indicates the language code to use. If this is omitted, the current user language is used. The value that is substituted for this symbol must specify a number of days since 01-01-0001. Any date before 01-01-0001 (i.e. any integer value <= 0) will be interpreted as invalid and will print as an empty string Any date past 31-12-9999 will be interpreted as 31-12-9999. Note that it isn't possible to use a comma direct after a %D *xxx* substitution symbol other than for selecting a language. As a workaround select a space as the language code, this will substitute the users default language and close the type element. Now it is possible to use the comma that should be included in your string. See the example in the example section.  |
| %D( *format*)  |  Use for dates. This option enables you to define your own date format by using the following subformats of the ‘%D’ format:  |
| %u *xxx* [ *,lang*]  | Use for UTC dates. *xxx* is the code for a UTC date format defined in the data dictionary. *lang* indicates the language code to use. If this is omitted, the current user language is used. The value that is substituted for this symbol must specify a UTC long format value of which only the local date will be used. Any time before January 1, 1970, 00:00:00 UTC (i.e. any integer value < 0) will be interpreted as invalid and will print as an empty string Valid integer value 0 (corresponding to January 1, 1970, 00:00:00 UTC) will print as an empty string. Any local date past 31-12-9999 will be interpreted as 31-12-9999. Note that it isn't possible to use a comma direct after a %u *xxx* substitution symbol other than for selecting a language. As a workaround select a space as the language code, this will substitute the users default language and close the type element. Now it is possible to use the comma that should be included in your string. See the example in the example section.  |
| %U *xxx* [ *,lang*]  | Use for UTC times. *xxx* is the code for a UTC time format defined in the data dictionary. *lang* indicates the language code to use. If this is omitted, the current user language is used. The value that is substituted for this symbol must specify a UTC long format value of which only the local time will be used. Any time before January 1, 1970, 00:00:00 UTC (i.e. any integer value < 0) will be interpreted as invalid and will print as an empty string Valid integer value 0 (corresponding to January 1, 1970, 00:00:00 UTC) will print as an empty string. Note that it isn't possible to use a comma direct after a %U *xxx* substitution symbol other than for selecting a language. As a workaround select a space as the language code, this will substitute the users default language and close the type element. Now it is possible to use the comma that should be included in your string. See the example in the example section.  |
| %u( *format*)  |  Use for UTC dates. This option enables you to define your own date format by using the subformats described for the ‘%D( *format*)’ symbol. You can combine these subformats with other formats. Note that strings returned by name of month and day formats are language dependent. The value that is substituted for this symbol must specify a UTC long format value of which only the local date will be used. Any time before January 1, 1970, 00:00:00 UTC (i.e. any integer value < 0) will be interpreted as invalid and will print as an empty string Valid integer value 0 (corresponding to January 1, 1970, 00:00:00 UTC) will print as an empty string. Any local date past 31-12-9999 will be interpreted as 31-12-9999.  |
| %U( *format*)  |  Use for UTC times. This option enables you to define your own time using the following subformats of the ‘%U’ format.  |

## Miscellaneous substitution types
There are some more type elements for specific purposes:
| | |
|---|---|
| %A *xxx* [ *,CUR*]  |  Use for amounts. *xxx* is the code for an amount format defined in the data dictionary. *CUR* indicates the currency code to use. If this is omitted, the default currency of the company of the user is used.  |
| %@<format>@ |  Make it possible to use edit$() formatting characters for printf$(). Replace <format> format specifier by the formatting characters as described for [edit$()](edit.md). Implicit conversion of the supplied value from its original type to type string is performed. Remark: When a double value is supplied the conversion is not completely implicit, the precision element is used in a way similar to the way it is used for the '%f' substitution type. The resulting string value is formatted according to the format string.  |

## Strings
```

string result(80), word(20)
word = "word"
result = sprintf$("This is a '%*s' of 10 positions",10,word)
    | result contains "This is a '␣␣␣␣␣␣word' of 10 positions"
```

## Doubles
```

string result(80)
result = sprintf$("number: %-*.*f",10,2,1.2)
    | result contains "number: 1.20␣␣␣␣␣␣"
    | minimum length of the double value is 10 positions
    | number of digits after decimal sign is 2
```
For %g the style used depends on the value converted. Style e is used only if the exponent resulting from the conversion is less than -4 or greater than or equal to the precision. Otherwise style f is used.
```

result = sprintf$("number: %-*.*g",10,3,1234.567)
    | result contains "number: 1.23e+03␣␣"
     | e style because the exponent (3) is equal to the precision.
result = sprintf$("number: %-*.*g",10,6,1234.567)
    | result contains "number: 1234.57␣␣␣"
    | f style because the exponent (3) is greater than -4 and smaller than the precision (6).
```

## Amounts
```

| Suppose the default currency is USD ($)
| and A001 is defined as "$$ 999T999T999VD99"
string result(80)
result = sprintf$("%A001", 1234.56)
    | result contains "$␣␣000,001,234.56"
result = sprintf$("%-10A001,hfl", 1234.56)
    | result contains "fl␣000.001.234,56"
result = sprintf$("%-.10A001,hfl", 1234.56)
    | result contains "001.234,56"; there is insufficient space
    | for currency symbol
```

## Dates
```

| Suppose date format 002 is: "year/month/day in month"
string result(80)
>result = sprintf$("%D002", 727168)
    | result contains "1991/12/2"
```
```

| Example of substitution symbol %D(format)
string result(80)
result = sprintf$("%D(Date: %02d/%02m/%04Y)", date.num())
    | result contains "Date:␣12/07/1993"
result = sprintf$("Date: %D(%02d %-20H %04Y)", date.num())
    | result contains "Date:␣12␣June␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣␣1993"
```

## UTC dates and times
```

| Date format 002 is "year/month/day in month"
| Time format 001 is "12 hour format:minutes:seconds AM/PM symbol"
string result(80)
result = sprintf$("%u002 %U001", utc.num(), utc.num())
    | Result contains "1997/01/01␣10:02:53␣pm"
```
```

string result(80)
result = sprintf$("UTC: %u(%02d/%02m/%04Y) %U(%02h%x%02m%x%02s %a)", utc.num(), utc.num())
    | result contains "UTC:␣22/07/1997␣06:24:53␣am"
    | provided that for the user's language the time
    | separator is ":" and the AM symbol is "am"
```
```

| Using a comma after a %u substitution symbol
string result(80)
result = sprintf$("%u001, ,Message text....", utc.num())
    | result contains "06-05-15,Message text...."
```

## Examples
| | | |
|---|---|---|
| Format | Value | Result |
| %f | 1.2 | `"1.200000"` |
| %10f | 1.2 | `"␣␣1.200000"` |
| %10.2f | 1.2 | `"␣␣␣␣␣␣1.20"` |
| %-10.2f | 1.267 | `"1.27␣␣␣␣␣␣"` |
| %10.6g | 1234.567 | `"␣␣␣1234.57"` |
| %10.3g | 1234.567 | `"␣␣1.23e+03"` |
| %10.2e | 12.34 | `"␣␣1.23e+01"` |
| %-10.2e | 12.34 | `"1.23e+01␣␣"` |
| %10d | 1 | `"␣␣␣␣␣␣␣␣␣1"` |
| %10d | -1 | `"␣␣␣␣␣␣␣␣-1"` |
| %-10d | 1 | `"1␣␣␣␣␣␣␣␣␣"` |
| %-10d | -1 | `"-1␣␣␣␣␣␣␣␣"` |
| %10s | "12" | `"␣␣␣␣␣␣␣␣12"` |
| %-10s | "12" | `"12␣␣␣␣␣␣␣␣"` |
| %10s | "123456789012" | `"123456789012"` |
| %.10s | "123456789012" | `"1234567890"` |
| %@ZZVD99@ | 1.267 | `"␣1.26"` |
| %1$*3$.*2$f | 3.14, 5, 8 | `"␣3.14000"` (effective similar to format %8.5f and value 3.14)  |

## Some string formats
| | |
|---|---|
| Format | Result |
| %s | Returns the full string. |
| %20s | Right justifies the string in a field of 20 positions. If the string is longer than 20 positions, the field is lengthened to accommodate the full string.  |
| %-20s | Left justifies the string in a field of 20 positions. If the string is longer than 20 positions, the field is lengthened to accommodate the full string.  |
| %20.20s | Right justifies the string and limits its size to 20 positions. Partially displayable multibyte characters (2 characters wide) will be spaced out.  |

## Related topics
- [Formatting input and output - overview and synopsis](overview_and_synopsis.md)
- Almost the same functionality: [sprintf$()](sprintf.md)
