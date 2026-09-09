# Data types
There are six types of variables:

- [Long variables](#long)

- [Double variables](#double)

- [Boolean variables](#boolean)

- [String variables](#string)

- [Table variables](#table)

- [Domain variables](#domain)

## Long variables
*Long* variables can contain integer values.
The supported value range is the signed 32-bit value range: [-2^31 … 2^31 - 1].
In decimal notation, this is the range [-2,147,483,648 … 2,147,483,647].
In hexadecimal notation, this is the range [-0x8000,0000 … 0x7fff,ffff].
Physically, 4 bytes are used for each long variable.
Using the term [BitCountOfLong](#BitCountOfLong) described below, we can abstract from its actual value 32 and say that the supported value range of long variables is the signed *BitCountOfLong*-bit value range: [-2^(BitCountOfLong-1) … 2^(BitCountOfLong-1) - 1] and that BitCountOfLong / 8 bytes are used for each long variable.
As of [bshell TIV](../tiv/tiv_overview.md) [level 2000](../tiv/tiv_2000.md) the bshell can be configured to run in the [64-bit bshell mode](#Long64).
In the [64-bit bshell mode](#Long64), the value of [BitCountOfLong](#BitCountOfLong) is set to 64, so the supported value range of *long* variables is the signed 64-bit value range: [-2^63 … 2^63 - 1].
In decimal notation, this is the range [-9,223,372,036,854,775,808 … 9,223,372,036,854,775,807].
In hexadecimal notation, this is the range [-0x8000,0000,0000,0000 … 0x7fff,ffff,ffff,ffff].
Physically, in [64-bit bshell mode](#Long64), 8 bytes are used for each long variable.

## Double variables
*Double* variables are used for any number containing a decimal point, with a maximum of 15 significant decimal digits (8 bytes).
3GL variables of type double typically use the IEEE 64-bit floating point representation, which uses a 52-bit mantissa.
The distance between neighboring floating point values depends on their size.
E.g. the floating point neighboring values of 1 are 1 - 2^-53 and 1 + 2^-52, whereas the floating point neighboring values of 2 are 2 - 2^-52 and 2 + 2^-51.
The smallest integer value that cannot be represented exactly in a floating point variable is 2^53 + 1.
The floating point neighbors of 2^53 are 2^53 - 1 and 2^53 + 2.
In decimal notation: the smallest integer value that cannot be represented exactly in a floating point variable is 9,007,199,254,740,993; the floating point neighbors of 9,007,199,254,740,992 are 9,007,199,254,740,991 and 9,007,199,254,740,994.

## Boolean variables
*Boolean* variables can have two values: true or false.

## String variables
A *string* variable contains a string value, i.e. a sequence of characters. The maximum length of a string is 1024 characters.

## Character encoding
The default character encoding used in the 3GL language is the [TSS encoding](../misc/tss.md). In TSS, some characters are encoded in one byte, while other characters are encoded in a sequence of four bytes.
Other supported character encodings are [UTF-8](../misc/utf8.md), [UTF-16](../misc/utf16.md), and also external 'native' character sets. The support comprises several functions for conversion to TSS (e.g. [utf8.import()](../functions_multibyte_strings/utf8.import.md), [uni.import()](../functions_multibyte_strings/uni.import.md), [mb.import$()](../functions_multibyte_strings/mb.import.md), and [mb.import.raw()](../functions_multibyte_strings/mb.import.raw.md)) and several functions for conversion from TSS (e.g. [utf8.export()](../functions_multibyte_strings/utf8.export.md), [uni.export()](../functions_multibyte_strings/uni.export.md), [mb.export$()](../functions_multibyte_strings/mb.export.md), and [mb.export.raw()](../functions_multibyte_strings/mb.export.raw.md)). Above that, the output of the functions for XML serialization (e.g. [xmlString$()](../functions_xml/serialize_xml_object_return.md), [xmlWriteToString()](../functions_xml/serialize_xml_object_string.md), and [xmlAllocString()](../functions_xml/serialize_xml_object_alloc.md)) is always encoded in UTF-8 and the input of the functions for XML de-serialization (e.g. [xmlReadFromString()](../functions_xml/de_serialize_xml_object_string.md)) may be encoded in UTF-8, UTF-16 or ISO-8859-1.

## Length in characters (character length)
Each string value has a *length in characters*, i.e. the total number of characters in the string value. The *length in characters* of a string value is also called its *character length*.
Notice that, regarding the character length, there is a difference between a single-byte string value and a [multibyte string value](multibyte_strings.md#character length).

## Capacity in characters (character capacity)
Each string variable has a *capacity in characters*, i.e. the maximum length in characters for the string values that can be stored in the string variable. The *capacity in characters* of a string variable is also called its *character capacity*.
Notice that, regarding the character capacity, there is a difference between a single-byte string variable and a [multibyte string variable](multibyte_strings.md#character capacity).

## Length in bytes (byte length)
Each string value also has a *length in bytes*, i.e. the total number of bytes of the string representation. The *length in bytes* of a string value is also called its *byte length*.
Notice that, regarding the byte length, there is no difference between a single-byte string value and a [multibyte string value](multibyte_strings.md#byte length).

## Capacity in bytes (byte capacity)
Each string variable also has a *capacity in bytes*, i.e. the maximal byte length for the string values that can be stored in the string variable. The *capacity in bytes* of a string variable is also called its *byte capacity*.
Notice that, regarding the byte capacity, there is a difference between a single-byte string variable and a [multibyte string variable](multibyte_strings.md#byte capacity).

## Display width
Each string value also has a *display width*, i.e. the number of positions needed to display the string value in a fixed width font. Individual characters can have a display width of 0, 1, or 2. The display width of a string value is the sum of the display widths of the individual characters in the string value.

## Table variables
A *table* variable is used for database tables in your program. The table must be defined in the data dictionary.

## Domain variables
A *domain* variable is a variable of a certain type that is defined in the data dictionary. Each of the following types are possible: long, byte, integer, date, enumerate, set, float, double, string, text. Each domain defined in the data dictionary can be used in a declaration of your program. See also [Domains](domains.md).

## BitCountOfLong
In this manual, the term BitCountOfLong is used to refer to the size (counted in bits) of a long variable.
Using this term, we can abstract from its actual value.
This way, we can say that the supported value range of long variables is the signed *BitCountOfLong*-bit value range: [-2^(BitCountOfLong-1) … 2^(BitCountOfLong-1) - 1].
Furthermore we can say that BitCountOfLong / 8 bytes are used for each long variable.
In [32-bit bshell mode](#Long32), the value of BitCountOfLong is set to 32.
In [64-bit bshell mode](#Long64), the value of BitCountOfLong is set to 64.

## The 32-bit bshell mode
By default, the bshell runs in the 32-bit bshell mode.
In the 32-bit bshell mode, the value of [BitCountOfLong](#BitCountOfLong) is set to 32, so the supported value range of [long variables](#long) is the signed 32-bit value range: [-2^31 … 2^31 - 1].

## The 64-bit bshell mode
As of [bshell TIV](../tiv/tiv_overview.md) [level 2000](../tiv/tiv_2000.md) the bshell can be configured to run in the 64-bit bshell mode.
In the 64-bit bshell mode, the value of [BitCountOfLong](#BitCountOfLong) is set to 64, so the supported value range of [long variables](#long) is the signed 64-bit value range: [-2^63 … 2^63 - 1].
The 64-bit bshell mode can be configured by setting the [bshell resource](../misc/bshell_resources.md) *utc40*, e.g. in the file $BSE/lib/defaults/all.
The function [get.long.byte.count()](../functions_system_and_user_information/get.long.byte.count.md) can be used to retrieve the size (counted in bytes) of [long variables](#long), that is the value BitCountOfLong / 8.
In general, the bshell is less forgiving in the 64-bit mode than in the 32-bit mode. In 32-bit mode an overflow of the signed 32-bit range is often solved by wrapping around, i.e. by adding or subtracting 2^32 until the value is in the signed 32-bit value range. In 64-bit mode an overflow of the signed 64-bit range will be solved analogously by wrapping around, i.e. by repeatedly adding or subtracting 2^64 until the value is in the signed 64-bit value range. But apart from that, it is considered as a fatal action and it may cause (now or in a future bshell version) the current 3GL process to be terminated.
Also, when in 64-bit mode a signed 64-bit value outside the signed 32-bit value range is used where a signed 32-bit value is expected, in practice it will be wrapped around to the signed 32-bit value range by repeatedly adding or subtracting 2^32 until the value is in the signed 32-bit value range. But apart from that, it is considered as a fatal action and it may cause (now or in a future bshell version) the current 3GL process to be terminated.
Points of attention when using the 64-bit bshell mode should at least be:
| | | |
|---|---|---|
| Issue | Behavior in 32-bit mode | Behavior in 64-bit mode |
| [Arithmetic operators](arithmetic_operators.md) of which the exact result is outside the signed 32-bit value range. | Overflow, in practice solved by wrapping around to the signed 32-bit value range by repeatedly adding or subtracting 2^32 until the value is in the signed 32-bit value range. Overall, the exact or wrapped around resulting value is known to be in the signed 32-bit value range. | In many cases an overflow of the signed 32-bit value range is not an overflow of the signed 64-bit value range. When the exact result of an arithmetic operation is outside the signed 64-bit value range, in practice it will be wrapped around to the signed 64-bit value range by repeatedly adding or subtracting 2^64 until the value is in the signed 64-bit value range. But apart from that, it is considered as a fatal action and it may cause (now or in a future bshell version) the current 3GL process to be terminated. Overall, if the 3GL process is not terminated, the exact or wrapped around resulting value is known to be in the signed 64-bit value range, but that is a much weaker condition than being in the signed 32-bit value range. |
| [Compile time evaluation of constant integer expressions](arithmetic_operators.md#compile_time_constants) of which the exact *unsigned* 32-bit result is outside the signed 32-bit value range, so it is in the range [2^31 … 2^32 - 1]. | The value is wrapped from the *unsigned* 32-bit value range to the signed 32-bit value range by subtracting 2^32. The resulting value is negative and is in the range [-2^31 … -1]. | The *unsigned* 32-bit value can be stored without value change in a long variable. The resulting value is positive and is in the range [2^31 … 2^32 - 1]. |
| Implicit or explicit [long to string type conversion](type_conversions.md#long_to_string_type_conversion) | If no value restriction of the long value is known, then the resulting string length is at most 11. | If no value restriction of the long value is known, then the resulting string length is at most 20, but that is a much weaker condition than being at most 11. |
| Implicit or explicit [string to long type conversion](type_conversions.md#string_to_long_type_conversion) | If no value restriction of the string value is known, then the resulting long value is still known to be in the signed 32-bit value range. | If no value restriction of the string value is known, then the resulting long value is still known to be in the signed 64-bit value range, but that is a much weaker condition than being in the signed 32-bit value range. |
| Implicit or explicit [long to double type conversion](type_conversions.md#long_to_double_type_conversion) | Even if no value restriction of the long value is known, then still it can be represented in a double without loss of precision. At the edges of the signed 32-bit value range, neighboring floating point numbers have a distance of 2^-22. | The full signed 64-bit integer value range cannot be represented without loss of precision. At the edges of the signed 64-bit value range, neighboring floating point numbers have a distance of 2^10. The smallest integer value that cannot be represented exactly in a floating point variable is 2^53 + 1. The floating point neighbors of 2^53 are 2^53 - 1 and 2^53 + 2. In decimal notation: the smallest integer value that cannot be represented exactly in a floating point variable is 9,007,199,254,740,993; the floating point neighbors of 9,007,199,254,740,992 are 9,007,199,254,740,991 and 9,007,199,254,740,994. |
| Implicit or explicit [double to long type conversion](type_conversions.md#double_to_long_type_conversion) | If no value restriction of the double value is known, then the exact resulting integer value may be outside the signed 32-bit range and the result is undefined. Overall, any resulting value is known to be in the signed 32-bit value range. | If no value restriction of the double value is known, then the exact resulting integer value may be outside the signed 64-bit range and the result is undefined. Overall, any resulting value is known to be in the signed 64-bit value range, but that is a much weaker condition than being in the signed 32-bit value range. |
| Storage of a long value in 4 bytes, e.g. by means of [ims.w.long()](../functions_ims/ims.w.long.md) or [seq.w.long()](../functions_directory_file_operations/seq.w.long.md) or [store.long()](../functions_string_operations/store.long.md) | The inverse function (e.g. [ims.r.long()](../functions_ims/ims.r.long.md) or [seq.r.long()](../functions_directory_file_operations/seq.r.long.md) or [load.long()](../functions_string_operations/load.long.md)) will retrieve the original supplied integer value. | The inverse function (e.g. [ims.r.long()](../functions_ims/ims.r.long.md) or [seq.r.long()](../functions_directory_file_operations/seq.r.long.md) or [load.long()](../functions_string_operations/load.long.md)) will retrieve the exact original supplied integer value if and only if that integer value is within the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]). Otherwise, the inverse function would retrieve the original supplied integer value, wrapped to the signed 32-bit value range [-2^31 … 2^31 - 1] (i.e. [-2,147,483,648 … 2,147,483,647]) by repeatedly adding or subtracting 2^32 until the value is in the signed 32-bit value range. This involves some loss of information. Therefore, the original storage action is considered as a fatal action and it may cause (now or in a future bshell version) the current 3GL process to be terminated. |
| Storage of a long value in a database field of type DB.LONG | Even if no value restriction of the long value is known, then still it can be stored in the database without loss of information. | The long value can only be stored in the database without loss of information when it is in the signed 32-bit value range Otherwise, the long value will be wrapped to the signed 32-bit value range before being stored in the database. This involves some loss of information. It is considered as a fatal action and it may cause (now or in a future bshell version) the current 3GL process to be terminated. |
| Storage of a long value in a database field of type DB.TIME | Any non-negative [UTC](../functions_date_time_zones/overview.md#utc) long format value in the signed 32-bit value range can be stored in the database without loss of information. | Typically, in this 64-bit bshell mode, the [Utc40 mode](../functions_date_time_zones/overview.md#Utc40) is active. Any non-negative [UTC](../functions_date_time_zones/overview.md#utc) long format value less than or equal to the maximum supported value 253,402,214,400 (0x3a,fff2,f000), corresponding to the begin of the last day of the last four-digit year, i.e. December 31, 9999, 00:00:00 UTC, can be stored in the database without loss of information. When, instead of that, the [Utc64 mode](../functions_date_time_zones/overview.md#Utc64) is active, the same maximum supported value is used. Otherwise, the [Utc32 mode](../functions_date_time_zones/overview.md#Utc32) is active and the maximum supported value is the maximum signed 32-bit value, corresponding to UTC time 03:14:07 on Thursday, January 19, 2038. In each case, any attempt to store a negative value or a value above the maximum supported value is considered as a fatal action and may cause (now or in a future bshell version) the current 3GL process to be terminated. |
| Transmission of a long value in an [event array parameter](../events/event_array_parameters.md) | Even if no value restriction of the long value is known, then still it can be transmitted in an event array parameter. | The long value can only be transmitted in an event array parameter when it is in the signed 32-bit range. |
| Conversion of a date/time later than UTC time 03:14:07 on Thursday, January 19, 2038 to a [UTC](../functions_date_time_zones/overview.md#utc) long value, e.g. by means of the utc function in a [runtime expression](../functions_expressions_runtime/expr.compile.md) or by means of [date.to.utc()](../functions_date_time_zones/date.to.utc.md), [date.with.timezone.info.to.utc()](../functions_date_time_zones/date.with.timezone.info.to.utc.md), [local.to.utc()](../functions_date_time_zones/local.to.utc.md), [local.with.timezone.info.to.utc()](../functions_date_time_zones/local.with.timezone.info.to.utc.md), or [week.to.utc()](../functions_date_time_zones/week.to.utc.md). | Error value -1. | A correct result greater than 2^32 - 1. Date/time values not past the begin of the last day of the last four-digit year, i.e. December 31, 9999, 00:00:00 UTC are supported in all cases. Date/time values within a reasonable number of years past that moment are supported in several cases. Especially, it is *not* specified that functions [date.to.utc()](../functions_date_time_zones/date.to.utc.md), [date.with.timezone.info.to.utc()](../functions_date_time_zones/date.with.timezone.info.to.utc.md), [local.to.utc()](../functions_date_time_zones/local.to.utc.md), [local.with.timezone.info.to.utc()](../functions_date_time_zones/local.with.timezone.info.to.utc.md), and [week.to.utc()](../functions_date_time_zones/week.to.utc.md) return error value -1 for date/time combinations outside this range. |
| Conversion of a [UTC](../functions_date_time_zones/overview.md#utc) long value to a date/time, e.g. by means of [utc.to.local()](../functions_date_time_zones/utc.to.local.md) or [utc.to.local.with.timezone.info()](../functions_date_time_zones/utc.to.local.with.timezone.info.md). | Even if no value restriction of the long value is known, then still the resulting date is at most somewhere in January 2038. | If no value restriction of the long value is known, then also no restriction on the resulting date can be given; it can be even past the last four-digit year 9999, such that functions like [num.to.date()](../functions_date_time_zones/num.to.date.md), [num.to.date$()](../functions_date_time_zones/num.to.dates.md), and [num.to.week()](../functions_date_time_zones/num.to.week.md) cannot convert it to the corresponding year, month and day of the month or week and day of the week. |

## Related topics
- [3GL programming language features: overview](overview.md)

- [Variables](variables.md)

- [Bshell resource "utc40"](../misc/bshell_resources.md)
