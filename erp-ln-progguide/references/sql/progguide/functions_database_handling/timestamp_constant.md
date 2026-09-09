# Timestamp constant
The timestamp constant specifies a timestamp value.

## Syntax
```

<timestamp constant>
    ::= TIMESTAMP '<timestamp string>'

<timestamp string>
    ::= <year>-<month>-<day> <hours>:<minutes>:<seconds>[<timezone offset>]

<year>            ::= <digit>...
<month>           ::= <digit>...
<day>             ::= <digit>...
<hours>           ::= <digit>...
<minutes>         ::= <digit>...
<seconds>         ::= <digit>...

<timezone offset> ::= <sign><hours_offset>:<minutes_offset>
<sign>            ::= - | +
<hours_offset>    ::= <digit>...
<minutes_offset>  ::= <digit>...
```

## Syntactical restrictions
The timestamp represented by the timestamp constant must be a valid timestamp according to the Gregorian calender.
The minimum timestamp constant in UTC is "1970-01-01 00:00:00".
The maximum timestamp constant in UTC is "2038-01-19 03:14:07".
In [Utc40 mode](sql_data_types.md#Utc40) and in [Utc64 mode](sql_data_types.md#Utc64), the maximum timestamp constant in UTC is "9999-12-31 00:00:00".
For the minimum and maximum timestamp constant in the local timezone, the local timezone displacement and daylight savings time must be taken into account.
The timezone offset must be in the range from -12:59 to 13:00.

## Semantics
The data type of a timestamp constant is *timestamp*. The timestamp string is assumed to be in local time.

## Examples
The following timestamp constant represents the timestamp January 10, 2003, 12:04:35.
```

TIMESTAMP '2003-1-10 12:04:35'
```
The following timestamp constant represents the timestamp March 10, 1, 12:04:01.
```

TIMESTAMP '1-03-10 12:4:1'
```
The following timestamp constant with timezone offset represents the timestamp March 30, 2022, 13:42:17 in the specified timezone offset.
```

TIMESTAMP '2022-03-30 13:42:17+2:00'
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)

- [timestamp](sql_data_types.md#timestamp)

- [BitCountOfUtc](sql_data_types.md#BitCountOfUtc)

- [ByteCountOfUtc](sql_data_types.md#ByteCountOfUtc)

- [Utc32 mode](sql_data_types.md#Utc32)

- [Utc40 mode](sql_data_types.md#Utc40)

- [Utc64 mode](sql_data_types.md#Utc64)
