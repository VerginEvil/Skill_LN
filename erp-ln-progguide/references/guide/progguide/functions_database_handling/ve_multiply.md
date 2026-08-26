# Operator * (multiply)
The operator * multiplies the values of two value expressions.

## Syntax
```

<operator *>
    ::= Value expression * Value expression
```

## Semantics
The following table shows the data types that are allowed for the left and right value expression and the resulting data type. The type of the left value expression is on the vertical axis. The type of the right value expression is on the horizontal axis. A hyphen ('-') indicates that the combination is not allowed.
| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| * | I | R | S | D | T | ID | IS | Ra |
| I | I | R | - | - | - | ID | IS | - |
| R | R | R | - | - | - | - | - | - |
| S | - | - | - | - | - | - | - | - |
| D | - | - | - | - | - | - | - | - |
| T | - | - | - | - | - | - | - | - |
| ID | ID | - | - | - | - | - | - | - |
| IS | IS | - | - | - | - | - | - | - |
| Ra | - | - | - | - | - | - | - | - |
I=Integer R=Real S=String D=Date T=TimeStamp ID=Interval Days IS=Interval Seconds Ra=Raw
The multiplication of values of types *integer* and *real* follow the normal rules for multiplication of numeric values.
The multiplication of a value of type *interval days* and a value of type *integer* yields a value of type *interval days*. The multiplication of value of type *interval seconds* and a value of type *integer* yields a value of type *interval seconds*. Arithmetic operations involving values of type *date* or *timestamp* and *interval days* or *interval seconds* obey the natural rules associated with dates and yield valid results according to the Gregorian calendar.

## Examples
*Example 1*: The following expression multiplies the constants 1 and 2.
```

1 * 2
```
*Example 2*: The following expression multiplies by 2 the number of days a person was old on his hiredate.
```

( hiredate-birthdte ) * 2
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
