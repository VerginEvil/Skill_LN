# Query specification
A query specification defines a row set. The row set can be built up from multiple (database) tables. Rows can be filtered, joined and grouped.

## Syntax
```

<query specification>
    ::= SELECT clause <select list>
        FROM clause <from list>
        [ WHERE clause Search condition ]
        [ GROUP BY clause <group list>
           [ HAVING clause Search condition ] ]
```

## Semantics
The result of the *<query specification>* is the result of the FROM clause, followed by application of the optional WHERE, GROUP BY and HAVING clauses and the SELECT clause. The column names and descriptors are the same as those of the SELECT clause.

## Related topics
- [Query expression](query_expression.md)
- [SELECT statement](select_statement.md)
- [Infor Enterprise Server SQL](baan_sql.md)
