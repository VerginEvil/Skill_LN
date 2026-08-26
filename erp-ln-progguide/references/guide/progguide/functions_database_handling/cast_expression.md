# CAST expression
With the CAST expression you can assign a type to a parameter.

## Syntax
```

<cast expression>
    ::= CAST ( Parameter AS <parameter cast type> )

<parameter cast type>
    ::= INTEGER | REAL | DATE | TIMESTAMP | STRING | RAW
```

## Syntactical restrictions
The value of *Parameter* is restricted to the name of a column. A syntax error will result when any other type of expression is used.

## Semantics
The cast operator assigns the type *<parameter cast type>* to the *<parameter>*. The cast expression itself will also be of type *<parameter cast type>*.

## Examples
The following CAST expression assigns the type *integer* to the parameter *param*.
```

CAST ( :param AS INTEGER )
```
The following CAST expression assigns the type *raw* to the parameter *param*.
```

CAST ( :param AS RAW )
```

## Resolving type conflicts on parameters
The cast operator is used to properly type parameters in case of ambiguities or in case of possible type conflicts.
In the following example, both *param1* and *param2* cannot be typed, because each type is comparable to itself.
```

:param1 = :param2
```
This problem can be resolved using the CAST expression.
```

:param1 = CAST( :param2 AS STRING )
```
In the following example the first comparison types *param* as *date*, while the second comparison types it as *real*.
```

:param = hiredate  or  :param = 0
```
Using the CAST expression this can be resolved.
```

:param = hiredate  or  CAST( :param AS DATE ) = 0
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
