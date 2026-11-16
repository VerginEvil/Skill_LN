# Operator \ (modulo)
The operator \ takes the modulo of the values of two value expressions.

## Syntax
```

<operator \>
    ::= <value expression> \ <value expression>
```

## Semantics
The following table shows the data types that are allowed for the left and right value expression and the resulting data type. The type of the left value expression is on the vertical axis. The type of the right value expression is on the horizontal axis. A hyphen ('-') indicates that the combination is not allowed.
| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| \ | I | R | S | D | T | ID | IS | Ra |
| I | I | - | - | - | - | - | - | - |
| R | - | - | - | - | - | - | - | - |
| S | - | - | - | - | - | - | - | - |
| D | - | - | - | - | - | - | - | - |
| T | - | - | - | - | - | - | - | - |
| ID | - | - | - | - | - | - | - | - |
| IS | - | - | - | - | - | - | - | - |
| Ra | - | - | - | - | - | - | - | - |
I=Integer R=Real S=String D=Date T=TimeStamp ID=Interval Days IS=Interval Seconds Ra=Raw
The result of the modulo operator is defined by the following equivalence:
```

    a \ b = c  ⟺  b * n + c = a, n is integer and c in <-b..+b>
```
For any a and b there exist two pairs (n,c) that obey this rule. The n that is the closest to 0, determines which pair is taken.
For example, for a=7 and b=3 the pairs (n=2,c=1) and (n=3,c=–2 ) are candidates. In this case n=2 is closest to 0 and hence the outcome of 7\3=1.
As another example, for a=–7 and b=3 the pairs (n=–2,c=–1) and (n=–3,c=2) are candidates. In this case n=–2 is closest to 0 and hence the outcome of –7\3=–1.

## Examples
*Example 1*: The following expression takes the modulo of 5 and 3. The result is 2.
```

5 \ 3
```
*Example 2*: The following expression takes the modulo of –7 and 3. The result is –1.
```

-7 \ 3
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
