# Query expression
A query expression defines a row set. The row set can be built up from multiple query specifications using the UNION operator.

## Syntax
```

<query expression>
    ::= Query specification
      | Query specification UNION operator <query expression>
```

## Semantics
The result of the *<query expression>* is the result of the *<query specification>* or the result of applying the [UNION](union.md) operator.

## Examples
The following example shows the simplest *query expression*, a *query specification*:
```

select empno, lastname
from dbtst120
where salary > 30000
```
The following example shows a *query expression* built up from two *query specification* s:
```

select empno, lastname
from dbtst120
where salary > 30000
union all
select empno, lastname
from dbtst120
where salary < 10000
```

## Related topics
- [SELECT statement](select_statement.md)
- [UNION operator](union.md)
- [Infor Enterprise Server SQL](baan_sql.md)
