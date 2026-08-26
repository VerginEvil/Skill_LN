# IN predicate
An IN predicate is True if the value of the expression on the left hand side is contained in the collection of values on the right hand side. The collection of values can be specified by a list of values or it can be specified by a subquery. In the latter case it is checked if the value is contained in the result set of the subquery.

## Syntax
```

<in predicate>
    ::= Value expression [NOT] IN ( Sub query )
      | Value expression [NOT] IN ( <in value list> )

<in value list>
    ::= Value expression [ { , Value expression }... ]
```

## Syntactical restrictions
The degree of the *<sub query>* shall be 1.
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
The following equivalences hold:
```

   expr NOT IN ( ... )  <=>  NOT ( expr IN ( ... ) )
```
```

   expr IN ( v1, v2, ... )  <=>  expr = v1 OR expr = v2 OR ...
```
For the exact semantics see [Comparison predicate](comparison_pred.md), [NOT boolean operator](not_sc.md) and [OR boolean operator](or_sc.md).

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
