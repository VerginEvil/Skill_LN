# Simplest comparison predicate
The simplest comparison predicate compares two value expressions. It is used to define the semantics of the general [comparison predicate](comparison_pred.md).

## Syntax
```

<simplest comparison predicate>
    ::= <value expression> <comparison operator> <value expression>

<comparison operator>
    ::= = | <> | != | < | <= | > | >=
```

## Semantics
If one of the value expressions is NULL then the comparison predicate evaluates to Unknown.
If the value expressions are of type *string* and the values are of unequal length, then, for the purpose of comparison, the shorter string is right padded with spaces so that its length equals the length of the longer string.
If the value expressions are of type *raw* and the values are of unequal length, then *no* padding is used for the purpose of comparison.
The values of the value expressions are compared using the normal semantics of the relational operators.

## Syntactical restrictions
The types of the left value expression and the right value expression must be [comparable](comparable_datatypes.md).

## Examples
The following comparison predicate evaluates to True.
```

2 > 1
```
The following comparison predicate (where each ␣ represents one space character) evaluates to True.
```

'S' = 'S␣␣␣'
```
The following comparison predicate evaluates to True if empno is 10. It evaluate to Unknown if empno is NULL. It evaluates to False otherwise.
```

empno = 10
```
The following comparison predicate evaluates to False.
```

x'ab' = x'abc'
```

## Related topics
- [Comparison predicate](comparison_pred.md)

- [Infor Enterprise Server SQL](baan_sql.md)
