# Operator / (divide)
The operator / divides the values of two value expressions.

## Syntax
```

<operator />
    ::= <value expression> / <value expression>
```

## Semantics
The following table shows the data types that are allowed for the left and right value expression and the resulting data type. The type of the left value expression is on the vertical axis. The type of the right value expression is on the horizontal axis. A hyphen ('-') indicates that the combination is not allowed.
*Note*: the division of two integer values yields a real value.
| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| / | I | R | S | D | T | ID | IS | Ra |
| I | R | R | - | - | - | - | - | - |
| R | R | R | - | - | - | - | - | - |
| S | - | - | - | - | - | - | - | - |
| D | - | - | - | - | - | - | - | - |
| T | - | - | - | - | - | - | - | - |
| ID | - | - | - | - | - | - | - | - |
| IS | - | - | - | - | - | - | - | - |
| Ra | - | - | - | - | - | - | - | - |
I=Integer R=Real S=String D=Date T=TimeStamp ID=Interval Days IS=Interval Seconds Ra=Raw
The division of values of types *integer* and *real* follow the normal rules for division of numeric values.

## Examples
*Example*: The following expression divids the constants 1 and 2.
```

1 / 2
```
*Note*: the result is of type *real*.

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
