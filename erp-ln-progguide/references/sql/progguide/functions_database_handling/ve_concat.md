# Operator (string concatenation)
The operator & concatenates the (string) values of two value expressions.

## Syntax
```

<operator &>
    ::= <value expression> & <value expression>
      | <value expression> || <value expression>
```

## Semantics
The following table shows the data types that are allowed for the left and right value expression and the resulting data type. The type of the left value expression is on the vertical axis. The type of the right value expression is on the horizontal axis. A hyphen ('-') indicates that the combination is not allowed.
| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| & | I | R | S | D | T | ID | IS | Ra |
| I | - | - | - | - | - | - | - | - |
| R | - | - | - | - | - | - | - | - |
| S | - | - | S | - | - | - | - | - |
| D | - | - | - | - | - | - | - | - |
| T | - | - | - | - | - | - | - | - |
| ID | - | - | - | - | - | - | - | - |
| IS | - | - | - | - | - | - | - | - |
| Ra | - | - | - | - | - | - | - | Ra |
I=Integer R=Real S=String D=Date T=TimeStamp ID=Interval Days IS=Interval Seconds Ra=Raw

## Examples
*Example 1*: The following expression concatenates the constants 'AB' and 'C'. The result is 'ABC'.
```

'AB' || 'C'
```
*Example 2*: The following expression concatenates the first character of firstnme and the string constant 'B'.
```

firstnme(1;1) & 'B'
```
*Example 3*: The following expression concatenates the raw string x'A' and the raw string x'D'. The result is the raw string x'A0D0'.
```

x'A' & x'D'
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
