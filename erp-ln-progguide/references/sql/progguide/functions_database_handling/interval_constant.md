# Interval constant
The interval constant specifies an interval value. This can either be a number of days or a number of seconds.

## Syntax
```

<interval constant>
    ::= INTERVAL [-] '<digit>...' DAY
      | INTERVAL [-] '<digit>...' SECOND
```

## Syntactical restrictions
The value of the interval constant must lie in the range [–2147483647 .. +2147483647].

## Semantics
The data type of an interval constant is *interval days* or *interval seconds*.

## Examples
```

INTERVAL '2' DAY
INTERVAL - '60' SECOND
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
