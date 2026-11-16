# EXTRACT expression
With the EXTRACT expression you can extract a date/time field from a date or a timestamp.

## Syntax
```

<extract expression>
    ::= EXTRACT ( <extract field> FROM <value expression> )

<extract field>
    ::= YEAR | MONTH | DAY | HOUR | MINUTE | SECOND
```

## Syntactical restrictions
The type of *<**value expression**>* shall be *timestamp* or *date*.

## Semantics
If the *<**value expression**>* is NULL, then the result of the EXTRACT expression is also NULL.
The data type of the result of the EXTRACT expression is an integer.
If the *HOUR*, *MINUTE* or *SECOND* field is extracted from a date, then the result is 0.

## Examples
The following EXTRACT expression returns the year from a date.
```

EXTRACT ( YEAR FROM CURRENT_DATE )
```
The following EXTRACT expression returns the hour from the timestamp value in the column *startime*.
```

EXTRACT ( HOUR FROM startime )
```

## Related topics
- [Value expression](value_expression.md)

- [Infor Enterprise Server SQL](baan_sql.md)
