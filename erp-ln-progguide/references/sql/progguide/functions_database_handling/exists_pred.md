# EXISTS predicate
An EXISTS predicate is True if the evaluation of the subquery results in a non-empty row set.

## Syntax
```

<exists predicate>
    ::= EXISTS ( <subquery> )
```

## Semantics
If the evaluation of the *<**subquery**>* results in a non-empty row set, then the result of the EXISTS predicate is True. Otherwise the result is False.

## Examples
The following condition is True if table *dbtst120* is not empty.
```

EXISTS( SELECT * FROM dbtst120 )
```
The following condition is True if there exists an employee whose salary is larger than *a.salary*.
```

EXISTS( SELECT * FROM dbtst120 WHERE salary > a.salary )
```

## Related topics
- [Infor Enterprise Server SQL](baan_sql.md)
