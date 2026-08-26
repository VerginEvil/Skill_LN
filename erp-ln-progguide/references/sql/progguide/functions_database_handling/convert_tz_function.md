# CONVERT_TZ function
With the CONVERT_TZ function you can convert timestamp values from one timezone to another.

## Syntax
```

<convert_tz function>
    ::= CONVERT_TZ ( Value expression, <from_timezone>, <to_timezone> )

<from_timezone>
    ::= String constant

<to_timezone>
    ::= String constant
```

## Syntactical restrictions
The type of the *<value expression>* shall be *timestamp*.

## Semantics
If the *<value expression>* is NULL, then the result of the CONVERT_TZ function is also NULL.
The data type of the result of the CONVERT_TZ function is a *timestamp*.
The arguments *<from_timezone>* and *<to_timezone>* must represent valid timezones. An empty string can be used to indicate the local timezone.

## Examples
The following function converts the *startime* timestamp value from UTC to MET.
```

CONVERT_TZ ( startime, 'UTC', 'MET' )
```
The following function converts the current time from timezone 'Europe/Amsterdam' to timezone 'Asia/Tokyo'.
```

CONVERT_TZ ( CURRENT_TIMESTAMP, 'Europe/Amsterdam', 'Asia/Tokyo' )
```
The following function converts the current time from UTC to local time.
```

CONVERT_TZ ( CURRENT_TIMESTAMP, 'UTC', '' )
```

## Related topics
- [Value expression](value_expression.md)
- [Infor Enterprise Server SQL](baan_sql.md)
