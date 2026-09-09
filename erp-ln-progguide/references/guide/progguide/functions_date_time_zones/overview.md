# Dates, times, time zones overview
Use these functions to manipulate dates, times, and time zones.

## Universal Coordinated Time
Infor Enterprise Server provides time-zone independent date and time support. The user interface always shows local dates and times. Internally, however, Infor Enterprise Server stores dates and times in Universal Coordinated Time ( UTC). It represents both date and time in a single integer value referred to as the UTC long format. This integer value represents the number of seconds since UTC time 00:00:00 on January 1, 1970.
The maximum value 2^31 - 1 of the signed 32-bit range corresponds to UTC time 03:14:07 on Thursday, January 19, 2038.
In [64-bit bshell mode](../3gl_features/data_types.md#Long64) the UTC-related functions work well in a much larger range. The first logical limitation is the restriction to years of four decimal digits, so the date must be before January 1 of the year 10,000. The UTC-related functions work well within that range and can even be expected to work well within a reasonable number of years outside that range. Especially, it is *not* specified that functions [date.to.utc()](date.to.utc.md), [date.with.timezone.info.to.utc()](date.with.timezone.info.to.utc.md), [local.to.utc()](local.to.utc.md), [local.with.timezone.info.to.utc()](local.with.timezone.info.to.utc.md), and [week.to.utc()](week.to.utc.md) return error value -1 for date/time combinations outside this range.
However, when internally a computation from a day number to a (year, month, day) tuple is needed, then there may be an error condition when the exact year is above 9999. This restriction is at least observable in the following cases.

- [num.to.date()](num.to.date.md)

- [num.to.date$()](num.to.dates.md)

- [num.to.week()](num.to.week.md)

- [utc.add()](utc.add.md)

- [utc.to.date()](utc.to.date.md)

- [utc.to.date.with.timezone.info()](utc.to.date.with.timezone.info.md)

- [utc.to.week()](utc.to.week.md)

- [sprintf$()](../functions_formatting_io/sprintf.md), when using a format with one of the type conversion specifiers 'D' or 'u'

- [vsprintf$()](../functions_formatting_io/vsprintf.md), when using a format with one of the type conversion specifiers 'D' or 'u'

The UTC long format value of the last second of the last four-digit year, i.e. UTC time 23:59:59 on December 31, 9999, is 253,402,300,799 (0x3a,fff4,417f). Notice that this is a value between 2^37 and 2^38.
Further, notice that the last second of the last four-digit year in UTC, i.e. December 31, 9999, 23:59:59 UTC may correspond to a local time moment already in the year 10,000, dependent on the used time zone. Therefore, the maximum fully supported UTC value is chosen to be somewhat earlier, namely the begin of the last day of the last four-digit year, i.e. December 31, 9999, 00:00:00 UTC. Its UTC long format value is 253,402,214,400 (0x3a,fff2,f000).
Whenever a UTC long format value is stored in or retrieved from a sequence of bytes or a UTC long format value is exchanged between any client and a database server, then this value should not be greater than the above specified maximum fully supported UTC value. Using a greater value when the bshell is in [64-bit mode](../3gl_features/data_types.md#Long64) is considered as a fatal error and may lead (now or in a future version of the bshell) to termination of the current 3GL process.

## BitCountOfUtc
In this manual, the term BitCountOfUtc is used to refer to the number of significant bits in a [UTC](#utc) long format value.
Using the term BitCountOfUtc, we can abstract from its actual value.
This way, we can say that the supported value range of UTC long format values is restricted to the non-negative part of the signed *BitCountOfUtc*-bit value range: [0 … 2^(BitCountOfUtc-1) - 1].
Notice that there are other restrictions on the supported UTC long format value range, which may be weaker or stronger than the restriction specified above.
The relation between the term BitCountOfUtc and the term [ByteCountOfUtc](#ByteCountOfUtc) defined below is as follows.
```

         BitCountOfUtc = 8 * ByteCountOfUtc
```

## ByteCountOfUtc
In this manual, the term ByteCountOfUtc is used to refer to the number of bytes used when a [UTC](#utc) long format value is stored in or retrieved from a sequence of bytes.
Using the term ByteCountOfUtc, we can abstract from its actual value.
The relation between the term ByteCountOfUtc and the term [BitCountOfUtc](#BitCountOfUtc) defined above is as follows.
```

         BitCountOfUtc = 8 * ByteCountOfUtc
```
It must be realized that the influence of the value of ByteCountOfUtc is not restricted to the bshell. For example, the number of bytes used to exchange a UTC long format value between any client and a database server is also determined by ByteCountOfUtc. See also the description of the SQL [timestamp](../functions_database_handling/sql_data_types.md#timestamp) data type.
The actual value of ByteCountOfUtc can be configured by setting the [resource](../misc/bshell_resources.md) *utc40*, e.g. in the file $BSE/lib/defaults/all.
The bshell function [get.utc.byte.count()](../functions_system_and_user_information/get.utc.byte.count.md) can be used to retrieve the actual value of ByteCountOfUtc.
The following list enumerates several bshell functions of which the behavior is influenced by the value of ByteCountOfUtc. The list may be incomplete.

- [expr.compile()](../functions_expressions_runtime/expr.compile.md), when using the function fmax().

- [ims.r.utc()](../functions_ims/ims.r.utc.md)

- [ims.w.utc()](../functions_ims/ims.w.utc.md)

- [load.utc()](../functions_string_operations/load.utc.md)

- [store.utc()](../functions_string_operations/store.utc.md)

- [qss.search()](../functions_searching_sorting_data/qss.search.md)

- [qss.sort()](../functions_searching_sorting_data/qss.sort.md)

- [rdi.column()](../functions_runtime_dictionary_information/rdi.column.md)

- [rdi.index()](../functions_runtime_dictionary_information/rdi.index.md)

- [rdi.table()](../functions_runtime_dictionary_information/rdi.table.md)

- [rdi.table.column()](../functions_runtime_dictionary_information/rdi.table.column.md)

- [seq.r.utc()](../functions_directory_file_operations/seq.r.utc.md)

- [seq.w.utc()](../functions_directory_file_operations/seq.w.utc.md)

- [set.fmax()](../functions_mathematical_operations/set.fmax.md)

- [set.max()](../functions_mathematical_operations/set.max.md)

## Utc32 mode
In Utc32 mode, the value of [ByteCountOfUtc](#ByteCountOfUtc) is set to 4, so [BitCountOfUtc](#BitCountOfUtc) is 32.
The Utc32 mode is the default mode. It is active when the [resource](../misc/bshell_resources.md) *utc40* is not set or when it is set to the value 0.
In Utc32 mode, when a UTC long format value is stored in or retrieved from a sequence of bytes or a UTC long format value is exchanged between any client and a database server, then a sequence of 4 bytes is used, and the order and interpretation of the bytes is exactly the same as when the bshell function [load.long()](../functions_string_operations/load.long.md) is used.
The default byte order (big endian) is as follows.
| | | | |
|---|---|---|---|
| Byte | Name | Value range | Weight factor |
| First byte | B3 | -128 … 127 | 256^3 |
| Second byte | B2 | 0 … 255 | 256^2 |
| Third byte | B1 | 0 … 255 | 256^1 |
| Fourth byte | B0 | 0 … 255 | 256^0 |
The non-default byte order (little endian) is as follows. This byte order is only used when in bshell function [load.utc()](../functions_string_operations/load.utc.md) the *endian* argument is set to 1.
| | | | |
|---|---|---|---|
| Byte | Name | Value range | Weight factor |
| First byte | B0 | 0 … 255 | 256^0 |
| Second byte | B1 | 0 … 255 | 256^1 |
| Third byte | B2 | 0 … 255 | 256^2 |
| Fourth byte | B3 | -128 … 127 | 256^3 |
In both byte orders, the UTC long format value represented by this sequence of bytes is `B3 * 256^3 + B2 * 256^2 + B1 * 256^1 + B0 * 256^0`.
In this mode, the supported value range is the non-negative part of the signed 32-bit value range: [0 … 2^31 - 1].
The maximum value 2^31 - 1 of the supported value range corresponds to UTC time 03:14:07 on Thursday, January 19, 2038.

## Utc40 mode
In Utc40 mode, the value of [ByteCountOfUtc](#ByteCountOfUtc) is set to 5, so [BitCountOfUtc](#BitCountOfUtc) is 40.
The Utc40 mode is active when the [resource](../misc/bshell_resources.md) *utc40* is set to any value not equal to 0.
In Utc40 mode, when a UTC long format value is stored in or retrieved from a sequence of bytes or a UTC long format value is exchanged between any client and a database server, then a sequence of 5 bytes is used.
For [compatibility](#Compatibility) reasons, the order and interpretation of the first 4 bytes is almost the same as when the bshell function [load.long()](../functions_string_operations/load.long.md) is used.
The default byte order (big endian) is as follows.
| | | | |
|---|---|---|---|
| Byte | Name | Value range | Weight factor |
| First byte | B3 | 0 … 255 | 256^3 |
| Second byte | B2 | 0 … 255 | 256^2 |
| Third byte | B1 | 0 … 255 | 256^1 |
| Fourth byte | B0 | 0 … 255 | 256^0 |
| Fifth byte | B4 | -128 … 127 | 256^4 |
The non-default byte order (little endian) is as follows. This byte order is only used when in bshell function [load.utc()](../functions_string_operations/load.utc.md) the *endian* argument is set to 1.
| | | | |
|---|---|---|---|
| Byte | Name | Value range | Weight factor |
| First byte | B0 | 0 … 255 | 256^0 |
| Second byte | B1 | 0 … 255 | 256^1 |
| Third byte | B2 | 0 … 255 | 256^2 |
| Fourth byte | B3 | 0 … 255 | 256^3 |
| Fifth byte | B4 | -128 … 127 | 256^4 |
In both byte orders, the UTC long format value represented by this sequence of bytes is `B4 * 256^4 + B3 * 256^3 + B2 * 256^2 + B1 * 256^1 + B0 * 256^0`.
In this mode, the supported value range is the non-negative part of the signed 40-bit value range: [0 … 2^39 - 1].
The maximum value 2^39 - 1 (i.e. 549,755,813,887 or 0x7f,ffff,ffff) of the supported value range corresponds to UTC time 12:18:07 on January 25, 19391.
The UTC long format value of the begin of the last day of the last four-digit year, i.e. UTC time 00:00:00 on December 31, 9999, is 253,402,214,400 (0x3a,fff2,f000). Notice that this is a value between 2^37 and 2^38, so it is well within the supported value range.
This value corresponding to December 31, 9999, 00:00:00 UTC is the maximum supported value when the bshell is involved in storing or retrieving a UTC long format value in or from a sequence of bytes or exchanging such a value with a database server. Using a greater value when the bshell is in [64-bit mode](../3gl_features/data_types.md#Long64) is considered as a fatal error and may lead (now or in a future version of the bshell) to termination of the current 3GL process.

## Utc64 mode
In Utc64 mode, the value of [ByteCountOfUtc](#ByteCountOfUtc) is set to 8, so [BitCountOfUtc](#BitCountOfUtc) is 64.
In Utc64 mode, when a UTC long format value is stored in or retrieved from a sequence of bytes or a UTC long format value is exchanged between any client and a database server, then a sequence of 8 bytes is used.
For [compatibility](#Compatibility) reasons, the order and interpretation of the first 4 bytes is almost the same as when the bshell function [load.long()](../functions_string_operations/load.long.md) is used.
The default byte order (big endian) is as follows.
| | | | |
|---|---|---|---|
| Byte | Name | Value range | Weight factor |
| First byte | B3 | 0 … 255 | 256^3 |
| Second byte | B2 | 0 … 255 | 256^2 |
| Third byte | B1 | 0 … 255 | 256^1 |
| Fourth byte | B0 | 0 … 255 | 256^0 |
| Fifth byte | B7 | -128 … 127 | 256^7 |
| Sixth byte | B6 | 0 … 255 | 256^6 |
| Seventh byte | B5 | 0 … 255 | 256^5 |
| Eighth byte | B4 | 0 … 255 | 256^4 |
The non-default byte order (little endian) is as follows. This byte order is only used when in bshell function [load.utc()](../functions_string_operations/load.utc.md) the *endian* argument is set to 1.
| | | | |
|---|---|---|---|
| Byte | Name | Value range | Weight factor |
| First byte | B0 | 0 … 255 | 256^0 |
| Second byte | B1 | 0 … 255 | 256^1 |
| Third byte | B2 | 0 … 255 | 256^2 |
| Fourth byte | B3 | 0 … 255 | 256^3 |
| Fifth byte | B4 | 0 … 255 | 256^4 |
| Sixth byte | B5 | 0 … 255 | 256^5 |
| Seventh byte | B6 | 0 … 255 | 256^6 |
| Eighth byte | B7 | -128 … 127 | 256^7 |
In both byte orders, the UTC long format value represented by this sequence of bytes is `B7 * 256^7 + B6 * 256^6 + B5 * 256^5 + B4 * 256^4 + B3 * 256^3 + B2 * 256^2 + B1 * 256^1 + B0 * 256^0`.
In this mode, the supported value range is the non-negative part of the signed 64-bit value range: [0 … 2^63 - 1].
The UTC long format value of the begin of the last day of the last four-digit year, i.e. UTC time 00:00:00 on December 31, 9999, is 253,402,214,400 (0x3a,fff2,f000). Notice that this is a value between 2^37 and 2^38, so it is well within the supported value range.
This value corresponding to December 31, 9999, 00:00:00 UTC is the maximum supported value when the bshell is involved in storing or retrieving a UTC long format value in or from a sequence of bytes or exchanging such a value with a database server. Using a greater value when the bshell is in [64-bit mode](../3gl_features/data_types.md#Long64) is considered as a fatal error and may lead (now or in a future version of the bshell) to termination of the current 3GL process.
The step from Utc40 to Utc64 mode is in fact useless, as the maximum value 2^39 - 1 (hexadecimal notation 0x7f,ffff,ffff) of the Utc40 value range corresponds to UTC time 12:18:07 on January 25, 19391, which is already far beyond the range of years of four decimal digits.
Notice that there is no documented way to activate the Utc64 mode. The Utc64 mode only exists for test purposes and is not meant to be used in a normal user environment.

## Compatibility of utc functions and long functions in the different utc modes
The [Utc32 mode](#Utc32) described above is the default mode. When it is active, usage of the described utc functions is not necessary, as in this mode they are equivalent to the corresponding long functions, as indicated in the following table.
| | |
|---|---|
| utc function | long function |
| [ims.r.utc()](../functions_ims/ims.r.utc.md) | [ims.r.long()](../functions_ims/ims.r.long.md) |
| [ims.w.utc()](../functions_ims/ims.w.utc.md) | [ims.w.long()](../functions_ims/ims.w.long.md) |
| [load.utc()](../functions_string_operations/load.utc.md) | [load.long()](../functions_string_operations/load.long.md) |
| [store.utc()](../functions_string_operations/store.utc.md) | [store.long()](../functions_string_operations/store.long.md) |
| [seq.r.utc()](../functions_directory_file_operations/seq.r.utc.md) | [seq.r.long()](../functions_directory_file_operations/seq.r.long.md) |
| [seq.w.utc()](../functions_directory_file_operations/seq.w.utc.md) | [seq.w.long()](../functions_directory_file_operations/seq.w.long.md) |
In the [Utc40 mode](#Utc40) and the [Utc64 mode](#Utc64) described above there is also a certain degree of compatibility between the utc functions [load.utc()](../functions_string_operations/load.utc.md) and [store.utc()](../functions_string_operations/store.utc.md) at one side and the corresponding long functions [load.long()](../functions_string_operations/load.long.md) and [store.long()](../functions_string_operations/store.long.md) at the other side. This is shown in the following table.
| | | | |
|---|---|---|---|
| description | utc value | value read | value write |
| utc function |  | [load.utc()](../functions_string_operations/load.utc.md) | [store.utc()](../functions_string_operations/store.utc.md) |
| long function |  | [load.long()](../functions_string_operations/load.long.md) | [store.long()](../functions_string_operations/store.long.md) |
| non-negative signed 32-bit value | utc in the range [0 … 0x7fff,ffff] | compatible | compatible, provided that the extra bytes are initialized to 0 |
| value above signed 32-bit maximum value | 0x7fff,ffff < utc | incompatible | incompatible |
Notice that in the [Utc40 mode](#Utc40) and the [Utc64 mode](#Utc64) described above there is no compatibility between the utc functions [ims.r.utc()](../functions_ims/ims.r.utc.md), [ims.w.utc()](../functions_ims/ims.w.utc.md), [seq.r.utc()](../functions_directory_file_operations/seq.r.utc.md), and [seq.w.utc()](../functions_directory_file_operations/seq.w.utc.md) at one side and the corresponding long functions [ims.r.long()](../functions_ims/ims.r.long.md), [ims.w.long()](../functions_ims/ims.w.long.md), [seq.r.long()](../functions_directory_file_operations/seq.r.long.md), and [seq.w.long()](../functions_directory_file_operations/seq.w.long.md) at the other side. The utc functions read or write a sequence of [ByteCountOfUtc](#ByteCountOfUtc) bytes to or from the supplied byte array or file, updating the current position differently than the long functions, which read or write a sequence of 4 bytes.

## Orthogonality of the 64-bit bshell mode and the different utc modes
The [64-bit bshell mode](../3gl_features/data_types.md#Long64) was introduced in order to enable the bshell to handle [UTC](#utc) long format values above the maximum signed 32-bit value, corresponding to UTC time 03:14:07 on Thursday, January 19, 2038. On top of that, the [Utc40 mode](#Utc40) and the [Utc64 mode](#Utc64) were introduced in order to enable the complete portingset to exchange such high [UTC](#utc) long format values.
The phrase 'on top of that' suggests a dependency, but in fact the [Utc40 mode](#Utc40) or the [Utc64 mode](#Utc64) can be active also when the bshell is in the [32-bit mode](../3gl_features/data_types.md#Long32). In such a configuration, the date/time/utc-related conversion functions are restricted to signed 32-bit UTC values and to times before UTC time 03:14:08 on Thursday, January 19, 2038. Apart from that, exchange of [UTC](#utc) long format values inside the portingset uses five-byte or eight-byte quantities.
So, the notions of the width of long bshell values and the exchange of [UTC](#utc) long format values inside the portingset are independent and can be seen as two orthogonal configuration axes, as illustrated in the following table.
| | | |
|---|---|---|
|  | [32-bit bshell mode](../3gl_features/data_types.md#Long32) | [64-bit bshell mode](../3gl_features/data_types.md#Long64) |
| [Utc32 mode](#Utc32) | Long bshell values are in the signed 32-bit range. Date/time/utc-related conversion functions are restricted to signed 32-bit UTC values and to times less than or equal to Thursday, January 19, 2038, 03:14:07 UTC. Exchange of [UTC](#utc) long format values inside the portingset uses four-byte quantities. | Long bshell values are in the signed 64-bit range. Date/time/utc-related conversion functions are restricted to UTC values and times less than or equal to December 31, 9999, 00:00:00 UTC. Date/time values within a reasonable number of years past that moment are supported in several cases. Exchange of [UTC](#utc) long format values inside the portingset uses four-byte quantities. It is restricted to UTC values in the signed 32-bit range, i.e. to times less than or equal to Thursday, January 19, 2038, 03:14:07 UTC. Any attempt to exchange a UTC long format value which is negative or greater than the indicated maximum value is considered as a fatal error and may lead (now or in a future bshell version) to termination of the current 3GL process. |
| [Utc40 mode](#Utc40) | Long bshell values are in the signed 32-bit range. Date/time/utc-related conversion functions are restricted to signed 32-bit UTC values and to times times less than or equal to Thursday, January 19, 2038, 03:14:07 UTC. Exchange of [UTC](#utc) long format values inside the portingset uses five-byte quantities. | Long bshell values are in the signed 64-bit range. Date/time/utc-related conversion functions are restricted to UTC values and times than or equal to December 31, 9999, 00:00:00 UTC. Date/time values within a reasonable number of years past that moment are supported in several cases. Exchange of [UTC](#utc) long format values inside the portingset uses five-byte quantities. It is restricted to UTC values less than or equal to December 31, 9999, 00:00:00 UTC. Any attempt to exchange a UTC long format value which is negative or greater than the indicated maximum value is considered as a fatal error and may lead (now or in a future bshell version) to termination of the current 3GL process. |
| [Utc64 mode](#Utc64) | Long bshell values are in the signed 32-bit range. Date/time/utc-related conversion functions are restricted to signed 32-bit UTC values and to times times less than or equal to Thursday, January 19, 2038, 03:14:07 UTC. Exchange of [UTC](#utc) long format values inside the portingset uses eight-byte quantities. | Long bshell values are in the signed 64-bit range. Date/time/utc-related conversion functions are restricted to UTC values and times than or equal to December 31, 9999, 00:00:00 UTC. Date/time values within a reasonable number of years past that moment are supported in several cases. Exchange of [UTC](#utc) long format values inside the portingset uses eight-byte quantities. It is restricted to UTC values less than or equal to December 31, 9999, 00:00:00 UTC. Any attempt to exchange a UTC long format value which is negative or greater than the indicated maximum value is considered as a fatal error and may lead (now or in a future bshell version) to termination of the current 3GL process. |

## Time zones
The UTC functions described in this section support conversion between local dates and times and UTC. Users can set their local time zone via the user interface. 3GL/4GL programs can modify the time zone at runtime using various time zone functions.

## Week handling
Infor Enterprise Server handles week numbering according to ISO:5601. Week 01 is the week that includes the first Thursday of the year or January 4. Monday is the first day of the week (that is, day 1). Sunday is the last day of the week (that is, day 7).
In the company-data settings in the data dictionary it is possible to define the first day of the week (that is, day 01) for individual Infor Enterprise Server users. If a user’s first day of the week is Monday, then week numbering follows the ISO standard. However, if a user’s first day of the week is other than Monday (Sunday or Wednesday, for example), the week number is calculated differently. The week number is always the ISO week number of the Monday that occurs in the user’s week.
The following diagram illustrates this:
In the example, the user’s first day of the week is a Wednesday. The week number of the week beginning Wednesday 9 and ending Tuesday 15 is the ISO week number for the Monday that occurs in that week. The ISO week number of Monday 14 is week 6, so Wednesday 9 to Tuesday 15 is week 6.
Note  For an explanation of date and time formats, see [Formatting input and output - overview and synopsis](../functions_formatting_io/overview_and_synopsis.md).

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Resource "utc40"](../misc/bshell_resources.md)
