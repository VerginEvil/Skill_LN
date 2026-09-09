# IN predicate
An IN predicate is True if the value of the expression on the left hand side is contained in the collection of values on the right hand side. The collection of values can be specified by a list of values or it can be specified by a subquery. In the latter case it is checked if the value is contained in the result set of the subquery.

## Syntax
```

<in predicate>
    ::= <value expression> [NOT] IN ( <subquery> )
      | <value expression> [NOT] IN ( <in value list> )

<in value list>
    ::= <value expression> [ { , <value expression> }... ]
```

## Syntactical restrictions
The [degree](sql_glossary.md#Degree) of the *<**subquery**>* shall be 1.
Example of correct usage.
```

empno IN ( SELECT empno FROM ... )
```
Examples of *incorrect* usage:
```

empno = ( SELECT empno, salary ... )
```
```

empno = ( SELECT * from dbtst120 )
```

## Semantics
The following equivalences hold.
```

expr NOT IN ( ... )  ⟺  NOT ( expr IN ( ... ) )

expr IN ( v )  ⟺  expr = v

expr IN ( v1, v2, ... )  ⟺  expr IN ( v1 ) OR expr IN ( v2, ... )
```
For the exact semantics see the pages about [the comparison operators](comparison_pred.md), [the NOT operator](not_sc.md) and [the OR operator](or_sc.md).

## Examples
The following condition is True if *empno* is either 100, 200 or 300.
```

empno IN ( 100, 200, 300 )
```
The following condition is True if *empno* is equal to at least one of the *mgrno* values of dbtst100.
```

empno IN ( select mgrno from dbtst100 )
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
