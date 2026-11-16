# Operator + (add)
The operator + adds the values of two value expressions.

## Syntax
```

<operator +>
    ::= <value expression> + <value expression>
```

## Semantics
The following table shows the data types that are allowed for the left and right value expression and the resulting data type. The type of the left value expression is on the vertical axis. The type of the right value expression is on the horizontal axis. A hyphen ('-') indicates that the combination is not allowed.
| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| + | I | R | S | D | T | ID | IS | Ra |
| I | I | R | - | - | - | - | - | - |
| R | R | R | - | - | - | - | - | - |
| S | - | - | - | - | - | - | - | - |
| D | - | - | - | - | - | D | - | - |
| T | - | - | - | - | - | - | T | - |
| ID | - | - | - | D | - | ID | - | - |
| IS | - | - | - | - | T | - | IS | - |
| Ra | - | - | - | - | - | - | - | - |
I=Integer R=Real S=String D=Date T=TimeStamp ID=Interval Days IS=Interval Seconds Ra=Raw
The addition of values of types *integer* and *real* follow the normal rules for addition of numeric values.
The addition of a value of type *date* and a value of type *interval days* yields a value of type *date*. The addition of a value of type *timestamp* and a value of type *interval seconds* yields a value of type *timestamp*. Arithmetic operations involving values of type *date* or *timestamp* and *interval days* or *interval seconds* obey the natural rules associated with dates and yield valid results according to the Gregorian calendar.

## Examples
*Example 1*: The following expression adds the constants 1 and 2.
```

1 + 2
```
*Example 2*: The following expression adds the date "July 16, 2002" and the interval "2 days". The result is "July 18, 2002".
```

DATE '2002-7-16' + 2
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
