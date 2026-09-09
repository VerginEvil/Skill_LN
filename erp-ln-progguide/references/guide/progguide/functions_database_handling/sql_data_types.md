# SQL data types
This section describes the data types that are supported by the SQL processor.

## Data types

## integer
The data type *integer* can hold integer values.
The supported value range is the signed 32-bit value range: [-2^31 … 2^31 - 1].
In decimal notation, this is the range [-2,147,483,648 … 2,147,483,647].
In hexadecimal notation, this is the range [-0x8000,0000 … 0x7fff,ffff].

## real
The data type *real* is used for *approximate* numeric values.
*Note*: Literals of type *real* may not be exactly representable within the data type *real*. For example, the literal "0.1" is not representable as a real. The same holds for operations on values of type *real*. For example, the division of 1 and 10 yields a value that is not representable as a real. In such cases, a real value is chosen that is the closest approximation.

## string
The data type *string* can hold a string of characters. The characters can be both single-byte and multibyte (TSS) characters. The character set is defined by the current locale.

## date
The data type *date* can hold values that represent a valid date according to the Gregorian calendar.
The minimum date is "0001-01-01", that is January 1, 0001. The maximum date is "9999-12-31", that is December 31, 9999.

## timestamp
The data type *timestamp* can hold values that represent a valid timestamp (date with time) according to the Gregorian calendar.
Timestamps are maintained in UTC, because the meaning of a timestamp differs from location to location on the surface of the earth.
The concept of UTC (Universal Coordinated Time) is further described in the [overview of bshell functions for dates, times and time zones](../functions_date_time_zones/overview.md).
The minimum timestamp value in UTC is "1970-01-01 00:00:00". This corresponds to integer value 0 of the underlying integer representation of the UTC timestamp value.
The maximum timestamp value in UTC is "2038-01-19 03:14:07". This corresponds to integer value 2^31 - 1 (i.e. the maximum signed 32-bit value) of the underlying integer representation of the UTC timestamp value.
In [Utc40 mode](#Utc40) and in [Utc64 mode](#Utc64) (described below), the maximum timestamp value in UTC is "9999-12-31 00:00:00".
For the minimum and maximum timestamp value in the local timezone, the local timezone displacement and daylight savings time must be taken into account.

## interval days
The data type *interval days* can hold values that represent the number of days between two dates.
The supported value range is the signed 32-bit value range: [-2^31 … 2^31 - 1].
In decimal notation, this is the range [-2,147,483,648 … 2,147,483,647].
In hexadecimal notation, this is the range [-0x8000,0000 … 0x7fff,ffff].

## interval seconds
The data type *interval seconds* can hold values that represent the number of seconds between two timestamps.
The supported value range is the signed 32-bit value range: [-2^31 … 2^31 - 1].
In decimal notation, this is the range [-2,147,483,648 … 2,147,483,647].
In hexadecimal notation, this is the range [-0x8000,0000 … 0x7fff,ffff].
In some implementations (depending on the underlying data base) the supported value range of the data type *interval seconds* is the signed 64-bit value range: [-2^63 … 2^63 - 1].
In decimal notation, this is the range [-9,223,372,036,854,775,808 … 9,223,372,036,854,775,807].
In hexadecimal notation, this is the range [-0x8000,0000,0000,0000 … 0x7fff,ffff,ffff,ffff].

## raw
The data type *raw* can hold a string of unsigned bytes. The value of an unsigned byte lies in the range 0..255.

## Correspondence of SQL data types with Infor Enterprise Server 3GL and database data types
The following table shows which Infor Enterprise Server Baan 3GL/database type corresponds with a certain SQL type:
| | |
|---|---|
| SQL type | Infor Enterprise Server 3GL/ Database type |
| integer | char, int, long, enum, bitset, mail, text |
| real | float, double |
| date | date |
| timestamp | time (UTC) |
| string | string, multibyte string |
| raw | raw |

## BitCountOfUtc
In this manual, the term BitCountOfUtc is used to refer to the number of significant bits in a UTC timestamp value.
Using the term BitCountOfUtc, we can abstract from its actual value.
This way, we can say that the supported value range of UTC timestamp values is restricted to the non-negative part of the signed *BitCountOfUtc*-bit value range: [0 … 2^(BitCountOfUtc-1) - 1].
The relation between the term BitCountOfUtc and the term [ByteCountOfUtc](#ByteCountOfUtc) defined below is as follows.
```

         BitCountOfUtc = 8 * ByteCountOfUtc
```
The term [BitCountOfUtc](../functions_date_time_zones/overview.md#BitCountOfUtc) is further described in the [overview of bshell functions for dates, times and time zones](../functions_date_time_zones/overview.md).

## ByteCountOfUtc
In this manual, the term ByteCountOfUtc is used to refer to the number of bytes used to exchange a UTC timestamp value between any client and a database server.
Using the term ByteCountOfUtc, we can abstract from its actual value.
The relation between the term ByteCountOfUtc and the term [BitCountOfUtc](#BitCountOfUtc) defined above is as follows.
```

         BitCountOfUtc = 8 * ByteCountOfUtc
```
The actual value of ByteCountOfUtc can be configured by setting the resource "utc40", e.g. in the file $BSE/lib/defaults/all.
The term [ByteCountOfUtc](../functions_date_time_zones/overview.md#ByteCountOfUtc) is further described in the [overview of bshell functions for dates, times and time zones](../functions_date_time_zones/overview.md).

## Utc32 mode
In Utc32 mode, the value of [ByteCountOfUtc](#ByteCountOfUtc) is set to 4, so [BitCountOfUtc](#BitCountOfUtc) is 32.
The Utc32 mode is the default mode. It is active when the resource "utc40" is not set or when it is set to value 0.
In Utc32 mode, when a UTC timestamp value is exchanged between any client and a database server, then a sequence of 4 bytes is used.
The term [Utc32 mode](../functions_date_time_zones/overview.md#Utc32) is further described in the [overview of bshell functions for dates, times and time zones](../functions_date_time_zones/overview.md).

## Utc40 mode
In Utc40 mode, the value of [ByteCountOfUtc](#ByteCountOfUtc) is set to 5, so [BitCountOfUtc](#BitCountOfUtc) is 40.
The Utc40 mode is active when the resource "utc40" is set to any value not equal to 0.
In Utc40 mode, when a UTC timestamp value is exchanged between any client and a database server, then a sequence of 5 bytes is used.
The term [Utc40 mode](../functions_date_time_zones/overview.md#Utc40) is further described in the [overview of bshell functions for dates, times and time zones](../functions_date_time_zones/overview.md).

## Utc64 mode
In Utc64 mode, the value of [ByteCountOfUtc](#ByteCountOfUtc) is set to 8, so [BitCountOfUtc](#BitCountOfUtc) is 64.
In Utc64 mode, when a UTC timestamp value is exchanged between any client and a database server, then a sequence of 8 bytes is used.
The term [Utc64 mode](../functions_date_time_zones/overview.md#Utc64) is further described in the [overview of bshell functions for dates, times and time zones](../functions_date_time_zones/overview.md).
Notice that there is no documented way to activate the Utc64 mode. The Utc64 mode only exists for test purposes and is not meant to be used in a normal user environment.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)

- [Overview of bshell functions for dates, times and time zones](../functions_date_time_zones/overview.md)

- [BitCountOfUtc in the bshell](../functions_date_time_zones/overview.md#BitCountOfUtc)

- [ByteCountOfUtc in the bshell](../functions_date_time_zones/overview.md#ByteCountOfUtc)

- [Utc32 mode in the bshell](../functions_date_time_zones/overview.md#Utc32)

- [Utc40 mode in the bshell](../functions_date_time_zones/overview.md#Utc40)

- [Utc64 mode in the bshell](../functions_date_time_zones/overview.md#Utc64)

- [Resource "utc40"](../misc/bshell_resources.md)
